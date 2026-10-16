# Guidance for research assistants

## Scope and canonical material

Work only in `GoGoKo699/Quantum-Routing-Bandwidth` unless the author separately authorizes another repository. Read the README, `docs/theorem-map.md`, and `docs/related-work.md` before changing a scientific claim. The exact helper laws and entropy budget live in `docs/bandwidth.md`; the fixed-error independent-helper law lives in `docs/mixed-helpers.md`. Their conditional entropy ingredient is in `docs/entropy-flow.md`. Keep one canonical proof per statement and link to it from the map.

The scientific core consists of the matching independent-helper fixed-error law, its exact clean/unknown endpoints, the full-rank zero-error boundary, and the correlated-helper counterexample. Improve correctness, attribution, clarity, and reproducibility without adding unrelated models or writing a manuscript unless requested. The theorem map organizes reading and scrutiny; it is not external review.

## Scientific invariants

- Both module–bus interfaces are bounded. The bus is not part of a freely controlled module. The norm budget is per physical two-qubit contact, not a fixed global norm.
- Payload and bus inputs can have arbitrary reference entanglement. Unknown-helper identities hold on arbitrary helpers and their references; clean-helper identities hold on the initialized-helper subspace.
- The exact constructions restore helpers and an arbitrary bus. For independent mixed helpers, distinguish the constructed exact physical helper marginal return from approximate joint/reference restoration and approximate bus accuracy. The error is a half diamond distance with fixed inserted helper purifications, not an error guarantee for arbitrary replacement helper states.
- The independent preparations are known and independent of the payload/bus. No measurement, reset, input-label-dependent control, or unlisted initialized workspace is allowed. Compression and decompression are reversible internal operations; entropy-bearing qubits remain spectators.
- Free internal controls define the matching interaction-time theorem. The finite-strength compiler is a separate construction, not a universal finite-speed lower bound. Keep preparation cost, control count, total duration, and contact time distinct.
- Entropy deficit is `log2(D) - S(omega)`, not quadratic purity or work. The entropy-budget converse is general, but the mixed-helper matching law requires the stated product preparation; the correlated-state counterexample rules out arbitrary-state entropy-only saturation.
- A state-1-design argument requires a common input-independent unitary. It does not bound every selected input by a square-root rate.
- The fixed-error independent-helper law holds for all `s >= 0` and fixed `0 < epsilon <= 0.1`, uniformly in the preparation bias. Its constants need not remain bounded as error tends to zero. The older direct full-cut continuity estimate is a weaker statement, not a restriction of this law.
- High process fidelity is not equivalent to worst-case diamond accuracy. The mixed-helper upper bound uses complete isometries. Reuse without gate-by-gate preparation-error accumulation refers to one invariant good sector and no new physical noise.

## Attribution and evidence

Credit the published conditional-variance bound, entropy-fluctuation speed limits, Hamiltonian averaging, reversible polarization concentration/compression, and prior initialization-sensitive state transfer. Preserve the theorem-level distinctions and source locations in `docs/related-work.md`. Do not infer novelty or publication endorsement from numerical tests. Keep journal-target discussion and development diaries out of the scientific presentation.

## Verification and editing

Run `python check_repository.py` and `python verify.py`. The latter creates fresh outputs under `build/verification`; update the tracked result summary only from an executed run after source changes, preserving its source hashes. Documentation-only edits do not require replacing historical numerical timings. The numerical suite is a consistency check, not external review. Inspect complete operator or allowed-input isometry errors, not only selected-state fidelities.

For documentation use GitHub `$...$` and `$$...$$` math, blank lines around display blocks, relative navigation links, and no display equations in tables. Preserve the MIT license and the exact purpose/contact paragraph. Add cited foundational papers to both the related-work guide and the BibTeX file.

## Teaching

Use Revise → Learn → Test, one selection-only question per coaching turn, and targeted revision after an error. Prefer genuine clickable controls where available; ordinary chat text is not an interactive widget. Establish readiness from demonstrated grasp of the model, exact versus fixed-error tasks, reference test, entropy budget, coherent construction, and control-cost qualification. Separate theorem, proof, finite checks, originality, and significance.
