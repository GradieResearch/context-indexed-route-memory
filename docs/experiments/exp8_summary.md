# Experiment 8: Self-Organizing Contextual Route Acquisition

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; route-acquisition thread imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Candidate main mechanism result after thread/human review.

## Purpose

Experiment 7 showed that a clean context-conditioned route field can be composed recurrently. Experiment 8 asks the missing bridge question: > Can a local plastic graph acquire that clean context-conditioned route field from one-step transition experience, then solve unseen multi-step traversal queries by recurrence? The model trains only on local transitions such as: It is then evaluated on held-out composition tasks such as: The main experiment should keep `--path-train-repeats 0`, so the model never directly trains on the final multi-step answers. A recurrent graph with context-bound structural plasticity can acquire local transition routes from sparse experience, and once those routes re

Source path: `experiments/experiment8_self_organizing_route_acquisition/EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment8_self_organizing_route_acquisition/EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md`
- Task/design clue: Experiment 7 showed that a clean context-conditioned route field can be composed recurrently. Experiment 8 asks the missing bridge question: > Can a local plastic graph acquire that clean context-conditioned route field from one-step transition experience, then solve unseen multi-step traversal queries by recurrence? The model trains only on local transitions such as: It is then evaluated on held-out composition tasks such as: The main experiment should keep `--path-train-repeats 0`, so the model never directly trains on the final multi-step answers. A recurrent graph with context-bound structural plasticity can acquire local transition routes from sparse experience, and once those routes re
- Run scripts detected: `experiments/experiment8_self_organizing_route_acquisition/run_exp8_self_organizing_route_acquisition.py`, `experiments/experiment8_self_organizing_route_acquisition/run_exp8_suite.py`, `experiments/experiment8_self_organizing_route_acquisition/start.ps1`, `experiments/experiment8_self_organizing_route_acquisition/start.sh`, `experiments/experiment8_self_organizing_route_acquisition/start_exp8.ps1`
- Analysis CSVs detected: 27; plot files detected: 42; generated/design reports detected: 5.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment8_self_organizing_route_acquisition/EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md`: Experiment 7 showed that a clean context-conditioned route field can be composed recurrently. Experiment 8 asks the missing bridge question: > Can a local plastic graph acquire that clean context-conditioned route field from one-step transition experience, then solve unseen multi-step traversal queries by recurrence? The model trains only on local transitions such as: It is then evaluated on held-out composition task
- `experiments/experiment8_self_organizing_route_acquisition/TRACKER_UPDATE_EXP8.md`: Date: 2026-05-02 Experiment: Exp8 Self-organizing contextual route acquisition Run names: - exp8_full_self_organizing_route_field - exp8_no_recurrence - exp8_no_structural_plasticity - exp8_no_context_binding - exp8_no_inhibition - exp8_no_reward_gate - exp8_no_homeostasis - exp8_context_bleed Config highlights: - local one-step transition training only - no direct multi-step composition training by default - distrib
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_report.md`: Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently. - `transition_accuracy`: one-step transition learning. - `composition_accuracy`: unseen multi-step recurrent traversal. - `route_table_accuracy`: direct inspection of the learned local route field. - `mean_target_rank`: whether the t
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_report.md`: Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently. - `transition_accuracy`: one-step transition learning. - `composition_accuracy`: unseen multi-step recurrent traversal. - `route_table_accuracy`: direct inspection of the learned local route field. - `mean_target_rank`: whether the t
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_report.md`: Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently. - `transition_accuracy`: one-step transition learning. - `composition_accuracy`: unseen multi-step recurrent traversal. - `route_table_accuracy`: direct inspection of the learned local route field. - `mean_target_rank`: whether the t

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp8_context_bleed | Stress-tests context contamination | TODO: import intended expectation from thread digest | comp=0.8338; route=0.9449; transition=0.9449 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_full_self_organizing_route_field | Reference/full mechanism | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | comp=0.048; route=0.3478; transition=0.3478 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | comp=0.0; route=1.0; transition=1.0 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |
| exp8_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | comp=0.0312; route=0.0257; transition=0.0257 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| route_table_accuracy | Direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_target_rank | Average rank of the true target. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_correct_margin | Correct target score margin over the strongest wrong target. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_context_margin | Correct context/world support margin over competing contexts/worlds. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_wrong_route_activation | Activation assigned to competing routes. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy_mean | Mean one-step route learning accuracy across seeds/conditions. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_accuracy_mean | Mean multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| route_table_accuracy_mean | Mean direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Self-organized route field reaches perfect local metrics in the main summary

