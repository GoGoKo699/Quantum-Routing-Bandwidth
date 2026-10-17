"""Uniform spectral compression and reference-preserving noisy-helper routing.

No preparation samples are measured. A known permutation compresses helper
labels once; the existing raw-contact construction acts exactly on the good
subspace. Every helper sector and payload input column is checked below.
Fixed-input helper purifications are retained in the operator-error test.
"""
from __future__ import annotations
from bisect import bisect_left
from functools import lru_cache
import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import binom
from scipy.optimize import brentq
from verify_workspace_construction import compiled_swap, embed, mu, apply_local


def deficit(p: float) -> float:
    if not 0 <= p <= .5:
        raise ValueError('p must lie in [0, 1/2]')
    beta = 1 - 2*p
    if beta < .1:
        # Positive series avoids cancellation close to a maximally mixed qubit.
        return sum(beta**(2*k)/(2*k*(2*k-1)) for k in range(1, 12))/math.log(2)
    if p == 0:
        return 1.
    return 1 + (p*math.log(p)+(1-p)*math.log1p(-p))/math.log(2)


@lru_cache(maxsize=None)
def counts(s: int) -> tuple[int, ...]:
    if s < 0:
        raise ValueError('Nonnegative helper count required')
    acc = 0
    out = []
    for k in range(s+1):
        acc += math.comb(s, k)
        out.append(acc)
    return tuple(out)


def spectral_tail(s: int, p: float, r: int) -> float:
    """Exact binomial-shell sum outside the largest 2**(s-r) eigenvalues."""
    if not 0 <= r <= s or not 0 <= p <= .5:
        raise ValueError('Need 0<=r<=s and 0<=p<=1/2')
    if r == 0 or p == 0:
        return 0.
    rank = 1 << (s-r)
    cc = counts(s)
    k = bisect_left(cc, rank)
    included = rank - (cc[k-1] if k else 0)
    excluded = math.comb(s, k) - included
    partial = 0. if not excluded else math.exp(math.log(excluded)+k*math.log(p)+(s-k)*math.log1p(-p))
    return float(binom.sf(k, s, p) + partial)


def extractable(s: int, p: float, delta: float) -> int:
    if not 0 < delta < 1:
        raise ValueError('delta must lie in (0,1)')
    lo, hi = 0, s
    while lo < hi:
        mid = (lo+hi+1)//2
        if spectral_tail(s, p, mid) <= delta:
            lo = mid
        else:
            hi = mid-1
    return lo


def hoeffding_choice(s: int, p: float, delta: float) -> int:
    """Conservative constructive count used in the uniform asymptotic proof."""
    x = s*(1-2*p)**2
    return math.floor(x/(8*math.log(2))) if x >= 8*math.log(1/delta) else 0


def compression(s: int) -> np.ndarray:
    """Output label of each input; a full permutation needing no workspace."""
    order = sorted(range(1 << s), key=lambda x: (x.bit_count(), x))
    perm = np.empty(1 << s, dtype=int)
    perm[order] = np.arange(1 << s)
    return perm


def weights(s: int, p: float) -> np.ndarray:
    return np.array([p**x.bit_count()*(1-p)**(s-x.bit_count()) for x in range(1 << s)])


def block_gain(N: int, r: int) -> float:
    b, extra = divmod(N, r+1)
    return (r+1-extra)*mu(b) + extra*mu(b+1)


def route_blocks(n: int, s: int, r: int) -> tuple[list[np.ndarray], dict]:
    """Propagate every helper block using the actual coherent contact sequence.

    `compiled_swap` uses physical raw Ising intervals and encoding permutations,
    not a target effective gate. Its first N-r qubits include all entropy-bearing
    helper spectators. It commutes with each helper Z after the whole gate.
    """
    if not 0 <= r <= s:
        raise ValueError('0<=r<=s required')
    N = n+s
    U, gate_time, _ = compiled_swap(N-r, r)
    compress = compression(s)
    d = 1 << (n+1)
    local = []
    max_return = 0.
    for x in range(1 << s):
        y = int(compress[x])
        clean = y >> (s-r)
        entropy = y & ((1 << (s-r))-1)
        physical = (entropy << r) | clean
        inds = np.array([((a << s) | physical)*2+c for a in range(1 << n) for c in (0, 1)])
        V = U[np.ix_(inds, inds)]
        other = U[:, inds].copy()
        other[inds] = 0
        max_return = max(max_return, float(np.linalg.norm(other, 'fro')))
        assert np.linalg.norm(V.conj().T@V-np.eye(d), 'fro') < 1e-11
        local.append(V)
    assert max_return < 1e-11

    nq = 2*n+1
    dim = 1 << nq
    target = np.zeros((dim, dim), complex)
    for l in range(1 << n):
        for rr in range(1 << n):
            for c in (0, 1):
                x = (l << (n+1)) | (rr << 1) | c
                y = (rr << (n+1)) | (l << 1) | c
                target[y, x] = 1
    target *= np.exp(-1j*(2*n+1)*np.pi/4)
    shift = np.arange(dim)
    for x in range(dim):
        left = x >> (n+1)
        rotated = ((left << 1) & ((1 << n)-1)) | (left >> (n-1))
        shift[x] = (rotated << (n+1)) | (x & ((1 << (n+1))-1))
    out = []
    max_good = 0.
    for xl in range(1 << s):
        for xr in range(1 << s):
            A = np.eye(dim, dtype=complex)
            for j in range(n):
                for base, x in ((0, xl), (n, xr)):
                    sites = (base+j,)+tuple(base+i for i in range(n) if i != j)+(2*n,)
                    A = apply_local(A, local[x], sites, nq)
            A = apply_local(A, local[xl], tuple(range(n))+(2*n,), nq)
            B = np.empty_like(A)
            B[shift] = A
            out.append(B)
            if compress[xl] < (1 << (s-r)) and compress[xr] < (1 << (s-r)):
                max_good = max(max_good, float(np.linalg.norm(B-target, 2)))
    assert max_good < 1e-11
    return out, {'n': n, 's': s, 'r': r, 'physical_qubits': 2*N+1,
                 'helper_sectors': 1 << (2*s), 'payload_bus_columns_per_sector': dim,
                 'maximum_helper_block_leakage': max_return, 'maximum_good_subspace_error': max_good,
                 'interaction_time_J_units': (2*n+1)*gate_time, 'target': target}


