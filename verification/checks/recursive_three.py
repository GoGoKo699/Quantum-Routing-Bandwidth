"""Full-basis check of a small-gate, exact, recursive control construction.

Each three-data-qubit encoding is one Toffoli plus two CNOTs. Local controls
are still charged zero duration. Monomial propagation avoids dense matrices.
"""
from pathlib import Path
import json
import numpy as np

def run(level:int)->dict:
    n=3**level; nq=n+1; d=1<<nq
    perm=np.arange(d,dtype=np.int64); phase=np.ones(d,complex)
    counts={'raw_contact_intervals':0,'local_X':0,'local_CNOT':0,'local_Toffoli':0}
    def bit(a,s): return (a>>(nq-1-s))&1
    def xx(s):
        nonlocal perm
        perm^=1<<(nq-1-s);counts['local_X']+=1
    def cx(a,b):
        nonlocal perm
        perm^=bit(perm,a)<<(nq-1-b);counts['local_CNOT']+=1
    def ccx(a,b,c):
        nonlocal perm
        perm^=(bit(perm,a)&bit(perm,b))<<(nq-1-c);counts['local_Toffoli']+=1
    def enc(triple,inverse=False):
        q,a,b=triple
        if inverse:
            cx(q,b);cx(q,a);ccx(a,b,q)
        else:
            ccx(a,b,q);cx(q,a);cx(q,b)
    def sim(ell,t):
        nonlocal phase
        if ell==0:
            mag=sum(1-2*bit(perm,s) for s in range(n))
            phase*=np.exp(-1j*t*mag*(1-2*bit(perm,n)))
            counts['raw_contact_intervals']+=1
            return
        reps=list(range(0,n,3**(ell-1)))
        triples=[tuple(reps[j:j+3]) for j in range(0,len(reps),3)]
        for shift in range(4):
            for q,a,b in triples:
                if shift&2:xx(a)
                if shift&1:xx(b)
            for tri in triples: enc(tri)
            sim(ell-1,t/4)
            for tri in reversed(triples):enc(tri,True)
            for q,a,b in triples:
                if shift&2:xx(a)
                if shift&1:xx(b)
    gain=1.5**level;t=np.pi/(4*gain)
    sim(level,t)
    target=np.exp(-1j*np.pi/4*(1-2*bit(np.arange(d),0))*(1-2*bit(np.arange(d),n)))
    assert np.array_equal(perm,np.arange(d))
    err=float(np.max(np.abs(phase-target)))
    assert err<1e-11
    return {'level':level,'data_qubits':n,'physical_qubits_including_bus':nq,
      'gain':gain,'contact_time_for_pi_over_4_ZZ':t,
      'full_operator_error':err,'basis_states_checked':d,**counts}
rows=[run(k) for k in (0,1,2)]
out={'all_passed':True,'checks':rows,
  'routing_time_scaling_exponent':float(np.log(2)/np.log(3)),
  'note':'All durations of local X/CNOT/Toffoli are excluded; this is not a wall-clock speedup theorem.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
