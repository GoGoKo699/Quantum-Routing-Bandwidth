# Three worked bridges

These examples connect the [Watrous foundation](learning.md) to the [30-milestone map](milestones.md). They instantiate existing proofs rather than establish additional results. The textbook supplies states, channels, spectra, and entropy; the linked project documents supply the dynamical model and routing identities.

## 1. Unchanged marginals can conceal complete information transfer

**Foundation:** Watrous §§2.1.3, 2.2.2, and 5.2. **Milestones:** M03, M09, M18.

Take one payload qubit on each side and inaccessible references $L',R'$. Initially prepare

$$
|\Omega_0\rangle
=|\Phi^+\rangle_{LL'}\otimes|\Phi^+\rangle_{RR'},
\qquad
|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.
$$

Across the cut $LL'$ versus $RR'$, this is a product: each Bell pair is wholly on one side. Its cut entropy is zero. After swapping only the physical payloads $L,R$,

$$
|\Omega_1\rangle
=|\Phi^+\rangle_{RL'}\otimes|\Phi^+\rangle_{LR'}.
$$

Both pairs now cross the cut, and the reduced state on $LL'$ is $I_4/4$. Its entropy is two bits. Yet the single-qubit marginals of $L$ and $R$ were $I_2/2$ before the operation and remain $I_2/2$ afterward. Checking those marginals would miss the entire task.

The references never travel and cannot be used as clean helpers. Their role is to expose where unknown quantum information went. With $n$ payload qubits per side, the ideal exchange creates $2n$ bits across this reference-assisted cut. The bus and helpers occupy their specified sides of the complete cut in the [converse](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

A pure global test can have a mixed accessible physical state. For local helper purifications and the payload Bell pairs, the physical entropy deficit is $1+2s[1-h_2(p)]$ when a pure bus is chosen for the lower-bound test. Unitary internal processing preserves that deficit. The [entropy-rate argument](bandwidth.md#32-entropy-deficit-cut-rate) converts it into a bound on how fast the required correlations can be created.

## 2. Occupied spectators can assist without losing their data

**Foundation:** Watrous §1.1.3 and Chapter 4. **Milestones:** M20–M23.

Let $q$ be a target qubit, $a,b$ two occupied spectator qubits, and $C$ the bus. Their physical contact is

$$
H=JZ_C(Z_q+Z_a+Z_b).
$$

Apply the reversible encoding $E$: first a Toffoli controlled by $a,b$ onto $q$, then CNOTs from $q$ to $a$ and $b$. Directly following the computational-basis labels gives

$$
E^\dagger(Z_q+Z_a+Z_b)E
=Z_q\otimes D_{ab},\qquad D_{ab}=\operatorname{diag}(3,1,1,1).
$$

The encoded interaction's sign depends on the target; its magnitude still depends on the spectators. Four coherent spectator XOR translations remove that dependence:

$$
\frac14\sum_{u\in\{00,01,10,11\}}X_uD_{ab}X_u
=\frac32 I_{ab}.
$$

Every diagonal entry sees the same multiset $\{3,1,1,1\}$. If $H_u$ denotes the decoded-frame translated contact, these Hamiltonians commute. Four equal intervals of total duration $t$, with their control frames restored, therefore give

$$
\prod_u e^{-i(t/4)H_u}
=e^{-i(3J/2)t Z_qZ_C}\otimes I_{ab}.
$$

This is an identity on arbitrary superpositions and on inputs entangled with references. There is no average over unknown input labels, measurement, or discarded output. Spectators may become correlated during the sequence; the completed operation restores their entire subsystem.

Watrous's mixed-unitary channels describe convex combinations of output operations. The construction above instead uses a prescribed coherent sequence of conjugated Hamiltonians. Commutation is what turns its Hamiltonian average into an exact finite-time identity. These are not the same physical operation.

Larger blocks give gain $\mu_b=\mathbb E|\epsilon_1+\cdots+\epsilon_b|$. Balanced blocks and reversible use of clean leaders give the [matching construction](bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers). The [synchronized schedule](accuracy-and-resources.md#3-short-exact-synchronized-block-schedules) avoids enumerating the product of the blocks' lists. These gains charge contact time; they do not charge internal encoding or pulse duration. The [finite-control calculation](control-models.md#24-finite-control-consequence) is a separate clock.

## 3. A near-clean prefix is a joint promise, not perfect independent bits

**Foundation:** Watrous §§4.3 and 5.3.1–5.3.2. **Milestones:** M25–M28.

Consider three independent helpers with $p=0.1$. Their eight basis probabilities are

| Hamming weight | Number of labels | Probability per label |
|---:|---:|---:|
| 0 | 1 | 0.729 |
| 1 | 3 | 0.081 |
| 2 | 3 | 0.009 |
| 3 | 1 | 0.001 |

The four largest eigenvalues sum to $0.972$. A fixed permutation maps their labels into $000,001,010,011$, where the first output bit is zero. Complete the permutation bijectively on the other four labels. The first bit is now zero with probability $0.972$; the other two helpers hold the remaining entropy and correlations. Nothing was cooled by a reset, and total entropy is unchanged.

For two modules, this choice gives a favorable-sector weight $0.972^2$ and an unfavorable weight

$$
\Delta=1-0.972^2=0.055216.
$$

Suppose the entire routing unitary is exactly correct on this common favorable sector and preserves it. With fixed helper purifications, its complete-operation half diamond error is at most $2\sqrt\Delta$, about $0.470$. This small example illustrates the mechanism; it does **not** certify a one-percent route. The [finite-size certificates](accuracy-and-resources.md#2-finite-size-advantage-against-every-unknown-helper-protocol) use larger helper pools and much smaller tails.

The general construction compresses once, keeps every entropy-bearing qubit as an occupied spectator, routes, and decompresses once. Its exact action on the common favorable sector is why the initial preparation error is not multiplied by the number of gates. It must agree with the ideal with one common phase on that sector; correct output labels without phase control are insufficient.

The [mixed-helper theorem](mixed-helpers.md#41-complete-reference-preserving-error-without-accumulation) preserves the physical helper marginal exactly in its construction and controls remaining correlations, including preparation-reference correlations, by the stated complete-operation error. This is not exact restoration on arbitrary helper inputs. New pulse or Hamiltonian errors have a separate [composition bound](accuracy-and-resources.md#5-error-composition-and-reuse).

Independence is used to obtain a large high-probability subspace from the preparation entropy deficit. The [correlated-helper counterexample](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped) shows why entropy alone does not imply that concentration for arbitrary helper states. The final milestones combine this boundary with the exact/full-rank distinction and the interaction-strength budget.
