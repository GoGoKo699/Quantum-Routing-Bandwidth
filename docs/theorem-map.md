# Theorem and proof map

**Central statement:** for independent, known helper preparations, reusable initialization changes the optimal interaction-time bandwidth of a qubit bottleneck. The converse bounds information flow; a coherent construction reaches the same scaling and preserves the helper preparation to a specified complete-operation accuracy.

This map identifies the mathematical dependencies and the scope of each result. Full proofs remain in their linked canonical documents. Numerical checks support finite identities; they do not establish asymptotic theorems or independent validation.

## 1. Model and main theorem

Two modules each contain $`n\ge1`$ unknown payload qubits and $`s\ge0`$ helpers. Their only connection is one bus qubit. All $`n+s`$ contacts per module may act simultaneously, each with operator norm at most $`J`$. Internal operations in either module or on the bus have zero charged duration. Both interfaces remain bounded. Controls are input-independent, with no measurement, reset, direct intermodule coupling, or extra initialized workspace.

Each module's helpers are independently prepared in the known state $`\rho_p^{\otimes s}`$, where $`\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|`$ and $`0\le p\le1/2`$. The preparations are independent of the payload and bus. Define $`d(p)=1-h_2(p)`$.

**Theorem A — fixed-error bandwidth.** For every fixed $`0\lt \epsilon\le0.1`$,

```math
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(
\frac{n}{J\sqrt{(n+s)[1+s\,d(p)]}}
\right).
```

The constants are independent of $`n,s,p`$, including size-dependent polarization. The error convention is

```math
\frac12\|\Phi_U-\Phi_{\ast}\|_\diamond\le\epsilon.
```

