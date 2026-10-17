"""Full-matrix check of the two-qubit-gate compiled nine-data-qubit primitive."""
from pathlib import Path
import json,time
import numpy as np
from finite_control import execute_columns
start=time.monotonic();k=2;theta=.371;n=9;nq=n+1;dim=1<<nq
U=execute_columns(k,theta)
x=np.arange(dim);sign=(1-2*((x>>(nq-1))&1))*(1-2*(x&1))
U[x,x]-=np.exp(-1j*theta*sign)
# Unnormalized Frobenius norm is a rigorous upper bound on spectral norm.
fro=float(np.linalg.norm(U,'fro'))
assert fro<1e-11
out={'data_qubits':n,'bus_qubits':1,'full_input_columns':dim,
     'explicit_two_qubit_control_gates':390,
     'operator_error_upper_bound_by_unnormalized_Frobenius':fro,
     'maximum_entry_error':float(np.max(abs(U))),
     'runtime_seconds':time.monotonic()-start,
     'all_passed':True}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
