# Related work and attribution

The contribution is a matched full-register bandwidth characterization, including fixed-error independent mixed helpers, under a specified internal-control model. Existing results already connect initialization, collective interactions, and transfer speed. The source comparisons delimit the claim rather than certify the absence of all prior work. The [theorem map](theorem-map.md) identifies how these ingredients enter the central proof.

## D26

D. Devulapalli, C. Yin, A. Y. Guo, E. Schoute, A. M. Childs, A. V. Gorshkov, and A. Lucas, **Quantum Routing and Entanglement Dynamics Through Bottlenecks**, *PRX Quantum* **7**, 010310 (2026). [Publisher](https://doi.org/10.1103/7b1x-hjcy) · [arXiv:2505.16948](https://arxiv.org/abs/2505.16948).

This is the nearest bottleneck-routing predecessor. In the final published paper, Section V, Theorem 5, Equation (48), printed page 010310-13, bounds average entanglement with minimum segment width and a small exponent loss. Section VI discusses restrictions on time dependence and internal terms. Its matching square-root construction concerns free particles. Here a direct conditional-rate argument permits arbitrary well-defined switching and internal control for pairwise qubit contacts. The matching qubit construction uses filled, internally controllable modules, not a bare star with unavailable leaf-to-leaf controls.

## UHMG26

T. Upadhyaya, Y. Hong, T. C. Mooney, and A. V. Gorshkov, **Robustness-Runtime Tradeoff for Quantum State Transfer**, [arXiv:2602.22312v1](https://arxiv.org/abs/2602.22312v1), DOI [10.1103/15lg-dl56](https://doi.org/10.1103/15lg-dl56).

In the arXiv manuscript, Theorem 1 on page 3 relates exact robust-subspace transfer to commutator Schatten norms without imposing locality. Page 2, Equations (3)–(5) and the adjacent text, explicitly includes multiple transferred qubits. The power-law applications give an initialization-sensitive time dependence; the paper also provides robust transfer constructions. The Outlook on page 5 notes the exact full-rank thermal-state obstruction and raises approximate thermal-ancilla transfer.

Neither initialization-assisted communication, compression before transfer, nor the full-rank obstruction is a first-result claim here. The stated theorem does not itself supply the extensive throughput and fixed-preparation half diamond law of [Mixed helpers](mixed-helpers.md). The additional steps are a payload-sized cut requirement, a conserved entropy-budget rate bound, and a matching returned-helper construction on two bounded interfaces. This is a comparison to the identified statements, not a claim that no alternative derivation from existing tools is possible.

## DF19

F. Dupuis and O. Fawzi, **Entropy accumulation with improved second-order term**, *IEEE Transactions on Information Theory* **65**(11), 7596–7612 (2019). [DOI](https://doi.org/10.1109/TIT.2019.2929564) · [arXiv:1805.11652v2](https://arxiv.org/abs/1805.11652v2).

Corollary III.5 on page 6 of the arXiv manuscript bounds conditional entropy variance. Relabeling its small subsystem as the bus gives $V(C|A)\le\log_2^2(2d_C^2+1)$, independent of the conditioning register/reference dimension. This published ingredient suffices for the bandwidth exponents. The elementary second-moment derivation in [Entropy flow](entropy-flow.md) provides a different qubit constant, not a claim to invent conditional-variance bounds or improve their general-dimensional dependence.

## GP22

L. P. Garcia-Pintos, S. B. Nicholson, J. R. Green, A. del Campo, and A. V. Gorshkov, **Unifying Quantum and Classical Speed Limits on Observables**, *Physical Review X* **12**, 011038 (2022). [DOI](https://doi.org/10.1103/PhysRevX.12.011038).

This work relates observable and entropy rates to fluctuations. The commutator/Cauchy–Schwarz mechanism and entropy-fluctuation speed limits are established. The conditional formulation here accommodates inaccessible references; routing-specific ingredients are the physical-state entropy budget, contact geometry, and matching construction.

## K25

D. Kim, Y. Kimura, H. Mackay, Y. Mitsuhashi, H. Nishikawa, C. Rubiliani, C. Shang, A. Ukai, and T. Kuwahara, **Spectral Small-Incremental-Entangling: Breaking Quasi-Polynomial Complexity Barriers in Long-Range Interacting Systems**, [arXiv:2509.12014](https://arxiv.org/abs/2509.12014), DOI [10.1103/8fcr-5tf4](https://doi.org/10.1103/8fcr-5tf4).

Its spectral-entangling strength controls Rényi-entropy growth uniformly over inputs. For $V=J(\sum_j Z_j)\otimes Z_C$, that strength is $nJ$, while the normalized Frobenius norm is $J\sqrt n$. The spectral theorem gives an input-uniform collective benchmark in this example, rather than the full-data or common-ensemble bound here. Neither theorem is asserted to subsume the other's distinct entropy and input guarantees.

## B23

A. Bapat, A. M. Childs, A. V. Gorshkov, and E. Schoute, **Advantages and limitations of quantum routing**, *PRX Quantum* **4**, 010313 (2023). [DOI](https://doi.org/10.1103/PRXQuantum.4.010313) · [arXiv:2206.01766](https://arxiv.org/abs/2206.01766).

Hamiltonian routing, initialized storage ancillas, and fast internal operations are established resources. Placing the bus within a freely controlled block changes the cost of one interface. Here there are three regions, both interfaces are bounded, and the helper count and input-state promise are explicit. Conversely, this construction relies on internal module controls and is not a bare-star algorithm.

## VC02

G. Vidal and J. I. Cirac, **Optimal simulation of nonlocal Hamiltonians using local operations and classical communication**, *Physical Review A* **66**, 022315 (2002). [DOI](https://doi.org/10.1103/PhysRevA.66.022315) · [arXiv:quant-ph/0108076](https://arxiv.org/abs/quant-ph/0108076).

Local-unitary Hamiltonian simulation, majorization, and local ancillary resources are established. The normalized-trace-norm argument in [Control models](control-models.md) proves optimal gain only inside the specified convex-averaging class, not general optimal control of the full router.

## K07

P. Kaye, **Cooling algorithms based on the 3-bit majority**, [arXiv:quant-ph/0703194](https://arxiv.org/abs/quant-ph/0703194) (2007).

Reversible three-bit majority compression and recursive small compression gates predate this construction. Their role here is coherent concentration of a Hamiltonian contact while restoring arbitrary spectator information, rather than polarization cooling. CNOT fanout creates reversible correlations, not copies of an unknown state.

## SV98

L. J. Schulman and U. Vazirani, **Scalable NMR Quantum Computation**, [arXiv:quant-ph/9804060v1](https://arxiv.org/abs/quant-ph/9804060v1) (1998).

Section 2, especially Theorem 1 on page 6, develops reversible polarization concentration without initially available clean workspace. This is the foundational compression precedent for [Mixed helpers, Section 3](mixed-helpers.md#3-reversible-concentration-at-finite-error). The concentration mechanism is not new here. The routing proof uses a spectral permutation, retains all entropy-bearing qubits as occupied spectators, and bounds the complete compression–route–decompression isometry. It does not import an efficient implementation claim for its own global encoding from this predecessor.

## Claim boundaries

The main [fixed-error law](mixed-helpers.md) concerns independent known product helper states; the [exact laws](bandwidth.md) concern pure-helper and arbitrary-unknown-helper tasks. The entropy-budget converse alone does not establish arbitrary-state saturation. The correlated-helper example shows why that extension is false. Exact marginal return is distinct from exact restoration of all correlations in the mixed case.

[Finite-control statements](control-models.md) concern the displayed compiler. The law is not a hardware noise-tolerance or bounded-speed advantage claim. The theorem comparison and finite numerical checks do not establish priority, independent endorsement, or editorial judgment.
