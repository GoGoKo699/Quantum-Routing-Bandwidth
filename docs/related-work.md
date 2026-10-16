# Related work and attribution

The contribution studied here is a matched full-register bandwidth characterization under a specified control model, with a same-hardware comparison between initialized and unknown helpers. Existing results already connect initialization, collective interactions, and transfer speed. The source comparisons below delimit the claim; they are not an exhaustive absence-of-prior-art certificate.

## D26

D. Devulapalli, C. Yin, A. Y. Guo, E. Schoute, A. M. Childs, A. V. Gorshkov, and A. Lucas, **Quantum Routing and Entanglement Dynamics Through Bottlenecks**, *PRX Quantum* **7**, 010310 (2026). [Publisher](https://doi.org/10.1103/7b1x-hjcy) · [arXiv:2505.16948](https://arxiv.org/abs/2505.16948).

This is the nearest bottleneck-routing predecessor. Its final Theorem 5 bounds average entanglement under a minimum switching-segment width and a small exponent loss; its discussion identifies unrestricted time dependence and internal terms as extensions. Its matching square-root construction concerns free particles. Here the direct conditional-rate argument permits arbitrary well-defined switching and internal control for pairwise qubit contacts. The matching construction is for filled, internally controllable qubit modules, not a bare star with inaccessible leaf-to-leaf controls.

## UHMG26

T. Upadhyaya, Y. Hong, T. C. Mooney, and A. V. Gorshkov, **Robustness-Runtime Tradeoff for Quantum State Transfer**, [arXiv:2602.22312](https://arxiv.org/abs/2602.22312), DOI [10.1103/15lg-dl56](https://doi.org/10.1103/15lg-dl56). The publisher acceptance record is dated 16 September 2026.

This work relates ancillary-state robustness to Schatten-norm commutator growth and derives initialization-sensitive transfer bounds for power-law interactions, including a square-root initialization dependence. Its framework encompasses multiple transferred qubits. Neither initialization-assisted communication nor a square-root initialization tradeoff is a first-result claim here. The distinct task is extensive payload exchange through one bounded qubit interface, with matched optimal times and an unknown-helper comparator on identical hardware. Architectural differences alone do not establish scientific significance.

## DF19

F. Dupuis and O. Fawzi, **Entropy accumulation with improved second-order term**, *IEEE Transactions on Information Theory* **65**(11), 7596–7612 (2019). [DOI](https://doi.org/10.1109/TIT.2019.2929564) · [arXiv:1805.11652](https://arxiv.org/abs/1805.11652).

Corollary III.5 bounds conditional entropy variance by $\log_2^2(2d_B^2+1)$, independent of the conditioning subsystem's dimension. This published ingredient suffices for the bandwidth exponents. The elementary second-moment derivation in [Entropy flow](entropy-flow.md) provides a different qubit constant, not a claim to have invented conditional-variance bounds or improved their general-dimensional dependence.

## GP22

L. P. Garcia-Pintos, S. B. Nicholson, J. R. Green, A. del Campo, and A. V. Gorshkov, **Unifying Quantum and Classical Speed Limits on Observables**, *Physical Review X* **12**, 011038 (2022). [DOI](https://doi.org/10.1103/PhysRevX.12.011038).

This work relates observable and entropy rates to fluctuations. The commutator/Cauchy–Schwarz mechanism and the use of entropy fluctuations in a speed limit are established. The conditional formulation used here accommodates inaccessible references; the routing-specific ingredients are the physical-state entropy budget, contact geometry, and matching construction.

## K25

D. Kim, Y. Kimura, H. Mackay, Y. Mitsuhashi, H. Nishikawa, C. Rubiliani, C. Shang, A. Ukai, and T. Kuwahara, **Spectral Small-Incremental-Entangling: Breaking Quasi-Polynomial Complexity Barriers in Long-Range Interacting Systems**, [arXiv:2509.12014](https://arxiv.org/abs/2509.12014), DOI [10.1103/8fcr-5tf4](https://doi.org/10.1103/8fcr-5tf4).

Its spectral-entangling strength controls Rényi-entropy growth uniformly over inputs. For $V=J(\sum_j Z_j)\otimes Z_C$, that strength is $nJ$, while the normalized Frobenius norm is $J\sqrt n$. Thus the stated spectral theorem gives an input-uniform collective benchmark in this example, rather than the full-data or common-ensemble bound here. Neither theorem is asserted to subsume the other's distinct entropy and input guarantees.

## B23

A. Bapat, A. M. Childs, A. V. Gorshkov, and E. Schoute, **Advantages and limitations of quantum routing**, *PRX Quantum* **4**, 010313 (2023). [DOI](https://doi.org/10.1103/PRXQuantum.4.010313) · [arXiv:2206.01766](https://arxiv.org/abs/2206.01766).

Hamiltonian routing, initialized storage ancillas, and fast internal operations are established resources. In fast-partition comparisons, placing the bus within a freely controlled block changes the cost of one interface. Here there are three regions, both interfaces are bounded, and the helper count and input-state promise are explicit. Conversely, this repository's construction relies on internal module controls and is not a bare-star routing algorithm.

## VC02

G. Vidal and J. I. Cirac, **Optimal simulation of nonlocal Hamiltonians using local operations and classical communication**, *Physical Review A* **66**, 022315 (2002). [DOI](https://doi.org/10.1103/PhysRevA.66.022315) · [arXiv:quant-ph/0108076](https://arxiv.org/abs/quant-ph/0108076).

Local-unitary Hamiltonian simulation, majorization, and the role of local ancillary systems are established. The normalized-trace-norm argument in [Control models](control-models.md) proves optimal gain only inside the specified convex-averaging class. It is not an invocation of a general optimal-control theorem for the full router.

## K07

P. Kaye, **Cooling algorithms based on the 3-bit majority**, [arXiv:quant-ph/0703194](https://arxiv.org/abs/quant-ph/0703194) (2007).

Reversible three-bit majority compression and recursive use of small compression gates predate this construction. Their role here is coherent concentration of a Hamiltonian contact while restoring arbitrary spectator information, rather than polarization cooling. Coherent CNOT fanout of the clean leaders creates reversible correlations, not copies of an unknown state.

## Claim boundaries

The [main theorem](bandwidth.md) concerns exact pure-helper initialization and ideal internal control. The entropy-deficit converse also applies to mixed physical states, but its existence alone does not establish matching achievability from a scalar entropy budget for arbitrary mixed helpers. [Finite-control statements](control-models.md) concern the displayed compiler. Numerical checks test the stated identities and inequalities and do not establish priority, independent proof endorsement, or a hardware implementation.
