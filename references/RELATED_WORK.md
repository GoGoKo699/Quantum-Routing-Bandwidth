# Related work and attribution

The contribution is a matched full-register bandwidth characterization, including fixed-error independent mixed helpers, under a specified internal-control model. Existing results already connect initialization, collective interactions, and transfer speed. The source comparisons delimit the claim rather than certify the absence of all prior work. The [theorem map](../science/theorem-map.md) identifies how these ingredients enter the central proof.

## D26

D. Devulapalli, C. Yin, A. Y. Guo, E. Schoute, A. M. Childs, A. V. Gorshkov, and A. Lucas, **Quantum Routing and Entanglement Dynamics Through Bottlenecks**, *PRX Quantum* **7**, 010310 (2026). [Publisher](https://doi.org/10.1103/7b1x-hjcy) · [arXiv:2505.16948](https://arxiv.org/abs/2505.16948).

In the final published paper, Section V, Theorem 5, Equation (48), printed page 010310-13, bounds average entanglement with a minimum segment width, an additive term, and a small exponent loss. Section VI discusses restrictions on time dependence and internal terms. The matching square-root construction concerns free particles. Our direct conditional-rate proof permits arbitrary well-defined switching and internal control for pairwise qubit contacts. Its matching qubit construction uses filled, internally controllable modules, not a bare star with unavailable leaf-to-leaf gates.

The final paper's own per-edge norm convention is explicit in Section II A. The different [normalizations analyzed here](../science/accuracy-and-resources.md#6-what-changes-under-a-different-interaction-budget) prevent a per-edge result from being read as a fixed-total-strength advantage.

## UHMG26

T. Upadhyaya, Y. Hong, T. C. Mooney, and A. V. Gorshkov, **Robustness-Runtime Tradeoff for Quantum State Transfer**, [arXiv:2602.22312v1](https://arxiv.org/abs/2602.22312v1), DOI [10.1103/15lg-dl56](https://doi.org/10.1103/15lg-dl56).

Theorem 1 on page 3 relates exact robust-subspace transfer to commutator Schatten norms without a locality assumption. Page 2, Equations (3)–(5), explicitly encompasses multiple transferred qubits. The paper gives power-law applications and robust constructions. Its page-5 Outlook states the exact full-rank thermal-state obstruction and raises approximate thermal-ancilla transfer.

Applying a separate necessary commutator condition to each payload qubit gives simultaneous conditions, not an additive transfer-time requirement. An extensive throughput conclusion needs an additional aggregate information-flow argument; the $2n$-bit reference-assisted entropy requirement supplies that step here. This is not a proof that no alternative derivation from existing tools is possible.

Neither initialization-assisted transfer, compression before transfer, nor the full-rank obstruction is a novelty claim. The distinct statement is the matched extensive fixed-error time on two bounded interfaces, with complete preparation-reference restoration accuracy and a same-hardware unknown-helper comparator. The [mixed-helper proof](../science/mixed-helpers.md) addresses this model, not all power-law thermal transfer. The source's theorem and Outlook were checked directly; no unpublished version or private correspondence is relied on.

## DF19

F. Dupuis and O. Fawzi, **Entropy accumulation with improved second-order term**, *IEEE Transactions on Information Theory* **65**(11), 7596–7612 (2019). [DOI](https://doi.org/10.1109/TIT.2019.2929564) · [arXiv:1805.11652v2](https://arxiv.org/abs/1805.11652v2).

Corollary III.5 on page 6 bounds conditional entropy variance. Relabeling its small subsystem as the bus gives $V(C|A)\le\log_2^2(2d_C^2+1)$ independent of register/reference dimension. This published ingredient suffices for the bandwidth exponents. Its equation and definitions were checked, including the rendered corollary. The [elementary qubit alternative](../science/entropy-flow.md#2-elementary-qubit-constant) improves a constant, not the general-dimensional variance theorem.

## GP22

L. P. García-Pintos, S. B. Nicholson, J. R. Green, A. del Campo, and A. V. Gorshkov, **Unifying Quantum and Classical Speed Limits on Observables**, *Physical Review X* **12**, 011038 (2022). [DOI](https://doi.org/10.1103/PhysRevX.12.011038).

Fluctuation-based observable and entropy speed limits predate this work. The conditional formulation here accommodates inaccessible references; the resource-specific steps are the physical-state entropy budget, contact geometry, and matching construction. The commutator/Cauchy–Schwarz mechanism is not presented as new.

## K25

D. Kim, Y. Kimura, H. Mackay, Y. Mitsuhashi, H. Nishikawa, C. Rubiliani, C. Shang, A. Ukai, and T. Kuwahara, **Spectral Small-Incremental-Entangling: Breaking Quasi-Polynomial Complexity Barriers in Long-Range Interacting Systems**, [arXiv:2509.12014v2](https://arxiv.org/abs/2509.12014v2), DOI [10.1103/8fcr-5tf4](https://doi.org/10.1103/8fcr-5tf4).

Its spectral-entangling strength controls Rényi-entropy growth uniformly over inputs. For $V=J(\sum_j Z_j)\otimes Z_C$, that strength is $nJ$, whereas the normalized Frobenius norm is $J\sqrt n$. Its input-uniform benchmark differs from a full-data or common-ensemble bound. Neither theorem is claimed to subsume the other's entropy and input guarantees.

## B23

A. Bapat, A. M. Childs, A. V. Gorshkov, and E. Schoute, **Advantages and limitations of quantum routing**, *PRX Quantum* **4**, 010313 (2023). [DOI](https://doi.org/10.1103/PRXQuantum.4.010313) · [arXiv:2206.01766](https://arxiv.org/abs/2206.01766).

Hamiltonian routing, initialized storage ancillas, and fast internal operations are established resources. Placing the bus within a freely controlled block changes the cost of one interface. Here there are three regions, both interfaces are bounded, and the helper input promise is explicit. Conversely, this construction requires internal module controls and is not a bare-star algorithm.

## VC02

G. Vidal and J. I. Cirac, **Optimal simulation of nonlocal Hamiltonians using local operations and classical communication**, *Physical Review A* **66**, 022315 (2002). [DOI](https://doi.org/10.1103/PhysRevA.66.022315) · [arXiv:quant-ph/0108076v2](https://arxiv.org/abs/quant-ph/0108076v2).

Local-unitary Hamiltonian simulation, majorization, and local ancilla resources are established. The [trace-norm argument](../science/control-models.md#5-optimal-gain-within-a-specified-averaging-class) proves optimal gain only inside a specified averaging class, not arbitrary optimal control of the router. Synchronized averaging exploits additive block structure; no new general averaging theorem is claimed.

## K07

P. Kaye, **Cooling algorithms based on the 3-bit majority**, [arXiv:quant-ph/0703194](https://arxiv.org/abs/quant-ph/0703194) (2007).

Reversible three-bit majority compression and recursive small compression gates predate this construction. Their role here is concentration of a Hamiltonian contact while restoring arbitrary spectator information, rather than polarization cooling. CNOT fanout creates reversible correlations, not copies of an unknown state.

## SV98

L. J. Schulman and U. Vazirani, **Scalable NMR Quantum Computation**, [arXiv:quant-ph/9804060v1](https://arxiv.org/abs/quant-ph/9804060v1) (1998).

Section 2 and Theorem 1 develop reversible polarization concentration without initially available clean workspace. This is the compression precedent for [Mixed helpers, Section 3](../science/mixed-helpers.md#3-reversible-concentration-at-finite-error). We retain entropy-bearing qubits as occupied spectators and control the complete compression–route–decompression isometry. An efficient implementation result for another compression method is not silently transferred to our global encoding.

## A07

K. M. R. Audenaert, **A sharp continuity estimate for the von Neumann entropy**, *Journal of Physics A: Mathematical and Theoretical* **40**(28), 8127–8136 (2007). [DOI](https://doi.org/10.1088/1751-8113/40/28/S18) · [arXiv:quant-ph/0610146](https://arxiv.org/abs/quant-ph/0610146), whose preprint title is *A Sharp Fannes-type Inequality for the von Neumann Entropy*.

The entropy bound $|S(\rho)-S(\sigma)|\le t\log_2(d-1)+h_2(t)$, with trace distance $t$, is used in the fixed-error converse. Applying it to payload-sized marginals and their joint state removes the helper-dimension penalty. That choice of subsystems, not the continuity inequality itself, is the routing-specific step.

## H63

W. Hoeffding, **Probability Inequalities for Sums of Bounded Random Variables**, *Journal of the American Statistical Association* **58**(301), 13–30 (1963). [DOI](https://doi.org/10.1080/01621459.1963.10500830).

The bounded independent-sum inequality is used twice for polarization concentration and with a union bound for coherent translation-list selection. The list is drawn offline and fixed before the input is supplied. No randomized mixture of physical output channels is substituted for the coherent protocol.

## W18

J. Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018). [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).

Chapters 2–3 supply the channel, purification, and completely bounded trace-norm formalism; Chapters 4–5 supply spectral and entropy background. The preparation-inclusive channels here have fixed inserted helper purifications and arbitrary payload/bus inputs. Isometry operator bounds are used as sufficient half diamond bounds, not identified with average process fidelity. The author's available manuscript is linked, not redistributed.

## Scope of the comparison

The primary records and theorem statements above support the stated attribution. Targeted searches for routing initialization, mixed/thermal ancilla transfer, and occupied-data Hamiltonian amplification did not identify an equivalent full package; search non-detection is not proof of novelty. Adjacent optical routing and repeater-channel capacity problems have different tasks and resource models and are not used as comparators.

The main matching law concerns identically distributed, independent known helper states. The entropy-budget converse alone does not prove arbitrary-state saturation; the correlated-helper example disproves it. Physical marginal return is distinct from exact restoration of all correlations. Finite-control claims concern the displayed compiler, and resource-normalization results concern their explicitly changed budgets. No outside proof endorsement or editorial conclusion is asserted by this record.
