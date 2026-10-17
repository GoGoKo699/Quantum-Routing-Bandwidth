# Control models and coherent implementations

The matching bandwidth laws charge only contact time. This note distinguishes that idealization from a specified finite-strength compiler and from the length of the classical control list. The target includes restoration of arbitrary spectator information and the bus; internal gates never act on inaccessible references.

## 1. Two distinct clocks

In the interaction-time model, unitaries inside $`L`$, $`R`$, or $`C`$ are instantaneous. In the finite-control compiler, all one- and two-qubit gates within a module, and bus-only gates, have generator norm at most $`G`$. Disjoint gates may run in parallel; every internal pair is available. There is no native Toffoli, extra initialized workspace, or cross-module control. Define $`\delta=\pi/(2G)`$. Contacts are off during local gates in this explicit schedule.

An exact exchange uses $`2n+1`$ bus SWAPs: for each $`j`$, swap $`L_j`$ with $`C`$ and then $`R_j`$ with $`C`$; finally swap $`L_1`$ with $`C`$. The left payload then has labels $`(R_n,R_1,\ldots,R_{n-1})`$. Shift them left by one. The cycle is two involutions on positions modulo $`n`$, $`x\mapsto-x`$ then $`x\mapsto-x-1`$, each implementable by disjoint SWAPs. The bus returns to its input state.

The norm-$`J`$ Hamiltonian $`J\mathrm{SWAP}`$ implements a bus SWAP in $`\pi/(2J)`$ up to global phase. The final internal permutation costs at most $`2\delta`$, so a feasible sequential comparator is

```math
T_{\mathrm{seq}}=\frac{(2n+1)\pi}{2J}+\frac\pi G\qquad(n\gt 1).\qquad\text{(1)}
```

The final permutation is unnecessary at $`n=1`$. Comparing only with an unamplified three-Ising SWAP would give the amplified compiler an artificially weak comparator.

## 2. Exact finite-duration compiler

### 2.1 Shorter three-data-qubit cycle

For q,a,b, the encoding E is Toffoli(a,b -> q), followed by CX(q,a) and CX(q,b). In the decoded frame, $`E^\dagger(Z_q+Z_a+Z_b)E=Z_q\mathrm{diag}(3,1,1,1)`$.

Instead of repeating encode/evolve/decode four times, encode once, visit the spectator translations in Gray-code order 00,01,11,10, and decode once at the end. The physical transitions are $`EX_bE^\dagger`$ and $`EX_aE^\dagger`$. They are Clifford affine permutations, although E itself is not Clifford.

For shift 01, a chronological circuit is

CX(q,a), CX(a,q), CX(a,b), CX(q,a) in parallel with $`X_b`$.

For shift 10, it is

CX(q,b), CX(b,q), CX(b,a), CX(q,b) in parallel with $`X_a`$.

Each transition therefore takes $`4\delta`$. There are three transitions. After $`E^\dagger`$ at the end, an $`X_a`$ restores the last Gray-code frame.

### 2.2 No native Toffoli or initialized ancilla

Let $`V^2=X`$, with eigenvalues 1 and i. A standard exact five-two-qubit construction of Toffoli is

CV(b,q), CX(a,b), $`\mathrm{CV}^\dagger(b,q)`$, CX(a,b), CV(a,q).

Its net exponent of V on q is $`b-(a\oplus b)+a=2ab`$. It is exact on arbitrary superpositions.

CX and X are Hermitian involutions and can be implemented, up to a common global phase, in $`\delta=\pi/(2G)`$ with norm-G generators. Controlled V has spectral phases 0 and $`\pi/2`$ and can be implemented in $`\delta/2`$ with norm G after a scalar shift. Thus this Toffoli takes $`(7/2)\delta`$ and E takes $`(11/2)\delta`$. The full cycle takes

```math
2\cdot\frac{11}{2}\delta+3\cdot4\delta+\delta=24\delta
```

of internal-control time, plus its charged contact time. This is an explicit feasible cost, not the minimum synthesis time for this three-qubit operation. Further gate fusion could reduce constants without changing the recurrence below.

### 2.3 Recursive compilation and costs

