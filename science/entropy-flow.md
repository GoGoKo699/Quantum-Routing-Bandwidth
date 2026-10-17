# Entropy flow through small interfaces

## 1. Published conditional-variance bound

Let rho_AB be an arbitrary finite-dimensional state. A may include arbitrarily many inaccessible reference systems. Let h act on AB, and let B have dimension d_B. Other Hamiltonian terms confined to A or to its complement do not contribute to dot S_A. Initially assume full rank; singular states are treated below.

The contact contribution can be written

```math
\dot S_A=i\mathrm{Tr}\rho[h,\log_2\rho_A\otimes I_B],
```

up to the irrelevant sign convention for the commutator. Since rho commutes with log rho, the same magnitude is obtained with the conditional modular difference K. Center both K and h, and apply Cauchy-Schwarz to the state-weighted inner product:

```math
|\dot S_A|
\le 2\sqrt{V(B|A)_\rho}\,\Delta_\rho h.
```

Using [DF19](../references/RELATED_WORK.md#df19), Corollary III.5, yields

```math
\boxed{|\dot S_A|\le
2\log_2(2d_B^2+1)\,\Delta_\rho h
\le 2\log_2(2d_B^2+1)\sqrt{\mathrm{Tr}\rho h^2}.}
\qquad\text{(1)}
```

For a bus qubit, the coefficient is c_DF=2 log_2 9. This combines the cited conditional-variance inequality with a state-weighted commutator estimate.

## 2. Elementary qubit constant

Use natural logarithms in this paragraph. Set sigma=rho_A tensor I_B and K=ln rho-ln sigma. Let r_i and s_j denote eigenvalues of rho and sigma, and use the spectral-overlap distribution

```math
p_{ij}=r_i|\langle i|j\rangle|^2,
\qquad X_{ij}=\ln r_i-\ln s_j,
```

including only r_i>0 and s_j>0. Then E X^2=Tr rho K^2; this identity is valid even when the logarithms do not commute. The operator inequality rho<=d_B sigma follows, for example, by pinching in a basis of B and bounding each positive diagonal block by rho_A. Let B_0=sigma^{-1/2}rho sigma^{-1/2} on the support of sigma. Then

```math
\mathbb E e^X=\mathrm{Tr}\rho^2\sigma^{-1}
=\mathrm{Tr}\sigma B_0^2\le d_B,
```

and

```math
\mathbb E e^{-X}=\mathrm{Tr}\Pi_\rho\sigma\le d_B.
```

The scalar inequality x^2<=e^x+e^{-x}-2 gives

```math
\mathrm{Tr}\rho K^2\le2(d_B-1).
```

Centering can only decrease this second moment. Therefore for a bus qubit,

```math
\boxed{|\dot S_A|\le c_0\sqrt{\mathrm{Tr}\rho h^2},
\qquad c_0=\frac{2\sqrt2}{\ln2}.}
\qquad\text{(2)}
```

This is a sharper qubit coefficient than (1), but does not change the exponent. The d_B dependence of this elementary bound is worse for large d_B than the published logarithmic estimate, so it is not an improved general-dimensional SIE theorem.

## 3. Supports and admissible controls

When rho is singular, one must not project log sigma onto supp rho before squaring. Off-support components of log sigma acting on supp rho contribute to Tr rho K^2. One may assign finite values to log rho on its kernel, compute the rho-weighted moments on the support of sigma, and take a regularized limit. The rank-deficient verification cases use this convention.

For an integrated entropy inequality, regularize the entire finite physical/reference state by a small maximally mixed component, evolve it with the same unitary, prove the differential statement, integrate, and let the regularization vanish by entropy continuity. This avoids assuming differentiability at every rank-changing endpoint.

Internal pulses do not change S_A. General bounded-contact controls follow by their well-defined propagators and continuity; no Trotter step count enters the rate proof. Unbounded internal Hamiltonians are not included in the contact second moment because their entropy contribution across the chosen cut is identically zero.

## 4. Weighted average-input entropy-flow theorem

Let L be any set of physical qubits, R the other data region, and C a set of bus qubits. There is no direct L-R coupling. For each c in C, write the genuinely interacting part of all L-c edges as

```math
H_{Lc}^{\rm int}(t)
=\sum_{j\in L}\sum_{a,b=x,y,z}
\gamma_{jcab}(t)\sigma_j^a\sigma_c^b.
```

Terms acting on only one side are absorbed into internal controls. If the original edge h_jc has operator norm at most J_jc(t), orthogonal projection onto its two-sided Pauli terms contracts its normalized Frobenius norm. Distinct j,c,a,b strings are orthogonal, so

```math
\|H_{Lc}^{\rm int}(t)\|_F^2
\le\sum_{j\in L}J_{jc}(t)^2.
\qquad\text{(3)}
```

This step does NOT claim that removal of local terms contracts the operator norm.

Consider a pure-state ensemble with

```math
\mathbb E_\psi |\psi\rangle\langle\psi|=I/D.
```

Every input is acted on by the SAME input-independent controlled unitary. Its ensemble average remains I/D at all times, despite any correlations developed in individual members. Applying (2) separately to each c, averaging absolute values, and using Jensen gives

```math
\begin{aligned}
\mathbb E_\psi|\dot S_L(\psi_t)|
&\le c_0\sum_{c\in C}
\mathbb E_\psi\sqrt{\langle (H_{Lc}^{\rm int})^2\rangle_{\psi_t}}\\
&\le c_0\sum_{c\in C}\|H_{Lc}^{\rm int}(t)\|_F\\
&\le c_0\sum_{c\in C}\sqrt{\sum_{j\in L}J_{jc}(t)^2}.
\end{aligned}
\qquad\text{(4)}
```

The same theorem follows using published bound (1) with c_0 replaced by c_DF. Integrating proves

```math
\boxed{\mathbb E_\psi|S_L(\psi_T)-S_L(\psi_0)|
\le c_0\int_0^T\sum_{c\in C}
\sqrt{\sum_{j\in L}J_{jc}(t)^2}\,dt.}
\qquad\text{(5)}
```

For uniform contacts, this is at most c_0 J |C| sqrt(|L|) T. There is no additive constant, factor n^delta, minimum segment length, or derivative condition. Compare the restricted-time-dependence average-input bound of [D26](../references/RELATED_WORK.md#d26).

This is not an input-uniform O(sqrt n) rate bound. For example, a GHZ logical qubit in the leaves under Z_C sum_j Z_j can have instantaneous entropy rate proportional to nJ. The proof neither assumes nor implies S(average rho)=average S(rho). It uses the linearity of the second moment and concavity of the square root. It also fails if the control schedule is selected using the unknown input's classical label: then the average evolved state need not stay maximally mixed.

Additional known-initialized workspace is not free under this theorem. More generally, if an average physical state is bounded by kappa I/D, the same proof acquires sqrt(kappa). Unitary dynamics preserve that spectral domination. The entropy-deficit refinement and its matching workspace law are proved in [Initialization and routing bandwidth](bandwidth.md).


## 5. No-helper converse and sequential comparator

For $`n`$ unknown qubits in each module, test the channel on local Bell pairs with inaccessible references. With a chosen pure bus, the accessible physical state satisfies $`\omega(t)\preceq2I/D`$ at every time. Pauli orthogonality gives $`\|H_{LC}^{\mathrm{int}}\|_F^2\le nJ^2`$. Equations (2)-(3) imply a cut entropy rate at most $`4J\sqrt n/\ln2`$. An exact exchange raises the reference-assisted cut entropy from zero to $`2n`$ bits, hence

```math
T\ge\frac{\ln2}{2J}\sqrt n.
```

The published-variance constant alone gives $`T\ge\sqrt n/(\sqrt2\log_2 9\,J)`$, with the same scaling. If the required operation restores an arbitrary bus, purify a maximally mixed bus on the opposite side of the cut. The physical test is then exactly $`I/D`$, improving the first coefficient to $`\ln2/\sqrt2`$. This stronger coefficient belongs to the stronger task; the construction meets that task too.

For normalized payload Choi fidelity $`F_e\ge1-\epsilon`$, the pure global output is within trace distance $`\sqrt\epsilon`$ of the ideal payload Choi vector times a pure environment vector. Entropy continuity yields

```math
T\ge\frac{\ln2}{4J\sqrt n}
\left[2n(1-\sqrt\epsilon)-h_2(\sqrt\epsilon)\right].
```

This preserves the exponent at fixed sufficiently small error. It is a process-fidelity bound, not an identification of process fidelity with diamond distance.

For at most one active contact at a time, add the entropy changes of both register cuts. Their sum must grow by $`4n`$ bits, while its derivative is at most $`4J/\ln2`$. Consequently $`T_{\mathrm{division}}\ge n\ln2/J`$, even with free internal controls. See [Control models](control-models.md) for an explicit sequential schedule and the finite-speed comparison.
