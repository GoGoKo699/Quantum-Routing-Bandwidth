# Quantum Routing Bandwidth

**How much reusable initialization increases the bandwidth of a quantum bottleneck.**

Two internally controllable modules exchange arbitrary quantum data through one bus qubit. Occupied qubits can coherently strengthen a selected contact while retaining their information. Initialized helpers provide a further, quantifiable improvement and return to their initial states after use.

## Main result

Each module contains $n\ge1$ payload qubits and $s\ge0$ helpers. The same hardware is used in both comparisons: every module-qubit–bus interaction has operator norm at most $J$, and all contacts may operate simultaneously. Internal operations confined to either module or the bus have zero charged duration. The task exchanges the payloads, preserves correlations with inaccessible references, and restores the helpers and bus.

With helpers initialized in $|0\rangle^{\otimes s}$,

$$
T_{\mathrm{clean}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{(n+s)(s+1)}}\right).
$$

With helpers containing arbitrary unknown information that must be preserved,

$$
T_{\mathrm{unknown}}(n,s)
=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right).
$$

The constants are independent of $n$ and $s$. Initialization therefore changes the optimal interaction-time scaling by $\Theta(\sqrt{s+1})$ without changing the contacts or payload. At $s=0$, the law is $\Theta(\sqrt n/J)$.

These are **interaction-time laws with free internal controls**. The contact budget is per pair, rather than a fixed total Hamiltonian norm. Preparation of the clean helpers is an input resource. The exact constructions can have long control lists; the separately analyzed bounded-strength compiler has linear total duration at fixed internal/contact strength ratio.

## Read the work

| Question | Resource |
|---|---|
| What is the precise task, and why do the bounds match? | [Initialization and routing bandwidth](docs/bandwidth.md) |
| Why can rapid internal processing not remove the bottleneck? | [Conditional entropy and weighted information flow](docs/entropy-flow.md) |
| How do coherent averaging, control count, and finite gate speed differ? | [Control models and implementations](docs/control-models.md) |
| Which results and techniques are established prior work? | [Related work](docs/related-work.md) and [BibTeX references](references.bib) |
| How can the calculations be reproduced? | [Verification guide](docs/verification.md) and [recorded results](results/verification.json) |
| How should I learn the definitions and proof mechanism? | [Self-study guide](docs/learning.md) |

The converse combines a conditional entropy-rate bound with a conserved entropy deficit. The construction combines sign encoding, coherent spectator translations, and reversible use of initialized leaders. The entropy-flow result also accommodates unequal contacts and multiple bus qubits under a common input-independent control schedule.

## Reproduce

Using Python 3.13 in a virtual environment:

```bash
python -m pip install -r requirements.txt
python check_repository.py
python verify.py
```

The verifier runs eight deterministic suites in an isolated temporary directory. Full results and logs are written to `build/verification/`; tracked reference results are not overwritten. The tests include full allowed-input isometries, optimized entropy-rate interactions, noncommuting entropy-deficit tests, and an explicit bounded-strength compiler. Numerical residuals check finite identities; the proofs establish the universal scaling statements.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT](LICENSE).
