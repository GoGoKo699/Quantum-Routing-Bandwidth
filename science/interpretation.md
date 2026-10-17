# Initialization, information flow, and usable bandwidth

The results distinguish three resources that can otherwise be conflated: the number and strength of physical contacts, the quantum information already occupying the module, and the known part of its preparation. Their optimal-time comparison holds the contacts and payload fixed while changing the helper input promise.

## Unknown information is not an idle obstacle

An unknown spectator cannot simply be set to a favorable spin orientation: doing so would destroy its information or require an additional storage resource. The occupied-data construction instead encodes the sign of a collective contact into a selected target and then removes its dependence on spectator labels through a coherent sequence of commuting interactions.

The completed operation acts as identity on every spectator subsystem, including correlations with references. For a block of $`b`$ occupied qubits, the effective contact gain is the average absolute magnetization $`\mu_b=\Theta(\sqrt b)`$. The spectators help without being measured or consumed. This is an operator identity, not a statement limited to single-excitation states or favorable computational-basis inputs. The [construction](bandwidth.md#51-an-occupied-data-block) supplies its explicit encoding and averaging sequence.

This explains why no-helper register exchange can take $`\Theta(\sqrt n/J)`$ in the free-internal-control model, whereas a time-division bus with at most one active contact has a linear lower bound. Simultaneous contacts and internal processing are essential to that comparison; a bare star with no usable internal module operations is a different model.

## A preparation promise changes usable collective strength

The largest collective contact eigenvalue can scale linearly with the number of contacts. An accurate operation on an unknown register cannot assume that its physical state occupies only that extremal sector. The reference-assisted input test and the conserved physical entropy deficit constrain how much weight can reach the strongly interacting part of the spectrum.

For independently prepared helpers, that deficit is

```math
\mathcal I(\omega)=1+2s[1-h_2(p)]
```

on the pure-bus lower-bound test. The [conditional entropy rate](entropy-flow.md) and [contact moment estimate](bandwidth.md#2-entropy-deficit-controls-contact-second-moments) turn it into an information-flow limit. This limits arbitrary internal processing without imposing a minimum switching interval.

The upper bound reaches the same scaling by concentrating preparation weight reversibly into useful leader bits. The remaining entropy stays in the device, in qubits that the occupied-data construction already knows how to preserve. Thus initialization is useful not because entropy is erased during routing, but because a known distribution permits coherent concentration into a large favorable subspace.

At fixed hardware, define one-direction throughput as $`\mathcal B=n/T`$. The [matching law](mixed-helpers.md#1-task-and-matching-law) gives throughput of order $`J\sqrt{(n+s)[1+s(1-h_2(p))]}`$ at fixed nonzero error. Counting both directions multiplies throughput by two. No frequency bandwidth or unrestricted channel-capacity statement is intended.

## Returned resources and reference correlations

Returning a helper marginal is weaker than returning its complete quantum state together with its correlations. The [fixed-preparation maps](mixed-helpers.md#1-task-and-matching-law) include inaccessible helper purifications in the output comparison and allow arbitrary reference-entangled payload and bus inputs.

For the specified diagonal mixed preparation, the construction returns the physical helper density matrix exactly. Joint correlations and bus inaccuracies are bounded by the complete-operation half diamond error. On one common favorable helper sector the full route agrees exactly with the ideal operation, including one common phase. That is the reason initial preparation error does not grow gate by gate in the ideal sequence.

Coherent reuse on fresh payloads retains the same favorable sector. It therefore retains the same initial-sector error bound in the absence of new physical noise. This is not a collection of independent error-free calls: unfavorable-sector errors may be correlated across uses. Pulse errors, Hamiltonian perturbations, and list-approximation errors have their own [composition bound](accuracy-and-resources.md#5-error-composition-and-reuse).

## Two limits on an entropy-only interpretation

**Zero error tests the full support.** A full-rank helper preparation gives nonzero weight to every helper eigenstate. An exactly unitary output channel has a pure Choi state, so every such component must implement the same operation; exact preparation-reference return then forces the unknown-helper operation on the full space. A nonzero bias can improve fixed-error scaling without improving the zero-error law. The constants of the fixed-error result need not remain bounded as the error goes to zero.

**Equal entropy does not imply equal concentration.** A state with a small pure spike and a substantial maximally mixed component can have extensive entropy deficit but still require the unknown-helper time scale at small fixed error. The [correlated-helper example](mixed-helpers.md#7-why-the-product-state-assumption-cannot-be-dropped) makes this distinction explicit. Entropy deficit gives a general converse; independent preparation supplies the spectral concentration used to attain it. Neither statement warrants a universal entropy-only law for arbitrary mixed helpers.

## The contact budget determines the operational comparison

Under a per-contact bound, adding module qubits increases the quadratic contact strength. The clean and unknown comparisons nevertheless use identical wiring and the same strengths, so their relative initialization enhancement is not an extra-wire advantage.

The [alternative-budget analysis](accuracy-and-resources.md#6-what-changes-under-a-different-interaction-budget) isolates this issue. With a fixed quadratic edge budget $`\Lambda_2`$, the matched time is $`\Theta_\epsilon(n/[\Lambda_2\sqrt{1+sd(p)}])`$, and the preparation enhancement survives. With a fixed sum of edge strengths $`\Lambda_1`$, the optimum is $`\Theta_\epsilon(n/\Lambda_1)`$, regardless of the helper initialization class. In that normalization there is no parametrically growing enhancement.

The [finite certificates](accuracy-and-resources.md#2-finite-size-advantage-against-every-unknown-helper-protocol) compare a constructed upper bound with a lower bound for every allowed unknown-helper protocol, not just with one convenient implementation. Their input promises differ exactly as stated in the resource comparison.

## Interaction time is not an apparatus runtime

Synchronized block translations remove an unnecessary product of control-list lengths. With fixed nonzero polarization, fixed accuracy, and an extensive helper pool, the route has a linear number of exact contact intervals. This does not assign zero physical cost to concentration, global encoding, or pulses.

The [displayed finite-strength compiler](control-models.md#24-finite-control-consequence) has linear total duration at a fixed internal/contact strength ratio. Its constants can improve in suitable regimes, but it does not establish a sublinear fixed-hardware runtime. Conversely, its limitation is not a theorem excluding every better finite-speed implementation.

The scientific conclusion is a matched characterization of a bounded quantum interface under explicit preparation, control, and accuracy assumptions. The information-flow converse, coherent realization, exact endpoints, and counterexamples jointly identify which resource is quantified and which changes of task alter the answer.
