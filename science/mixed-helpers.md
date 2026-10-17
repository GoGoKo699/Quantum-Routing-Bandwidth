# Imperfect initialization and reusable routing bandwidth

## 1. Task and matching law

Use the same two-module, one-qubit-bus model as [the exact bandwidth theorem](bandwidth.md). Each module has $`n\ge1`$ payload qubits and $`s\ge0`$ helper qubits, with $`N=n+s`$ bounded-strength contacts. Every contact has operator norm at most $`J`$. Arbitrary module-internal controls and bus-only controls have zero charged duration. Both interfaces are bounded; there is no direct module-to-module coupling, measurement, reset, or extra initialized workspace.

The helpers in each module are independently prepared in the known state

```math
\rho_p^{\otimes s},\qquad
\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|,
\qquad 0\le p\le\tfrac12.
```

Define their entropy deficit per helper by $`d(p)=1-h_2(p)`$, in bits. The two modules' helper preparations are independent of one another and of the payload and bus. The payload and bus may have arbitrary external reference entanglement.

A strong error convention makes restoration precise. Retain an inaccessible purification of each helper preparation,

```math
|\chi_p\rangle_{HE}
=\sum_{x\in\{0,1\}^s}\sqrt{q_x}|x\rangle_H|x\rangle_E,
\qquad q_x=p^{|x|}(1-p)^{s-|x|}.
```

Let $`\Phi_U`$ insert these fixed purifications and apply the physical protocol $`U`$. Let $`\Phi_{\ast}`$ insert the same purifications, exchange the payloads, and act as identity on the bus, helpers, and preparation references. Require

```math
\frac12\|\Phi_U-\Phi_{\ast}\|_\diamond\le\epsilon.
\qquad\text{(1)}
```

The supremum includes all payload/bus inputs and all their reference extensions. The helper purifications are fixed input resources, not additional freely chosen input qubits or controllable workspace. Different purifications of the same helper states give the same guarantee by an isometry on the inaccessible reference.

**Theorem.** For every fixed $`0\lt \epsilon\le0.1`$, the optimal interaction time under (1) satisfies

```math
\boxed{
T_{\epsilon,p}(n,s)
=\Theta_\epsilon\!\left(
\frac{n}{J\sqrt{(n+s)\{1+s[1-h_2(p)]\}}}
\right).
}
\qquad\text{(2)}
```

The constants may depend on $`\epsilon`$, but not on $`n,s,p`$. The statement is uniform even when $`p`$ varies with system size. In particular, it includes $`p=0`$, $`p=1/2`$, and arbitrarily weak polarization. It applies to all $`s\ge0`$, not only $`s\le n`$.

The error covers the complete routing operation and helper restoration, rather than error per helper or per gate. The constructed protocol returns the physical helper density matrix **exactly** for this diagonal preparation. Residual data-helper correlations, bus errors, and changes in preparation-reference correlations are covered by (1); they are not asserted to vanish exactly.

This is a preparation-error theorem with ideal unitary controls. It is not a theorem about decoherence during the route, imperfect pulses, unknown calibration, or finite internal-control speed. Preparation and compression costs are outside the charged interaction-time model. A known product mixed state is not interchangeable with an arbitrary state of the same entropy; Section 7 gives a counterexample.

## 2. Converse: an entropy budget with a payload-sized continuity bound

Purify the helpers locally as above. Put every payload qubit in a Bell pair with an inaccessible reference on its own side, and choose a pure bus for this lower-bound test. The complete state including references is pure. The accessible physical state $`\omega`$ has

```math
\mathcal I(\omega)=\log_2D-S(\omega)=1+2s\,d(p).
\qquad\text{(3)}
```

