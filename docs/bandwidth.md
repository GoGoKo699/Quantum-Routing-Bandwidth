# Initialization and routing bandwidth

## 1. Result, model, and comparison

There are three internally controllable regions: two modules L and R and a single bus qubit C. Each module contains N=n+s qubits: n designated payload qubits and s helper qubits. Assume n>=1 and s>=0. There is no direct L-R interaction. A pair interaction between any module qubit j and C has operator norm at most J. All contacts may act simultaneously. Arbitrary unitaries confined to a module or to C take zero time. The contact Hamiltonian may have arbitrary time dependence with a well-defined propagator; no minimum switching interval is imposed. Set hbar=1.

The task is to exchange the two n-qubit payloads, including their correlations with arbitrary references. The construction returns C in its original arbitrary unknown state. Compare two helper specifications on **the same physical hardware and the same payload**:

- Clean: the s helpers in each module initially occupy |0>^s and must return there.
- Unknown: the s helpers contain arbitrary unknown quantum information, possibly entangled with references, and must be restored.

There are no additional initialized degrees of freedom, measurements, resets, feedback, or input-dependent control sequences. No internal control connects different regions. In particular, the bus is not included in either freely controlled module.

Let T_clean(n,s) and T_unknown(n,s) be the infimum interaction times for the respective exact tasks. The main laws are

```math
\boxed{T_{\mathrm{clean}}(n,s)=\Theta\!\left(\frac{n}{J\sqrt{(n+s)(s+1)}}\right),}
\tag{1}
```

```math
\boxed{T_{\mathrm{unknown}}(n,s)=\Theta\!\left(\frac{n}{J\sqrt{n+s}}\right).}
\tag{2}
```

The constants in these comparisons do not depend on n or s. Thus the optimal times at fixed n and s differ by Theta(sqrt(s+1)). This is not a comparison that gives the clean case more physical contacts.

The bounds concern interaction time with free internal operations, not runtime with bounded local-gate speed. Preparation of the initial clean helpers is an assumed resource, not a charged operation. The bound is per contact, not a fixed total interaction-norm or control-work budget. Exact control lists can be exponentially long. These qualifications are part of the theorem, not implementation details to be omitted from it.

For 0<=s<=n, (1) simplifies to Theta(sqrt(n/(s+1))/J). The full formula also covers s>n.

## 2. Entropy deficit controls contact second moments

The converse controls concentration in the contact spectrum through a conserved entropy deficit.

For a physical density operator omega on a D-dimensional Hilbert space, write

```math
\mathcal I(\omega)=\log_2D-S(\omega).
\tag{3}
```

This is an entropy deficit in bits. It is invariant under any unitary on the physical system. It is not the quadratic purity Tr omega^2 and is not an energy, work, or temperature.

### 2.1 Remove only cut-local terms

For one module-bus cut, expand the genuine two-sided part of the contacts as

```math
H_{\mathrm{int}}=\sum_{\mu=x,y,z}A_\mu\otimes\sigma_C^\mu,
\qquad A_\mu=\sum_{j,a}c_{ja\mu}\sigma_j^a.
\tag{4}
```

Terms acting on only one side do not contribute to the entropy derivative and are absorbed into the internal terms. Let

```math
v_\mu^2=\sum_{j,a}c_{ja\mu}^2,\qquad v^2=\sum_\mu v_\mu^2.
```

Orthogonal projection onto the two-sided Pauli coefficients contracts the normalized Frobenius norm. If the original edge has norm at most J_j, its normalized Frobenius norm is at most J_j. Therefore

```math
v^2\le\sum_jJ_j^2.
\tag{5}
```

This does NOT assume that subtracting the cut-local terms contracts the operator norm.

### 2.2 A Gaussian bound on each collective coefficient

For fixed mu, the summands on distinct sites commute. With normalized trace tau and v_mu>0,

