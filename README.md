# Quantum Routing Bandwidth

**How much reusable initialization increases the bandwidth of a quantum bottleneck.**

Two internally controllable modules exchange arbitrary quantum data through one bus qubit. Occupied qubits coherently strengthen a selected contact while retaining their information. Independently prepared helpers supply a further, quantifiable improvement even when initialization is imperfect.

Start with the [theorem and proof map](docs/theorem-map.md) for the central result, its dependencies, and a focused technical reading route.

## Main result

Each module contains $n\ge1$ payload qubits and $s\ge0$ helpers. Every module-qubit–bus interaction has operator norm at most $J$, and all contacts may operate simultaneously. Internal operations confined to either module or the bus have zero charged duration. Both interfaces remain bounded; there is no measurement, reset, or extra initialized workspace.

For helpers independently prepared in the known state $\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|$, with $0\le p\le1/2$, the matching fixed-error law is

$$
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(
\frac{n}{J\sqrt{(n+s)\{1+s[1-h_2(p)]\}}}
\right).
$$

For every fixed $0<\epsilon\le0.1$, the constants are uniform in $n,s,p$. The error is a complete-operation half diamond distance including arbitrary reference-entangled payload/bus inputs and the fixed helpers' inaccessible preparation references. Compression, routing, and decompression return the physical helper density matrix exactly; remaining joint correlations and bus errors are included in the error budget. Preparation error does not accumulate gate by gate because the entire operation agrees with the ideal on one common high-probability subspace.

The [full theorem](docs/mixed-helpers.md) separates zero error from fixed nonzero error and gives a correlated-state counterexample: entropy deficit alone does not characterize achievable bandwidth for arbitrary helper states.

## Exact endpoints on the same hardware

With exactly initialized helpers that must return clean,

$$
T_{\mathrm{clean}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{(n+s)(s+1)}}\right).
$$

With helpers holding arbitrary unknown information that must be preserved,

$$
T_{\mathrm{unknown}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right).
$$

These exact constructions restore every helper and an arbitrary bus, including reference correlations. The constants are independent of $n,s$. Initialization changes the optimal interaction-time scaling by $\Theta(\sqrt{s+1})$ at fixed contacts and payload. At $s=0$, the law is $\Theta(\sqrt n/J)$. The exact full-rank mixed-helper task has the unknown-helper scale; it is not the uniform zero-error limit of the fixed-error theorem.

These are **interaction-time laws with free internal controls**, under a per-contact rather than fixed total-norm budget. Helper preparation is an input resource. Exact control lists may be long, and the displayed bounded-strength compiler has linear total duration at fixed internal/contact strength ratio. Preparation robustness is not a claim about ongoing decoherence, noisy pulses, or a fixed-hardware runtime advantage.

## Read the work

| Question | Resource |
|---|---|
| What is the central theorem and its proof structure? | [Theorem and proof map](docs/theorem-map.md) |
| What survives imperfect initialization at complete-operation accuracy? | [Mixed helpers and reusable bandwidth](docs/mixed-helpers.md) |
| Why do the exact clean/unknown helper bounds match? | [Initialization and routing bandwidth](docs/bandwidth.md) |
| Why can rapid internal processing not remove the bottleneck? | [Conditional entropy and weighted information flow](docs/entropy-flow.md) |
| How do coherent averaging, control count, and finite gate speed differ? | [Control models and implementations](docs/control-models.md) |
| Which results and techniques are established prior work? | [Related work](docs/related-work.md) and [BibTeX references](references.bib) |
| How can the calculations be reproduced? | [Verification guide](docs/verification.md) and [recorded results](results/verification.json) |
| How should I learn the definitions and mechanism? | [Self-study guide](docs/learning.md) |

## Reproduce

Using Python 3.13 in a virtual environment:

```bash
python -m pip install -r requirements.txt
python check_repository.py
python verify.py
```

The verifier runs nine deterministic suites in an isolated temporary directory. Full results and logs are written to `build/verification/`; tracked reference results are not overwritten. Tests include full input isometries, optimized entropy-rate interactions, noncommuting entropy-budget checks, mixed-helper spectral and reference-preserving operator checks, and a bounded-strength compiler. Numerical residuals check finite identities; the proofs establish the scaling statements. Neither passing tests nor this reading map constitutes independent technical review.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT](LICENSE).
