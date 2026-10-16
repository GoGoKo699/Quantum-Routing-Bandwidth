# Thirty milestones for understanding routing bandwidth

**Map identifier: QRB-W18-30-v1.** This is a learner-independent understanding map of the current project. It contains exactly **30 milestones: 14 background/preliminary targets and 16 narrative/innovation targets**. Adapt teaching within a target, not the count or allocation to a learner's self-assessment.

Fourteen background milestones connect states, channels, entropy, spectral tools, probability, and the actual dynamical resource model. Sixteen narrative milestones build the converse and coherent construction, join them at the fixed-error law, and integrate its physical meaning and boundaries. Both phases move from local objects or mechanisms to a global synthesis: M14 assembles the task; M30 assembles the contribution. This is not every technical lemma or neighboring subject, and it is not a rearranged textbook table of contents.

Use the [Watrous section and notation map](learning.md) as the sole educational foundation. Source pointers below distinguish those foundations from the canonical research proofs. The [worked bridges](learning-bridges.md) supply small complete examples. The [coaching protocol](coaching.md) governs challenges, immediate learning feedback, retries, and completion; no progress is asserted by this map.

Dependencies are earlier milestone IDs. Teaching intensity is a project-based default of one, two, or three rounds for a learning block after a failed challenge; actual misconceptions determine the explanation. Every milestone still begins with its own two-question challenge under the coaching protocol.

## Background and preliminaries

### M01. Registers carry unknown states

**Central question:** What must survive when the input state is unknown?

**Understanding target:** Distinguish preserving amplitudes and phases from transporting a known basis label. Identify payload, helper, and bus as different roles, not different kinds of qubit.

**Dependencies:** None. **Teaching intensity:** 1.