```math
\tau(e^{uA_\mu})
=\prod_j\cosh\!\left(u\sqrt{\sum_a c_{ja\mu}^2}\right)
\le e^{u^2v_\mu^2/2}.
\tag{6}
```

The scalar Gaussian integral identity e^{tx^2}=E_G exp(sqrt(2t)Gx), G standard normal, implies

```math
\tau(e^{tA_\mu^2})\le(1-2tv_\mu^2)^{-1/2},
\quad 0\le t\lt 1/(2v_\mu^2).
\tag{7}
```

These expressions are unchanged when A_mu is tensored with identities on the remaining physical qubits.

### 2.3 Gibbs variational estimate at a fixed entropy deficit

Apply nonnegativity of relative entropy to omega and the normalized state exp(t A_mu^2)/Tr exp(t A_mu^2). Expanding this inequality, with natural logarithms in this calculation, gives

```math
t\mathrm{Tr}(\omega A_\mu^2)
\le\mathcal I(\omega)\ln2+\ln\tau(e^{tA_\mu^2}).
\tag{8}
```

No commutation between omega and A_mu is required. Choose t=1/(4v_mu^2). Equations (7)-(8) yield

```math
\mathrm{Tr}(\omega A_\mu^2)
\le4\ln2\,[\mathcal I(\omega)+1/2]v_\mu^2.
\tag{9}
```

The v_mu=0 case is trivial.

For Hermitian X_1,X_2,X_3, the operator inequality

```math
(X_1+X_2+X_3)^2\preceq3(X_1^2+X_2^2+X_3^2)
```

follows because the difference is the sum over i<j of (X_i-X_j)^2. Apply it to X_mu=A_mu tensor sigma_C^mu. Thus

```math
\boxed{\mathrm{Tr}(\omega H_{\mathrm{int}}^2)
\le12\ln2\,[\mathcal I(\omega)+1/2]\sum_jJ_j^2.}
\tag{10}
```

This is a state-dependent estimate. It interpolates between root-mean-square strength O(sqrt(sum J_j^2)) for bounded entropy deficit and a potentially collective O(sum J_j) strength when the deficit is extensive. No false input-uniform square-root limit is being asserted.

## 3. From the second moment to information flow

Let A include a module and any local inaccessible references, and let B=C be the bus qubit. The conditional entropy-rate lemma in [Entropy flow](entropy-flow.md) gives

```math
|\dot S_A|\le c_0\sqrt{\mathrm{Tr}(\rho_{AC}h^2)},
\qquad c_0=2\sqrt2/\ln2.
\tag{11}
```

Only the physical part of A is acted on by h; hence its second moment is the same when evaluated in the accessible physical density operator omega.

### 3.1 Published foundation and attribution

