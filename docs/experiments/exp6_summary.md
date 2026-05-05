# Experiment 6: Route Audit Successor World

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; route-audit thread imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: `docs/threads/experiment6_export.md`
- Manuscript relevance: Candidate supplement documenting corrected route-audit failure mode.

## Purpose

Experiment 5 introduced contextual successor rules, but the review pass uncovered a methodological problem: the traversal loop reconstituted the symbolic concept-plus-context state after every recurrent step. That made several context metrics partly tautological and weakened the meaning of the route-selection claims. Experiment 6 asks: > If we stop rebuilding the symbolic state after every step and instead audit the raw recurrent trajectory, can the graph still choose the right transition family under context and compose it across multiple steps? The task introduces several context-dependent transition rules over the same number concepts: The same start state can now map to different next st

Source path: `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`
- Task/design clue: Experiment 5 introduced contextual successor rules, but the review pass uncovered a methodological problem: the traversal loop reconstituted the symbolic concept-plus-context state after every recurrent step. That made several context metrics partly tautological and weakened the meaning of the route-selection claims. Experiment 6 asks: > If we stop rebuilding the symbolic state after every step and instead audit the raw recurrent trajectory, can the graph still choose the right transition family under context and compose it across multiple steps? The task introduces several context-dependent transition rules over the same number concepts: The same start state can now map to different next st
- Run scripts detected: `experiments/experiment6_route_audit_successor/run_exp6_route_audit_successor.py`, `experiments/experiment6_route_audit_successor/run_exp6_suite.py`, `experiments/experiment6_route_audit_successor/start.ps1`, `experiments/experiment6_route_audit_successor/start.sh`
- Analysis CSVs detected: 1; plot files detected: 8; generated/design reports detected: 2.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`: Experiment 5 introduced contextual successor rules, but the review pass uncovered a methodological problem: the traversal loop reconstituted the symbolic concept-plus-context state after every recurrent step. That made several context metrics partly tautological and weakened the meaning of the route-selection claims. Experiment 6 asks: > If we stop rebuilding the symbolic state after every step and instead audit the
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`: This experiment tests whether the recurrent plastic graph can choose among multiple transition systems using context while being evaluated on the raw recurrent trajectory rather than a reconstructed symbolic state. - `best_composition_accuracy`: whether the graph can compose mode-conditioned transitions across multiple steps. - `composition/accuracy_mode_*`: whether some contexts are easier or more fragile than other

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp6_no_context_routing | Removes context or world indexing | TODO: import intended expectation from thread digest | best comp=0.1639; best transition=0.2127 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | best comp=0.1557; best transition=0.1905 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | best comp=0.1557; best transition=0.2032 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_full_route_audit | Reference/full mechanism | TODO: import intended expectation from thread digest | best comp=0.1516; best transition=0.1937 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | best comp=0.1475; best transition=0.1968 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | best comp=0.041; best transition=0.0476 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |
| exp6_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | best comp=0.0; best transition=0.0 | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| best_accuracy | Best recorded task accuracy in a run. | Generated analysis CSV/report | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| best_composition_accuracy | Best recorded multi-step route composition accuracy. | Generated analysis CSV/report | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| best_transition_accuracy | Best recorded one-step transition accuracy. | Generated analysis CSV/report | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Raw route audit still shows low composition

Claim: Exp6 local artifacts show low absolute composition accuracy under the corrected raw recurrent trajectory audit.
Evidence: `exp6_full_route_audit` has best_composition_accuracy=0.1516; the highest row is `exp6_no_context_routing` at 0.1639.
Caveat: This is evidence of a failure/diagnostic condition, not a capability success.
Source path: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`

## What this experiment supports

- Local evidence summarized above; final supported-claim language must be imported into `docs/manuscript/CLAIMS_AND_EVIDENCE.md` after human/thread review.

## What this experiment does not prove

- Does not establish novelty by itself.
- Does not remove the need for baseline and reproducibility review.

## Known implementation or interpretation caveats

- Thread digest has not been reviewed.
- Check run profile, seeds, and aggregation before manuscript use.

## Artifacts

| Path | Type | Description | Manuscript relevance | Notes |
| --- | --- | --- | --- | --- |
| `experiments/experiment6_route_audit_successor/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/run_exp6_route_audit_successor.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/run_exp6_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_mode.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_path_length.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_adaptation_curve.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_best_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_context_confusion.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_recurrent_drive.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_route_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_wrong_route_activation.png` | plot | Plot image | high | Indexed locally; review before citing. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp6 accuracy by mode | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 accuracy by path length | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_path_length.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 adaptation curve | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_adaptation_curve.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 best composition accuracy | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_best_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 context confusion | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_context_confusion.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 recurrent drive | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_recurrent_drive.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 route margin | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_route_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp6 wrong route activation | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_wrong_route_activation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment6_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread concludes Exp6 is negative-but-informative: recurrence and structural plasticity are load-bearing, but the full model does not robustly solve context-conditioned composition under a raw recurrent audit.
Caveat: No statistical reruns or seed analysis were discussed; endpoint accuracy alone was judged insufficient.
Source thread: `docs/threads/experiment6_export.md`
Related local artifact path: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`
Status: Preliminary

## Key results (thread-integrated)

### Result 1: Raw recurrent audit is negative but informative

Claim: Exp6 does not validate robust context-conditioned compositional route traversal.
Evidence: Local comparison reports `exp6_full_route_audit` best composition accuracy 0.1516, and the thread states the full model's correct route did not dominate competing routes.
Caveat: The result is not a total architectural failure because recurrence and structural plasticity remain load-bearing.
Source thread: `docs/threads/experiment6_export.md`
Source artifact: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_route_margin.png`
Manuscript status: Historical only

### Result 2: Recurrence and structural plasticity are load-bearing but insufficient

Claim: Removing recurrence or structural plasticity damages Exp6 performance, but the full model still fails reliable route control.
Evidence: `exp6_no_recurrence` has 0.0 best composition and transition accuracy; `exp6_no_structural_plasticity` has best composition about 0.041, below the full model.
Caveat: Necessity in this setup does not imply sufficiency for robust compositional memory.
Source thread: `docs/threads/experiment6_export.md`
Source artifact: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`
Manuscript status: Preliminary

### Result 3: Context identity is not route execution

Claim: Exp6 distinguishes preserving context identity from executing the correct context-conditioned route.
Evidence: The thread reports a diagonal context-confusion plot while best composition remained low and route margins were negative.
Caveat: The context-confusion metric itself may need deeper audit.
Source thread: `docs/threads/experiment6_export.md`
Source artifact: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_context_confusion.png`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`
Manuscript status: Promising

## What this experiment supports (thread-integrated)

- Route-margin metrics are necessary to avoid overclaiming.
- Recurrence and structural plasticity can be load-bearing without solving route selection.

## What this experiment does not prove (thread-integrated)

- It does not prove robust context-conditioned route memory.
- It does not prove context routing is harmful; the no-context-routing endpoint score is ambiguous.

## Follow-up actions (thread-integrated)

- Fix stale Exp6 README wording in a docs-only cleanup.
- Consider a multi-seed rerun only if exact Exp6 numeric comparisons are used.
