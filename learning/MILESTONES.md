# Thirty milestones for understanding routing bandwidth

**Map identifier: QRB-W18-30-v1.** The map contains exactly **30 project-defined milestones: 14 background/preliminary targets and 16 narrative/innovation targets**. Its questions, dependencies, and understanding targets are common to every reader.

The background connects quantum states, references, channels, entropy, spectral tools, probability, and the physical control model. M14 assembles those objects into the complete operational comparison. The narrative then joins a local information-flow estimate and a coherent contact construction into matching bandwidth laws; M30 integrates the results, their meaning, and their boundaries. This allocation follows the routing problem, not a textbook table of contents or a reader's assessment history.

The single educational anchor is John Watrous's *The Theory of Quantum Information*. The [Watrous bridge](WATROUS_BRIDGE.md) supplies section pointers and notation translations; [worked examples](WORKED_EXAMPLES.md) connect them to the research. The [scientific account](../science/README.md) owns the exact statements and proofs.

Each milestone has a central question, understanding target, earlier dependencies, conceptual connection, source pointers, and story role. Together they support understanding of the full contribution; specialist details remain in the linked proofs.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M06 | Unknown data, inaccessible references, complete operations, and accuracy |
| Background/preliminaries | M07–M14 | Entropy, spectral resources, and dynamical controls assembled into the task |
| Narrative/innovation | M15–M19 | Interface entropy rate, contact geometry, and the extensive-payload converse |
| Narrative/innovation | M20–M24 | Spectator-preserving amplification and matching exact endpoints |
| Narrative/innovation | M25–M28 | Imperfect initialization, joint restoration, and the limits of entropy-only reasoning |
| Narrative/innovation | M29–M30 | Finite certificates, resource normalization, attribution, and the full physical story |

## Background and preliminaries

### M01. Registers carry unknown states

**Central question:** What must survive when the input state is unknown?

**Understanding target:** Distinguish preserving amplitudes and phases from transporting a known basis label. Identify payload, helper, and bus as different roles, not different kinds of qubit.

**Dependencies:** None.

**Conceptual connection:** A routing operation must preserve relative phases as well as populations. This is why the same hardware is tested on unknown quantum data rather than a known classical label.