Dupuis and Fawzi [DF19](related-work.md#df19), Corollary III.5, established

```math
V(C|A)_\rho\le\log_2^2(2d_C^2+1).
```

Centering the conditional logarithm K=log_2 rho_AC-log_2(rho_A tensor I_C), expressing the entropy derivative as a commutator, and applying weighted Cauchy-Schwarz gives

```math
|\dot S_A|\le2\sqrt{V(C|A)_\rho}\,\Delta_\rho h
\le2\log_2 9\sqrt{\mathrm{Tr}\rho h^2}.
\tag{12}
```

This published-lemma route gives the same n,s exponents with a different numerical constant.

For the smaller constant c_0, the elementary argument in [Entropy flow](entropy-flow.md) uses rho_AC <= d_C(rho_A tensor I_C). In the spectral-overlap distribution of rho and sigma=rho_A tensor I_C, X=ln r_i-ln s_j satisfies E exp(X)<=d_C and E exp(-X)<=d_C. The scalar inequality X^2<=exp(X)+exp(-X)-2 then yields Tr rho(ln rho-ln sigma)^2<=2(d_C-1). At d_C=2 the commutator estimate gives (11). Noncommuting logarithms are handled through the overlap distribution, not by assuming simultaneous diagonalizability. For singular rho, off-support contributions of log sigma must not be discarded before squaring; the support treatment is given in [Entropy flow](entropy-flow.md).

Conditional-variance and entropy-fluctuation ingredients have prior precedents [DF19](related-work.md#df19), [GP22](related-work.md#gp22). Their role here is the combination with (10), the specified physical initialization budget, and a matching routing construction.

### 3.2 Entropy-deficit cut rate

Combining (10)-(11) gives

```math
\boxed{|\dot S_A|
\le 4\sqrt{6/\ln2}\sqrt{\mathcal I(\omega)+1/2}
\sqrt{\sum_jJ_j(t)^2}.}
\tag{13}
```

All entropy units are bits. Internal Hamiltonians have zero entropy contribution across the chosen cut and preserve I. They may have arbitrary norm; they need not be estimated by (13). For singular reference tests, regularize the complete state, apply the differential bound, integrate, and take the limit using entropy continuity. Instantaneous internal pulses do not change cut entropy. More general controls follow by their well-defined propagators and continuity.

For several bus qubits, apply the estimate to each bus-site term and sum. For an input ensemble whose mean physical density operator is bar omega, Jensen's inequality on the second moments similarly yields

```math
\mathbb E|\dot S_L|
\le4\sqrt{6/\ln2}\sqrt{\mathcal I(\bar\omega)+1/2}
\sum_c\sqrt{\sum_jJ_{jc}(t)^2}.
\tag{14}
```

The same unitary must act on every possible input. Otherwise bar omega need not evolve unitarily. At I=0, the sharper one-design constant in [Entropy flow](entropy-flow.md) applies, but (14) supplies a broader entropy-deficit dependence.

## 4. Clean-helper lower bound

Prepare each payload qubit maximally entangled with a reference on its own side. Prepare all 2s physical helpers and C pure. The reference test is pure globally, but its **accessible physical** density operator omega has entropy 2n bits in dimension D=2^{2(n+s)+1}. Therefore

```math
\mathcal I(\omega(t))=2s+1
\tag{15}
```

at all times, despite intermediate correlations, purity concentration, or mixing inside the modules.

Take A to be all physical L qubits together with the n local payload references. Initially S_A=0. An exact payload exchange with the stated helper return produces S_A=2n. Its left cut has N=n+s norm-J contacts. Integrating (13) gives

```math
T\ge\frac{\sqrt{\ln2}}{2\sqrt6}
\frac{n}{J\sqrt{(n+s)(2s+3/2)}}
\ge\frac{\sqrt{\ln2}}{4\sqrt3}
\frac{n}{J\sqrt{(n+s)(s+1)}}.
\tag{16}
```

This uses no assumption that the control leaves the clean helpers pure at intermediate times. Indeed the construction below generally does not.

The converse would also hold if final helpers were allowed to change: an exactly unitary payload channel makes its Choi state pure and factorized from the remaining output. Its reference-assisted cut still carries at least 2n bits. Keeping the return requirement in the task makes the comparison and the constructive statement unambiguous.

### 4.1 Approximate routing

The fixed-error clean-helper law for every $`s\ge0`$ is the $`p=0`$ case of the [mixed-helper theorem](mixed-helpers.md#1-task-and-matching-law). Its converse uses a payload-sized mutual-information estimate, rather than a continuity penalty proportional to the number of helpers.

For the Bell-reference test above, let $`F_e\ge1-\eta`$ be the payload Choi overlap with the ideal pure target after all other outputs are traced out. The payload trace distance from that target is at most $`e=\sqrt\eta`$. Applying the [payload-sized endpoint argument](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound) gives

```math
S_A(T)\ge2n-4ne-\frac32h_2(e),\qquad e=\sqrt\eta.
\tag{17}
```

Replace the required entropy change $`2n`$ in the rate integration by this expression. For fixed sufficiently small $`\eta`$ it is proportional to $`n`$, uniformly in $`s`$. High Choi fidelity here supplies a necessary test of routing accuracy; it is not identified with a worst-case diamond guarantee. The exact construction satisfies the stronger complete-operation specification.

## 5. Matching exact construction with returned clean helpers

Let m=s+1. Divide the N physical qubits of one module into m balanced blocks of sizes b_1,...,b_m, with each size either floor(N/m) or ceil(N/m). Choose as leaders the current payload target q_0 and the s clean helpers q_1,...,q_s. All remaining n-1 payload qubits are distributed as spectators across the blocks.

### 5.1 An occupied-data block

For a block of b qubits, the exact sign-encoding and coherent spectator translations synthesize

```math
J\mu_b Z_{q_i}Z_C\otimes I_{\mathrm{spectators}},
\quad
\mu_b=\mathbb E\left|\sum_{j=1}^{b}\epsilon_j\right|
=\frac{b}{2^{b-1}}\binom{b-1}{\lfloor(b-1)/2\rfloor}.
\tag{18}
```

Each epsilon_j is an independent uniform sign. Here identity on spectators is a full operator identity, not an average channel on random spectator inputs. To recall the encoding explicitly, write a block basis label as (q,r), with spectator Hamming weight w. Set f=1 if 2w>b and f=0 otherwise; output leader q'=q xor f and output spectators r'=r xor q'. The collective magnetization of the output is (-1)^q |b-2w|. Thus a reversible permutation E obeys E^dagger(sum Z_j)E=Z_q D_b. Averaging all spectator XOR translations gives the scalar mean mu_b.

All conjugated diagonal interactions commute. Equal-duration intervals therefore implement the averaged Hamiltonian **exactly**, with no vanishing-interval limit. Applying the block simulations simultaneously yields

```math
H_{\mathrm{block}}=JZ_C\sum_{i=0}^{s}\mu_{b_i}Z_{q_i},
\tag{19}
```

with identity on every unknown spectator.

### 5.2 Coherent use of the initialized leaders

Before (19), perform the module-internal fanout

```math
F=\prod_{i=1}^{s}\mathrm{CNOT}_{q_0\to q_i},
```

and undo F afterward. On inputs with the helpers in |0>^s,

```math
F^\dagger e^{-itH_{\mathrm{block}}}F
\bigl(|\psi\rangle\otimes|0\rangle^{\otimes s}\bigr)
=
\left(e^{-iJ\gamma_{n,s}tZ_{q_0}Z_C}|\psi\rangle\right)
\otimes|0\rangle^{\otimes s},
\tag{20}
```

where

```math
\gamma_{n,s}=\sum_i\mu_{b_i}.
\tag{21}
```

The fanout creates and later removes correlations; it does not clone an unknown state. Formula (20) is a code-subspace isometry identity for clean helpers, not an identity on arbitrary helper inputs. It preserves arbitrary spectator data and arbitrary reference entanglement and works for an arbitrary bus state.

### 5.3 Uniform gain estimate

For the sign sum S_b, E S_b^2=b and E S_b^4=3b^2-2b. Interpolation between its first, second, and fourth moments gives

```math
\sqrt{b/3}\le\mathbb E|S_b|=\mu_b\le\sqrt b.
```

Balanced block sizes obey b_i>=N/(2m). Cauchy-Schwarz supplies the upper bound. Hence

```math
\boxed{\sqrt{(n+s)(s+1)/6}\le\gamma_{n,s}\le\sqrt{(n+s)(s+1)}.}
\tag{22}
```

No optimal prefactor is claimed. The explicit block grouping need not maximize the gain at small n,s.

### 5.4 Full payload exchange

Rotate the target and bus bases to realize the XX, YY, and ZZ versions of (20). The three angle-pi/4 operations commute on the target-bus subsystem and give SWAP up to a fixed global phase in time 3pi/(4J gamma_n,s).

A buffered sequence uses 2n+1 target-bus SWAPs. For j=1,...,n, swap L_j with C, then R_j with C. Finally swap L_1 with C and rotate only the L payload labels left by one position. The output is precisely the payload exchange with the bus restored; all helpers were restored after each elementary gate. Therefore

```math
\boxed{T_{\mathrm{clean}}(n,s)\le\frac{3\pi(2n+1)}{4J\gamma_{n,s}}.}
\tag{23}
```

Equations (16),(22),(23) prove (1). Synchronize the block translations using the same counter, restricted to the spectator bits of each block. Uniform marginal coverage of every block suffices because the contact is additive. The [exact synchronized schedule](accuracy-and-resources.md#3-short-exact-synchronized-block-schedules) uses

```math
K_{\mathrm{exact}}=2^{\max_i(b_i-1)}
=2^{\lceil(n+s)/(s+1)\rceil-1}
```

intervals per Ising gate. All conjugated contacts commute, so no short-time approximation is involved. At $`s=0`$ this reduces to $`2^{n-1}`$; with $`s=\Theta(n)`$ it is bounded independently of $`n`$. Internal controls are still free. Approximate-list guarantees are in [Accuracy and resources](accuracy-and-resources.md#4-polynomial-contact-lists-at-fixed-uniform-accuracy); finite gate-speed costs are separate in [Control models](control-models.md).

## 6. Unknown helpers on identical hardware

For the unknown-helper task, put every physical module qubit, including the s helpers, in a Bell pair with its own inaccessible reference. The bus can be fixed pure for the lower bound. The physical density matrix always obeys omega<=2I/D. Orthogonality of the pair-contact Pauli coefficients gives

```math
\mathrm{Tr}\omega H_{\mathrm{int}}^2\le2(n+s)J^2.
```

Only the payload must cross the cut, generating 2n bits. Equation (11) yields

```math
T_{\mathrm{unknown}}(n,s)\ge\frac{\ln2}{2J}\frac{n}{\sqrt{n+s}}.
\tag{24}
```

For the upper bound, use all N=n+s qubits in the occupied-data block amplifier. Its spectators, including the unknown helpers, are returned after each target-bus operation. Exchange only the n payload labels in the same buffered sequence:

```math
T_{\mathrm{unknown}}(n,s)
\le\frac{3\pi(2n+1)}{4J\mu_{n+s}}.
\tag{25}
```

Since sqrt((n+s)/3)<=mu_(n+s)<=sqrt(n+s), (24)-(25) prove (2). Both cases have identical numbers and strengths of bus contacts, identical payloads, free internal controls, and helper return. The only altered promise is the initial helper state.

## 7. Consequences and scope

For s between zero and n, the exact optimal clean-helper interaction time has the following scaling:

| Clean helpers per module | Interaction time |
|---|---|
| 0 or a fixed number | Theta(sqrt(n)/J) |
| Theta(log n) | Theta(sqrt(n/log n)/J) |
| Theta(sqrt n) | Theta(n^(1/4)/J) |
| Theta(n) | Theta(1/J) |

The entries refer to ideal internal controls. In particular, the constant-time endpoint does not imply a constant-depth, bounded-strength implementation of the internal encodings or fanout.

Equation (13) bounds arbitrary mixed physical states through their entropy deficit. The exact construction and law (1) use pure helpers. The [mixed-helper theorem](mixed-helpers.md) gives the matching fixed-error law for independent known product preparations, including their preparation references. The [correlated-state counterexample](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped) explains why entropy alone does not determine achievable bandwidth for arbitrary helper states. Preparation robustness is distinct from ongoing dynamical noise.

With bounded control strength, the displayed small-gate recursive implementation has linear total duration at a fixed internal/contact strength ratio G/J. That is a statement about a particular compiler, not a universal linear lower bound for all finite-speed protocols. The workspace law and this finite-control comparison use distinct resource models.
