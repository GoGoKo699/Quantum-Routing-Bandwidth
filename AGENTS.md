# Guidance for research assistants

## Scope and canonical material

Work only in `GoGoKo699/Quantum-Routing-Bandwidth` unless the author separately authorizes another repository. Read the README, `docs/bandwidth.md`, and `docs/related-work.md` before changing a scientific claim. The main definitions and matched helper laws live in `docs/bandwidth.md`; their entropy ingredient is in `docs/entropy-flow.md`. Keep one canonical proof per statement and link to it.

## Scientific invariants

- Both module–bus interfaces are bounded. The bus is not part of a freely controlled module. The norm budget is per physical two-qubit contact, not a fixed global norm.
- The input payload and unknown helpers can have arbitrary reference entanglement. Clean-helper identities hold on the initialized-helper subspace; they are not identities on arbitrary helper inputs.
- Exact constructions restore every helper and an arbitrary bus. No measurement, reset, input-label-dependent control, or unlisted initialized workspace is allowed.
- Free internal controls define the matching interaction-time theorem. The finite-strength compiler is a separate construction, not a universal finite-speed lower bound. Keep preparation cost, control count, total duration, and contact time distinct.
- The entropy deficit is `log2(D) - S(omega)`, not quadratic purity or work. A state-1-design argument requires a common input-independent unitary. It does not bound every individual input state by a square-root rate.
- High process fidelity is not equivalent to worst-case diamond accuracy. The clean-helper approximate converse is stated for `0 <= s <= n` with small fixed error.

## Attribution and evidence

Credit the published conditional-variance bound, entropy-fluctuation speed limits, Hamiltonian averaging, reversible compression, and prior initialization-sensitive state transfer. Keep the model-level distinctions in `docs/related-work.md`. Do not infer novelty or publication endorsement from numerical tests. Keep journal-target discussion and development diaries out of the scientific presentation.

## Verification and editing

Run `python check_repository.py` and `python verify.py`. The latter creates fresh outputs under `build/verification`; update the tracked result summary only from an executed run, preserving its source hashes. The numerical suite is a consistency check, not external review. Inspect complete operator or allowed-input isometry errors, not only selected state fidelities. For documentation use GitHub `$...$` and `$$...$$` math, blank lines around display blocks, relative navigation links, and no display equations in tables. Preserve the MIT license and the exact purpose/contact paragraph.

## Teaching

Use Revise → Learn → Test, one selection-only question per coaching turn, and targeted revision after an error. Prefer genuine clickable controls where available; ordinary chat text is not an interactive widget. Establish readiness from the learner's demonstrated grasp of the model, reference test, entropy bound, construction, and control-cost qualification. Separate the theorem statement, proof mechanism, numerical checks, and significance judgment.