**Sources:** Watrous §§2.1.1–2.1.2; [model](../science/bandwidth.md#1-result-model-and-comparison).

**Story role:** Begin with the object being moved, before an architecture or speed claim.

### M02. Composite systems and reductions

**Central question:** What does a local density matrix omit?

**Understanding target:** Use tensor products and partial trace to distinguish the accessible state from its correlations with other systems. Recognize that identical marginals need not mean identical joint states.

**Dependencies:** M01.

**Conceptual connection:** The partial trace forgets correlations. The reference-assisted routing test later distinguishes outputs that have identical local density operators but carry different quantum information.

**Sources:** Watrous §2.1.3; [reference example](WORKED_EXAMPLES.md#1-unchanged-marginals-can-conceal-complete-information-transfer).

**Story role:** Make the missing information in a local-state test visible.

### M03. Purifications and inaccessible references

**Central question:** Why test a router on half of an entangled pair?

**Understanding target:** Explain how a reference tests preservation of quantum information without supplying a physical operation or usable workspace. Distinguish physical mixedness from global purity.

**Dependencies:** M02.

**Conceptual connection:** Purification turns preservation of unknown information into preservation of entanglement. References supply a test of the operation without adding controllable qubits to the resource budget.

**Sources:** Watrous §2.1.3; [reference example](WORKED_EXAMPLES.md#1-unchanged-marginals-can-conceal-complete-information-transfer).

**Story role:** Turn preservation of correlations into part of the operational task.

### M04. Channels and their complete representations

**Central question:** How is a routing task specified for all inputs?

**Understanding target:** Relate a unitary to its channel and an inserted preparation to an isometry. Explain the normalized Choi test, including its input-dimension normalization.

**Dependencies:** M03.

**Conceptual connection:** A normalized Choi state describes one complete channel test; an inserted helper preparation instead fixes part of a larger isometry. Keeping these representations separate prevents the helper promise from becoming an arbitrary-input promise.

**Sources:** Watrous §§2.2.1–2.2.2; [notation](WATROUS_BRIDGE.md#notation-and-normalization).

**Story role:** Replace an example trajectory with a complete operation.

### M05. State distance and fidelity conventions

**Central question:** Which numerical notion of accuracy is being reported?

**Understanding target:** Distinguish trace distance, root fidelity, and squared pure-target overlap. Translate the convention in an equation before comparing its error with another statement.

**Dependencies:** M02, M04.

**Conceptual connection:** Watrous uses root fidelity, whereas the verification programs report squared pure-target overlaps. The square and the trace-distance factor matter when transporting an accuracy bound into the converse.

**Sources:** Watrous §3.1.1 and §3.2; [notation](WATROUS_BRIDGE.md#notation-and-normalization).

**Story role:** Prevent a convention change from masquerading as stronger accuracy.

### M06. Reference-aware channel accuracy

**Central question:** What changes when accuracy must include every input and reference?

**Understanding target:** Explain half diamond distance and identify the input and output systems of the fixed-preparation maps. Distinguish a fixed inserted helper purification from an arbitrary helper input.

**Dependencies:** M04, M05.

**Conceptual connection:** The diamond norm allows an inaccessible reference to accompany any payload input. The fixed helper purification makes joint restoration part of the output comparison without granting control of the preparation reference.

**Sources:** Watrous §§3.3.1–3.3.3; [error convention](../science/mixed-helpers.md#1-task-and-matching-law).

**Story role:** Specify the guarantee before evaluating a protocol.

### M07. Entropy and initialization

**Central question:** What resource does a biased helper provide?

**Understanding target:** Interpret binary and von Neumann entropy, the deficit from the maximally mixed state, and its conservation under physical unitaries. Do not identify entropy deficit with work or energy.

**Dependencies:** M02.

**Conceptual connection:** Internal unitaries can concentrate polarization locally but cannot change the physical state's total entropy deficit. That conservation law remains available even when the control sequence is unrestricted.

**Sources:** Watrous §§5.1.1–5.1.2 and §§5.2.1–5.2.2; [budget](../science/bandwidth.md#2-entropy-deficit-controls-contact-second-moments).

**Story role:** Introduce the resource that will differ between helper promises.

### M08. Relative entropy and constrained concentration

**Central question:** How can lack of entropy constrain spectral weight?

**Understanding target:** Recognize the entropy deficit as relative entropy to the maximally mixed state. Explain why comparing with a normalized exponential operator limits an expectation without assuming commuting states.

**Dependencies:** M07.

**Conceptual connection:** Relative entropy to a normalized exponential operator bounds a state-weighted second moment. This variational step connects preparation quality to usable interaction strength without requiring simultaneous diagonalization.

**Sources:** Watrous §§5.2.1–5.2.3; [variational step](../science/bandwidth.md#23-gibbs-variational-estimate-at-a-fixed-entropy-deficit).

**Story role:** Connect a conserved scalar to the possible weight on large eigenvalues.

### M09. Mutual information and continuity

**Central question:** How can an approximate task still require extensive information flow?

**Understanding target:** Use mutual information and data processing to select payload-sized subsystems. Explain why the continuity penalty must be associated with the correct dimension rather than every helper.

**Dependencies:** M03, M06, M08.

**Conceptual connection:** An approximate swap must still establish mutual information between the payload/reference subsystems on opposite sides. Choosing those subsystems removes an unnecessary continuity penalty proportional to the helper count.

**Sources:** Watrous §5.2; [payload-sized converse](../science/mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Make the eventual endpoint robust to a fixed nonzero error.

### M10. Operator norms and typical strength

**Central question:** Why is a largest eigenvalue not a root-mean-square strength?

**Understanding target:** Distinguish operator norm, Schatten two-norm, normalized Frobenius norm, and a state-weighted second moment. Track their dimension factors and behavior under identity extension.

**Dependencies:** M01.

**Conceptual connection:** Orthogonal Pauli coefficients add quadratically under normalized trace, while aligned extremal eigenvalues may add linearly. The proof needs the former together with the actual state's spectral weight, not an input-uniform replacement for operator norm.

**Sources:** Watrous §1.1.3; [notation](WATROUS_BRIDGE.md#notation-and-normalization).

**Story role:** Identify the strength measure that the information-flow proof can use.

### M11. Hamiltonians, locality, and two clocks

**Central question:** Which operations consume the routing resource?

**Understanding target:** Read bounded contact Hamiltonians and freely controlled regions as a precise dynamical model. Separate contact duration, internal gate duration, and per-contact versus aggregate budgets.

**Dependencies:** M04, M10.

**Conceptual connection:** Treating module unitaries as instantaneous isolates the interface resource. Charging their duration changes the comparator, just as replacing individual contact bounds by an aggregate strength bound changes the theorem.

**Sources:** Watrous §1.1.3 for operator background; local [control models](../science/control-models.md#1-two-distinct-clocks).

**Story role:** Supply the dynamical setting that is not the textbook’s focus.

### M12. Spectral rearrangement and coherent control

**Central question:** What can a unitary rearrange without changing entropy?

**Understanding target:** Distinguish spectra from eigenvectors, reversible permutations from resets, and averaging Hamiltonians from mixing channels. Explain why commutation matters for exact sequence synthesis.

**Dependencies:** M04, M10.

**Conceptual connection:** A reversible basis permutation changes where a spectrum is supported, not its eigenvalues. A prescribed product of commuting conjugated evolutions then realizes a Hamiltonian average coherently, rather than randomizing the output channel.

**Sources:** Watrous §4.1.1 and §§4.3.1–4.3.2; [coherent example](WORKED_EXAMPLES.md#2-occupied-spectators-can-assist-without-losing-their-data).

**Story role:** Prepare both the interaction encoding and the later concentration step.

### M13. Probability concentration and source coding

**Central question:** What does a high-probability subspace guarantee jointly?

**Understanding target:** Relate probability mass, subspace dimension, and compression. Recognize a joint favorable sector without treating compressed bits as independent perfectly pure outputs or discarding the remainder.

**Dependencies:** M07, M12.

**Conceptual connection:** The probability of an entire zero-prefix subspace is the useful preparation promise. It controls a coherent operation on all payload inputs even though the compressed prefix bits need not be independently pure.

**Sources:** Watrous §1.2.2 and §§5.3.1–5.3.2; [preparation example](WORKED_EXAMPLES.md#3-a-near-clean-prefix-is-a-joint-promise-not-perfect-independent-bits).

**Story role:** Connect spectral probability to a reversible preparation promise.

### M14. The complete routing comparison

**Central question:** What exactly is held fixed when initialization is varied?

**Understanding target:** Assemble the hardware, payload, helper promises, inaccessible references, charged controls, and return/error requirements into one task. Explain why a complete channel comparison is stronger than a selected-state transfer.

**Dependencies:** M06, M09, M11, M13.

**Conceptual connection:** The two helper tasks keep payload, contacts, allowed internal processing, and restoration obligations fixed. Identifying the one altered input promise is necessary before calling their times a resource separation.

**Sources:** Watrous Chapters 2–5 as mapped in [Learning](WATROUS_BRIDGE.md); [task](../science/theorem-map.md#1-model-and-main-theorem).

**Story role:** Complete the background phase by unifying the objects and resource model.

## Narrative and innovation

### M15. A small interface controls the entropy factor

**Central question:** How does the bus dimension enter an entropy rate?

**Understanding target:** Explain the conditional-log commutator and the role of conditional variance in a state-weighted rate bound. Separate the published ingredient from the project’s application and alternative qubit constant.

**Dependencies:** M09, M10, M14.

**Conceptual connection:** The bus dimension limits the conditional-log fluctuation factor even when the register includes large references. The remaining state-weighted interaction factor is where geometry and initialization enter.

**Sources:** Watrous §5.2 and §1.1.3 for foundations; [conditional rate](../science/entropy-flow.md#1-published-conditional-variance-bound), with DF19 credited there.

**Story role:** Begin the converse with a local interaction and a dimension-limited entropy factor.

### M16. Contact geometry gives a quadratic budget

**Central question:** Why do many pairwise contacts add in squared coefficients?

**Understanding target:** Explain Pauli orthogonality after removing cut-local terms. Identify normalized Frobenius projection as the valid step, without assuming an operator-norm contraction.

**Dependencies:** M10, M11, M15.

**Conceptual connection:** Cut-local terms cannot change the cut entropy. Removing them by an orthogonal coefficient projection is justified in normalized Frobenius norm, avoiding an unsupported operator-norm step.

**Sources:** Watrous §1.1.3; [contact decomposition](../science/bandwidth.md#21-remove-only-cut-local-terms).

**Story role:** Convert physical pair constraints into a geometry-sensitive interaction measure.

### M17. Entropy deficit bounds usable contact strength

**Central question:** Why can internal control not freely occupy the strongest spectral tail?

**Understanding target:** Connect independent-site spectral moments, the exponential-moment estimate, and the conserved physical entropy deficit. Distinguish arbitrary evolved states from the normalized trace distribution used in the spectral estimate.

**Dependencies:** M08, M13, M16.

**Conceptual connection:** Gaussian-type spectral tails constrain the contact, while relative entropy constrains the evolving state. Their combination prevents unlimited internal processing from concentrating arbitrary weight in the strongest part of the spectrum.

**Sources:** Watrous §5.2; [moment proof](../science/bandwidth.md#2-entropy-deficit-controls-contact-second-moments).

**Story role:** Combine state resource and geometry before making a speed claim.

### M18. The payload forces a cut-entropy change

**Central question:** Why does exchanging n qubits require 2n bits on the reference cut?

**Understanding target:** Build the Bell-reference test, locate each subsystem on its side, and explain the approximate payload-sized mutual-information endpoint. Do not count helper references as new physical purity.

**Dependencies:** M03, M09, M14.

**Conceptual connection:** The payload marginals can remain maximally mixed throughout a perfect exchange. The reference cut reveals the required transfer through correlations and gives a payload-sized condition for approximate success.

**Sources:** Watrous §§2.1.3 and 5.2; [endpoint](../science/mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Turn the requested operation into a required extensive change.

### M19. The bandwidth converse

**Central question:** How do required change and permitted rate constrain all protocols?

**Understanding target:** Assemble the lower bound, explain why internal switching restrictions are unnecessary, and recognize the common-input condition in the weighted ensemble version. Do not turn it into a bound on every specially prepared state.

**Dependencies:** M15, M17, M18.

**Conceptual connection:** Integrating a state-dependent rate gives a lower bound on every permitted schedule, not merely on the constructed protocol. The ensemble version retains its common-input-control condition and permits specially prepared states outside that premise.

**Sources:** [Entropy flow](../science/entropy-flow.md#4-weighted-average-input-entropy-flow-theorem); [mixed-helper converse](../science/mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Finish the converse chain, with its scope visible.

### M20. The three-qubit sign encoding

**Central question:** How can occupied qubits alter a target’s effective contact?

**Understanding target:** Follow the reversible encoding of the collective magnetization into target sign and spectator magnitude. Explain why a reversible map does not erase the spectator data.

**Dependencies:** M11, M12, M14.

**Conceptual connection:** The encoding separates the target's sign from the spectators' magnitude. Because it is a bijection, the spectators' unknown information is retained rather than erased to obtain the larger contact.

**Sources:** Watrous Chapter 4 for spectral background; [worked encoding](WORKED_EXAMPLES.md#2-occupied-spectators-can-assist-without-losing-their-data).

**Story role:** Start the matching construction with a complete local mechanism.

### M21. Exact restoration through commuting translations

**Central question:** Why do translated contacts eliminate spectator dependence?

**Understanding target:** Explain the finite commuting-product identity and the identity action on arbitrary spectators, including reference entanglement. Extend the idea to synchronized marginal translations rather than every joint label.

**Dependencies:** M20.

**Conceptual connection:** Each block only needs a uniform marginal list because the contact is additive over blocks. Commutation then gives an exact finite-time operator identity, and reference preservation follows from identity on the spectator factors.

**Sources:** [Occupied blocks](../science/bandwidth.md#51-an-occupied-data-block); [synchronized lists](../science/accuracy-and-resources.md#3-short-exact-synchronized-block-schedules).

**Story role:** Lift the toy encoding into reusable coherent contact amplification.

### M22. Balanced blocks and initialized leaders

**Central question:** Why do clean leaders produce a larger coherent gain?

**Understanding target:** Explain reversible target-to-leader fanout, additive block gains, and the balanced-block scaling. Distinguish the clean-helper input subspace from an identity on arbitrary helpers.

**Dependencies:** M21.

**Conceptual connection:** Clean leaders can be reversibly correlated with the target so their block strengths add. The balanced partition relates this local mechanism to the total number of contacts and initialized helpers.

**Sources:** [Clean-helper construction](../science/bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers).

**Story role:** Connect a local gain to the number of reusable initialized degrees of freedom.

### M23. From one contact to a full register exchange

**Central question:** How do local interactions implement the complete payload permutation?

**Understanding target:** Connect three rotated Ising operations to SWAP, then follow the buffered 2n+1-SWAP route and final internal permutation. Check phases, helper return, and an arbitrary bus, not only payload labels.

**Dependencies:** M04, M22.

**Conceptual connection:** A local gate identity becomes useful for routing only when the complete wire permutation, its phase, and the bus's original information are restored. The buffered sequence meets those requirements without a clean-bus assumption.

**Sources:** [Full exchange](../science/bandwidth.md#54-full-payload-exchange); [two clocks and buffered route](../science/control-models.md#1-two-distinct-clocks).

**Story role:** Assemble the primitive into an operation on the whole input space.

### M24. Matching exact endpoints

**Central question:** What makes an achievable protocol an optimal scaling law?

**Understanding target:** Compare the converse and construction on identical hardware for clean and unknown helpers. Explain the no-helper square-root endpoint and the separate time-division comparator without conflating their controls.

**Dependencies:** M19, M23.

**Conceptual connection:** An upper bound alone demonstrates feasibility; the entropy lower bound limits every admissible alternative. Their common exponent establishes optimal interaction-time scaling for each exact helper promise.

**Sources:** [Exact endpoints](../science/bandwidth.md#6-unknown-helpers-on-identical-hardware); [time division](../science/entropy-flow.md#5-no-helper-converse-and-sequential-comparator).

**Story role:** Integrate the two proof chains for the exact tasks.

### M25. Concentrating imperfect preparation

**Central question:** How is a useful leader subspace obtained from biased mixed helpers?

**Understanding target:** Explain the largest-eigenvalue mass criterion and the iid concentration estimate, including the fallback when little polarization is available. Retain all entropy-bearing helpers as occupied spectators.

**Dependencies:** M13, M22.

**Conceptual connection:** Reversible concentration transfers entropy into qubits that the contact amplifier can use as occupied spectators. No pure qubits are created by a reset, and small bias is handled by the same bound or the no-concentration fallback.

**Sources:** Watrous §§4.3 and 5.3 for foundations; [reversible concentration](../science/mixed-helpers.md#3-reversible-concentration-at-finite-error), crediting SV98.

**Story role:** Replace a perfect-purity promise by a controlled high-probability subspace.

### M26. Complete error and reusable helpers

**Central question:** Why is one preparation error budget enough for the entire route?

**Understanding target:** Use the common favorable subspace and its common phase to bound the inserted-preparation isometry. Distinguish exact helper marginal return, approximate correlations, and new errors during fresh-payload reuse.

**Dependencies:** M06, M23, M25.

**Conceptual connection:** All gates are correct on the same invariant preparation sector with one common phase. This is why initial preparation error need not add gate by gate, whereas new control errors have a separate composition bound.

**Sources:** [Complete error](../science/mixed-helpers.md#41-complete-reference-preserving-error-without-accumulation); [reuse](../science/accuracy-and-resources.md#5-error-composition-and-reuse).

**Story role:** Make the compressed construction satisfy the actual reference-inclusive task.

### M27. The uniform fixed-error law

**Central question:** What does the main theorem say as bias and helper count change?

**Understanding target:** Assemble matching bounds uniformly in n, s, and p at fixed error. Predict pure, maximally mixed, weak-bias, and extensive-helper limits without assuming constants remain uniform as error vanishes.

**Dependencies:** M19, M26.

**Conceptual connection:** The quantity one plus the total iid entropy deficit joins the unknown-helper and polarized-helper regimes. Uniformity in the bias is separate from uniformity as the allowed error tends to zero.

**Sources:** [Main theorem](../science/mixed-helpers.md#1-task-and-matching-law); [theorem map](../science/theorem-map.md#1-model-and-main-theorem).

**Story role:** Complete the central resource characterization, not only one operating point.

### M28. Why the law has boundaries

**Central question:** Why do full rank and correlated preparation change the inference?

**Understanding target:** Explain the pure-Choi zero-error argument and the correlated pure-spike counterexample. Distinguish a general entropy-budget converse from matching achievability for an arbitrary state with that entropy.

**Dependencies:** M04, M12, M27.

**Conceptual connection:** Full rank forces every eigenstate component to implement the exact unitary when zero error is required. At nonzero error, spectral concentration permits discarding only a small weight in the error analysis; a broad maximally mixed component can prevent that concentration.

**Sources:** [Zero error](../science/mixed-helpers.md#5-zero-error-and-nonzero-error-are-different-tasks); [correlated helpers](../science/mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped).

**Story role:** Identify the exact assumptions responsible for saturation of the converse.

### M29. Accuracy, contact lists, and resource normalization

**Central question:** Which operational advantages survive a changed resource budget?

**Understanding target:** Separate finite universal certificates from ratios of two constructions; exact/sampled list length from internal runtime; and per-contact, quadratic, and sum-of-strength budgets. Explain the finite compiler’s scope without inventing a universal finite-speed impossibility.

**Dependencies:** M11, M24, M27.

**Conceptual connection:** A finite construction beats the full comparator class only when its upper bound lies below the class's lower bound. The resource analysis then determines whether that comparison concerns contact time, count, quadratic strength, or a fixed sum of strengths.

**Sources:** [Accuracy and resources](../science/accuracy-and-resources.md); [finite control](../science/control-models.md#24-finite-control-consequence).

**Story role:** Translate mathematical bandwidth into its precise operational claims and limits.

### M30. The whole result and its place in the literature

**Central question:** What is the complete contribution, and what does it not establish?

**Understanding target:** Explain the model, conserved resource, converse, coherent realization, accuracy promise, and boundaries as one story. Attribute imported tools and prior routing results, distinguish proofs from numerical checks, and state the contribution without claiming a fixed-hardware speedup.

**Dependencies:** M14, M27, M28, M29.

**Conceptual connection:** The result joins a reference-assisted information requirement, a conserved preparation budget, and a coherent realization. Its significance is a matched interface-resource law with explicit initialization and accuracy assumptions, not an assertion of faster noisy hardware.

**Sources:** [Theorem map](../science/theorem-map.md); [related work](../references/RELATED_WORK.md); [verification](../verification/README.md).

**Story role:** Integrate the narrative phase and complete the project-understanding map.

## Integration

M14 joins the background into the precise routing task. M30 joins the converse, construction, accuracy convention, and resource boundaries into the complete scientific account. Continue from the map to the [proof dependencies](../science/theorem-map.md) or the [physical interpretation](../science/interpretation.md) for a connected specialist reading.
