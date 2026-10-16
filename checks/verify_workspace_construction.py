"""Exact coherent workspace-assisted contact construction.

All internal controls are free. Every physical bus contact has norm J=1.
No measurements, resets or extra initialized workspace are used. The returned
unitary is tested on the entire data+arbitrary-bus input subspace with helpers
in |0>. No claim about other helper inputs or finite-clock efficiency is made.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

I2=np.eye(2,dtype=complex)
HAD=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
PH=np.diag([1,1j]).astype(complex)
SW=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)

def mu(b:int)->float:
    if b<1: raise ValueError('Block size must be positive')
    return b*math.comb(b-1,(b-1)//2)/2**(b-1)

def blocks(n:int,s:int)->list[list[int]]:
    if n<1 or s<0: raise ValueError('Need n>=1 and s>=0')
    N=n+s;m=s+1
    sizes=[N//m+int(i<N%m) for i in range(m)]
    leaders=[0]+list(range(n,N));spec=list(range(1,n));out=[];p=0
    for leader,b in zip(leaders,sizes):
        out.append([leader]+spec[p:p+b-1]);p+=b-1
    assert p==n-1
    return out

def embed(a:np.ndarray,sites:tuple[int,...],nq:int)->np.ndarray:
    d=1<<nq;out=np.zeros((d,d),complex)
    for x in range(d):
        col=sum(((x>>(nq-1-i))&1)<<(len(sites)-1-k) for k,i in enumerate(sites))
        for row in range(1<<len(sites)):
            y=x
            for k,i in enumerate(sites):
                bit=(row>>(len(sites)-1-k))&1;mask=1<<(nq-1-i)
                y=(y|mask) if bit else (y&~mask)
            out[y,x]+=a[row,col]
    return out

def encode_block(bits:list[int],group:list[int])->None:
    b=len(group);q=bits[group[0]];w=sum(bits[i] for i in group[1:])
    first=q^int(2*w>b)
    bits[group[0]]=first
    for i in group[1:]: bits[i]^=first

def compiled_zz(n:int,s:int,theta:float,dense:bool=True)->tuple[np.ndarray,float,dict]:
    N=n+s;d=1<<N;gs=blocks(n,s);gain=sum(mu(len(g)) for g in gs)
    mags=np.array([N-2*x.bit_count() for x in range(d)],float)
    K=1<<(n-1);phase=np.ones(2*d,complex);av=np.zeros(d)
    t=theta/gain
    for u in range(K):
        frame=[]
        for x in range(d):
            bits=[(x>>(N-1-i))&1 for i in range(N)]
            # Fan the target's Z value into clean leaders, not cloned states.
            for i in range(n,N): bits[i]^=bits[0]
            # Coherent translation of unknown spectator labels.
            for k in range(n-1): bits[k+1]^=(u>>(n-2-k))&1
            for g in gs: encode_block(bits,g)
            frame.append(sum(z<<(N-1-i) for i,z in enumerate(bits)))
        assert len(set(frame))==d, 'Every control frame must be a unitary permutation'
        vals=mags[np.array(frame)]
        av+=vals/K
        phase*=np.exp(-1j*t*np.kron(vals,[1.,-1.])/K)
    inds=np.array([(x<<s) for x in range(1<<n)])
    expected=np.array([gain*(1-2*(x>>(n-1))) for x in range(1<<n)])
    err=float(np.max(abs(av[inds]-expected)))
    assert err<1e-12
    return (np.diag(phase) if dense else phase),t,{'n':n,'s':s,'N':N,'block_sizes':[len(g) for g in gs],
        'gain':gain,'raw_intervals_per_Ising':K,'exact_generator_error':err}

def compiled_swap(n:int,s:int)->tuple[np.ndarray,float,dict]:
    N=n+s;zz,t,row=compiled_zz(n,s,np.pi/4)
    U=np.eye(1<<(N+1),dtype=complex)
    for rot in (I2,HAD,PH@HAD):
        Q=embed(rot,(0,),N+1)@embed(rot,(N,),N+1)
        U=(Q@zz@Q.conj().T)@U
    inds=np.array([((data<<s)<<1)|bus for data in range(1<<n) for bus in (0,1)])
    target=np.exp(-1j*np.pi/4)*embed(SW,(0,N),N+1)
    err=float(np.linalg.norm(U[:,inds]-target[:,inds],2))
    assert err<2e-11
    row.update({'swap_time':3*t,'isometry_operator_error':err,'input_columns':len(inds)})
    return U,3*t,row

def apply_local(A:np.ndarray,u:np.ndarray,sites:tuple[int,...],nq:int)->np.ndarray:
    if len(set(sites))!=len(sites): raise ValueError('Duplicate sites')
    other=tuple(i for i in range(nq) if i not in sites)
    axes=sites+other+(nq,)
    T=A.reshape((2,)*nq+(A.shape[1],)).transpose(axes)
    shape=T.shape
    T=(u@T.reshape(1<<len(sites),-1)).reshape(shape)
    return T.transpose(np.argsort(axes)).reshape(A.shape)

def full_route(n:int,s:int)->dict:
    N=n+s;nq=2*N+1;hub=2*N;d=1<<nq;cols=1<<(2*n+1)
    A=np.zeros((d,cols),complex);target=np.zeros_like(A)
    for l in range(1<<n):
      for r in range(1<<n):
       for c in (0,1):
        col=(l<<(n+1))|(r<<1)|c
        x=(l<<(s+N+1))|(r<<(s+1))|c
        y=(r<<(s+N+1))|(l<<(s+1))|c
        A[x,col]=1;target[y,col]=1
    u,t,row=compiled_swap(n,s)
    for j in range(n):
        for base in (0,N):
            sites=(base+j,)+tuple(base+i for i in range(n) if i!=j)+tuple(range(base+n,base+N))+(hub,)
            A=apply_local(A,u,sites,nq)
    sites=tuple(range(N))+(hub,)
    A=apply_local(A,u,sites,nq)
    # Left register is [r_n,r_1,...,r_{n-1}]; rotate data only.
    perm=np.arange(d)
    for x in range(d):
        vals=[(x>>(nq-1-i))&1 for i in range(n)]
        vals=vals[1:]+vals[:1];y=x
        for i,v in enumerate(vals):
            mask=1<<(nq-1-i);y=(y|mask) if v else y&~mask
        perm[x]=y
    B=np.empty_like(A);B[perm]=A;A=B
    phase=np.exp(-1j*(2*n+1)*np.pi/4)
    err=float(np.linalg.norm(A-phase*target,2))
    overlap=np.vdot(target,A)/cols
    F=float(abs(overlap)**2)
    assert err<3e-11
    return {'n':n,'s':s,'physical_qubits':nq,'input_columns':cols,
            'bus_swaps':2*n+1,'time':(2*n+1)*t,'isometry_operator_error':err,
            'full_data_and_bus_process_fidelity':F,'helpers_returned':True}

if __name__=='__main__':
    out={'model':'Free internal controls, J=1 per contact, s initialized helpers per module, arbitrary bus',
         'spectral':[],'gate':[],'route':[],'scaling':[]}
    for n in range(1,9):
      for s in range(5):
        _,_,r=compiled_zz(n,s,.371,dense=False)
        r['gain_over_sqrt_Nm']=r['gain']/np.sqrt((n+s)*(s+1))
        assert 1/np.sqrt(6)-1e-12<=r['gain_over_sqrt_Nm']<=1+1e-12
        out['spectral'].append(r)
    for n,s in [(1,0),(1,1),(1,3),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2),(4,1),(4,2),(5,1)]:
        _,_,r=compiled_swap(n,s);out['gate'].append(r)
    for n,s in [(1,0),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)]:
        out['route'].append(full_route(n,s))
    for n in (16,64,256,1024):
      for s in (0,1,int(np.sqrt(n)),n):
        gain=sum(mu(len(g)) for g in blocks(n,s));dirty=mu(n+s)
        out['scaling'].append({'n':n,'s':s,'clean_gain':gain,'dirty_gain_same_hardware':dirty,
                              'achievable_speed_ratio':gain/dirty,'time':3*np.pi*(2*n+1)/(4*gain)})
    out['all_passed']=True
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'spectral_checks':len(out['spectral']),'gate_checks':len(out['gate']),
                     'full_routes':out['route'],
                     'max_gate_error':max(r['isometry_operator_error'] for r in out['gate']),
                     'all_passed':True},indent=2))
