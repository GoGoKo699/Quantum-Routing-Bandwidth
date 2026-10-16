# Verification and reproduction

Proofs are in [Bandwidth](bandwidth.md), [Mixed helpers](mixed-helpers.md), [Entropy flow](entropy-flow.md), [Accuracy and resources](accuracy-and-resources.md), and [Control models](control-models.md). Programs check finite identities and stated numerical inequalities. They are not experiments, independent review, or numerical proofs of asymptotic theorems.

## Run

Use Python 3.13 with the pinned NumPy 2.3.5 and SciPy 1.17.0 dependencies:

```bash
python -m pip install -r requirements.txt
python check_repository.py
python verify.py
```

The verifier copies check sources into a temporary directory, runs each with one BLAS thread and assertions enabled, and writes complete JSON outputs, logs, and a summary under `build/verification/`. Use `--output PATH` for another directory. A failed assertion, nonzero exit, missing success flag, or timeout fails the run. Optimization mode is rejected.

The [finite certificates and full closure checks](../results/scientific-closure.json) retain the quantitative examples. The [tracked summary](../results/verification.json) records source hashes, output hashes, environment, counts, and diagnostic residuals from an executed run. Timing and raw-output hashes can differ between runs; they are provenance, not portable numerical targets. Normal verification never replaces this tracked record.

## Coverage

| Suite | Coverage |
|---|---|
| `verify_workspace_construction.py` | 40 spectral checks, 12 target–bus isometries, eight complete routes; synchronized exact block averaging |
| `verify_entropy_budget.py` | 120 Gibbs states, 100 fixed-spectrum orbit maxima, 60 noncommuting states, 54 moment-generating bounds, 16,512 partitions |
| `audit_conditional_rate.py` | 204 states with exact Hamiltonian optimization at fixed weighted second moment; support handling included |
| `audit_ensemble_cut.py` | 1,152 states in 18 switched segments of a six-qubit/two-bus system with unequal contacts |
| `audit_translation_approximation.py` | 33 no-helper uniform-label approximation checks |
| `recursive_three.py` | Complete monomial operators for one, three, and nine occupied data qubits |
| `verify_finite_control.py` | Toffoli decomposition, bounded generators, frame changes, costs, and 100 buffered permutations |
| `verify_full_nine.py` | All 1,024 columns of the nine-data-qubit plus bus compiler, using 390 internal gates |
| `verify_mixed_helpers.py` | 546 spectral checks, 216 compression bounds, six helper-block routes, purification-inclusive errors, correlated-state examples |
| `verify_scientific_closure.py` | 260 integer spectral crosschecks, five finite universal-comparator certificates, 15 synchronized/random-list checks, three fresh-payload reuse checks, 12 perturbation checks |

The largest clean-helper full route has 11 physical qubits and 128 allowed arbitrary-payload/bus input columns. The mixed-helper route tests separately propagate every helper sector and payload/bus column, through 11 physical qubits. The clean-helper isometry is not claimed on arbitrary helper inputs. Algebraic residuals below approximately $10^{-14}$ in these cases are floating-point consistency checks, not physical gate fidelities.

The closure suite's fresh-payload check uses two different payload pairs, a common bus, and all 64 helper sectors. It evaluates the complete fixed-purification Gram operator on all 32 payload/bus input columns. This tests the same initial preparation-error bound on fresh batches rather than only on repeated powers of one input gate. It does not test new physical noise.

Large finite-size examples use integer binomial-shell weights for rational $p=1/10$, rational gains, and rational bounds on constants. The tail decisions and strict time comparisons are exact rational arithmetic. Approximate decimal fields display those results; no 2,049- or 8,193-qubit state-vector evolution is claimed. The finite certificate compares a mixed-helper upper bound with a lower bound for **every** admissible unknown-helper protocol at the same error, contacts, and payload.

The ensemble suite includes a selected collective state that violates an incorrectly input-uniform square-root rate bound. Its finite-difference residual is a diagnostic, distinct from its asserted rate/moment comparisons. Hamiltonian optimization in the conditional suite is exact for each sampled state, not an optimization over all states.

## Maintenance

`check_repository.py` checks syntax, local links and citation anchors, math delimiters, bibliography keys, the contact paragraph, the original license, exact suite coverage, and all check-source hashes. CI runs both the repository checker and complete numerical suite. Update the tracked result file only from a successful associated run after changing scientific check sources. Keep full generated cases in the ignored build directory or export them as a verification bundle.