Claim: The main Exp8 summary reports 1.0 transition, route-table, and composition accuracy for the full self-organizing route-field variant across 30 seeds.
Evidence: `exp8_full_self_organizing_route_field`: transition_accuracy_mean=1.0, route_table_accuracy_mean=1.0, composition_accuracy_mean=1.0, n_seeds=30.
Caveat: Synthetic symbolic route world; thread/human review needed before final manuscript wording.
Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_report.md`

### Result 2: No recurrence separates route storage from route execution

Claim: The no-recurrence Exp8 row keeps transition and route-table accuracy at 1.0 while composition accuracy is 0.0.
Evidence: `exp8_no_recurrence`: transition_accuracy_mean=1.0, route_table_accuracy_mean=1.0, composition_accuracy_mean=0.0.
Caveat: Interpret as local evidence for this benchmark family, not a universal recurrence claim.
Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`

### Result 3: Structural-plasticity removal collapses acquisition in the main summary

Claim: The no-structural-plasticity Exp8 row reports low transition, route-table, and composition accuracy.
Evidence: `exp8_no_structural_plasticity`: transition_accuracy_mean=0.0257, route_table_accuracy_mean=0.0257, composition_accuracy_mean=0.0312.
Caveat: This supports a benchmark-specific mechanism claim, not biological necessity.
Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`

### Result 4: Context bleed degrades margins and composition relative to full

Claim: The context-bleed row has lower composition accuracy than the full row.
Evidence: `exp8_context_bleed`: composition_accuracy_mean=0.8338, compared with full composition_accuracy_mean=1.0.
Caveat: Needs thread review to distinguish route contamination from other causes.
Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`

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
| `experiments/experiment8_self_organizing_route_acquisition/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/run_exp8_self_organizing_route_acquisition.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/run_exp8_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/start_exp8.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/TRACKER_UPDATE_EXP8.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_mode.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_steps.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_context_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_correct_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_route_table.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_failure_taxonomy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_target_rank.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 42 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp8 accuracy by mode | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_mode.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 accuracy by steps | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_steps.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 composition accuracy | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 context margin | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_context_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 correct margin | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_correct_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 exposure curve composition | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 exposure curve margin | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 exposure curve route table | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_route_table.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 failure taxonomy | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_failure_taxonomy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 target rank | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_target_rank.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp8 transition accuracy | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_transition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| route margin heatmap exp8 full self organizing route field seed0 minus one exp1 | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_minus_one_exp1.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (30) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result.
Evidence: The thread says Exp8 full self-organizing route field achieved 1.0 transition, composition, and route-table accuracy across 30 seeds with one exposure repeat; no-recurrence kept route-table accuracy but failed composition; no-structural-plasticity stayed near random.
Caveat: Controlled symbolic number world; exposure curve was later described as not a real curve and reward/homeostasis were not stressed.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_report.md`
Status: Strong

## Key results (thread-integrated)

### Result 1: Local plasticity can acquire a route field from one-step experience

Claim: Exp8 supports local structural plasticity forming a context-conditioned route table that recurrence can execute compositionally.
Evidence: Local summary shows `exp8_full_self_organizing_route_field` at 1.0 transition, route-table, and composition accuracy across 30 seeds.
Caveat: Synthetic symbolic benchmark; external baselines remain required.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`
Manuscript status: Strong

### Result 2: Route storage and route execution dissociate

Claim: Exp8 no-recurrence preserves local route memory but cannot perform multi-step composition.
Evidence: Local summary shows `exp8_no_recurrence` transition and route-table accuracy 1.0 with composition accuracy 0.0.
Caveat: This is a benchmark-specific internal ablation.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`
Manuscript status: Strong

## What this experiment supports (thread-integrated)

- Structural plasticity can acquire local route fields in the symbolic benchmark.
- Recurrence executes stored route fields.

## What this experiment does not prove (thread-integrated)

- It does not show noisy/delayed feedback robustness; Exp9 addresses stress.
- It does not prove biological plausibility.

## Follow-up actions (thread-integrated)

- Use Exp8 as an early core mechanism result only with explicit symbolic-task caveats.
