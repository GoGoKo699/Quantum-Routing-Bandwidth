# Quantum information through a bounded interface

A small interface need not behave as a sequence of independent wires. Several bounded contacts can act simultaneously, and internal reversible processing can organize the information already stored in a module so that it assists communication. The question is how much **unknown quantum data** can be exchanged this way, and how the answer changes when some qubits have a known preparation.

The model has three separately controlled regions: a left module, one bus qubit, and a right module. Neither interface is free. Each module contains the same number of payload and helper qubits in every comparison. The task includes arbitrary payload correlations with inaccessible references; the bus and helper resources must satisfy the specified return guarantee. The time charged is the duration of bounded pairwise contacts, with module-internal unitaries treated as instantaneous.

## Connected reading route

| Step | Scientific question | Account |
|---|---|---|
| 1 | What is transferred, what is held fixed, and what counts as accurate return? | [Exact task](bandwidth.md#1-result-model-and-comparison) and [fixed-preparation error](mixed-helpers.md#1-task-and-matching-law) |
| 2 | How can a small bus limit entropy flow even with strong internal controls? | [Conditional entropy rate, supports, and weighted interfaces](entropy-flow.md) |
| 3 | How does the preparation budget limit usable contact strength? | [Entropy-deficit moment bound](bandwidth.md#2-entropy-deficit-controls-contact-second-moments) |
| 4 | Can occupied data attain the permitted scaling without being discarded? | [Sign encoding, block averaging, and returned helpers](bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers) |
| 5 | Does imperfect preparation retain the advantage at complete-operation accuracy? | [Reversible concentration, routing, and decompression](mixed-helpers.md) |
| 6 | Which comparisons remain valid at finite size and under other strength budgets? | [Finite certificates and accuracy](accuracy-and-resources.md); [finite-duration controls](control-models.md) |
| 7 | What do these results establish about the physical resource? | [Interpretation and boundaries](interpretation.md) |

The [theorem map](theorem-map.md) gives a shorter dependency-based route. The [learning route](../learning/README.md) supplies foundations and complete small examples before these specialist arguments.

## Main result and its endpoints

Write $`N=n+s`$ for module size and $`d(p)=1-h_2(p)`$ for the entropy deficit of a known independently prepared helper. For fixed complete-operation error $`0\lt\epsilon\le0.1`$,

```math
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(\frac{n}{J\sqrt{N[1+sd(p)]}}\right).
```

The upper and lower constants are independent of $`n,s,p`$. The lower bound combines an extensive reference-assisted information requirement with a preparation-dependent rate. The upper bound reversibly concentrates the helpers and uses entropy-bearing qubits as occupied spectators. It is exact on one common high-probability sector; this controls the entire inserted-preparation channel rather than a sum of input-specific gate errors.

Exactly clean helpers give time $`\Theta(n/[J\sqrt{N(s+1)}])`$. Arbitrary unknown helpers give $`\Theta(n/[J\sqrt N])`$. These [exact laws](bandwidth.md) are proved separately from the fixed-error result. Full rank prevents a growing initialization advantage in the zero-error task, while [correlated preparations](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped) show that a scalar entropy deficit is not a sufficient achievability invariant for every helper spectrum.

## Attribution and verification

Conditional-variance estimates, reversible polarization concentration, Hamiltonian simulation by conjugation, and initialization-sensitive transfer all have established precedents. The [related-work account](../references/RELATED_WORK.md) identifies their roles and the exact comparison to the closest routing results. The contribution studied here is the matched extensive-throughput characterization in this model, not the invention of those tools.

The [verification guide](../verification/README.md) connects each finite check to a proof or construction. Exact rational certificates establish finite comparisons using proved bounds; they are not simulations of the corresponding large register. Neither these tests nor the ideal interaction-time model establishes device performance or independent proof validation.
