"""Optimize the entropy-rate Hamiltonian for each sampled state.

This is an adversarial numerical consistency check, not an optimization over
all states and not an independent proof or review. Natural logarithms are used.
The support of sigma, not the support of rho, is retained when squaring K.
"""
from __future__ import annotations
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh, expm

RNG = np.random.default_rng(2026101601)
OUT = Path(__file__).resolve().parent

def random_unitary(d: int) -> np.ndarray:
    z = RNG.normal(size=(d,d)) + 1j*RNG.normal(size=(d,d))
    q,r = np.linalg.qr(z)
    return q * (np.diag(r)/np.abs(np.diag(r))).conj()

def spectral_log(a: np.ndarray, threshold: float=2e-14):
    p,u = eigh((a+a.conj().T)/2)
    if p.min() < -1e-11:
        raise ValueError('Matrix is not positive semidefinite.')
    p = np.maximum(p,0)
    logs = np.zeros_like(p)
    keep = p > threshold
    logs[keep] = np.log(p[keep])
    return (u*logs)@u.conj().T,p,u,keep

def inspect(rho: np.ndarray, da: int, db: int) -> dict:
    ra = np.trace(rho.reshape(da,db,da,db),axis1=1,axis2=3)
    sig = np.kron(ra,np.eye(db))
    lr,p,u,keep = spectral_log(rho)
    ls,s,v,skeep = spectral_log(sig)
    # If sigma has a kernel, it is outside the relevant support. The matrices
    # above use zero there; it never contributes to the rho-weighted moments.
    k = lr-ls
    m = float(np.trace(rho@k).real)
    m2 = float(np.trace(rho@k@k).real)
    var = max(0.,m2-m*m)
    overlaps = np.abs(u[:,keep].conj().T@v[:,skeep])**2
    pr = p[keep,None]*overlaps
    x = np.log(p[keep,None])-np.log(s[None,skeep])
    m2_overlap = float(np.sum(pr*x*x))
    ep = float(np.sum(pr*np.exp(x)))
    em = float(np.sum(pr*np.exp(-x)))
    # Q is the Hermitian coefficient of the entropy derivative as a linear
    # functional of h. Solve its weighted Hilbert-Schmidt dual exactly.
    Q = 1j*(rho@ls-ls@rho)
    qe = u.conj().T@Q@u
    den = p[:,None]+p[None,:]
    inv = np.divide(2.,den,out=np.zeros_like(den),where=den>2e-14)
    he = inv*qe
    h = u@he@u.conj().T
    energy2 = float(np.trace(rho@h@h).real)
    dual2 = float(np.sum(inv*np.abs(qe)**2))
    assert abs(energy2-dual2)<1e-8
    optimized_rate = np.sqrt(max(0.,dual2))
    residual = 0.
    if energy2 > 1e-18:
        h /= np.sqrt(energy2)
        rate = float(np.trace(h@Q).real)
        residual = abs(rate-optimized_rate)
        assert abs(np.trace(rho@h).real)<1e-8
        assert abs(np.trace(rho@h@h).real-1)<1e-8
        assert residual<1e-8
    assert abs(pr.sum()-1)<1e-10
    assert abs(m2-m2_overlap)<1e-8
    assert ep<=db+1e-9 and em<=db+1e-9
    assert m2<=2*(db-1)+1e-8
    assert var<=np.log(2*db*db+1)**2+1e-8
    assert dual2<=4*var+1e-8
    return {'da':da,'db':db,'rank':int(keep.sum()),'second_moment':m2,
            'variance':var,'optimized_rate_nats_at_unit_RMS':float(optimized_rate),
            'ratio_to_elementary_rate_bound':float(optimized_rate/(2*np.sqrt(2*(db-1)))),
            'ratio_to_Dupuis_Fawzi_rate_bound':float(optimized_rate/(2*np.log(2*db*db+1))),
            'spectral_formula_residual':abs(m2-m2_overlap),'dual_optimum_residual':residual}

def main() -> None:
    rows=[]
    for da in (2,3,4,8,16):
        for db in (2,3):
            d=da*db
            for repeat in range(18):
                u=random_unitary(d)
                if repeat%3==0:
                    rank=max(1,d//4)
                    p=np.r_[RNG.random(rank),np.zeros(d-rank)]
                elif repeat%3==1:
                    p=np.exp(RNG.uniform(-24,0,d))
                else:
                    p=RNG.random(d)
                p/=p.sum()
                rows.append(inspect((u*p)@u.conj().T,da,db))
    # Pure Schmidt states challenge support bookkeeping. Optimizing h is
    # analytical for each p; scan includes a tiny Schmidt probability.
    for da in (2,4,8):
        for prob in (1e-10,1e-7,.001,.01,.05,.083,.2,.5):
            psi=np.zeros(da*2,complex)
            psi[0]=np.sqrt(prob);psi[3]=np.sqrt(1-prob)
            rows.append(inspect(np.outer(psi,psi.conj()),da,2))
    result={'all_assertions_passed':True,'states_tested':len(rows),
            'qubit_bus_states_tested':sum(r['db']==2 for r in rows),
            'max_qubit_bus_optimized_rate_nats':max(r['optimized_rate_nats_at_unit_RMS'] for r in rows if r['db']==2),
            'max_ratio_to_elementary_bound':max(r['ratio_to_elementary_rate_bound'] for r in rows),
            'max_spectral_formula_residual':max(r['spectral_formula_residual'] for r in rows),
            'max_dual_optimum_residual':max(r['dual_optimum_residual'] for r in rows),
            'scope':'For every sampled state, optimize over all Hermitian h with Tr(rho h^2)=1. Not a global state optimization.',
            'seed':2026101601,'cases':rows}
    (OUT/'audit_conditional_rate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