Both maps insert the same fixed purifications of the helper preparations. The ideal map exchanges the payloads and preserves the bus, helpers, and inaccessible preparation references. The supremum ranges over arbitrary payload/bus inputs and their reference extensions, not arbitrary replacement helper inputs. See [Mixed helpers, Section 1](mixed-helpers.md#1-task-and-matching-law).

The normalization is **per contact**, not a fixed total Hamiltonian norm. The result is not a bounded-speed implementation claim. At fixed $`\epsilon`$ and $`p\lt 1/2`$, the bandwidth enhancement grows with the preparation entropy deficit; at $`p=1/2`$ the unknown-helper scale is recovered.

## 2. Result hierarchy

| Result | Role | Canonical proof |
|---|---|---|
| A: the fixed-error independent-helper law above | Main matched resource characterization | [Mixed helpers, Sections 2–4](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound) |
| B: exact clean and arbitrary-unknown helper laws | Exact endpoints and same-hardware comparator | [Bandwidth, Sections 4–6](bandwidth.md#4-clean-helper-lower-bound) |
| C: full-rank zero-error restriction and correlated-state counterexample | Boundaries of A, not separate universal resource laws | [Mixed helpers, Section 5](mixed-helpers.md#5-zero-error-and-nonzero-error-are-different-tasks) and [Section 7](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped) |
| D: weighted information-flow inequalities | General converse mechanism, including unequal contacts and multiple bus qubits | [Entropy flow, Section 4](entropy-flow.md#4-weighted-average-input-entropy-flow-theorem) and [Bandwidth, Section 3.2](bandwidth.md#32-entropy-deficit-cut-rate) |

Result B reads

```math
T_{\mathrm{clean}}=\Theta\!\left(\frac{n}{J\sqrt{(n+s)(s+1)}}\right),
\qquad
T_{\mathrm{unknown}}=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right).
```

These are exact tasks, with full helper and arbitrary-bus restoration. The zero-error claim is proved separately; it is not obtained by setting $`\epsilon=0`$ in constants that depend on $`\epsilon`$.

## 3. Lower-bound dependency chain

### L1. Conditional entropy rate

For a register/reference subsystem $`A`$ and a qubit bus $`C`$, the contact contribution obeys

```math
|\dot S_A|\le c\sqrt{\mathrm{Tr}(\omega H_{\mathrm{int}}^2)}.
```

A published conditional-variance inequality, [DF19, Corollary III.5](related-work.md#df19), suffices with $`c=2\log_2 9`$. The [elementary qubit argument](entropy-flow.md#2-elementary-qubit-constant) improves the constant to $`2\sqrt2/\ln2`$ without changing the scaling. The two routes are alternatives, not successive assumptions. The conditional logarithms need not commute, and the support treatment matters for reference tests. See [Entropy flow, Sections 1–3](entropy-flow.md#1-published-conditional-variance-bound).

### L2. Geometry and conserved initialization budget

Only genuine two-sided contact terms enter $`H_{\mathrm{int}}`$. Pauli orthogonality, a sub-Gaussian spectral estimate, and the relative-entropy variational inequality give

```math
\mathrm{Tr}(\omega H_{\mathrm{int}}^2)
\le12\ln2\,[\mathcal I(\omega)+1/2]\sum_jJ_j^2,
\qquad
\mathcal I(\omega)=\log_2D-S(\omega).
```

The projection that removes cut-local terms contracts the normalized Frobenius norm; no operator-norm contraction is assumed. Unbounded internal controls do not enter this second moment and cannot directly change the chosen cut entropy. Physical unitary evolution preserves $`\mathcal I`$. See [Bandwidth, Section 2](bandwidth.md#2-entropy-deficit-controls-contact-second-moments).

### L3. Extensive payload requirement

Purify helpers locally and Bell-pair each payload qubit with a local inaccessible reference. The accessible physical deficit is $`1+2s\,d(p)`$. The exact target requires $`2n`$ bits across the reference-assisted left cut.

For approximate routing, use the mutual information of the two payload-and-payload-reference subsystems. It gives

```math
S_A(T)\ge2n-4n\epsilon-\tfrac32h_2(\epsilon).
```

The error penalty depends on the payload size, not the helper count, so the converse holds for all $`s`$. Combining L1–L3 proves the lower half of A. A high-fidelity test is necessary for any accurate channel; it is not assumed equivalent to diamond accuracy. See [Mixed helpers, Section 2](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

## 4. Matching construction and its error accounting

### U1. Concentrate preparation weight without extra workspace

A fixed helper-basis permutation puts probability at least $`1-\delta`$ into a zero-prefix subspace with $`r`$ specified zero bits. The exact spectral criterion is that the largest $`2^{s-r}`$ eigenvalues carry that probability. For independent preparations, a uniform concentration estimate permits

```math
r+1\ge c_\delta[1+s\,d(p)].
```

The remaining entropy stays in the other helper qubits. Reversible polarization concentration is established prior machinery [SV98](related-work.md#sv98); no measurement or purity creation is being asserted. See [Mixed helpers, Section 3](mixed-helpers.md#3-reversible-concentration-at-finite-error).

### U2. Use occupied spectators and compressed leaders

An occupied block of size $`b`$ realizes coupling $`J\mu_b`$ to its leader, with identity on arbitrary spectators, where $`\mu_b=\mathbb E|\epsilon_1+\cdots+\epsilon_b|=\Theta(\sqrt b)`$. Encoding, commuting spectator translations, and decoding give a full operator identity. Balanced blocks and reversible leader fanout then give

```math
\gamma_{N,r}=\Theta(\sqrt{N(r+1)}),\qquad N=n+s.
```

The entropy-bearing helper qubits remain occupied spectators; correlations introduced by compression are permitted. Three Ising rotations implement a target–bus SWAP. The buffered schedule uses $`2n+1`$ such SWAPs and restores the bus. See [Bandwidth, Section 5](bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers).

### U3. One common good subspace for the complete route

Compress once, execute the whole route, and decompress once. The actual and ideal unitaries agree on a common good helper sector with one common phase. Its bad weight is $`\Delta\le2\delta`$, so their fixed-preparation isometries differ by at most $`2\sqrt\Delta`$. Taking $`\delta=\epsilon^2/8`$ proves the complete half diamond bound in A.

This is not a per-gate error estimate. Exact helper marginal return follows from the block-diagonal action in the original helper eigenbasis. The same common-sector estimate controls repeated coherent uses with fresh payloads, but does not describe new gate noise or ongoing decoherence. See [Mixed helpers, Sections 4.1–4.2](mixed-helpers.md#41-complete-reference-preserving-error-without-accumulation).

## 5. Boundaries that belong beside the main result

**Exact versus approximate.** For $`0\lt p\le1/2`$, full rank and exact preparation-reference return force the full unknown-helper operation. Thus the exact law has no polarization enhancement. This obstruction is already identified in the Outlook of [UHMG26](related-work.md#uhmg26); A is a matched fixed-error answer in the present architecture.

**Entropy versus spectral concentration.** A correlated helper state $`(1-a)I/2^s+a|0^s\rangle\langle0^s|`$ can have extensive entropy deficit while retaining a substantial maximally mixed component. At small fixed error it obeys the unknown-helper routing scale. The converse is entropy-based, but its saturation requires more than entropy alone. See [Mixed helpers, Section 7](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped).

**Marginal return versus decoupling.** For the mixed preparation, the constructed physical helper marginal returns exactly; joint restoration, bus accuracy, and preparation-reference correlations satisfy the specified error bound. They are not exact identities on arbitrary helper inputs.

**Contact time versus total time.** The synchronized exact construction uses $`2^{\lceil N/(r+1)\rceil-1}`$ intervals per Ising gate, linear total contact count for extensive polarization, and potentially long lists in other regimes. Global internal encodings remain free. The [bounded-strength compiler](control-models.md#24-finite-control-consequence) has linear total duration at fixed $`G/J`$. That is a limitation of the displayed compiler, not a universal finite-speed impossibility theorem.

## 6. Theorem-level reading and scrutiny

A focused technical reading can proceed from the [main task](mixed-helpers.md#1-task-and-matching-law), through L1–L3 and U1–U3, to the scope boundaries above. The potentially consequential proof checks are the noncommuting conditional-log estimate, the removal of local terms without an invalid norm claim, the payload-sized continuity argument, and the one common good-sector phase needed for complete reference preservation. Every dependency has a canonical proof location rather than a separate duplicate derivation here.

For the originality comparison, [D26](related-work.md#d26) supplies the closest restricted-time bottleneck bound; [UHMG26](related-work.md#uhmg26) supplies the robustness–commutator framework, including multiple payload qubits. Merely invoking compression or changing architecture is not the claimed contribution. The additional statement is the matched extensive throughput law with fixed complete-operation error and returned preparation resources.

The [verification guide](verification.md) maps those proofs to ten deterministic suites. Passing tests and source hashes establish reproducibility of the finite checks, not outside scientific endorsement. No external technical assessment is recorded by this map.

## 7. Exposition structure

A compact presentation can lead with the physical question and Theorem A, explain L1–L3 as the information-flow mechanism, and show U1–U3 as the matching realization. Result B fixes the exact endpoints. Result C explains why exact and approximate initialization differ and why general helper entropy is not a complete operational invariant. Keep the weighted-interface statement, support details, spectral certificates, and finite-control compilation available as supporting material rather than competing main stories.

## 8. Quantitative accuracy and resource guarantees

[Accuracy and resources](accuracy-and-resources.md) provides the all-helper-size approximate unknown-helper converse, exact finite-size separation certificates, synchronized exact and sampled contact lists, error composition with fresh-payload reuse, and matched laws under quadratic and sum-of-strength budgets. These supporting results make the operational scope quantitative without changing the main theorem's input promises or free-internal-control convention.
