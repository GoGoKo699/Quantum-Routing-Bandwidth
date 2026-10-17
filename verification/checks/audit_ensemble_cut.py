"""Checks of a weighted multiple-bus 1-design entropy-rate inequality.

Every ensemble is all columns of ONE unitary with equal probabilities. A
state-dependent control choice would invalidate the argument and is not used.
Six physical qubits: L=(0,1), R=(2,3), C=(4,5). No initialized workspace.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, expm

RNG=np.random.default_rng(2026101602)
ROOT=Path(__file__).resolve().parent
I=np.eye(2,dtype=complex)
PAULI=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.]).astype(complex)]
N=6;D=2**N

def embed(op: np.ndarray,sites: tuple[int,...]) -> np.ndarray:
    rest=tuple(j for j in range(N) if j not in sites)
    order=sites+rest
    reverse=np.argsort(order)
    tensor=np.kron(op,np.eye(2**len(rest))).reshape([2]*(2*N))
    return tensor.transpose(list(reverse)+list(reverse+N)).reshape(D,D)

def random_h(d:int,strength:float) -> np.ndarray:
    a=RNG.normal(size=(d,d))+1j*RNG.normal(size=(d,d))
    a=(a+a.conj().T)/2
    a-=np.eye(d)*np.trace(a)/d
    return a*(strength/max(abs(eigh(a,eigvals_only=True))))

def correlation_h(strength:float) -> np.ndarray:
    out=sum(RNG.normal()*np.kron(p,q) for p in PAULI for q in PAULI)
    return out*(strength/max(abs(eigh(out,eigvals_only=True)))) if strength else out*0

def marginal_l(psi:np.ndarray) -> np.ndarray:
    m=psi.reshape(4,16)
    return m@m.conj().T

def log_psd(rho:np.ndarray) -> np.ndarray:
    p,u=eigh(rho)
    if p.min()<-1e-10: raise ValueError('Non-positive reduced state.')
    return (u*np.log(np.maximum(p,1e-15)))@u.conj().T

def entropy_l(psi:np.ndarray) -> float:
    p=eigh(marginal_l(psi),eigvals_only=True)
    p=p[p>1e-14]
    return float(-np.sum(p*np.log2(p)))

def main() -> None:
    U=np.eye(D,dtype=complex)
    weights=np.array([[1.,.3],[.7,.2]])
    rows=[]
    for segment in range(18):
        left=[];H=np.zeros((D,D),complex)
        for c in range(2):
            h=sum(embed(correlation_h(weights[j,c]),(j,4+c)) for j in range(2))
            left.append(h);H+=h
            for j in range(2):
                H+=embed(correlation_h(float(RNG.uniform(.1,1))),(2+j,4+c))
        strength=(.1,10.,500.)[segment%3]
        for sites in ((0,1),(2,3),(4,5)):
            H+=embed(random_h(4,strength),sites)
        duration=float(RNG.uniform(.002,.04))
        U=expm(-1j*duration*H)@U
        assert np.linalg.norm(U@U.conj().T-np.eye(D))<5e-11
        norms=np.array([np.linalg.norm(h,'fro')/np.sqrt(D) for h in left])
        elementary_bound=float(2*np.sqrt(2)/np.log(2)*norms.sum())
        published_bound=float(2*np.log2(9)*norms.sum())
        weighted_bound=float(2*np.sqrt(2)/np.log(2)*sum(np.linalg.norm(weights[:,c]) for c in range(2)))
        rates=[];pieces=[];moments=[];fd_errors=[]
        dt=1e-7/max(1.,strength/10)
        plus=expm(-1j*dt*H)@U;minus=expm(1j*dt*H)@U
        for col in range(D):
            psi=U[:,col]
            logL=np.kron(log_psd(marginal_l(psi)),np.eye(16))
            # dot S = -2 Im <psi| log(rho_L) H |psi> / ln2.
            rate=float(-2*np.imag(np.vdot(psi,logL@H@psi))/np.log(2))
            pc=[float(-2*np.imag(np.vdot(psi,logL@h@psi))/np.log(2)) for h in left]
            assert abs(sum(pc)-rate)<1e-9
            fd=(entropy_l(plus[:,col])-entropy_l(minus[:,col]))/(2*dt)
            fd_errors.append(abs(fd-rate))
            rates.append(rate);pieces.append(pc)
            moments.append([float(np.vdot(h@psi,h@psi).real) for h in left])
        avg_abs=float(np.mean(np.abs(rates)))
        avg_pieces=np.mean(np.abs(pieces),axis=0)
        moment_average=np.mean(moments,axis=0)
        assert np.max(abs(moment_average-norms**2))<1e-9
        assert np.all(avg_pieces<=2*np.sqrt(2)/np.log(2)*norms+1e-9)
        assert avg_abs<=elementary_bound+1e-9 and elementary_bound<=weighted_bound+1e-9
        rows.append({'segment':segment,'internal_strength':strength,'duration':duration,
                     'ensemble_size':D,'average_absolute_entropy_rate_bits':avg_abs,
                     'elementary_bound_bits':elementary_bound,'published_variance_bound_bits':published_bound,
                     'weighted_edge_bound_bits':weighted_bound,
                     'maximum_finite_difference_residual':max(fd_errors),
                     'flat_average_moment_residual':float(np.max(abs(moment_average-norms**2)))})
    # This explicitly defeats an incorrect input-uniform O(sqrt(n)) claim.
    n=64;p=.1
    special_rate=2*n*np.sqrt(p*(1-p))*np.log2((1-p)/p)
    false_flat_bound=2*np.sqrt(2)/np.log(2)*np.sqrt(n)
    result={'all_assertions_passed':True,'segments':len(rows),'pure_states_checked':len(rows)*D,
            'maximum_finite_difference_residual':max(r['maximum_finite_difference_residual'] for r in rows),
            'maximum_flat_moment_residual':max(r['flat_average_moment_residual'] for r in rows),
            'maximum_observed_bound_ratio':max(r['average_absolute_entropy_rate_bits']/r['elementary_bound_bits'] for r in rows),
            'selected_GHZ_state':{'n':n,'p':p,'actual_entropy_rate_bits':special_rate,
                                  'incorrect_1design_bound_for_a_single_state':false_flat_bound,
                                  'rejects_incorrect_uniform_bound':bool(special_rate>false_flat_bound)},
            'scope':'A common input-independent unitary and nonuniform pairwise contacts; two bus qubits. Not a theorem inferred from numerics.',
            'seed':2026101602,'cases':rows}
    (ROOT/'audit_ensemble_cut.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':main()
