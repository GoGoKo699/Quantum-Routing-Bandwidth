# Quantum Routing Bandwidth

**How much does reusable initialization increase the amount of unknown quantum information that can pass through a one-qubit interface?** Two internally controllable modules exchange complete registers through a shared bus. Occupied qubits can assist a selected contact without losing their data; independently polarized helpers provide a further improvement even when their preparation is imperfect.

Each module has $`n\ge1`$ payload qubits and $`s\ge0`$ helpers. Both module–bus interfaces are bounded: every pairwise contact has operator norm at most $`J`$, and contacts may operate simultaneously. Internal module operations and bus-only rotations have zero charged duration. There are no measurements, resets, or extra initialized qubits.

For independent known preparations $`\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|`$, with $`0\le p\le1/2`$, the optimal fixed-error interaction time is

```math
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(
\frac{n}{J\sqrt{(n+s)\{1+s[1-h_2(p)]\}}}
\right).
```

For every fixed $`0\lt\epsilon\le0.1`$, the constants are uniform in $`n,s,p`$. The error is a **complete-operation half diamond distance**, including arbitrary reference-entangled payload/bus inputs and the fixed helpers' inaccessible preparation references. The construction returns the physical helper density matrix exactly; remaining joint correlations and bus errors are included in the accuracy guarantee.

| Helper promise on the same hardware | Accuracy | Optimal interaction time |
|---|---|---|
| Pure helpers, returned clean | Exact | $`\Theta(n/[J\sqrt{(n+s)(s+1)}])`$ |
| Arbitrary unknown helpers, all information preserved | Exact | $`\Theta(n/[J\sqrt{n+s}])`$ |
| Independent known mixed helpers | Fixed complete-operation error | The entropy-deficit law above |

The exact tasks restore an arbitrary bus and all reference correlations. A full-rank mixed preparation has the unknown-helper scale at **zero** error; the fixed-error law is not uniform as the error tends to zero. At $`s=0`$, the routing time is $`\Theta(\sqrt n/J)`$.

## Read the science

Start with the [scientific account](science/README.md), then follow the [information-flow bound](science/entropy-flow.md), [exact helper laws and contact construction](science/bandwidth.md), and [imperfect initialization](science/mixed-helpers.md). The [physical interpretation](science/interpretation.md) joins their mechanisms and resource consequences. Specialists can use the [theorem and proof map](science/theorem-map.md) directly.

| Question | Authoritative account |
|---|---|
| Why can arbitrary internal processing not eliminate the bottleneck? | [Conditional entropy and weighted interfaces](science/entropy-flow.md) |
| How do occupied qubits assist without sacrificing their information? | [Coherent block construction and exact laws](science/bandwidth.md) |
| What survives imperfect initialization, including helper references? | [Matched mixed-helper law](science/mixed-helpers.md) |
| Is there a finite advantage against the entire unknown-helper class? | [Exact certificates, error composition, and resource budgets](science/accuracy-and-resources.md) |
| What changes when internal gates have finite duration? | [Control models and the bounded-strength compiler](science/control-models.md) |
| Which ingredients are established prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The converse combines a conditional entropy-rate estimate with a conserved physical entropy deficit. The construction concentrates preparation weight reversibly, uses all remaining qubits as occupied spectators, and decompresses after routing. One common high-probability sector controls preparation error for the entire operation; new control errors have a separate composition bound.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies relevant sections, the author's errata, and the notation changes needed for this project. [Three worked examples](learning/WORKED_EXAMPLES.md) connect references, coherent contact amplification, and preparation concentration to the proofs.

The [30-milestone map](learning/MILESTONES.md) retains **14 background/preliminary** and **16 narrative/innovation** targets. Each milestone has a central question, an understanding target, earlier dependencies, a conceptual connection, and scientific sources. The [learning entrypoint](learning/README.md) provides the route; the [LLM guide](llms.txt) maps study and research questions to authoritative files.

## Reproduce the checks

From the repository root, using Python 3.13:

```bash
python -m pip install -r verification/requirements.txt
python check_repository.py
python verification/tools/test_structure.py
python verification/run_all.py
```

The [verification guide](verification/README.md) describes ten deterministic scientific suites, structural regression tests, and the separate actual-GitHub rendering check. Executed scientific outputs and source hashes are in [verification/results](verification/results/verification.json). Finite numerical identities support the implementations; the written proofs and cited theorems establish universal and asymptotic claims.

## Scope and physical resources

The matching results charge **contact time with free internal controls**, under a per-contact rather than fixed total-norm budget. Initialization and internal compression are resources, not cost-free device operations. The displayed bounded-strength compiler has linear total duration at fixed internal/contact strength ratio; that is not a universal finite-speed impossibility theorem.

Synchronized block translations substantially shorten the exact contact list. With fixed nonzero polarization and $`s=\Theta(n)`$, the route uses $`O(n)`$ exact contact intervals, while global compression is still assigned zero duration. A fixed quadratic contact budget retains the initialization enhancement; a fixed sum of contact strengths removes its parametric growth. A correlated-helper counterexample shows why entropy deficit alone cannot determine achievable bandwidth for arbitrary helper states. Preparation robustness does not imply robustness to ongoing decoherence or noisy pulses.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT](LICENSE).
