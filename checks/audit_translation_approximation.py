"""Check the deterministic operator-error bound for sampled coherent translations.

Sampling selects ONE control list offline. Physical gates are coherent and no
measurement outcomes or randomly mixed channels are used. Small-n enumeration
checks the uniform bound; it does not establish asymptotic validity by itself.
"""
from __future__ import annotations
from pathlib import Path
import json,math
import numpy as np

RNG=np.random.default_rng(2026101603)
ROOT=Path(__file__).resolve().parent
THETA=np.pi/4

def mu(n:int) -> float:
    return n*math.comb(n-1,(n-1)//2)/2**(n-1)

def guarantee(n:int,error:float,failure:float) -> int:
    if n<2 or not 0<error<1 or not 0<failure<1:
        raise ValueError('n>=2 and error, failure in (0,1) are required.')
    gates=3*(2*n+1)
    tolerance=error*mu(n)/(gates*THETA)
    return math.ceil(n*n/(2*tolerance*tolerance)*((n-1)*math.log(2)+math.log(2/failure)))

def main() -> None:
    cases=[]
    for n in range(2,13):
        dim=2**(n-1)
        labels=np.arange(dim,dtype=np.int64)
        diagonal=np.array([abs(n-2*int(x).bit_count()) for x in labels],float)
        assert abs(diagonal.mean()-mu(n))<1e-12
        for samples in (32,128,512):
            selected=RNG.integers(0,dim,size=samples)
            average=sum(diagonal[labels^s] for s in selected)/samples
            deviation=float(np.max(abs(average-mu(n))))
            error=float(np.max(abs(np.exp(-1j*THETA*average/mu(n))-np.exp(-1j*THETA))))
            bound=THETA*deviation/mu(n)
            assert error<=bound+1e-13
            # Isospectrality makes every translation have the same trace norm;
            # averaging attains mu. This checks the constructive majorization
            # condition but is not a theorem about general finite-gate control.
            spectrum=np.array([n-2*w for w in range(n+1) for _ in range(math.comb(n,w))])
            top_half=np.sort(spectrum)[2**(n-1):].sum()/2**(n-1)
            assert abs(top_half-mu(n))<1e-12
            cases.append({'n':n,'samples':samples,'max_diagonal_deviation':deviation,
                          'operator_error_one_Ising_gate':error,'analytic_operator_error_bound':bound})
    counts=[{'n':n,'operator_error_budget':.01,'offline_failure_probability':.01,
             'guaranteed_samples_per_Ising':guarantee(n,.01,.01),
             'exact_samples_per_Ising':2**(n-1)} for n in (3,9,27,81)]
    result={'all_assertions_passed':True,'uniform_small_n_checks':len(cases),
            'maximum_operator_error_bound_violation':max(r['operator_error_one_Ising_gate']-r['analytic_operator_error_bound'] for r in cases),
            'asymptotic_samples_per_Ising':'O(n^4 / error^2) at fixed offline failure probability',
            'asymptotic_total_contact_intervals':'O(n^5 / error^2)',
            'caution':'The concentration constants are large. This does not give finite-speed efficiency or an elementary compilation of the global encoding.',
            'guaranteed_counts':counts,'seed':2026101603,'cases':cases}
    (ROOT/'audit_translation_approximation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
