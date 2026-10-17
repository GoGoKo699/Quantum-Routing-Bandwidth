# Learning from Watrous to routing bandwidth

**Educational anchor: John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018).** This is the single textbook foundation. The primary papers in [Related work](../references/RELATED_WORK.md) remain research citations, not additional prerequisite courses.

| Purpose | Route |
|---|---|
| Understand the project as a whole | [30 milestones](MILESTONES.md), from local objects to the full result |
| Connect the textbook to the mechanism | [Three worked bridges](WORKED_EXAMPLES.md) |
| Read the research directly | [Theorem map](../science/theorem-map.md) → linked canonical proofs |

The map organizes the scientific dependencies for any reader. The selected sections provide a targeted route into the work; specialist details remain in the linked scientific proofs.

## Anchor and access

Use the [author's book page](https://jhwatrous.github.io/books-and-courses.html), its [standard-layout manuscript](https://jhwatrous.github.io/TQI.pdf), and its [errata](https://jhwatrous.github.io/TQI.errata.pdf). Section numbers below refer to that manuscript. Printed page labels and a PDF viewer's page counter differ; use the section identifiers. The author supplies the manuscript for personal use and prohibits redistribution. Link to it; do not add a copy, extracted chapters, or textbook figures to this repository.

The available errata is dated July 23, 2025 and refers to the published edition. In the part of §3.3.3 containing Theorem 3.56 (printed pages 183–184), the corrected conclusion has $`2\sqrt\epsilon`$, not $`\sqrt{2\epsilon}`$. Consult the errata alongside a passage rather than treating an uncorrected printed formula as authoritative.

## Selected sections

The order follows the project. Chapter 1 is a reference when a mathematical definition is needed, not a separate preliminary course.

| Project question | Watrous sections | Local connection |
|---|---|---|
| What information does an unknown register carry? | §§2.1.1–2.1.3 | States, reductions, and inaccessible purifications; M01–M03 |
| What operation must routing implement? | §§2.2.1–2.2.2 | Channels, isometries, and normalized Choi tests; M04 |
| What counts as a small state or channel error? | §3.1.1, §3.2, §§3.3.1–3.3.3 | Trace distance, fidelity conventions, and reference-aware accuracy; M05–M06 |
| How is initialization quantified? | §§5.1.1–5.1.2 and §§5.2.1–5.2.3 | Entropy deficit, relative entropy, mutual information, and continuity; M07–M09 |
| Which strength and clock are being charged? | §1.1.3 for norms | The dynamical model is supplied locally; M10–M11 |
| What can a reversible rearrangement change? | §4.1.1 and §§4.3.1–4.3.2 | Spectral background, not an identification of mixed channels with coherent control; M12 |
| How is a high-probability subspace found? | §1.2.2 and §§5.3.1–5.3.2 | Concentration and compression intuition; M13 |

M14 assembles this background into the actual routing task. M15–M30 build the research argument using the canonical project proofs. The book is not being credited with the routing theorem, its conditional-variance input, or its contact-simulation construction. In particular, the dynamical rate argument is a project-specific bridge from static quantum-information tools.

## Notation and normalization

Keep the physics notation of this repository. Translate the anchor, rather than silently changing either source's definitions.

| In Watrous | Here | Check before substituting |
|---|---|---|
| A vector $`u`$ and outer product $`uu^*`$ | $`\lvert\psi\rangle`$ and $`\lvert\psi\rangle\langle\psi\rvert`$ | The asterisk on an operator is the adjoint, written $`\dagger`$ here. |
| Register spaces and density operators | $`L,R,C`$ and $`\omega,\rho`$ | Inaccessible reference systems are not controllable workspace. |
| Schatten two-norm $`\lVert A\rVert_2`$ | Normalized Frobenius norm $`\lVert A\rVert_F`$ in the proofs | Divide the Schatten norm by the square root of the full operator dimension. |
| Choi operator $`J(\Phi)`$ in §2.2.2 | A normalized Choi state when testing fidelity | Divide by input dimension. The bare $`J`$ in a contact bound denotes coupling strength, not a Choi operator. |
| Fidelity $`F`$ in Definition 3.11 | Squared pure-target overlap $`F_e`$ in the process tests | Root fidelity and squared overlap are not interchangeable. |
| Completely bounded trace norm in §3.3.2 | Diamond norm $`\lVert\cdot\rVert_\diamond`$ | The main error convention includes the factor $`1/2`$. |
| Entropic functions and relative entropy in Chapter 5 | $`S`$, $`h_2`$, and $`\mathcal I`$ | Entropies are in bits; moment-generating estimates explicitly use natural logarithms. |

For an operator on a $`D`$-dimensional space,

```math
\|A\|_F^2=\frac{\mathrm{Tr}(A^\dagger A)}D,
\qquad \|A\|_F=\frac{\|A\|_2}{\sqrt D}.
```

Thus the identity has normalized Frobenius norm one, whatever its dimension. Neither norm is the contact's operator norm. A statement proved for one must not be used as a bound for another without its dimension factor.

For a trace-preserving channel with input dimension $`d_{\mathrm{in}}`$, Watrous's Choi operator has trace $`d_{\mathrm{in}}`$. Set $`\tau_\Phi=J(\Phi)/d_{\mathrm{in}}`$. For a unitary target with normalized Choi vector $`|\Psi_{\ast}\rangle`$,

```math
F_e=\langle\Psi_{\ast}|\tau_\Phi|\Psi_{\ast}\rangle
=F\!\left(\tau_\Phi,|\Psi_{\ast}\rangle\langle\Psi_{\ast}|\right)^2.
```

The right-hand $`F`$ is Watrous's root fidelity. High Choi fidelity alone is not the same statement as a dimension-independent worst-case diamond guarantee.

The initialization budget is a familiar relative entropy:

```math
\mathcal I(\omega)=\log_2D-S(\omega)
=D\!\left(\omega\,\middle\|\,I/D\right).
```

On the right $`D(\cdot\|\cdot)`$ is relative entropy; inside $`I/D`$, $`D`$ is the Hilbert-space dimension. This budget measures lack of entropy, not work, temperature, or quadratic purity.

## From foundations to the project

The [worked bridges](WORKED_EXAMPLES.md) connect (i) references to the information-flow requirement, (ii) reversible rearrangement to spectator-preserving contact amplification, and (iii) compression to complete-operation preparation error. The [milestone map](MILESTONES.md) integrates them with the theorem's boundaries and resource budgets. The [specialist map](../science/theorem-map.md) retains the exact proof chain and primary attribution.

The [physical interpretation](../science/interpretation.md) combines the three bridges into the resource comparison. The proofs, rather than these examples, establish the universal statements.