**Sources:** Watrous §§2.1.1–2.1.2; [model](bandwidth.md#1-result-model-and-comparison).

**Story role:** Begin with the object being moved, before an architecture or speed claim.

### M02. Composite systems and reductions

**Central question:** What does a local density matrix omit?

**Understanding target:** Use tensor products and partial trace to distinguish the accessible state from its correlations with other systems. Recognize that identical marginals need not mean identical joint states.

**Dependencies:** M01. **Teaching intensity:** 2.

**Sources:** Watrous §2.1.3; [reference example](learning-bridges.md#1-unchanged-marginals-can-conceal-complete-information-transfer).

**Story role:** Make the missing information in a local-state test visible.

### M03. Purifications and inaccessible references

**Central question:** Why test a router on half of an entangled pair?

**Understanding target:** Explain how a reference tests preservation of quantum information without supplying a physical operation or usable workspace. Distinguish physical mixedness from global purity.

**Dependencies:** M02. **Teaching intensity:** 2.

**Sources:** Watrous §2.1.3; [reference example](learning-bridges.md#1-unchanged-marginals-can-conceal-complete-information-transfer).

**Story role:** Turn preservation of correlations into part of the operational task.

### M04. Channels and their complete representations

**Central question:** How is a routing task specified for all inputs?

**Understanding target:** Relate a unitary to its channel and an inserted preparation to an isometry. Explain the normalized Choi test, including its input-dimension normalization.

**Dependencies:** M03. **Teaching intensity:** 2.

**Sources:** Watrous §§2.2.1–2.2.2; [notation](learning.md#notation-and-normalization).

**Story role:** Replace an example trajectory with a complete operation.

### M05. State distance and fidelity conventions

**Central question:** Which numerical notion of accuracy is being reported?

**Understanding target:** Distinguish trace distance, root fidelity, and squared pure-target overlap. Translate the convention in an equation before comparing its error with another statement.

**Dependencies:** M02, M04. **Teaching intensity:** 2.

**Sources:** Watrous §3.1.1 and §3.2; [notation](learning.md#notation-and-normalization).

**Story role:** Prevent a convention change from masquerading as stronger accuracy.

### M06. Reference-aware channel accuracy

**Central question:** What changes when accuracy must include every input and reference?

**Understanding target:** Explain half diamond distance and identify the input and output systems of the fixed-preparation maps. Distinguish a fixed inserted helper purification from an arbitrary helper input.

**Dependencies:** M04, M05. **Teaching intensity:** 3.

**Sources:** Watrous §§3.3.1–3.3.3; [error convention](mixed-helpers.md#1-task-and-matching-law).

**Story role:** Specify the guarantee before evaluating a protocol.

### M07. Entropy and initialization

**Central question:** What resource does a biased helper provide?

**Understanding target:** Interpret binary and von Neumann entropy, the deficit from the maximally mixed state, and its conservation under physical unitaries. Do not identify entropy deficit with work or energy.

**Dependencies:** M02. **Teaching intensity:** 2.

**Sources:** Watrous §§5.1.1–5.1.2 and §§5.2.1–5.2.2; [budget](bandwidth.md#2-entropy-deficit-controls-contact-second-moments).

**Story role:** Introduce the resource that will differ between helper promises.

### M08. Relative entropy and constrained concentration

**Central question:** How can lack of entropy constrain spectral weight?

**Understanding target:** Recognize the entropy deficit as relative entropy to the maximally mixed state. Explain why comparing with a normalized exponential operator limits an expectation without assuming commuting states.

**Dependencies:** M07. **Teaching intensity:** 3.

**Sources:** Watrous §§5.2.1–5.2.3; [variational step](bandwidth.md#23-gibbs-variational-estimate-at-a-fixed-entropy-deficit).

**Story role:** Connect a conserved scalar to the possible weight on large eigenvalues.

### M09. Mutual information and continuity

**Central question:** How can an approximate task still require extensive information flow?

**Understanding target:** Use mutual information and data processing to select payload-sized subsystems. Explain why the continuity penalty must be associated with the correct dimension rather than every helper.

**Dependencies:** M03, M06, M08. **Teaching intensity:** 3.

**Sources:** Watrous §5.2; [payload-sized converse](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Make the eventual endpoint robust to a fixed nonzero error.

### M10. Operator norms and typical strength

**Central question:** Why is a largest eigenvalue not a root-mean-square strength?

**Understanding target:** Distinguish operator norm, Schatten two-norm, normalized Frobenius norm, and a state-weighted second moment. Track their dimension factors and behavior under identity extension.

**Dependencies:** M01. **Teaching intensity:** 2.

**Sources:** Watrous §1.1.3; [notation](learning.md#notation-and-normalization).

**Story role:** Identify the strength measure that the information-flow proof can use.

### M11. Hamiltonians, locality, and two clocks

**Central question:** Which operations consume the routing resource?

**Understanding target:** Read bounded contact Hamiltonians and freely controlled regions as a precise dynamical model. Separate contact duration, internal gate duration, and per-contact versus aggregate budgets.

**Dependencies:** M04, M10. **Teaching intensity:** 2.

**Sources:** Watrous §1.1.3 for operator background; local [control models](control-models.md#1-two-distinct-clocks).

**Story role:** Supply the dynamical setting that is not the textbook’s focus.

### M12. Spectral rearrangement and coherent control

**Central question:** What can a unitary rearrange without changing entropy?

**Understanding target:** Distinguish spectra from eigenvectors, reversible permutations from resets, and averaging Hamiltonians from mixing channels. Explain why commutation matters for exact sequence synthesis.

**Dependencies:** M04, M10. **Teaching intensity:** 2.

**Sources:** Watrous §4.1.1 and §§4.3.1–4.3.2; [coherent example](learning-bridges.md#2-occupied-spectators-can-assist-without-losing-their-data).

**Story role:** Prepare both the interaction encoding and the later concentration step.

### M13. Probability concentration and source coding

**Central question:** What does a high-probability subspace guarantee jointly?

**Understanding target:** Relate probability mass, subspace dimension, and compression. Recognize a joint favorable sector without treating compressed bits as independent perfectly pure outputs or discarding the remainder.

**Dependencies:** M07, M12. **Teaching intensity:** 2.

**Sources:** Watrous §1.2.2 and §§5.3.1–5.3.2; [preparation example](learning-bridges.md#3-a-near-clean-prefix-is-a-joint-promise-not-perfect-independent-bits).

**Story role:** Connect spectral probability to a reversible preparation promise.

### M14. The complete routing comparison

**Central question:** What exactly is held fixed when initialization is varied?

**Understanding target:** Assemble the hardware, payload, helper promises, inaccessible references, charged controls, and return/error requirements into one task. Explain why a complete channel comparison is stronger than a selected-state transfer.

**Dependencies:** M06, M09, M11, M13. **Teaching intensity:** 2.

**Sources:** Watrous Chapters 2–5 as mapped in [Learning](learning.md); [task](theorem-map.md#1-model-and-main-theorem).

**Story role:** Complete the background phase by unifying the objects and resource model.

## Narrative and innovation

### M15. A small interface controls the entropy factor

**Central question:** How does the bus dimension enter an entropy rate?

**Understanding target:** Explain the conditional-log commutator and the role of conditional variance in a state-weighted rate bound. Separate the published ingredient from the project’s application and alternative qubit constant.

**Dependencies:** M09, M10, M14. **Teaching intensity:** 3.

**Sources:** Watrous §5.2 and §1.1.3 for foundations; [conditional rate](entropy-flow.md#1-published-conditional-variance-bound), with DF19 credited there.

**Story role:** Begin the converse with a local interaction and a dimension-limited entropy factor.

### M16. Contact geometry gives a quadratic budget

**Central question:** Why do many pairwise contacts add in squared coefficients?

**Understanding target:** Explain Pauli orthogonality after removing cut-local terms. Identify normalized Frobenius projection as the valid step, without assuming an operator-norm contraction.

**Dependencies:** M10, M11, M15. **Teaching intensity:** 2.

**Sources:** Watrous §1.1.3; [contact decomposition](bandwidth.md#21-remove-only-cut-local-terms).

**Story role:** Convert physical pair constraints into a geometry-sensitive interaction measure.

### M17. Entropy deficit bounds usable contact strength

**Central question:** Why can internal control not freely occupy the strongest spectral tail?

**Understanding target:** Connect independent-site spectral moments, the exponential-moment estimate, and the conserved physical entropy deficit. Distinguish arbitrary evolved states from the normalized trace distribution used in the spectral estimate.

**Dependencies:** M08, M13, M16. **Teaching intensity:** 3.

**Sources:** Watrous §5.2; [moment proof](bandwidth.md#2-entropy-deficit-controls-contact-second-moments).

**Story role:** Combine state resource and geometry before making a speed claim.

### M18. The payload forces a cut-entropy change

**Central question:** Why does exchanging n qubits require 2n bits on the reference cut?

**Understanding target:** Build the Bell-reference test, locate each subsystem on its side, and explain the approximate payload-sized mutual-information endpoint. Do not count helper references as new physical purity.

**Dependencies:** M03, M09, M14. **Teaching intensity:** 3.

**Sources:** Watrous §§2.1.3 and 5.2; [endpoint](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Turn the requested operation into a required extensive change.

### M19. The bandwidth converse

**Central question:** How do required change and permitted rate constrain all protocols?

**Understanding target:** Assemble the lower bound, explain why internal switching restrictions are unnecessary, and recognize the common-input condition in the weighted ensemble version. Do not turn it into a bound on every specially prepared state.

**Dependencies:** M15, M17, M18. **Teaching intensity:** 2.

**Sources:** [Entropy flow](entropy-flow.md#4-weighted-average-input-entropy-flow-theorem); [mixed-helper converse](mixed-helpers.md#2-converse-an-entropy-budget-with-a-payload-sized-continuity-bound).

**Story role:** Finish the converse chain, with its scope visible.

### M20. The three-qubit sign encoding

**Central question:** How can occupied qubits alter a target’s effective contact?

**Understanding target:** Follow the reversible encoding of the collective magnetization into target sign and spectator magnitude. Explain why a reversible map does not erase the spectator data.

**Dependencies:** M11, M12, M14. **Teaching intensity:** 2.

**Sources:** Watrous Chapter 4 for spectral background; [worked encoding](learning-bridges.md#2-occupied-spectators-can-assist-without-losing-their-data).

**Story role:** Start the matching construction with a complete local mechanism.

### M21. Exact restoration through commuting translations

**Central question:** Why do translated contacts eliminate spectator dependence?

**Understanding target:** Explain the finite commuting-product identity and the identity action on arbitrary spectators, including reference entanglement. Extend the idea to synchronized marginal translations rather than every joint label.

**Dependencies:** M20. **Teaching intensity:** 3.

**Sources:** [Occupied blocks](bandwidth.md#51-an-occupied-data-block); [synchronized lists](accuracy-and-resources.md#3-short-exact-synchronized-block-schedules).

**Story role:** Lift the toy encoding into reusable coherent contact amplification.

### M22. Balanced blocks and initialized leaders

**Central question:** Why do clean leaders produce a larger coherent gain?

**Understanding target:** Explain reversible target-to-leader fanout, additive block gains, and the balanced-block scaling. Distinguish the clean-helper input subspace from an identity on arbitrary helpers.

**Dependencies:** M21. **Teaching intensity:** 2.

**Sources:** [Clean-helper construction](bandwidth.md#5-matching-exact-construction-with-returned-clean-helpers).

**Story role:** Connect a local gain to the number of reusable initialized degrees of freedom.

### M23. From one contact to a full register exchange

**Central question:** How do local interactions implement the complete payload permutation?

**Understanding target:** Connect three rotated Ising operations to SWAP, then follow the buffered 2n+1-SWAP route and final internal permutation. Check phases, helper return, and an arbitrary bus, not only payload labels.

**Dependencies:** M04, M22. **Teaching intensity:** 2.

**Sources:** [Full exchange](bandwidth.md#54-full-payload-exchange); [two clocks and buffered route](control-models.md#1-two-distinct-clocks).

**Story role:** Assemble the primitive into an operation on the whole input space.

### M24. Matching exact endpoints

**Central question:** What makes an achievable protocol an optimal scaling law?

**Understanding target:** Compare the converse and construction on identical hardware for clean and unknown helpers. Explain the no-helper square-root endpoint and the separate time-division comparator without conflating their controls.

**Dependencies:** M19, M23. **Teaching intensity:** 2.

**Sources:** [Exact endpoints](bandwidth.md#6-unknown-helpers-on-identical-hardware); [time division](entropy-flow.md#5-no-helper-converse-and-sequential-comparator).

**Story role:** Integrate the two proof chains for the exact tasks.

### M25. Concentrating imperfect preparation

**Central question:** How is a useful leader subspace obtained from biased mixed helpers?

**Understanding target:** Explain the largest-eigenvalue mass criterion and the iid concentration estimate, including the fallback when little polarization is available. Retain all entropy-bearing helpers as occupied spectators.

**Dependencies:** M13, M22. **Teaching intensity:** 3.

**Sources:** Watrous §§4.3 and 5.3 for foundations; [reversible concentration](mixed-helpers.md#3-reversible-concentration-at-finite-error), crediting SV98.

**Story role:** Replace a perfect-purity promise by a controlled high-probability subspace.

### M26. Complete error and reusable helpers

**Central question:** Why is one preparation error budget enough for the entire route?

**Understanding target:** Use the common favorable subspace and its common phase to bound the inserted-preparation isometry. Distinguish exact helper marginal return, approximate correlations, and new errors during fresh-payload reuse.

**Dependencies:** M06, M23, M25. **Teaching intensity:** 3.

**Sources:** [Complete error](mixed-helpers.md#41-complete-reference-preserving-error-without-accumulation); [reuse](accuracy-and-resources.md#5-error-composition-and-reuse).

**Story role:** Make the compressed construction satisfy the actual reference-inclusive task.

### M27. The uniform fixed-error law

**Central question:** What does the main theorem say as bias and helper count change?

**Understanding target:** Assemble matching bounds uniformly in n, s, and p at fixed error. Predict pure, maximally mixed, weak-bias, and extensive-helper limits without assuming constants remain uniform as error vanishes.

**Dependencies:** M19, M26. **Teaching intensity:** 2.

**Sources:** [Main theorem](mixed-helpers.md#1-task-and-matching-law); [theorem map](theorem-map.md#1-model-and-main-theorem).

**Story role:** Complete the central resource characterization, not only one operating point.

### M28. Why the law has boundaries

**Central question:** Why do full rank and correlated preparation change the inference?

**Understanding target:** Explain the pure-Choi zero-error argument and the correlated pure-spike counterexample. Distinguish a general entropy-budget converse from matching achievability for an arbitrary state with that entropy.

**Dependencies:** M04, M12, M27. **Teaching intensity:** 3.

**Sources:** [Zero error](mixed-helpers.md#5-zero-error-and-nonzero-error-are-different-tasks); [correlated helpers](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped).

**Story role:** Identify the exact assumptions responsible for saturation of the converse.

### M29. Accuracy, contact lists, and resource normalization

**Central question:** Which operational advantages survive a changed resource budget?

**Understanding target:** Separate finite universal certificates from ratios of two constructions; exact/sampled list length from internal runtime; and per-contact, quadratic, and sum-of-strength budgets. Explain the finite compiler’s scope without inventing a universal finite-speed impossibility.

**Dependencies:** M11, M24, M27. **Teaching intensity:** 3.

**Sources:** [Accuracy and resources](accuracy-and-resources.md); [finite control](control-models.md#24-finite-control-consequence).

**Story role:** Translate mathematical bandwidth into its precise operational claims and limits.

### M30. The whole result and its place in the literature

**Central question:** What is the complete contribution, and what does it not establish?

**Understanding target:** Explain the model, conserved resource, converse, coherent realization, accuracy promise, and boundaries as one story. Attribute imported tools and prior routing results, distinguish proofs from numerical checks, and state the contribution without claiming a fixed-hardware speedup.

**Dependencies:** M14, M27, M28, M29. **Teaching intensity:** 3.

**Sources:** [Theorem map](theorem-map.md); [related work](related-work.md); [verification](verification.md).

**Story role:** Integrate the narrative phase and complete the project-understanding map.

## Completion

Passing all M01–M30 under the coaching protocol completes the conceptual project tutorial. The final target is integration, not an additional unannounced exam. Reading a file, running verification, or approving a repository update does not count as a pass. Learner attempts and progress stay separate from this common map; no prior tutorial scores are imported.
