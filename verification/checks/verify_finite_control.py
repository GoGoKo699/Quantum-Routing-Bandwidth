"""Executed checks of the finite-control construction and analytic cost formulas."""
from pathlib import Path
import json,math
import numpy as np
from scipy.linalg import expm
from finite_control import *
ROOT=Path(__file__).resolve().parent

def layer_product(ops,nq=3):
    U=np.eye(1<<nq,dtype=complex)
    for op in ops:
        for gate in op.gates:U=apply_gate_columns(U,gate,nq)
    return U

# Exact five-two-qubit gate Toffoli, with no auxiliary system.
T=np.eye(8,dtype=complex);T[:,[3,7]]=T[:,[7,3]]
err_t=float(np.linalg.norm(layer_product(toffoli((0,1,2)))-T,2))
assert err_t<1e-13
E=layer_product(encode((0,1,2)));inv=layer_product(encode((0,1,2),True))
assert np.linalg.norm(inv@E-np.eye(8),2)<1e-13
transition_checks=[]
for shift in (1,2,3):
    P=np.eye(8,dtype=complex)[:,np.arange(8)^shift]
    err=float(np.linalg.norm(layer_product(transition((0,1,2),shift))-E@P@E.conj().T,2))
    assert err<1e-13;transition_checks.append({'shift':shift,'operator_error':err})

# Physical bounded generators realizing all primitive gates up to global phase.
# Delta=pi/2 at G=1. Controlled V has a spectrum {1,1,1,i}, so needs Delta/2.
generator_checks=[]
for name,U in MATRICES.items():
    if name in ('X','CX'):h=U;dt=math.pi/2
    else:
        P=np.kron(np.diag([0.,1.]),(I-X)/2)
        h=np.eye(4)-2*P
        if name=='CVdg':h=-h
        dt=math.pi/4
    actual=expm(-1j*h*dt);overlap=np.trace(U.conj().T@actual)/len(U)
    err=float(np.linalg.norm(actual-overlap*U,2))
    assert err<1e-13 and np.linalg.norm(h,2)<=1+1e-13
    generator_checks.append({'gate':name,'generator_norm':float(np.linalg.norm(h,2)),
                             'time_G_units':dt,'operator_error_up_to_global_phase':err})

cost_rows=[costs(k) for k in range(4)]
for row in cost_rows:
    k=row['k']
    assert row['control_duration_delta']==8*(4**k-1)
    assert row['contact_intervals']==4**k
    assert row['control_gate_count']==30*(12**k-1)//11
    assert abs(row['contact_time_J_units']-math.pi/(4*1.5**k))<1e-13

# Complete matrices with explicitly decomposed two-qubit controls at k=0,1.
operator_checks=[]
for k in (0,1):
    n=3**k;nq=n+1;d=1<<nq;theta=.371
    U=execute_columns(k,theta)
    idx=np.arange(d);sign=(1-2*((idx>>(nq-1))&1))*(1-2*(idx&1))
    target=np.diag(np.exp(-1j*theta*sign))
    err=float(np.linalg.norm(U-target,2));assert err<1e-12
    operator_checks.append({'k':k,'dimension':d,'operator_error':err})

# The buffered schedule uses 2n+1 bus swaps, then two involutions in L.
# Verify exact wire permutations including arbitrary bus input.
route_checks=[]
for n in range(1,101):
    state=list(range(2*n+1));bus=2*n
    swap_sites=[]
    for j in range(n):
        for q in (j,n+j):state[q],state[bus]=state[bus],state[q];swap_sites.append(q)
    state[0],state[bus]=state[bus],state[0];swap_sites.append(0)
    if n>1:
        # x -> -x, followed by x -> -x-1: net positional shift x -> x-1.
        for offset in (0,-1):
            for j in range(n):
                p=(offset-j)%n
                if j<p:state[j],state[p]=state[p],state[j]
    target=list(range(n,2*n))+list(range(n))+[bus]
    assert state==target and len(swap_sites)==2*n+1
    if n in (1,2,3,9,100):route_checks.append({'n':n,'bus_swaps':len(swap_sites),'full_wire_permutation_correct':True})

sweep=[best_compiled(3**10,R) for R in (1.,10.,100.,1e3,1e4,1e5,1e6,1e8)]
for n in (9,27,81,243):
    for R in (100.,1000.,10000.):
        # Same fixed R gives an n-independent optimum once its block fits.
        assert best_compiled(n,R)['best_k_within_family']<=3
nu=math.log(1.5)/math.log(6)
out={'all_passed':True,'scope':'Analytical construction and numerical consistency checks, not optimal-control or hardware certification.',
     'toffoli_operator_error':err_t,'transition_checks':transition_checks,
     'bounded_generator_checks':generator_checks,'cost_rows':cost_rows,
     'full_operator_checks':operator_checks,'buffered_route_checks':route_checks,
     'clock_sweep':sweep,'first_compiled_speedup_threshold_R':1092.,
     'control_speed_exponent_nu':nu,'full_size_recursive_control_rate_exponent':math.log(6)/math.log(3)}
(ROOT/'finite_control_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
