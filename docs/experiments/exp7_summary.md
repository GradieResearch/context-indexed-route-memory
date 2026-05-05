# Experiment 7: Route Field Diagnostics

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; diagnostic thread imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Candidate mechanism figure/supplement for clean route-field diagnostics.

## Purpose

Experiment 7 is the diagnostic follow-up to the contextual successor problem. Experiment 5 asked whether the graph could choose among multiple transition systems using context and then compose the selected route over several recurrent steps. The result was mechanistically useful but not yet a capability success: recurrence was clearly load-bearing, context routing helped, and structural plasticity helped, but the full model did not reliably compose contextual routes. Experiment 7 therefore does **not** make the task harder. It makes the mechanism easier to inspect. > When contextual traversal fails, does it fail because the graph did not learn the local transition table, did not preserve con

Source path: `experiments/experiment7_route_field_diagnostics/EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment7_route_field_diagnostics/EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md`
- Task/design clue: Experiment 7 is the diagnostic follow-up to the contextual successor problem. Experiment 5 asked whether the graph could choose among multiple transition systems using context and then compose the selected route over several recurrent steps. The result was mechanistically useful but not yet a capability success: recurrence was clearly load-bearing, context routing helped, and structural plasticity helped, but the full model did not reliably compose contextual routes. Experiment 7 therefore does **not** make the task harder. It makes the mechanism easier to inspect. > When contextual traversal fails, does it fail because the graph did not learn the local transition table, did not preserve con
- Run scripts detected: `experiments/experiment7_route_field_diagnostics/run_exp7_route_field_diagnostics.py`, `experiments/experiment7_route_field_diagnostics/run_exp7_suite.py`, `experiments/experiment7_route_field_diagnostics/start.ps1`, `experiments/experiment7_route_field_diagnostics/start.sh`
- Analysis CSVs detected: 24; plot files detected: 30; generated/design reports detected: 5.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment7_route_field_diagnostics/EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md`: Experiment 7 is the diagnostic follow-up to the contextual successor problem. Experiment 5 asked whether the graph could choose among multiple transition systems using context and then compose the selected route over several recurrent steps. The result was mechanistically useful but not yet a capability success: recurrence was clearly load-bearing, context routing helped, and structural plasticity helped, but the ful
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_report.md`: Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity. - `transition_accuracy` shows whether the local one-step route table was learned. - `compositi
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_report.md`: Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity. - `transition_accuracy` shows whether the local one-step route table was learned. - `compositi
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_report.md`: Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity. - `transition_accuracy` shows whether the local one-step route table was learned. - `compositi

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp7_context_bleed | Stress-tests context contamination | TODO: import intended expectation from thread digest | comp=1.0 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_full_route_field | Reference/full mechanism | TODO: import intended expectation from thread digest | comp=1.0 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | comp=1.0 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_noisy_plasticity | TODO: infer mechanism from design doc/thread digest | TODO: import intended expectation from thread digest | comp=1.0 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | comp=0.0536 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | comp=0.0288 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |
| exp7_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | comp=0.0 | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| route_table_accuracy | Direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_target_rank | Average rank of the true target. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_correct_margin | Correct target score margin over the strongest wrong target. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_context_margin | Correct context/world support margin over competing contexts/worlds. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_wrong_route_activation | Activation assigned to competing routes. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy | One-step route learning accuracy. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_accuracy | Multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Clean route field composes when recurrence is present

Claim: The unsaturated Exp7 summary reports full-route-field transition and composition accuracy of 1.0.
Evidence: `exp7_full_route_field` has transition_accuracy=1.0 and composition_accuracy=1.0.
Caveat: Exp7 is diagnostic and supplies/controls route fields; it is not the full acquisition story.
Source path: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`; `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_report.md`

### Result 2: No recurrence preserves one-step route knowledge but loses composition

Claim: The no-recurrence row keeps transition accuracy at 1.0 while composition accuracy is 0.0.
Evidence: `exp7_no_recurrence` has transition_accuracy=1.0, composition_accuracy=0.0, and route_table_accuracy=1.0.
Caveat: Diagnostic setting; thread review still needed for interpretation language.
Source path: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`; `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_route_summary.csv`

### Result 3: No structural plasticity is near chance in this diagnostic

Claim: The no-structural-plasticity row reports low transition and composition accuracy.
Evidence: `exp7_no_structural_plasticity` has transition_accuracy=0.0322 and composition_accuracy=0.0288.
Caveat: Does not by itself prove a general structural-plasticity theorem.
Source path: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`

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
| `experiments/experiment7_route_field_diagnostics/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/run_exp7_route_field_diagnostics.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/run_exp7_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/TRACKER_UPDATE_EXP7.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_mode.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_steps.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_context_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_correct_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_target_rank.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_transition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 30 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp7 accuracy by mode | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 accuracy by steps | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_steps.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 composition accuracy | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 context margin | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_context_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 correct margin | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_correct_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 target rank | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_target_rank.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 transition accuracy | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_transition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| route margin heatmap exp7 context bleed seed0 minus one | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| route margin heatmap exp7 context bleed seed0 plus one | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| route margin heatmap exp7 context bleed seed0 plus two | `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 accuracy by mode | `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp7 accuracy by steps | `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_accuracy_by_steps.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (18) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread says clean route fields compose perfectly when recurrence is present; no-recurrence preserves one-step transition knowledge but fails composition; no-context-binding and no-structural-plasticity degrade.
Caveat: The first Exp7 run was saturated; the unsaturated scale/anti-saturation run is the cleaner diagnostic result.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`; `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_report.md`
Status: Strong

## Key results (thread-integrated)

### Result 1: Clean route fields compose with recurrence

Claim: Exp7 shows that a clean context-conditioned route table can be composed recurrently.
Evidence: Unsaturated local artifacts show `exp7_full_route_field` transition and composition accuracy 1.0, while `exp7_no_recurrence` has transition accuracy 1.0 and composition 0.0.
Caveat: Exp7 is diagnostic and does not by itself prove route-field acquisition.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`; `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_route_summary.csv`
Manuscript status: Strong

## What this experiment supports (thread-integrated)

- Recurrence is needed to execute multi-step routes once local transition structure exists.
- Context binding and structural plasticity are meaningful diagnostic controls.

## What this experiment does not prove (thread-integrated)

- It does not show self-organization from one-step experience; Exp8 addresses that.

## Follow-up actions (thread-integrated)

- Use unsaturated Exp7 artifacts if this experiment appears in a supplementary mechanism figure.
