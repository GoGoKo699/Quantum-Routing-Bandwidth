# Self-study guide

Start with the physical model in the [README](../README.md), then follow the three bridges below. For research context, read the architecture and routing question in [D26](related-work.md#d26). For the entropy ingredient, use [DF19](related-work.md#df19), Corollary III.5, alongside the explicit proof in [Entropy flow](entropy-flow.md). A claim about an unknown quantum register must include inputs entangled with an inaccessible reference.

## 1. The resource comparison

### Revise

A qubit can store unknown information even when no one knows its state. A correct routing channel preserves superpositions and reference entanglement, not merely computational-basis labels.

### Learn

Both modules have $n+s$ physical qubits and the same bounded contacts. Clean helpers begin in a specified pure state and return there. Unknown helpers may already carry data and must preserve it. The word “free” applies only to the duration of internal controls in the interaction-time theorem; it does not mean that initialization or physical gates have no cost in an apparatus.

### Test

What changes between the two matching bandwidth laws? Open one answer.

<details><summary>A. The clean case receives more contacts.</summary>

No. The comparison fixes the number and strengths of all contacts. Revisit the definition of $N=n+s$.

</details>
<details><summary>B. Only the initial-state promise on the helpers changes.</summary>

Correct. The payload, hardware, allowed controls, and helper-return requirement are held fixed.

</details>
<details><summary>C. The unknown-helper case may discard its helpers.</summary>

No. Unknown helper information must be restored, including its correlations with references.

</details>
<details><summary>D. The clean case uses measurement and resetting after each gate.</summary>

No. The construction is coherent and returns the helpers without resets.

</details>

## 2. Why the bottleneck survives internal processing

### Revise

For a physical state on dimension $D$, the entropy deficit is $\mathcal I=\log_2 D-S(\omega)$. Any unitary preserves its eigenvalues and therefore preserves this deficit. A pure reference-assisted test can nevertheless have a mixed accessible physical state.

### Learn

The contacts have a large extreme eigenvalue but a much smaller typical squared magnitude. Their collective Pauli coefficients have sub-Gaussian spectral moments. The entropy deficit limits how much weight the evolving physical state can concentrate in the large-eigenvalue tail. A conditional entropy-rate inequality converts this second-moment limit into a speed limit across a cut. Internal controls can reorganize the state but cannot change the conserved budget or directly generate entropy across that cut.

With $n$ payload Bell pairs on each side, $2s$ initialized helpers and a pure bus, the accessible physical deficit is $2s+1$ bits. Exchanging the payload creates $2n$ bits across the reference-assisted left cut. Dividing the required entropy change by the maximum rate gives the lower bound.

### Test

Why is the square-root bound compatible with much faster entropy growth on a specially prepared collective state?

<details><summary>A. Such a state has a different physical-state entropy budget.</summary>

Correct. A selected collective state can have root-mean-square interaction of order $nJ$. The flat-data or common-ensemble hypothesis cannot be silently applied to it.

</details>
<details><summary>B. Entropy of an average state always equals average entropy.</summary>

No. That equality is false. The ensemble proof instead uses the linearity of the second moment and the concavity of the square root.

</details>
<details><summary>C. The proof restricts internal operations to slow switching.</summary>

No. The direct rate proof allows arbitrary well-defined switching and internal processing.

</details>
<details><summary>D. Reference systems are physically transmitted through the bus.</summary>

No. References are inaccessible and never acted on. They test whether all quantum information has been preserved.

</details>

## 3. How the upper bound preserves occupied data

### Revise

For three data qubits, an encoding maps the collective magnetization to $Z_q\operatorname{diag}(3,1,1,1)$. Four spectator translations average the diagonal coefficient to $3/2$.

### Learn

Every translation is part of a fixed coherent unitary sequence. The conjugated diagonal interactions commute, so the identity is exact at finite interval length. Decoding removes spectator dependence instead of measuring it. Larger occupied blocks give gain $\mu_b\sim\sqrt{2b/\pi}$.

With $s$ clean helpers, split the module into $s+1$ balanced blocks. Let the target lead one block and the clean helpers lead the others. Reversible CNOT fanout makes the leader contributions add during the contact operation; undoing it restores the clean helpers. The gain is of order $\sqrt{(n+s)(s+1)}$. Three rotated Ising operations form a SWAP, and $2n+1$ bus SWAPs exchange the payload and return the bus.

### Test

What follows from the exact square-root interaction-time construction alone?

<details><summary>A. A fixed-strength processor executes the full route in square-root time.</summary>

No. The interaction-time result does not charge internal gate duration. The finite-strength compiler is a separate calculation.

</details>
<details><summary>B. Every helper state, clean or unknown, obeys the clean-helper identity.</summary>

No. The clean-helper identity is restricted to the initialized-helper input subspace. Unknown helpers have their own full-data construction.

</details>
<details><summary>C. The stated coherent protocol attains the scaling under free internal controls.</summary>

Correct. The exact or sampled control-list length and the cost of executing internal gates must be assessed separately.

</details>
<details><summary>D. Fanout produces independent copies of the unknown target state.</summary>

No. It produces correlations that are later removed; it does not clone a quantum state.

</details>

## Readiness criterion

Explain the same-hardware comparison, construct the Bell-reference entropy test, identify where conditional variance and entropy deficit enter, derive the balanced-block gain, and distinguish contact time from total duration. For coaching, work one selection question at a time and revisit the relevant bridge after an incorrect response. Opening these answer panels provides feedback; it does not record or certify learner progress.