For $`m=3^k`$ data qubits assisting a designated target, the gain is $`a_k=(3/2)^k`$. Let $`D_k\delta`$ be the internal-control time for one amplified Ising operation. Disjoint triples are processed in parallel. Substitution of four lower-level simulations gives

```math
D_0=0,\qquad D_k=4D_{k-1}+24,
\qquad D_k=8(4^k-1).
\qquad\text{(2)}
```

There are $`4^k`$ raw contact intervals. The total number of elementary local gates (not depth) is

```math
N_k=30(12^k-1)/11.
```

For a target-bus SWAP, three Ising operations and four layers of single-qubit basis changes suffice. These layers rotate q and C in parallel. Its total duration in this schedule is

```math
t_k=\frac{3\pi}{4J(3/2)^k}+
\bigl[24\,4^k-20\bigr]\frac\pi{2G},\qquad k\ge1.
\qquad\text{(3)}
```

With $`m\le n`$, a suitable set of m data qubits can assist each target in turn; they are restored after each completed operation. All within-register pair connectivity has been granted, so no extra movement to arrange triples is silently required. The full route takes

```math
\boxed{T_k=(2n+1)t_k+\pi/G\quad(n\gt 1).}
\qquad\text{(4)}
```

The sequential option (1) is always included in optimization. The construction still preserves all unknown data, cross-register correlations, and an arbitrary bus state. Controls are fixed in advance, not selected from unknown input amplitudes.

### 2.4 Finite-control consequence

Set $`R=G/J`$. Relative to the direct norm-J target-bus SWAP, Equation (3) becomes

```math
\boxed{s_k(R)=(3/2)^{1-k}+\frac{24\,4^k-20}{R}.}
\qquad\text{(5)}
```

The $`k=1`$ primitive has $`s_1=1+76/R`$. It never beats the stronger direct-SWAP comparator under this compiler, even though its Ising coupling gain is 3/2.

The $`k=2`$ block has $`s_2=2/3+364/R`$, which beats that comparator only for $`R\gt1092`$. This is a threshold for this feasible compiler, not a physical threshold or impossibility theorem for smaller R.

Illustrative formula values, assuming the listed block fits inside n, are:

| G/J | Best block within this compiled family | Per-bus-SWAP duration / direct SWAP duration |
|---:|---:|---:|
| 100 | 1 (no amplification) | 1 |
| 1,000 | 1 (no amplification) | 1 |
| 10,000 | 27 | 0.596044 |
| 100,000 | 81 | 0.357536 |
| 1,000,000 | 243 | 0.222087 |

These are ideal analytical timings, not experimental estimates or noisy fidelities. The required ratios are substantial, and this compiler is conservative.

For neighboring positive recursion levels, $`s_k=s_{k+1}`$ at $`R=144\cdot6^k`$. Thus once the preferred block fits, the optimal k depends on R, not on n. At fixed R,

```math
\boxed{\min\{T_{\rm seq},T_1,T_2,\ldots\}=\Theta(n/J)}
```

within this explicitly compiled family.

When R itself grows, balancing the two terms gives $`6^k`$ of order R and

```math
T_{\rm compiled}=O\left(\frac nJ R^{-\nu}\right),
\qquad \nu=\frac{\ln(3/2)}{\ln6}=0.2262943855\ldots,
```

in the regime where the optimal block is available. To use the whole $`m=n=3^k`$ recursive register and retain the $`O(n^{\log_3 2}/J)`$ contact-time scaling, this compiler needs

```math
G/J\ \text{of order at least}\ n^{\log_3 6}
=n^{1.6309297536\ldots}
```

up to constants. This is precisely the size-dependent control resource that the free-control statement omits.

### 2.5 A qualified finite-R separation from every time-division protocol

