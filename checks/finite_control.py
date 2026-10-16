"""Finite-duration, ancilla-free compilation of the occupied-data bus construction.

Gates on disjoint pairs may run in parallel; all intra-register pairs are allowed.
Set delta = pi/(2G). X/CX gates take delta, controlled-sqrt(X) takes delta/2.
The bus contacts are off during this explicitly sequential control compilation.
Depth and duration statements describe this compiler, not an optimal-control bound.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence
import math
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
S=np.diag([1,1j]).astype(complex)
V=((1+1j)*I+(1-1j)*X)/2

def controlled(u:np.ndarray)->np.ndarray:
    out=np.eye(4,dtype=complex);out[2:,2:]=u;return out

MATRICES={'X':X,'CX':controlled(X),'CV':controlled(V),'CVdg':controlled(V.conj().T)}
@dataclass(frozen=True)
class Gate:
    name:str
    sites:tuple[int,...]

@dataclass(frozen=True)
class Layer:
    gates:tuple[Gate,...]
    duration_delta:float

@dataclass(frozen=True)
class Contact:
    time_J_units:float

Operation=Layer|Contact

def inverse_layer(layer:Layer)->Layer:
    inv={'X':'X','CX':'CX','CV':'CVdg','CVdg':'CV'}
    return Layer(tuple(Gate(inv[g.name],g.sites) for g in layer.gates),layer.duration_delta)

def merge_parallel(sequences:Sequence[list[Layer]])->list[Layer]:
    if not sequences:return []
    assert len({len(s) for s in sequences})==1
    layers=[]
    for i in range(len(sequences[0])):
        ds={s[i].duration_delta for s in sequences};assert len(ds)==1
        gs=tuple(g for s in sequences for g in s[i].gates)
        used=[q for g in gs for q in g.sites];assert len(used)==len(set(used))
        layers.append(Layer(gs,next(iter(ds))))
    return layers

def toffoli(triple:tuple[int,int,int])->list[Layer]:
    q,a,b=triple
    # Exponent of V on the target is b-(a xor b)+a=2ab.
    return [Layer((Gate('CV',(b,q)),),.5),
            Layer((Gate('CX',(a,b)),),1.),
            Layer((Gate('CVdg',(b,q)),),.5),
            Layer((Gate('CX',(a,b)),),1.),
            Layer((Gate('CV',(a,q)),),.5)]

def encode(triple:tuple[int,int,int],inverse:bool=False)->list[Layer]:
    q,a,b=triple
    ops=toffoli(triple)+[Layer((Gate('CX',(q,a)),),1.),Layer((Gate('CX',(q,b)),),1.)]
    return [inverse_layer(l) for l in reversed(ops)] if inverse else ops

def transition(triple:tuple[int,int,int],shift:int)->list[Layer]:
    """E X_shift E^dagger, compiled into four CNOT layers and one parallel X."""
    q,a,b=triple
    if shift==1: word=[(q,a),(a,q),(a,b),(q,a)];flipped=b
    elif shift==2: word=[(q,b),(b,q),(b,a),(q,b)];flipped=a
    elif shift==3: word=[(a,b),(b,q),(b,a),(a,b)];flipped=q
    else:raise ValueError('nonzero two-bit shift required')
    out=[Layer((Gate('CX',w),),1.) for w in word]
    assert flipped not in word[-1]
    out[-1]=Layer(out[-1].gates+(Gate('X',(flipped,)),),1.)
    return out

def compile_zz(k:int,theta:float=math.pi/4)->list[Operation]:
    if k<0:raise ValueError('k must be nonnegative')
    n=3**k;gain=1.5**k
    def sim(level:int,t:float)->list[Operation]:
        if level==0:return [Contact(t)]
        reps=list(range(0,n,3**(level-1)))
        triples=[tuple(reps[j:j+3]) for j in range(0,len(reps),3)]
        out:list[Operation]=list(merge_parallel([encode(tri) for tri in triples]))
        for idx in range(4):
            out.extend(sim(level-1,t/4))
            if idx<3:
                out.extend(merge_parallel([transition(tri,(1,2,1)[idx]) for tri in triples]))
        out.extend(merge_parallel([encode(tri,True) for tri in triples]))
        out.append(Layer(tuple(Gate('X',(tri[1],)) for tri in triples),1.))
        return out
    return sim(k,theta/gain)

def apply_gate_columns(U:np.ndarray,gate:Gate,nq:int)->np.ndarray:
    """Apply a small gate to all supplied input columns."""
    sites=gate.sites;r=len(sites);cols=U.shape[1]
    axes=list(sites)+[i for i in range(nq) if i not in sites]+[nq]
    v=np.transpose(U.reshape((2,)*nq+(cols,)),axes)
    out=MATRICES[gate.name]@v.reshape(1<<r,-1)
    return np.transpose(out.reshape((2,)*nq+(cols,)),np.argsort(axes)).reshape(1<<nq,cols)

def execute_columns(k:int,theta:float=math.pi/4,columns:np.ndarray|None=None)->np.ndarray:
    n=3**k;nq=n+1;dim=1<<nq
    U=np.eye(dim,dtype=complex) if columns is None else np.asarray(columns,dtype=complex).copy()
    basis=np.arange(dim);bits=((basis[:,None]>>np.arange(nq-1,-1,-1))&1)
    raw=(n-2*bits[:,:n].sum(axis=1))*(1-2*bits[:,n])
    for op in compile_zz(k,theta):
        if isinstance(op,Contact):U*=np.exp(-1j*op.time_J_units*raw)[:,None]
        else:
            for gate in op.gates:U=apply_gate_columns(U,gate,nq)
    return U

def costs(k:int)->dict:
    ops=compile_zz(k)
    layers=[op for op in ops if isinstance(op,Layer)]
    contacts=[op for op in ops if isinstance(op,Contact)]
    counts={name:sum(g.name==name for op in layers for g in op.gates) for name in MATRICES}
    return {'k':k,'helpers_including_target':3**k,'gain':1.5**k,
            'contact_intervals':len(contacts),'control_layers':len(layers),
            'control_duration_delta':sum(op.duration_delta for op in layers),
            'control_gate_count':sum(counts.values()),'gate_counts':counts,
            'contact_time_J_units':sum(op.time_J_units for op in contacts)}

def per_swap_ratio(k:int,R:float)->float:
    """Ratio to a direct norm-J SWAP; excludes common final register permutation."""
    if R<=0:raise ValueError('R=G/J must be positive')
    if k==0:return 1.
    return 1.5**(1-k)+(24*4**k-20)/R

def route_time(n:int,R:float,k:int)->float:
    """JT for the buffered routing schedule. J is the time unit."""
    if n<1 or k<0 or 3**k>n:raise ValueError('require 1 <= 3**k <= n')
    return (2*n+1)*math.pi/2*per_swap_ratio(k,R)+(math.pi/R if n>1 else 0.)

def best_compiled(n:int,R:float)->dict:
    choices=[(route_time(n,R,k),k) for k in range(int(math.log(n,3)+1e-10)+1)]
    t,k=min(choices)
    seq=route_time(n,R,0)
    return {'n':n,'G_over_J':R,'best_k_within_family':k,'block_size':3**k,
            'JT_compiled':t,'JT_sequential':seq,'time_ratio':t/seq,
            'per_bus_swap_ratio':per_swap_ratio(k,R)}
