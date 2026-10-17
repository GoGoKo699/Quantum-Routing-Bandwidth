"""Adversarial finite-dimensional checks of the entropy-deficit moment bound.

The universal claims rest on the analytical proof in science/bandwidth.md.
Tests include exact maximization over fixed-spectrum unitary orbits, Gibbs
states of H^2 (entropy-constrained moment maximizers), and noncommuting states.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.special import logsumexp
from verify_workspace_construction import embed,mu,blocks

PA=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.]).astype(complex)]
C0=2*np.sqrt(2)/np.log(2)

def entropy(rho:np.ndarray)->float:
    p=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    p=p[p>1e-15]
    return float(-np.sum(p*np.log2(p)))

def make_star(N:int,rng:np.random.Generator):
    d=1<<(N+1);v=np.zeros(3);H=np.zeros((d,d),complex);As=[np.zeros((1<<N,1<<N),complex) for _ in range(3)];budget=0.
    for j in range(N):
        # Include one-sided terms to test the correct orthogonal projection.
        B=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));B=(B+B.conj().T)/2
        J=float(rng.uniform(.05,1.5));B*=J/max(abs(np.linalg.eigvalsh(B)))
        budget+=J*J
        for a in range(3):
          for b in range(3):
            c=float(np.trace(B@np.kron(PA[a],PA[b])).real/4)
            H+=c*embed(np.kron(PA[a],PA[b]),(j,N),N+1)
            As[b]+=c*embed(PA[a],(j,),N)
            v[b]+=c*c
    assert sum(v)<=budget+1e-12
    return H,As,v,budget

def check_rate(rho,H,N):
    dA=1<<N;rA=np.trace(rho.reshape(dA,2,dA,2),axis1=1,axis2=3)
    p,u=eigh(rA);logA=(u*np.log2(np.maximum(p,1e-250)))@u.conj().T
    dr=-1j*(H@rho-rho@H);drA=np.trace(dr.reshape(dA,2,dA,2),axis1=1,axis2=3)
    rate=abs(float(np.trace(drA@logA).real))
    moment=float(np.trace(rho@H@H).real)
    assert rate<=C0*np.sqrt(max(moment,0))+1e-10
    return rate/(C0*np.sqrt(moment)) if moment>0 else 0.

rng=np.random.default_rng(2026101607)
out={'seed':2026101607,'gibbs_tests':[],'orbit_tests':[],'random_state_tests':[],
     'scalar_mgf_tests':[],'group_scaling_tests':0}
min_psd=0.;max_mgf=0.;max_rate=0.
for N in range(1,6):
  for rep in range(4):
    H,As,v,budget=make_star(N,rng);d=H.shape[0];H2=H@H
    Q=3*sum(np.kron(A@A,np.eye(2)) for A in As)-H2
    min_psd=min(min_psd,float(np.linalg.eigvalsh(Q)[0]))
    assert np.linalg.eigvalsh(Q)[0]>-1e-10
    for b,A in enumerate(As):
        if v[b]<1e-18: continue
        ev=np.linalg.eigvalsh(A)
        lg=float(logsumexp(ev*ev/(4*v[b]))-np.log(len(ev)))
        max_mgf=max(max_mgf,lg)
        assert lg<=.5*np.log(2)+1e-12
    ev,W=eigh(H2);ev=np.maximum(ev,0);scale=max(float(ev[-1]),1e-12)
    for beta in (0.,.1,1.,5.,20.,100.):
        p=np.exp(beta*ev/scale-logsumexp(beta*ev/scale))
        rho=(W*p)@W.conj().T
        I=np.log2(d)+float(np.sum(p*np.log2(np.maximum(p,1e-300))))
        actual=float(p@ev)
        bound=12*np.log(2)*(I+.5)*sum(v)
        assert actual<=bound+1e-10
        out['gibbs_tests'].append({'N':N,'rep':rep,'beta':beta,'I_bits':I,'ratio':actual/bound})
    # Exact worst moment over all unitary conjugates of uniform rank d/2^r.
    for r in range(N+2):
        rank=max(1,d>>r);actual=float(np.mean(ev[-rank:]));I=float(np.log2(d/rank))
        bound=12*np.log(2)*(I+.5)*sum(v)
        assert actual<=bound+1e-10
        out['orbit_tests'].append({'N':N,'r':r,'rank':rank,'max_moment':actual,'bound':bound})
    for rank in (1,max(1,d//3),d):
        M=rng.normal(size=(d,rank))+1j*rng.normal(size=(d,rank));rho=M@M.conj().T;rho/=np.trace(rho)
        I=np.log2(d)-entropy(rho);actual=float(np.trace(rho@H2).real)
        bound=12*np.log(2)*(I+.5)*sum(v)
        assert actual<=bound+1e-10
        ratio=check_rate(rho,H,N);max_rate=max(max_rate,ratio)
        out['random_state_tests'].append({'N':N,'rank':rank,'I_bits':I,'moment_ratio':actual/bound,'conditional_rate_ratio':ratio})
# Closed scalar MGF checks without a matrix cutoff: exact binomial spectra.
for N in (1,2,3,5,10,20,40,80,160):
    x=np.array([N-2*k for k in range(N+1)],float)
    logp=np.array([math.lgamma(N+1)-math.lgamma(k+1)-math.lgamma(N-k+1)-N*np.log(2) for k in range(N+1)])
    for tv in (.05,.1,.2,.25,.4,.49):
        lg=float(logsumexp(logp+tv*x*x/N));bound=-.5*np.log(1-2*tv)
        assert lg<=bound+1e-10
        out['scalar_mgf_tests'].append({'N':N,'t_v2':tv,'log_mgf':lg,'upper':bound})
for n in range(1,129):
  for s in range(0,129):
    gamma=sum(mu(len(g)) for g in blocks(n,s))
    norm=np.sqrt((n+s)*(s+1))
    assert norm/np.sqrt(6)-1e-10<=gamma<=norm+1e-10
    out['group_scaling_tests']+=1
out['summary']={'gibbs_states':len(out['gibbs_tests']),'fixed_spectrum_orbit_maxima':len(out['orbit_tests']),
  'noncommuting_states':len(out['random_state_tests']),'scalar_mgfs':len(out['scalar_mgf_tests']),
  'balanced_partitions':out['group_scaling_tests'],'min_operator_square_difference_eigenvalue':min_psd,
  'max_conditional_rate_ratio':max_rate,'all_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['summary'],indent=2))
