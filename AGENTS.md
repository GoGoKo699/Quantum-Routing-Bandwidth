# Research repository guidance

## Scope and authoritative account

Modify only `GoGoKo699/Quantum-Routing-Bandwidth` under the current project's grant. Read the root README, `science/README.md`, `science/theorem-map.md`, and `references/RELATED_WORK.md` before altering a scientific claim. The topic pages in `science/` own the definitions, theorems, proofs, constructions, examples, and physical interpretation. Give each result one canonical proof and cross-link it rather than maintaining a second full account.

Keep the scientific presentation focused on its question and contribution. Preserve motivation, assumptions, quantifiers, imported theorem attribution, proof domains, and reproduction pointers. Exclude publication planning, development diaries, and private cross-project records. Bibliographic source titles and references to an author's manuscript edition remain accurate source descriptions.

## Essential scientific distinctions

- Both module–bus interfaces are bounded; the bus belongs to neither freely controlled module. The main budget is per physical two-qubit contact. Label every changed aggregate-strength convention.
- Payload and bus inputs can have arbitrary reference entanglement. The exact unknown-helper task covers arbitrary helpers; the clean-helper identity has an initialized input subspace.
- The mixed-helper law uses known independent product preparations and a half diamond distance with their fixed inserted purifications. Exact physical helper marginal return in the construction is distinct from approximate joint/reference restoration and bus accuracy.
- Compression is reversible and retains entropy-bearing qubits as occupied spectators. There is no measurement, reset, input-dependent control, or extra clean workspace.
- The fixed-error theorem holds for all nonnegative helper counts, uniformly in the preparation bias at fixed error between zero and 0.1. Its constants may deteriorate in the zero-error limit. Full rank and correlated preparation have the separately stated consequences.
- Entropy deficit is relative entropy to the maximally mixed state, not work or quadratic purity. The general converse does not imply entropy-only achievability for arbitrary helper spectra.
- The one-design bound requires a common input-independent unitary. It does not bound every specially prepared state. High Choi fidelity is not a dimension-independent worst-case channel guarantee.
- Contact count, contact time, and finite-control runtime are distinct. The displayed compiler's linear duration at fixed strength ratio is not a universal finite-speed impossibility theorem.
- Nonaccumulation under ideal reuse concerns one invariant preparation sector. New synthesis and dynamical errors generally accumulate. Finite certificates evaluate proved bounds; they are not large-register circuit simulations or experimental data.

## Shared learning and attribution

John Watrous, *The Theory of Quantum Information* (2018), remains the sole educational anchor. `learning/WATROUS_BRIDGE.md` owns its section pointers, errata, and notation. `learning/WORKED_EXAMPLES.md` supplies complete local examples. Primary research citations are not additional prerequisite courses.

`learning/MILESTONES.md` is QRB-W18-30-v1: exactly 30 project-defined targets, with 14 background and 16 narrative milestones. Preserve their stable IDs, earlier dependencies, conceptual connections, and final synthesis. This public map contains no personal assessment procedure or learner state. Personal coaching instructions, answers, and progress remain outside the research repository; do not copy private guidance into public learning files or require readers to access a private source.

Preserve the MIT license and exact purpose/contact paragraph. Add a foundational source to both `references/RELATED_WORK.md` and `references/references.bib`. Keep imported tools distinct from the contribution and numerical checks distinct from proof or independent review.

## Verification and display

From the root, run `python check_repository.py`, `python verification/tools/test_structure.py`, and `python verification/run_all.py`. Scientific programs and pinned requirements are under `verification/`; detailed generated outputs go to the ignored `build/verification/`. Update tracked source provenance only from an executed run when paths or programs change. Preserve deterministic certificate bytes when the calculations are unchanged.

Use protected GitHub inline mathematics and fenced `math` blocks. Preserve equation labels as ordinary `\qquad\text{(n)}` content, not legacy `\tag{n}` output that can produce unsupported native MathML rows. Keep table pipes unambiguous and starred subscripts explicitly braced. These are repository-hosting precautions, not universal TeX restrictions.

The separate hosted-render workflow reads the current immutable commit and checks root, science, learning, reference, and verification pages at desktop/mobile widths. Retain source hashes, diagnostics, and screenshots. Visually inspect representative pages; a parser-ready expression can still have broken layout. A local preview or a blocked request is not an actual-host pass. Do not broaden the checks into a claim of independent scientific validation.