Finite duration does not erase every advantage. Combining the constructive timings with the [time-division converse](entropy-flow.md#5-no-helper-converse-and-sequential-comparator) gives a rigorous comparison against the whole time-division class, not merely one sequential schedule, when R is sufficiently large.

For example, at $`n=59049`$ and $`R=10^7`$, the best block in the compiled family is $`m=2187`$. Equations (3)-(4) give $`JT=23580.3126`$, whereas every time-division protocol satisfies $`JT\ge40929.6479`$. No matrix of that size was simulated: these numbers are evaluations of the proved formulas. The huge control ratio, gate count, and ideal error-free assumptions make this a mathematical existence example, not a device proposal. It is a constant-factor comparison at fixed R, not asymptotic sublinear runtime.


## 3. Polynomial contact count at fixed uniform accuracy

For the no-helper construction, the exponentially long exact list is not necessary for approximate routing in the same ideal internal-control model. This is a concentration argument about selecting a coherent control list, not a channel obtained by physically randomizing the input.

Select K independent, uniform spectator translations $`s_1,\ldots,s_K`$ OFFLINE, then fix that list for every run. The implemented diagonal coefficient is

```math
\bar D_K(r)=K^{-1}\sum_{\ell=1}^K D_n(r\oplus s_\ell).
```

Every summand lies in [0,n] and has mean $`\mu_n`$. Hoeffding's inequality followed by a union bound over the $`2^{n-1}`$ spectator labels gives

```math
\Pr\left(\|\bar D_K-\mu_nI\|\gt a\right)
\le2\,2^{n-1}\exp(-2Ka^2/n^2).
\qquad\text{(6)}
```

All interval Hamiltonians commute exactly. An intended Ising angle $`\theta=\pi/4`$ therefore has full operator error at most $`\theta a/\mu_n`$. The entire route uses $`M=3(2n+1)`$ such gates. Reusing a good list under target relabelings and basis conjugations, telescoping the product of unitaries bounds the final operator error by $`M\theta a/\mu_n`$, uniformly over all data and bus states.

To obtain operator error at most $`\eta`$ with offline-list failure probability at most p, it suffices to choose

```math
K\ge \frac{n^2M^2\theta^2}{2\eta^2\mu_n^2}
\left[(n-1)\ln2+\ln(2/p)\right].
\qquad\text{(7)}
```

For fixed p and $`\eta`$, $`K=O(n^4/\eta^2)`$ per Ising gate and the total contact count is $`O(n^5/\eta^2)`$. The charged contact duration is unchanged. A full-unitary operator error $`\eta`$ implies channel diamond distance at most 2 $`\eta`$.

This gives both a probabilistic existence statement and a polynomial-time procedure for drawing a list with a rigorous high-probability uniform guarantee. It does not give an efficient verification of a large sampled list, a deterministic derandomization, an elementary-gate compilation of the global encoding E, or a practical sequence. The conservative constants are large; for small n the exact list is much shorter. A good list is fixed before the unknown input arrives and the physical execution is coherent: there is no measurement, postselection, or random mixing of quantum outputs.


## 4. Exact recursive interaction-time construction

On three data qubits, one Toffoli and two CNOTs encode the sign of $`Z_q+Z_a+Z_b`$ into $`q`$, giving $`Z_q\mathrm{diag}(3,1,1,1)`$. Four coherent spectator translations yield exactly $`(3/2)Z_q`$. On $`n=3^k`$ occupied qubits, apply this identity to disjoint triples, then triples of representatives. Each completed simulation restores every unused data subsystem, so the identity can be recursively substituted without an assumption about intermediate states.

The target-bus gain is $`(3/2)^k`$ with $`4^k`$ contact intervals per Ising gate. The buffered route therefore takes $`3\pi(2n+1)/[4J(3/2)^k]=O(n^{\log_3 2}/J)`$. This is an exact polynomial-control-list construction with free internal X, CNOT, and Toffoli gates. Its finite-strength decomposition is in Section 2, not an implied runtime benefit.

## 5. Optimal gain within a specified averaging class

For the fixed collective contact $`H=JZ_C\sum_{j=1}^nZ_j`$, the normalized trace norm is $`\|H\|_{1,\mathrm{norm}}=J\mu_n`$. It is invariant under local conjugation and convex. A convex average equal to $`gZ_qZ_C\otimes I`$ must therefore have $`|g|\le J\mu_n`$. The exact sign-encoding construction attains this value. This is optimal amplification within convex Hamiltonian averaging of that fixed contact, not an optimal finite-gate synthesis theorem for arbitrary time-dependent contacts. Hamiltonian simulation by local conjugations and majorization is established prior work [VC02](../references/RELATED_WORK.md#vc02).