def main() -> None:
    spectrum_cases = 0
    for s in range(0, 13):
        perm = compression(s)
        assert np.array_equal(np.sort(perm), np.arange(1 << s))
        for p in (0., .01, .1, .25, .49, .5):
            w = weights(s, p)
            for r in range(s+1):
                brute = float(w[perm >= (1 << (s-r))].sum())
                assert abs(brute-spectral_tail(s, p, r)) < 3e-13
                spectrum_cases += 1
    uniform_cases = 0
    for s in (0, 1, 4, 16, 64, 256, 1024, 4096):
        for p in (0., 1e-5, .01, .1, .25, .4, .49, .49999, .5):
            beta2 = (1-2*p)**2
            d = deficit(p)
            assert beta2/(2*math.log(2))-1e-13 <= d <= beta2+1e-13
            for delta in (.01, 1e-5, 1e-9):
                r = hoeffding_choice(s, p, delta)
                assert spectral_tail(s, p, r) <= delta+2e-13
                c = 1/(2+8*math.log(1/delta)+8*math.log(2))
                assert r+1 >= c*(1+s*d)-1e-12
                if s:
                    k = math.floor(s*(.5-beta2**.5/4))
                    log_count = math.log(counts(s)[k])
                    assert log_count <= s*math.log(2)-s*beta2/8+1e-10
                uniform_cases += 1
    route_cases = []
    for n, s, r in ((1, 1, 1), (1, 3, 1), (2, 2, 1), (2, 3, 1), (2, 3, 2), (3, 2, 1)):
        matrices, row = route_blocks(n, s, r)
        target = row.pop('target')
        row['preparation_cases'] = []
        for p in (.001, .02, .1, .5):
            q = weights(s, p)
            qq = np.kron(q, q)
            tail = spectral_tail(s, p, r)
            bad = 2*tail-tail*tail
            bounds = []
            for cycles in (1, 2, 7):
                wanted = np.linalg.matrix_power(target, cycles)
                gram = np.zeros_like(target)
                for w, V in zip(qq, matrices):
                    e = np.linalg.matrix_power(V, cycles)-wanted
                    gram += w*(e.conj().T@e)
                # This is the complete fixed-purification isometry norm, uniformly
                # over every payload/bus state, including arbitrary references.
                error = math.sqrt(max(0., float(np.linalg.eigvalsh(gram)[-1])))
                bound = 2*math.sqrt(bad)
                assert error <= bound+1e-10
                bounds.append({'cycles': cycles, 'purified_isometry_operator_error': error,
                               'certified_upper': bound})
            row['preparation_cases'].append({'p': p, 'single_module_bad_weight': tail,
                                            'joint_bad_weight': bad, 'checks': bounds})
        route_cases.append(row)
    epsilon = .01
    delta = epsilon**2/8
    examples = []
    for s in (64, 256, 1024):
        for p in (.05, .1, .25):
            n = s
            r = extractable(s, p, delta)
            bad = spectral_tail(s, p, r)
            gamma = block_gain(n+s, r)
            examples.append({'n': n, 's': s, 'p': p, 'half_diamond_budget': epsilon,
                             'compressed_leaders': r, 'entropy_deficit_per_module': s*deficit(p),
                             'single_module_bad_weight': bad,
                             'certified_purified_error': 2*math.sqrt(2*bad-bad*bad),
                             'gain': gamma, 'same_hardware_unknown_gain': mu(n+s),
                             'achievable_gain_ratio': gamma/mu(n+s),
                             'interaction_time_J_units': 3*math.pi*(2*n+1)/(4*gamma)})
    counterexamples = []
    for s in (64, 256, 1024):
        a = .1
        q0 = a+(1-a)*2.**(-s)
        I = s+q0*math.log2(q0)+(1-q0)*(math.log2(1-a)-s)
        matched_p = brentq(lambda p: deficit(p)-I/s, 0., .5)
        assert abs(s*deficit(matched_p)-I) < 1e-8
        assert (1-a)/2 > delta  # Even one zero-prefix bit is impossible at delta.
        counterexamples.append({'s': s, 'spike_weight': a, 'entropy_deficit': I,
                                'same_entropy_product_p': matched_p,
                                'product_extractable_at_delta': extractable(s, matched_p, delta),
                                'spiked_extractable_at_delta': 0,
                                'both_uniform_mixture_weight': (1-a)**2})
    out = {'all_passed': True, 'scope': 'Analytical spectral sums and full helper-block operator checks; not physical noise simulation or independent proof review.',
           'spectral_checks': spectrum_cases, 'uniform_compression_checks': uniform_cases,
           'complete_routes': route_cases, 'finite_examples': examples, 'same_entropy_counterexamples': counterexamples,
           'largest_full_physical_qubits': max(x['physical_qubits'] for x in route_cases)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('complete_routes',)}, indent=2))


if __name__ == '__main__':
    main()
