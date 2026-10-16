# Accuracy, finite certificates, and resource normalization

This document supplies quantitative guarantees for the bandwidth theorems: an all-helper-size approximate comparator, finite-size speed certificates, shorter exact contact lists, coherent fixed-accuracy compilation, and the dependence on the interaction budget. The [main independent-helper theorem](mixed-helpers.md) and [exact endpoints](bandwidth.md) retain their specified input spaces. These results concern ideal internal control; they do not assert a device runtime or noise threshold.

## 1. Bandwidth and finite-error comparator

An exchange moves $`n`$ logical qubits in each direction. Define the one-direction bandwidth as $`\mathcal B=n/T`$; counting both directions multiplies it by two. No frequency bandwidth or bosonic channel capacity is meant. Write $`N=n+s`$ and

```math
B_e(n)=2n-4ne-\tfrac32h_2(e),\qquad 0\le e\le0.1.
```

Consider a protocol required to approximate the payload exchange tensored with identity on **arbitrary** helpers and bus, with half diamond error at most $`e`$. Purify the maximally mixed state of every physical qubit: place the left module's references inside the left cut, and the bus reference on the right. The accessible physical state is exactly $`I/D`$ throughout the unitary evolution. Initially the reference-assisted left entropy is zero. Pauli orthogonality gives

```math
\mathrm{Tr}\omega(H_{LC}^{\mathrm{int}})^2
=\|H_{LC}^{\mathrm{int}}\|_F^2\le NJ^2.
```

The payload-sized mutual-information argument in [Mixed helpers, Section 2](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound) gives final cut entropy at least $`B_e(n)`$, independent of the helper dimension. Thus

```math
\boxed{T_{\mathrm{unknown},e}\ge\frac{B_e(n)}{c_0J\sqrt N},
\qquad c_0=2\sqrt2/\ln2.}\tag{1}
```

