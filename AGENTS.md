# Guidance for research assistants

## Scope and canonical material

Modify only `GoGoKo699/Quantum-Routing-Bandwidth`. Read the README, `docs/theorem-map.md`, and `docs/related-work.md` before changing a scientific claim. Canonical statements are in `docs/bandwidth.md`, `docs/mixed-helpers.md`, `docs/entropy-flow.md`, and `docs/accuracy-and-resources.md`; control-cost results are in `docs/control-models.md`. Keep one canonical proof per statement and link to it.

The scientific core is the matched independent-helper fixed-error law, its exact clean/unknown endpoints, the full-rank zero-error boundary, and the correlated-helper counterexample. Furnishing improves navigation, teaching, attribution, and display; it does not authorize new models, altered claims, or a manuscript. Retain the MIT license and exact README purpose/contact paragraph. Do not copy private cross-project records into this public repository.

## Scientific invariants

- Both module–bus interfaces are bounded. The bus belongs to neither freely controlled module. The main norm budget is per physical two-qubit contact, not a fixed global norm. Changed aggregate budgets must be labeled.
- Payload and bus inputs may have arbitrary reference entanglement. Exact unknown-helper identities hold on arbitrary helpers and references; clean-helper identities hold on their initialized subspace.
- For independent mixed helpers, distinguish exact physical helper marginal return in the construction from approximate joint/reference restoration and bus accuracy. The error is a half diamond distance with fixed inserted helper purifications, not arbitrary replacement helper inputs.
- Preparations are known and independent of payload/bus. There is no measurement, reset, input-dependent control, or unlisted clean workspace. Compression is reversible; all entropy-bearing qubits remain in the device.
- The fixed-error law holds for all nonnegative helper counts and fixed error between zero and 0.1, uniformly in the stated iid bias. Constants may deteriorate as error tends to zero. The older direct full-cut continuity estimate is not a restriction of the stronger law.
- Free internal controls define the matching interaction-time result. The bounded-strength compiler is a separate construction, not a universal finite-speed lower bound. Preparation cost, contact count, contact time, and total time differ.
- Entropy deficit is lack of entropy relative to the maximally mixed state, not work or quadratic purity. The converse is general; saturation from entropy alone is false for arbitrary correlated helpers.
- The one-design argument uses a common input-independent unitary. It is not a bound on every selected collective state. High process fidelity is not equivalent to worst-case diamond accuracy.
- Nonaccumulating preparation error under ideal reuse comes from one invariant favorable sector. New synthesis and dynamical errors generally accumulate. A finite numerical certificate is not a large-circuit simulation or hardware validation.

## Learning and coaching

John Watrous, *The Theory of Quantum Information* (2018), is the single educational anchor. Use `docs/learning.md` for sections, errata, and notation, and `docs/learning-bridges.md` for the project-specific examples. Research citations remain essential but are not extra prerequisite textbooks. Supply explanations in the conversation instead of assigning prerequisite cover-to-cover reading. Do not redistribute the linked manuscript.

The canonical common map is `docs/milestones.md`: QRB-W18-30-v1, exactly 30 milestones, with 14 background and 16 narrative targets. It describes the project, not a learner's self-assessment. Adapt teaching inside milestones, not the count or targets. Keep attempts and progress out of the public scientific files.

Follow `docs/coaching.md` as the single protocol. Every round has Revise → Learn → Test. Each milestone starts with a two-question challenge; all answers in one attempt must be correct. After a failed challenge, give 1–3 targeted learning rounds with one-question tests and immediate feedback. Only failed challenges increase the next challenge size, capped at six. Challenge feedback follows the full-attempt rule. Prefer genuine answer-selection controls; ordinary links or expandable answer panels are not quiz submissions. Do not launch coaching during maintenance or infer passes from approval messages. Passing M01–M30 completes the conceptual tutorial, not independent proof review.

## Attribution, presentation, and verification

Credit conditional variance, entropy-fluctuation speed limits, Hamiltonian averaging, reversible compression, concentration inequalities, and prior routing/initialization work. Add foundational sources to both `docs/related-work.md` and `references.bib`. Keep journal-target judgments and development diaries out of reader-facing science. Preserve assumptions, proof domains, source provenance, and load-bearing limitations when removing redundancy.

Run `python check_repository.py` and `python verify.py`. The repository checker includes `tools/check_learning.py`, which validates the map, dependencies, source links, and learning entrypoints. The ten numerical suites remain separate. Replace tracked numerical results only after a relevant executed source change; furnishing alone does not justify new scientific provenance. Passing checks is not outside endorsement.

Use GitHub dollar-delimited math with blank lines around displays, no display equations inside tables, and local navigation links. Inspect rendered README, learning pages, and representative math-heavy science pages for macro errors, missing subscripts, bra–ket rendering, and overflow. Test the actual GitHub renderer when accessible; identify a local MathJax preview as local, not as hosting verification. Report which checks actually ran.
