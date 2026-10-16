# Verification and reproduction

The mathematical proofs are in [Bandwidth](bandwidth.md), [Entropy flow](entropy-flow.md), and [Control models](control-models.md). The programs check finite identities, numerical inequalities, support bookkeeping, and a specified compiler. They are not experiments, independent review, or numerical proofs of asymptotic theorems.

## Run

From the repository root, using Python 3.13:

```bash
python -m pip install -r requirements.txt
python check_repository.py
python verify.py
```

The pinned dependencies match the recorded run: NumPy 2.3.5 and SciPy 1.17.0. `verify.py` copies the check programs into a temporary directory, runs each with one BLAS thread, and writes logs, complete JSON cases, and a summary into `build/verification/`. It fails on a nonzero exit status, missing success flag, or timeout. Use `--output PATH` for another output directory. Assertions are part of the tests; run normal Python, not optimization mode.

The compact [recorded summary](../results/verification.json) includes the source SHA-256 hashes, environment, counts, output hashes, and diagnostic residuals. It is never silently replaced by a normal verification run. Floating-point values can differ slightly across platforms, and timing fields are not reproducibility targets. Raw generated output hashes identify that particular run; they are not expected to be byte-identical across hardware.

## Coverage

| Suite | What it checks |
|---|---|
| `verify_workspace_construction.py` | 40 spectral checks, 12 target–bus isometries, eight complete exchanges, clean-helper return and arbitrary bus restoration |
| `verify_entropy_budget.py` | 120 Gibbs states, 100 fixed-spectrum orbit maxima, 60 noncommuting states, 54 scalar moment bounds, 16,512 balanced partitions |
| `audit_conditional_rate.py` | 204 states; exact optimization over Hermitian interactions at fixed state and unit second moment, including singular-state support handling |
| `audit_ensemble_cut.py` | 1,152 states over 18 switched segments of a six-qubit, two-bus system; unequal contacts and strong internal controls |
| `audit_translation_approximation.py` | 33 uniform-label checks of coherent sampled-list operator bounds and explicit sufficient sample counts |
| `recursive_three.py` | Complete monomial operators for one, three, and nine occupied data qubits |
| `verify_finite_control.py` | Ancilla-free Toffoli decomposition, bounded generators, frame transitions, recursive costs and 100 buffered wire permutations |
| `verify_full_nine.py` | All 1,024 input columns of the nine-data-qubit plus bus compiled operation, using 390 internal gates |

The largest clean-helper exchange has three payload qubits and two helpers per module plus one bus: 11 physical qubits. Its allowed data-and-bus subspace has 128 input columns, all checked. The theorem does not claim the clean-helper isometry on all 2,048 arbitrary-helper inputs. The largest complete-routing residual across the executed examples is below $9\times10^{-15}$. The nine-data-qubit compiler's unnormalized Frobenius residual is below $7\times10^{-15}$; this bounds the spectral error above. These values are algebraic floating-point residuals, not projected hardware fidelities.

The ensemble suite includes a selected collective input that violates an incorrectly input-uniform square-root bound. It separately verifies the common-ensemble bound. Its finite-difference derivative residual is a recorded diagnostic, distinct from the asserted analytic rate and second-moment comparisons. The conditional-rate optimization is over interactions for each sampled state, not over all possible states or architectures.

## Inspection and maintenance

`check_repository.py` parses Python syntax, checks local Markdown links and citation anchors, checks math delimiters, verifies the MIT license blob and contact paragraph, and confirms that tracked result hashes match the checked source files. Display math uses GitHub dollar delimiters with blank surrounding lines. The CI workflow runs both checks and the complete numerical suite with read-only repository permissions.

Update `results/verification.json` only by copying a successfully generated `summary.json` after the associated source changes. Keep raw cases under the ignored build directory or export them as a separate verification bundle. Adding more numerical examples does not change the stated analytical scope.
