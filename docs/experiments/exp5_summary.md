# Experiment 5: Contextual Successor World

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; thread-derived caveats imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment6_export.md`
- Manuscript relevance: Deprecated or caveated precursor; Exp6 README identifies a methodological ambiguity.

## Purpose

Experiment 4 showed that recurrence and structural plasticity become load-bearing when the task actually requires traversal. The next question is whether the graph can do something more interesting than learn a single reusable chain. Experiment 5 asks: > Can the same recurrent plastic graph choose among multiple transition systems based on context, then compose the chosen route over several steps? The task introduces several context-dependent transition rules over the same number concepts: The same start state can now map to different next states depending on context: The graph therefore has to do more than memorize one successor chain. It has to preserve context, keep competing routes apart

Source path: `experiments/experiment5_contextual_successor/EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment5_contextual_successor/EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`
- Task/design clue: Experiment 4 showed that recurrence and structural plasticity become load-bearing when the task actually requires traversal. The next question is whether the graph can do something more interesting than learn a single reusable chain. Experiment 5 asks: > Can the same recurrent plastic graph choose among multiple transition systems based on context, then compose the chosen route over several steps? The task introduces several context-dependent transition rules over the same number concepts: The same start state can now map to different next states depending on context: The graph therefore has to do more than memorize one successor chain. It has to preserve context, keep competing routes apart
- Run scripts detected: `experiments/experiment5_contextual_successor/run_exp5_contextual_successor.py`, `experiments/experiment5_contextual_successor/run_exp5_suite.py`, `experiments/experiment5_contextual_successor/start.ps1`, `experiments/experiment5_contextual_successor/start.sh`
- Analysis CSVs detected: 2; plot files detected: 14; generated/design reports detected: 3.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment5_contextual_successor/EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`: Experiment 4 showed that recurrence and structural plasticity become load-bearing when the task actually requires traversal. The next question is whether the graph can do something more interesting than learn a single reusable chain. Experiment 5 asks: > Can the same recurrent plastic graph choose among multiple transition systems based on context, then compose the chosen route over several steps? The task introduces
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_report.md`: This experiment tests whether the recurrent plastic graph can choose among multiple transition systems using context, rather than storing a single universal chain. - `best_composition_accuracy`: whether the graph can compose mode-conditioned transitions across multiple steps. - `composition/accuracy_mode_*`: whether some contexts are easier or more fragile than others. - `composition/accuracy_steps_*`: whether longer
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_report.md`: This experiment tests whether the recurrent plastic graph can choose among multiple transition systems using context, rather than storing a single universal chain. - `best_composition_accuracy`: whether the graph can compose mode-conditioned transitions across multiple steps. - `composition/accuracy_mode_*`: whether some contexts are easier or more fragile than others. - `composition/accuracy_steps_*`: whether longer

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp5_full_contextual_traversal | Reference/full mechanism | TODO: import intended expectation from thread digest | best comp=0.1471; best transition=0.1404 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | best comp=0.1471; best transition=0.1404 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | best comp=0.1471; best transition=0.1404 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | best comp=0.1471; best transition=0.1404 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_context_routing | Removes context or world indexing | TODO: import intended expectation from thread digest | best comp=0.1176; best transition=0.1228 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | best comp=0.0882; best transition=0.1579 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |
| exp5_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | best comp=0.0; best transition=0.0 | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| best_accuracy | Best recorded task accuracy in a run. | Generated analysis CSV/report | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| best_composition_accuracy | Best recorded multi-step route composition accuracy. | Generated analysis CSV/report | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| best_transition_accuracy | Best recorded one-step transition accuracy. | Generated analysis CSV/report | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Contextual successor smoke suite remains low

Claim: Exp5 local smoke artifacts do not show reliable contextual multi-step composition.
Evidence: The suite smoke comparison has maximum best_composition_accuracy=0.1471 for `exp5_full_contextual_traversal`; the full contextual traversal row reports best_composition_accuracy=0.1471.
Caveat: Exp6 README identifies a traversal-loop ambiguity in Exp5, so Exp5 should be treated as caveated/deprecated until thread review.
Source path: `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv`; `experiments/experiment6_route_audit_successor/README.md`

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
| `experiments/experiment5_contextual_successor/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/run_exp5_contextual_successor.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/run_exp5_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_comparison.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_mode.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_path_length.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_adaptation_curve.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_best_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_context_confusion.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_recurrent_drive.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_wrong_route_activation.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_mode.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_path_length.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_adaptation_curve.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 14 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp5 accuracy by mode | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 accuracy by path length | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_path_length.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 adaptation curve | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_adaptation_curve.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 best composition accuracy | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_best_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 context confusion | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_context_confusion.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 recurrent drive | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_recurrent_drive.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 wrong route activation | `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_wrong_route_activation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 accuracy by mode | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 accuracy by path length | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_path_length.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 adaptation curve | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_adaptation_curve.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 best composition accuracy | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_best_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp5 context confusion | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_context_confusion.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (2) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread describes Exp5 as a mechanistic partial success but not a capability success; full composition was low, around 0.147, while no-recurrence was 0 and no-structural-plasticity was around 0.088.
Caveat: The thread notes small denominators and low absolute accuracy; context confusion looked strong but did not imply route traversal success.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv`; `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_report.md`
Status: Historical only

### Analysis source: `docs/threads/experiment6_export.md`

Completed result / design / caveat / decision: Identified flaw.
Evidence: The Exp6 thread says Exp5 reconstructed the symbolic concept-plus-context state after each recurrent step, weakening claims about raw recurrent route selection.
Caveat: This does not invalidate Exp5 as motivation, but it prevents treating Exp5 as a solved contextual traversal result.
Source thread: `docs/threads/experiment6_export.md`
Related local artifact path: `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`
Status: Historical only

## Key results (thread-integrated)

### Result 1: Mechanistic partial success, not capability success

Claim: Exp5 should be treated as a motivating failure/diagnostic precursor rather than evidence of reliable context-conditioned composition.
Evidence: Local suite smoke shows `exp5_full_contextual_traversal` best composition accuracy 0.1471; the thread independently identifies low composition and misleadingly strong context-confusion behavior.
Caveat: Traversal-loop reconstruction makes raw recurrent route-selection claims unsafe.
Source thread: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment6_export.md`
Source artifact: `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv`; `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_context_confusion.png`
Manuscript status: Historical only

## What this experiment supports (thread-integrated)

- Motivation for route-field diagnostics and raw recurrent audits.
- Evidence that context identity alone was not enough for reliable route execution.

## What this experiment does not prove (thread-integrated)

- It does not prove robust context-conditioned composition.
- It does not prove world/context indexing solves destructive interference.

## Follow-up actions (thread-integrated)

- Cite Exp5 only as a caveated precursor if it appears in the manuscript.
