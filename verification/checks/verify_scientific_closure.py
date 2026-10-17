"""Finite certificates and composition checks for the manuscript's stated model.

Exact integer arithmetic certifies rational preparation tails. Random-list
checks verify uniform finite identities, not asymptotic correctness. Reuse
checks retain fresh payloads and fixed helper purifications. No experiment or
large quantum circuit simulation is represented by a large spectral example.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json
import math
import numpy as np
from scipy.linalg import expm
from verify_mixed_helpers import (
    spectral_tail, extractable, route_blocks, weights, block_gain, deficit,
)
from verify_workspace_construction import mu, embed


@lru_cache(maxsize=None)
def rational_spectrum(s: int, a: int, b: int):
    """Shell counts, integer shell weights, and integer tails for p=a/b."""
    if s < 0 or not 0 <= 2*a <= b or b <= 0:
        raise ValueError('Need s>=0, b>0 and 0<=a/b<=1/2')
    cc = [math.comb(s, k) for k in range(s+1)]
    ww = [cc[k]*a**k*(b-a)**(s-k) for k in range(s+1)]
    tails = [0]*(s+2)
    for k in range(s, -1, -1):
        tails[k] = tails[k+1]+ww[k]
    assert tails[0] == b**s
    return cc, ww, tails


def exact_tail(s: int, a: int, b: int, r: int) -> Fraction:
    if not 0 <= r <= s:
        raise ValueError('0<=r<=s required')
    cc, _, tails = rational_spectrum(s, a, b)
    remaining = 1 << (s-r)
    for k, count in enumerate(cc):
        if remaining >= count:
            remaining -= count
        else:
            numerator = tails[k+1]+(count-remaining)*a**k*(b-a)**(s-k)
            return Fraction(numerator, b**s)
    return Fraction(0)


def exact_extractable(s: int, a: int, b: int, delta: Fraction) -> int:
    lo, hi = 0, s
    while lo < hi:
        mid = (lo+hi+1)//2
        if exact_tail(s, a, b, mid) <= delta:
            lo = mid
        else:
            hi = mid-1
    return lo


def exact_gain(N: int, r: int) -> Fraction:
    b, extra = divmod(N, r+1)
    def exact_mu(k):
        return Fraction(k*math.comb(k-1,(k-1)//2), 2**(k-1))
    return (r+1-extra)*exact_mu(b)+extra*exact_mu(b+1)


def ceil_sqrt(N: int) -> int:
    k = math.isqrt(N)
    return k if k*k == N else k+1


def finite_certificates() -> list[dict]:
    epsilon = Fraction(1,100)
    delta = epsilon*epsilon/8
    out = []
    for s in (128,256,512,1024,2048):
        n=s; N=n+s
        r=exact_extractable(s,1,10,delta)
        q=exact_tail(s,1,10,r)
        assert q <= delta
        if r<s:
            assert exact_tail(s,1,10,r+1)>delta
        gain=exact_gain(N,r)
        squared_error=4*(2*q-q*q)
        assert squared_error <= epsilon*epsilon
        # Rigorous rational roundings: pi<22/7, c0=2sqrt(2)/ln2<41/10,
        # h2(1/100)<1/10. A maximally mixed arbitrary bus gives kappa=1.
        upper=Fraction(3)*Fraction(22,7)*(2*n+1)/(4*gain)
        lower=(Fraction(49,25)*n-Fraction(3,20))/(Fraction(41,10)*ceil_sqrt(N))
        factor=lower/upper
        published_lower=(Fraction(49,25)*n-Fraction(3,20))/(Fraction(32,5)*ceil_sqrt(N))
        out.append({'n':n,'s':s,'p':'1/10','half_diamond_budget':'1/100',
            'compressed_prefix_bits':r,'gain_exact':str(gain),
            'exact_intervals_per_Ising':1<<((N+r)//(r+1)-1),
            'total_contact_intervals':3*(2*n+1)*(1<<((N+r)//(r+1)-1)),
            'bad_weight_approx':float(q),'purified_error_bound_approx':math.sqrt(float(squared_error)),
            'mixed_JT_upper_exact':str(upper),'unknown_JT_lower_exact':str(lower),
            'certified_time_advantage_lower_exact':str(factor),
            'mixed_JT_upper':float(upper),'unknown_JT_lower':float(lower),
            'certified_time_advantage_lower':float(factor),
            'unknown_JT_lower_published_exact':str(published_lower),
            'published_constant_advantage_lower_exact':str(published_lower/upper),
            'published_constant_advantage_lower':float(published_lower/upper),
            'strict_advantage_over_all_unknown_helper_protocols':bool(factor>1)})
    assert any(row['strict_advantage_over_all_unknown_helper_protocols'] for row in out)
    return out


def averaged_coefficients(N:int,r:int,selected:np.ndarray):
    """All physical-basis coefficients after sign encoding and leader fanout.

    Leaders occupy the first r+1 bits, and nonleaders are spectator bits.
    Translations are selected once and physically used in a coherent sequence.
    """
    m=r+1; spectators=N-m
    sizes=[N//m+int(i<N%m) for i in range(m)]
    labels=np.arange(1<<N,dtype=np.int64)
    bits=((labels[:,None]>>np.arange(N-1,-1,-1))&1)
    leader_sign=1-2*bits[:,:m]
    # Decode the fanout: helper leader signs become Z_target*Z_helper.
    leader_sign[:,1:] *= leader_sign[:,[0]]
    average=np.zeros(1<<N)
    exact=sum(mu(b)*leader_sign[:,i] for i,b in enumerate(sizes))
    for shift in selected:
        shift_bits=(int(shift)>>np.arange(spectators-1,-1,-1))&1
        spec=bits[:,m:]^shift_bits
        total=np.zeros(1<<N);start=0
        for i,b in enumerate(sizes):
            w=spec[:,start:start+b-1].sum(axis=1)
            total += leader_sign[:,i]*abs(b-2*w)
            start += b-1
        average += total/len(selected)
    return average,exact,sum(mu(b) for b in sizes)


def list_certificate(N:int,n:int,r:int,eta:float,offline_failure:float)->int:
    if N<n or not 0<=r<N or not 0<eta<1 or not 0<offline_failure<1:
        raise ValueError('Invalid list-bound inputs')
    gamma=block_gain(N,r);M=3*(2*n+1);theta=math.pi/4
    a=eta*gamma/(M*theta)
    return math.ceil(2*N*N/(a*a)*((N+1)*math.log(2)+math.log(1/offline_failure)))


def uniform_list_checks()->list[dict]:
    rng=np.random.default_rng(2026101611)
    out=[]
    for N,r in ((3,0),(5,1),(7,2),(8,3),(8,7)):
        dim=1<<(N-r-1)
        full,exact,gamma=averaged_coefficients(N,r,np.arange(dim))
        assert np.max(abs(full-exact))<1e-12
        sizes=[N//(r+1)+int(i<N%(r+1)) for i in range(r+1)]
        Ksync=1<<max(b-1 for b in sizes)
        shifts=[]
        for u in range(Ksync):
            shift=0
            for b in sizes:
                shift=(shift<<(b-1))|(u&((1<<(b-1))-1))
            shifts.append(shift)
        synchronized,_,_=averaged_coefficients(N,r,np.array(shifts))
        assert np.max(abs(synchronized-exact))<1e-12
        for K in (8,32,128):
            selected=rng.integers(0,dim,size=K)
            avg,ex,gamma=averaged_coefficients(N,r,selected)
            deviation=float(np.max(abs(avg-ex)))
            error=float(np.max(abs(np.exp(-1j*math.pi*avg/(4*gamma))-np.exp(-1j*math.pi*ex/(4*gamma)))))
            bound=math.pi*deviation/(4*gamma)
            assert error<=bound+1e-12
            out.append({'module_qubits':N,'helper_leaders':r,'samples':K,
                'uniform_diagonal_deviation':deviation,'full_operator_error':error,
                'operator_error_upper':bound,'full_averaging_identity':True,'synchronized_exact_intervals':Ksync,
                'synchronized_generator_error':float(np.max(abs(synchronized-exact)))})
    return out


def fresh_payload_checks()->list[dict]:
    """Two separate payload batches, arbitrary correlations via full isometries."""
    matrices,row=route_blocks(1,3,1)
    target=row['target']
    qubits=5; dim=1<<qubits # L1,R1,L2,R2,C
    ideal=embed(target,(2,3,4),qubits)@embed(target,(0,1,4),qubits)
    out=[]
    for p in (.01,.1,.4):
        qq=np.kron(weights(3,p),weights(3,p))
        gram=np.zeros((dim,dim),complex)
        for q,V in zip(qq,matrices):
            actual=embed(V,(2,3,4),qubits)@embed(V,(0,1,4),qubits)
            e=actual-ideal
            gram+=q*(e.conj().T@e)
        error=math.sqrt(max(0,float(np.linalg.eigvalsh(gram)[-1])))
        tail=spectral_tail(3,p,1);bound=2*math.sqrt(2*tail-tail*tail)
        assert error<=bound+1e-11
        out.append({'fresh_payload_batches':2,'n_per_module_per_batch':1,'s':3,'p':p,
            'payload_bus_input_columns':dim,'helper_sectors':64,
            'purified_isometry_operator_error':error,'same_preparation_bound':bound})
    return out


def perturbation_checks()->list[dict]:
    rng=np.random.default_rng(2026101612);out=[]
    for rep in range(12):
        def herm():
            A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
            return (A+A.conj().T)/2
        H=herm();E=.01*herm();t=float(rng.uniform(.05,2))
        gap=float(np.linalg.norm(expm(-1j*t*(H+E))-expm(-1j*t*H),2))
        bound=t*float(np.linalg.norm(E,2))
        assert gap<=bound+1e-12
        out.append({'time':t,'operator_error':gap,'Duhamel_upper':bound})
    return out


def main():
    integer_checks=0
    for s in range(1,11):
        for a,b in ((0,10),(1,10),(1,4),(1,2)):
            for r in range(s+1):
                q=exact_tail(s,a,b,r)
                assert abs(float(q)-spectral_tail(s,a/b,r))<1e-12
                integer_checks+=1
    certificates=finite_certificates()
    # Simple analytic constant inequalities used for rational enclosures.
    assert 2*math.sqrt(2)/math.log(2)<4.1
    assert 9**5<2**16  # c_DF=2log2(9)<32/5, using exact integers
    assert 1-deficit(.01)<.1
    out={'all_passed':True,'scope':'Exact rational spectral certification, finite operator checks and analytical timing bounds; no external review or hardware performance claim.',
        'exact_spectral_crosschecks':integer_checks,'finite_certificates':certificates,
        'uniform_list_checks':uniform_list_checks(),'fresh_payload_reuse':fresh_payload_checks(),
        'perturbation_checks':perturbation_checks(),
        'sample_count_examples':[{'n':n,'s':s,'r':r,'sufficient_list_length':list_certificate(n+s,n,r,.005,.01)}
            for n,s,r in ((16,16,0),(256,256,82),(1024,1024,400))]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('uniform_list_checks','perturbation_checks')},indent=2))

if __name__=='__main__':
    main()
