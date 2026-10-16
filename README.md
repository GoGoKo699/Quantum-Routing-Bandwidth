# Quantum Routing Bandwidth

**Reusable initialization and the optimal bandwidth of a quantum bottleneck.**

Two internally controllable modules exchange arbitrary quantum data through one bus qubit. Occupied qubits strengthen a selected contact while retaining their information. Independently prepared helpers supply an additional, quantifiable improvement even when their initialization is imperfect.

## Start here

| Purpose | Route |
|---|---|
| Learn the project | [30-milestone map](docs/milestones.md) and [Watrous anchor and notation](docs/learning.md) |
| Connect foundations to the result | [Three worked bridges](docs/learning-bridges.md); [coaching protocol](docs/coaching.md) |
| Read the science directly | [Theorem map](docs/theorem-map.md) → [fixed-error law](docs/mixed-helpers.md) |
| Check implementation and resources | [Accuracy and resources](docs/accuracy-and-resources.md); [control models](docs/control-models.md) |
| Inspect attribution | [Related work](docs/related-work.md) and [references](references.bib) |
| Reproduce the checks | [Verification](docs/verification.md) and [recorded results](results/verification.json) |

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The common map has 14 background milestones and 16 research milestones; its sections, notation translations, and local examples provide the bridge to the result. Specialist proofs remain directly accessible. [LLM reading guide](llms.txt).

## Main result

Each module contains $n\ge1$ payload qubits and $s\ge0$ helpers. Every module-qubit–bus interaction has operator norm at most $J$; all contacts may act simultaneously. Internal operations confined to either module or the bus have zero charged duration. Both interfaces remain bounded. There are no measurements, resets, or extra initialized qubits.

For helpers independently prepared in the known state $\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|$, with $0\le p\le1/2$, the optimal fixed-error interaction time is

$$
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(
\frac{n}{J\sqrt{(n+s)\{1+s[1-h_2(p)]\}}}
\right).
$$

For every fixed $0<\epsilon\le0.1$, the constants are uniform in $n,s,p$. The error is a complete-operation half diamond distance, including arbitrary reference-entangled payload/bus inputs and the fixed helpers' inaccessible preparation references. The physical helper density matrix returns exactly in the construction; remaining correlations and bus errors are included in the error budget. Compression, routing, and decompression share one invariant high-probability sector, so initial preparation error does not accumulate gate by gate.

The [full proof](docs/mixed-helpers.md) distinguishes zero error from fixed nonzero error. A correlated-state counterexample shows why entropy deficit alone is not a complete bandwidth invariant for arbitrary helper states.

## Exact endpoints

On identical hardware with the same payload,

$$
T_{\mathrm{clean}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{(n+s)(s+1)}}\right),
$$

$$
T_{\mathrm{unknown}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right).
$$

These exact tasks restore helpers and an arbitrary bus, including reference correlations. The changed resource is the initial helper promise, not extra wiring. At $s=0$, the time is $\Theta(\sqrt n/J)$. Any full-rank mixed preparation has the unknown-helper scale at zero error; the fixed-error law is not uniform as $\epsilon\to0$.

## Quantitative realization and scope

After concentration into $r$ near-clean leader bits, balanced blocks need only

$$
K_{\mathrm{exact}}=2^{\lceil(n+s)/(r+1)\rceil-1}
$$

exact interaction intervals per Ising gate. Synchronizing each block's translations suffices because the contact is an additive sum. For fixed nonzero polarization and $s=\Theta(n)$, this gives $O(n)$ total **exact contact intervals**. Global internal compression is still free in this theorem, and no efficient elementary implementation of every encoding is implied.

Exact rational spectral certificates demonstrate finite-size advantages over every allowed unknown-helper protocol at the same complete-operation accuracy, not just over one selected implementation. The [resource analysis](docs/accuracy-and-resources.md) also shows that a fixed sum of contact norms removes the parametric initialization advantage, while a fixed quadratic contact budget retains it.

The main normalization is **per contact**, not a fixed total Hamiltonian norm. Helper preparation is an input resource. The displayed finite-strength compiler has linear total duration at fixed internal/contact strength ratio. Preparation robustness is not robustness to ongoing decoherence or noisy pulses; their errors have a separate composition bound.

## Reproduce

Using Python 3.13 in a virtual environment:

```bash
python -m pip install -r requirements.txt
python check_repository.py
python verify.py
```

Ten deterministic suites run in an isolated temporary directory, with detailed results and logs written to `build/verification/`. Tracked results are not silently overwritten. Checks include full input isometries, entropy-rate interaction optimization, noncommuting entropy budgets, exact integer preparation certificates, synchronized averaging, fresh-payload reuse, and a bounded-strength compiler. Proofs establish the scaling laws; numerical checks are not independent review or hardware evidence.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT](LICENSE).