The published [DF19](related-work.md#df19) route proves the same inequality with $`c_0`$ replaced by $`c_{\mathrm{DF}}=2\log_2 9`$. At $`e=0`$, (1) has coefficient $`\ln2/\sqrt2`$. The maximally mixed bus is a legitimate reference test because this comparator must work on an arbitrary bus. This coefficient must not be silently used for a task that promises one fixed pure bus input.

If only payload Choi infidelity $`\zeta`$ is specified, projection of a purification onto the ideal Choi vector gives payload trace distance at most $`\sqrt\zeta`$. Replace $`e`$ in $`B_e`$ by $`\sqrt\zeta`$ whenever it is at most $`0.1`$. This is a necessary-condition argument, not an equivalence between Choi fidelity and diamond accuracy. The entropy-continuity step is the [Audenaert bound](related-work.md#a07); its use on payload-sized subsystems is why no factor proportional to $`s`$ appears.

Equation (1) also makes the correlated-helper counterexample precise for arbitrary $`s`$. A both-maximally-mixed component with weight $`w`$ and total payload infidelity at most $`\epsilon`$ has conditional infidelity at most $`\epsilon/w`$. Its physical state has at most the chosen pure bus's one-bit entropy deficit. The same proof, with an extra $`\sqrt2`$ in the rate, gives $`\Omega(n/[J\sqrt N])`$ for sufficiently small fixed $`\epsilon/w`$, without any restriction $`s\le n`$.

## 2. Finite-size advantage against every unknown-helper protocol

A comparison of two explicit constructions is not an exclusion of faster alternatives. To certify an advantage over all protocols in the unknown-helper class, compare its lower bound (1) with the mixed-helper constructive upper bound at the same error and contacts.

Set $`p=1/10`$ and $`e=\epsilon=1/100`$. Choose the maximum integer $`r`$ whose compressed zero-prefix tail is at most $`\delta=1/80000`$. Let $`q`$ be that exact tail and let $`\gamma_{N,r}`$ be the balanced-block gain. The mixed-helper error obeys

```math
E_{\mathrm{prep}}^2\le4(2q-q^2)\le\epsilon^2,
\qquad
JT_{\mathrm{mixed}}\le\frac{3\pi(2n+1)}{4\gamma_{N,r}}.
```

All required spectral decisions can be made with integers. At Hamming weight $`k`$, the eigenvalue numerator is $`9^{s-k}`$ with denominator $`10^s`$, repeated $`\binom sk`$ times. If the largest $`2^{s-r}`$ labels contain all shells below $`k_{\ast}`$ and $`u`$ labels in shell $`k_{\ast}`$, then

```math
q=\frac{\displaystyle\sum_{k\gt k_{\ast}}\binom sk9^{s-k}
+(\binom{s}{k_{\ast}}-u)9^{s-k_{\ast}}}{10^s}.\tag{2}
```

The inequalities $`q\le1/80000`$ and failure of the next prefix length are checked by integer cross multiplication, not floating-point tail evaluation. Gains are rational because every $`\mu_b`$ is rational.

For fully rational time enclosures, use $`\pi\lt 22/7`$, $`c_0\lt 41/10`$, $`h_2(1/100)\lt 1/10`$, and $`\sqrt N\le\lceil\sqrt N\rceil`$. Consequently

```math
U=\frac{3(22/7)(2n+1)}{4\gamma_{N,r}},\qquad
L=\frac{(49/25)n-3/20}{(41/10)\lceil\sqrt N\rceil}
```

satisfy $`JT_{\mathrm{mixed}}\lt U`$ and $`JT_{\mathrm{unknown},e}\gt L`$. The strict ratio $`L/U\gt 1`$ certifies an advantage, not merely an observed numerical trend.

| Payload and helpers per module $`n=s`$ | Prefix bits $`r`$ | Gain | Mixed $`JT`$ upper | Unknown $`JT`$ lower | Certified advantage factor, at least |
|---:|---:|---:|---:|---:|---:|
| 512 | 191 | 360 | 6.712 | 7.647 | 1.139 |
| 1024 | 426 | 768 | 6.289 | 10.640 | 1.692 |
| 2048 | 917 | 1536 | 6.288 | 15.296 | 2.433 |

Displayed upper values are rounded upward; lower values and advantage factors are rounded downward. These examples use the same number of contacts, the same payload, and the same error budget. Their helper input promises differ, exactly as in the resource comparison. Large systems are evaluated by exact spectral sums and proven timing formulas, **not simulated as large quantum circuits**.

The certificate does not depend on the smaller elementary entropy constant: replacing $`41/10`$ by $`32/5\gt c_{\mathrm{DF}}`$ still certifies an advantage at $`n=s=1024`$ and $`2048`$. In the latter case the factor exceeds $`1.55`$ using the published variance bound alone. The exact rational numbers and tail certificates are generated by [verify_scientific_closure.py](../checks/verify_scientific_closure.py).

The simple constant bounds themselves have elementary certificates: $`\ln2\gt 56/81`$, $`\sqrt2\lt 99/70`$, and $`9^5\lt 2^{16}`$. Also $`\ln100\lt 5`$ and $`-\ln(0.99)\le1/99`$ give $`h_2(0.01)\lt 0.1`$. The decimal table is therefore not needed to decide the strict speed comparison.

## 3. Short exact synchronized block schedules

The contact after sign encoding is an **additive sum** over blocks. Averaging every joint combination of spectator labels is unnecessary: uniform marginal translation in each block suffices.

Suppose the $`m=r+1`$ blocks have sizes $`b_i`$, and write $`w_i=b_i-1`$, $`w_{\max}=\max_i w_i`$. Use

```math
K_{\mathrm{exact}}=2^{w_{\max}}
=2^{\lceil N/(r+1)\rceil-1}\tag{3}
```

intervals. In interval $`\ell=0,\ldots,K_{\mathrm{exact}}-1`$, translate block $`i`$ by the low $`w_i`$ bits of $`\ell`$. Each of that block's $`2^{w_i}`$ translations occurs equally often. Thus

```math
\frac1{K_{\mathrm{exact}}}\sum_\ell
\sum_i Z_{q_i}D_{b_i}(x_i\oplus\ell_{[w_i]})
=\sum_i\mu_{b_i}Z_{q_i}\otimes I_{\mathrm{spectators}}.\tag{4}
```

Cross-block independence is not required because there are no products of the block coefficients in this Hamiltonian average. All conjugated contacts commute. Equal-duration evolution intervals therefore realize (4) exactly, not as a first-order approximation. Fanout conjugation preserves that identity on the whole helper basis, including the unfavorable sector. The physical helper marginal-return and common-sector arguments remain intact.

The full route uses $`3(2n+1)K_{\mathrm{exact}}`$ raw contact intervals. For the three finite certificates in Section 2, the exact lengths are respectively 32, 16, and 16 intervals per Ising gate; their total contact counts are 98,400, 98,352, and 196,656. At fixed $`p\lt 1/2`$, fixed accuracy, and $`s`$ proportional to $`n`$, the compression theorem allows $`r=\Theta(s)`$, so the **exact** contact count is $`O(n)`$. At $`r=0`$, the no-helper length remains $`2^{N-1}`$.

This reduction does not assign a small elementary-gate cost to compression or the internal block encodings. It removes an unnecessary product of averaging-list lengths, not the distinction between contact time and physical control time. [The raw-contact verifier](../checks/verify_workspace_construction.py) implements the synchronized schedule; the closure suite compares it with full joint averaging on every basis label in its finite tests.

## 4. Polynomial contact lists at fixed uniform accuracy

A polynomial alternative is available even where (3) is long. Choose $`K`$ independent uniform synchronized translation labels offline, then fix that list for every input and every gate. For any module basis label $`x`$, the dimensionless diagonal contact coefficient $`F_\ell(x)`$ lies in $`[-N,N]`$ and has the exact averaged coefficient as its mean. [Hoeffding's inequality](related-work.md#h63) and a union bound over the $`2^N`$ labels give

```math
\Pr\!\left(\|\overline F_K-F_{\ast}\|\gt a\right)
\le2^{N+1}\exp[-Ka^2/(2N^2)].\tag{5}
```

With $`M=3(2n+1)`$, $`\theta=\pi/4`$, and gain $`\gamma=\gamma_{N,r}`$, the intended contact duration is $`\theta/(J\gamma)`$. Diagonal exponentiation gives one-gate operator error at most $`\theta a/\gamma`$. A telescoping product bound gives full-unitary error at most $`M\theta a/\gamma`$. Reusing a good list under the fixed target relabelings and basis conjugations leaves this guarantee unchanged.

For full-route operator error at most $`\eta`$ and offline failure probability at most $`q_{\mathrm{off}}`$, it suffices that

```math
K\ge\frac{2N^2M^2\theta^2}{\eta^2\gamma^2}
\left[(N+1)\ln2+\ln(1/q_{\mathrm{off}})\right].\tag{6}
```

Using $`\gamma^2\ge N(r+1)/6`$, this is $`O(n^2N^2/[(r+1)\eta^2])`$ per gate and $`O(n^3N^2/[(r+1)\eta^2])`$ over the route at fixed offline confidence. The better of this bound and (3) may be used. In the explicit finite certificates, the short **exact** list is vastly better than this conservative concentration estimate.

For mixed preparation, take $`\delta=\epsilon^2/32`$ and $`\eta=\epsilon/2`$. The preparation isometry bound is at most $`\epsilon/2`$, while the approximation of the full physical unitary contributes at most $`\eta`$ to half diamond distance. The total is at most $`\epsilon`$. The asymptotic bandwidth law is unchanged at fixed error.

The compressed helper density is diagonal. Each translated, encoded, decoded interval is diagonal in helper labels, and target/bus basis changes do not rotate those labels. Hence the physical helper marginal still returns exactly for the specified input; payload/helper correlations are covered by the total error. Randomness chooses a list before execution and never mixes physical output channels or depends on unknown input data. The statement does not provide efficient verification of a large sampled list or an elementary-gate implementation of the compression permutation.

## 5. Error composition and reuse

For physical unitaries $`U,V`$ and any inserted pure preparation, operator error $`\|U-V\|\le\eta`$ implies half diamond error at most $`\eta`$. For pure input outputs $`|u\rangle,|v\rangle`$, this follows from their trace distance being bounded by $`\|u-v\|`$; reference extensions and mixed inputs follow by purification. It is also consistent with the completely bounded trace-norm framework in [W18, Chapter 3](related-work.md#w18).

If a route is exact on one invariant favorable preparation sector of bad weight $`\Delta`$, any number of ideal coherent uses on fresh payloads still agrees with the ideal on that same sector and differs by at most $`2\sqrt\Delta`$ on the inserted-preparation isometry. The bound includes references to all batches; it is not a claim that successive errors are independent. The fresh-batch check explicitly keeps two distinct payload pairs and the common bus, rather than just applying a power to one payload state.

Synthesis and dynamical errors are different. For a specified finite circuit with per-pulse operator errors $`\eta_\ell`$ and an integrable Hamiltonian perturbation $`E(t)`$ during contact evolution, telescoping and Duhamel's identity give

```math
\frac12\|\Phi_{\mathrm{actual}}-\Phi_{\ast}\|_\diamond
\le2\sqrt\Delta+\eta_{\mathrm{list}}
+\sum_\ell\eta_\ell+\int_0^T\|E(t)\|\,dt.\tag{7}
```

This bound is for unitary control imperfections. A contact perturbation bounded by $`e_j(t)`$ per edge has the conservative contribution $`\int\sum_j e_j(t)dt`$. No cancellation of such errors is assumed. Under repeated uses, the new synthesis/dynamical contributions generally accumulate, unlike the initial common-sector error. Equation (7) is a stability statement, not a fault-tolerance threshold, a Markovian-noise model, or evidence of practical control accuracy.

## 6. What changes under a different interaction budget

### 6.1 Per-contact and quadratic budgets

The primary theorem uses $`\|h_{jc}(t)\|\le J`$ for each edge. The aggregate quadratic strength on a module cut can therefore grow like $`J\sqrt N`$. This is why increasing the module changes even the no-initialization bandwidth.

If instead one imposes $`\sum_j\|h_{jc}(t)\|^2\le\Lambda_2^2`$ per module cut and allows arbitrary allocation, the same moment converse replaces $`J\sqrt N`$ by $`\Lambda_2`$. Equal allocation $`J=\Lambda_2/\sqrt N`$ in the construction attains it. Thus, within the same free-internal-control and fixed-error model,

```math
T_{\epsilon,p}^{(2)}
=\Theta_\epsilon\!\left(\frac{n}{\Lambda_2\sqrt{1+sd(p)}}\right).
\tag{8}
```

Unknown helpers have $`\Theta_\epsilon(n/\Lambda_2)`$ time. The relative initialization advantage survives this quadratic-budget comparison. The constraint is on the sum of **edge** squared norms, not necessarily on the Frobenius norm of a total Hamiltonian containing local terms.

### 6.2 A fixed sum of contact strengths removes the parametric advantage

Under $`\sum_j\|h_{jc}(t)\|\le\Lambda_1`$ per cut, let $`h`$ be the entire crossing interaction, including any one-sided pieces. Its norm is at most $`\Lambda_1`$. The conditional entropy rate is at most $`c_0\Lambda_1`$, on every state and with arbitrary references. An exact or fixed sufficiently accurate payload exchange still requires cut entropy of order $`n`$, giving $`\Omega(n/\Lambda_1)`$.

Sequential direct SWAPs at strength $`\Lambda_1`$, with $`2n+1`$ contacts and the free final internal permutation, give $`O(n/\Lambda_1)`$ independently of helper preparation. Therefore

```math
\boxed{T^{(1)}=\Theta_\epsilon(n/\Lambda_1)}\tag{9}
```

for clean, unknown, and independent mixed helpers in the corresponding exact/fixed-error tasks. This is an optimum over permitted allocations, not merely a uniform-rescaling example. Under this budget there is no parametrically growing initialization speedup. A norm bound on the total crossing interaction itself gives the same conclusion; a bound on the full Hamiltonian would additionally conflict with the free-internal-control convention.

Equations (8)-(9) identify precisely which bandwidth enhancement follows from which normalization. They must not be substituted for the per-contact theorem without stating the changed resources.

## 7. Scientific interpretation and use

The matched law says that, for the specified independent preparations, the entropy deficit can be reversibly concentrated into a larger useful interface coupling while preserving all unknown data. The entropy-flow converse fixes the optimum scaling. The correlated-helper counterexample prevents treating entropy as a complete invariant for arbitrary resource states. The finite certificates distinguish a universal comparator exclusion from an illustrative protocol ratio.

The mathematical package consists of the [main fixed-error law](mixed-helpers.md), [exact endpoints and conserved-budget proof](bandwidth.md), [conditional and weighted entropy flow](entropy-flow.md), the finite guarantees here, and the [bounded-strength compiler analysis](control-models.md). The [theorem map](theorem-map.md) specifies their logical dependencies and the [related-work guide](related-work.md) specifies attribution. This is a closed set of claims for the stated theoretical model, not a claim that every extension or implementation problem has been solved.