This entropy deficit is conserved by every admissible physical unitary, even while the helpers become correlated or locally more polarized. The [entropy-deficit cut bound](bandwidth.md#32-entropy-deficit-cut-rate) therefore gives

```math
|\dot S_A|
\le 4\sqrt{6/\ln2}\,J\sqrt{N\{3/2+2s\,d(p)\}},
\qquad\text{(4)}
```

where $`A`$ includes the entire physical left module, its payload references, and its helper-preparation references. Initially $`S_A=0`$. The underlying conditional entropy-rate estimate may equivalently use the published conditional-variance bound [DF19](../references/RELATED_WORK.md#df19), changing only a universal constant.

It is unnecessary to pay an error-continuity factor proportional to the helper dimension. Let $`a`$ consist of the left payload and its original payload references, and let $`b`$ be the corresponding right subsystem. Each has dimension $`2^{2n}`$. The ideal exchanged-payload Choi vector is maximally entangled across $`a:b`$, so its mutual information is $`4n`$ bits.

Tracing the helper, bus, and preparation-reference outputs cannot increase trace distance. Equation (1) puts the actual $`ab`$ state within trace distance $`\epsilon`$ of that vector. Entropy continuity on $`a`$, $`b`$, and $`ab`$ gives

```math
I(a:b)\ge4n-8n\epsilon-3h_2(\epsilon).
```

By data processing of mutual information and purity of the complete output,

```math
2S_A=I(A:A^c)\ge I(a:b).
```

Consequently

```math
S_A(T)\ge2n-4n\epsilon-\tfrac32h_2(\epsilon).
\qquad\text{(5)}
```

For $`0\lt \epsilon\le0.1`$ the right-hand side is at least $`b_\epsilon n`$, where

```math
b_\epsilon=2-4\epsilon-\tfrac32h_2(\epsilon)\gt 0.
```

Equations (4)-(5), using $`3/2+2sd(p)\le2[1+sd(p)]`$, imply the explicit lower bound

```math
T_{\epsilon,p}\ge
\frac{b_\epsilon}{4\sqrt{12/\ln2}}
\frac{n}{J\sqrt{N[1+sd(p)]}}.
\qquad\text{(6)}
```

This converse actually needs only the corresponding accuracy of the payload channel on its Bell-reference test, not helper return. The matching construction meets the stronger preparation-inclusive condition (1). The use of $`a,b`$ rather than the full helper-bearing cut removes the restriction $`s\le n`$ in the earlier direct entropy-continuity estimate. Singular states and instantaneous internal pulses are handled as in [Entropy flow](entropy-flow.md#3-supports-and-admissible-controls).

## 3. Reversible concentration at finite error

### 3.1 Exact spectral criterion

Let $`\lambda_1\ge\cdots\ge\lambda_{2^s}`$ be the helper eigenvalues. A unitary can place weight at least $`1-\delta`$ in a subspace where $`r`$ specified helper bits are zero precisely when

```math
\sum_{i=1}^{2^{s-r}}\lambda_i\ge1-\delta.
\qquad\text{(7)}
```

Necessity is the variational characterization of the sum of the largest eigenvalues; sufficiency maps their eigenvectors into the zero-prefix subspace. For the product state above, decreasing eigenvalue order is increasing Hamming weight. A fixed permutation of the $`s`$ helper bits' full computational-basis labels implements this mapping. It uses no measured label, extra Hilbert-space dimension, or reset.

The remaining $`s-r`$ qubits retain the compressed entropy. They are kept inside the module as arbitrary spectator qubits; nothing is discarded. After the routing operation the permutation is reversed.

Reversible polarization concentration is established prior work; see Schulman and Vazirani's [Scalable NMR Quantum Computation](https://arxiv.org/abs/quant-ph/9804060), especially its explicit treatment of initially absent clean workspace. The statement here composes concentration with data-preserving contact amplification and a complete-operation error bound. It is not a claim to invent purity concentration.

### 3.2 An elementary uniform estimate

Write $`\beta=1-2p`$ and $`x=s\beta^2`$. The binary entropy series gives

```math
\frac{\beta^2}{2\ln2}\le d(p)\le\beta^2.
\qquad\text{(8)}
```

Consider the helper labels with Hamming weight at most $`s(1/2-\beta/4)`$. Hoeffding's inequality applied first to the actual Bernoulli distribution and then to the uniform counting distribution gives

```math
\Pr_p(\text{outside})\le e^{-x/8},
\qquad
|\text{inside}|\le2^s e^{-x/8}.
\qquad\text{(9)}
```

The noninteger threshold is interpreted by its floor; the bounds remain valid. If $`x\ge8\ln(1/\delta)`$, choose

```math
r=\left\lfloor\frac{x}{8\ln2}\right\rfloor.
```

Then (9) fits the inside labels into $`2^{s-r}`$ output labels with zero prefix and failure weight at most $`\delta`$. If the threshold is not met, choose $`r=0`$, which has exactly zero failure weight. This fallback uses the occupied-data protocol, not a failed preparation step.

For $`0\lt \delta\le1/4`$, these choices satisfy the simple conservative bound

```math
r+1\ge c_\delta[1+sd(p)],
\qquad
c_\delta=\frac1{2+8\ln(1/\delta)+8\ln2}.
\qquad\text{(10)}
```

For small $`x`$, (8) and the fallback prove (10). For large $`x`$, use $`r+1\gt x/(8\ln2)`$ and $`sd(p)\le x`$. Thus no fixed-$`p`$ asymptotic assumption or unproved substitution of entropy for a helper count is needed. For finite examples, criterion (7) is much sharper than (9).

## 4. Route on the good subspace; decompress once

After compression, a module still has exactly $`N=n+s`$ qubits. Use the target and the $`r`$ near-clean prefix bits as $`r+1`$ block leaders. All remaining qubits, including the $`s-r`$ entropy-bearing helpers, are occupied spectators.

The [balanced-block construction](bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers) is an operator identity on arbitrary spectator inputs. Its use therefore requires no independence among the compressed spectators. With balanced block sizes $`b_i`$ and $`\mu_b=\mathbb E|\epsilon_1+\cdots+\epsilon_b|`$, its target-bus gain is

```math
\gamma_{N,r}=\sum_{i=0}^r\mu_{b_i},
\qquad
\sqrt{N(r+1)/6}\le\gamma_{N,r}\le\sqrt{N(r+1)}.
\qquad\text{(11)}
```

Exchange only the $`n`$ payloads with the buffered $`2n+1`$-SWAP schedule. On the subspace where both modules' prefix bits are zero, the complete operation is exactly the payload exchange tensored with identity on every helper and the bus, up to a common global phase. It costs

```math
T\le\frac{3\pi(2n+1)}{4J\gamma_{N,r}}.
\qquad\text{(12)}
```

Compression and decompression are each applied once around the whole route. Their duration is free only because internal operations are free in this model. The interaction sequence is finite, but can be exponentially long. This does not supply a new efficient bounded-strength compiler.

### 4.1 Complete reference-preserving error, without accumulation

Let $`P_G`$ project onto the two-module good helper subspace before compression. Its complement has initial weight

```math
\Delta\le1-(1-\delta)^2\le2\delta.
```

The actual and ideal full unitaries agree on every payload/bus input tensored with $`P_G`$, with the same phase. Both are norm-one unitaries on the bad subspace. For any normalized input including arbitrary payload/bus references and the fixed helper purifications,

```math
\|(U-U_{\ast})|\Psi\rangle\|
\le2\|(I-P_G)|\Psi\rangle\|
=2\sqrt\Delta.
\qquad\text{(13)}
```

The pure-output trace distance is no larger than this vector norm, and mixed payload inputs follow by purification. Equivalently the fixed-preparation isometries differ in operator norm by at most $`2\sqrt\Delta`$, which bounds their half diamond distance. Set

```math
\delta=\epsilon^2/8.
\qquad\text{(14)}
```

Then (13) proves (1), including the inaccessible helper references. There is no multiplication of $`\delta`$ by $`n`$ or by the number of elementary gates. The failure is one fixed low-weight input sector, not a fresh preparation failure sampled at every gate.

Without retaining a coherent helper purification, the diagonal mixture even gives a joint payload-bus-helper half diamond error at most $`\Delta`$, by convexity. The theorem uses the stronger square-root guarantee rather than relying on that weaker setting.

### 4.2 Exact marginal return and coherent reuse

After exact spectator averaging, conjugating by the fanout gives, for a target-bus Ising gate,

```math
JZ_qZ_C\left(\mu_{b_0}+\sum_{i=1}^r\mu_{b_i}Z_{h_i}\right)
\otimes I_{\rm spectators}.
\qquad\text{(15)}
```

This is diagonal in every helper bit even outside the good subspace. The target/bus basis rotations do not act on those bits. The full route followed by decompression therefore has the form

```math
U=\sum_x |x\rangle\langle x|_{H_LH_R}\otimes V_x
```

in the original helper eigenbasis, with every $`V_x`$ unitary on payload and bus. Consequently the joint physical helper density matrix is restored exactly for the specified diagonal input, for every payload input. The bad-sector $`V_x`$ may correlate helpers with data or change preparation-reference coherences; these effects are counted in (1).

The good and bad sectors are invariant, so any number of coherent uses on fresh payload registers still agrees with the ideal operation on the same original good sector. In the absence of any new physical noise, the same $`2\sqrt\Delta`$ bound applies to the **entire sequence**, including references to all payload batches. This is a bound on correlated preparation error, not an assertion of independent zero-error calls or indefinite fault tolerance under ongoing noise.

Combining (10)-(14) with (6) proves (2). The constants obtained here deteriorate when $`\epsilon`$ tends to zero; no uniform zero-error limit is claimed.

## 5. Zero error and nonzero error are different tasks

For $`0\lt p\le1/2`$, the helper state has full rank. If a physical unitary implements an exactly unitary payload-and-bus channel for that fixed helper input, each positive-weight eigenstate input must implement that same unitary channel: their Choi states form a convex mixture with a pure output. Stinespring uniqueness gives $`U=U_{\ast}\otimes V_H`$ on the full physical space. Under exact preparation-reference return, comparison of the nonzero Schmidt coefficients forces $`V_H`$ to be a common scalar identity.

Thus for the exact version of (1), a full-rank preparation requires the same operation as arbitrary unknown helpers. The existing unknown-helper converse and construction give

```math
\boxed{
T_{0,p}(n,s)=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right),
\qquad 0\lt p\le1/2.
}
\qquad\text{(16)}
```

This exact/full-rank obstruction is already explicitly noted in the Outlook of [UHMG26](../references/RELATED_WORK.md#uhmg26), which identifies approximate transfer with thermal ancillas as a further direction. Equation (2) supplies a matched answer for this modular routing problem, not a claim to have first noticed the obstruction.

For any fixed allowed error and fixed $`p\lt 1/2`$, increasing $`s`$ supplies a growing advantage. For zero error, no positive full-rank bias alone changes the unknown-helper exponent. The two statements are compatible because the constants and the tolerated rare input sectors change with the error requirement.

## 6. Finite spectral certificate and operator checks

For $`n=s=256`$, $`p=0.1`$, and complete-operation half diamond budget $`\epsilon=0.01`$, exact binomial-shell summation permits $`r=82`$ prefix leaders with one-module bad weight at most $`1.149\times10^{-5}`$. The balanced-block gain is $`160`$ and the complete purified-input error certificate is below $`0.009585`$. The same explicit unknown-helper amplifier has gain $`\mu_{512}\simeq18.0453`$; the ratio of the two construction gains is about $`8.87`$. This is not the ratio of independently optimized prefactors.

These large-size figures are calculations of spectral probabilities and proven timing formulas, not simulation of a 1,025-qubit circuit. The compressed prefix has high **joint** zero probability; it is not a set of independent perfectly clean qubits.

The executable check [verify_mixed_helpers.py](../verification/checks/verify_mixed_helpers.py) compares exact shell sums against complete spectra, checks the uniform concentration estimates, and propagates all helper sectors and payload/bus columns for small systems using the existing raw-contact implementation. Its largest full physical system has 11 qubits. For the purification-inclusive error, it evaluates the exact Gram operator

```math
\sum_x q_x(V_x-U_{\ast})^\dagger(V_x-U_{\ast}),
```

whose largest eigenvalue is the squared isometry operator error. This is uniform over all payload/bus inputs and their references. Helper-block invariance, good-subspace phases, and repeated uses are checked separately. Recorded finite examples do not establish the theorem by themselves.

## 7. Why the product-state assumption cannot be dropped

Consider instead, independently in each module,

```math
\sigma_s=(1-a)I/2^s+a|0^s\rangle\langle0^s|,
\qquad 0\lt a\lt 1.
```

Its entropy deficit is $`as-h_2(a)+o(1)`$, which is extensive. Nevertheless its largest-$`2^{s-r}`$ spectral mass is exactly

```math
a+(1-a)2^{-r}.
```

At small fixed compression error, no growing number of clean prefix bits can be obtained. More strongly, the two-module preparation has a both-maximally-mixed component of weight $`w=(1-a)^2`$. Payload Choi fidelity is linear in the helper input. If the average payload infidelity is at most $`\epsilon`$, that component has infidelity at most $`\epsilon/w`$. At sufficiently small fixed $`\epsilon/w`$, the reference-assisted unknown-helper bound forces time $`\Omega(n/[J\sqrt N])`$; the exact unknown-helper construction attains that scale.

Thus a fixed low-weight pure spike plus a large maximally mixed component can have extensive entropy deficit without the product-state bandwidth enhancement. The universal entropy-deficit **converse** remains true, but saturation from entropy alone is false for general correlated helper states. Spectral concentration is an essential hypothesis of the matching imperfect-initialization law.

## 8. Relation to existing work

[UHMG26](../references/RELATED_WORK.md#uhmg26) proves a general relationship between exact robust-subspace transfer and commutator Schatten norms, includes multiple transferred qubits, and gives a symmetric-subspace compression construction. Compression before transfer and mixed states supported in a favorable subspace therefore are not new mechanisms here. Its stated exact theorem and power-law light cones do not themselves supply an extensive full-register throughput bound or an iid full-rank fixed-error optimal-time law for the three-region bounded-bus model. The direct entropy budget and its matched coherent construction supply those additional steps.

The arXiv PDF's Outlook explicitly identifies approximate transfer with thermal ancillas as a further direction. The comparison refers to those theorem statements and that Outlook, rather than asserting the absence of related work elsewhere.

Schulman and Vazirani's reversible concentration machinery and the existing conditional-variance and routing predecessors remain essential attribution. This result does not solve general power-law thermal transfer, a fully characterized noisy-device problem, or optimal finite-speed compilation. The matched claim is Equation (2) with the preparation-inclusive error convention (1).
