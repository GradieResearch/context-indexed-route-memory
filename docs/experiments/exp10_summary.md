# Experiment 10: Rule Reversal, Retention, and Adaptive Rebinding

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; reversal/consolidation thread imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Candidate stability-plasticity/consolidation supplement after review.

## Purpose

Experiment 10 tests the next unresolved question after Experiment 9: > Can a graph change a learned route system without destroying itself? Experiments 7-9 established the mechanism stack: - clean route fields compose recurrently; - local structural plasticity can self-organize those route fields from one-step experience; - context binding separates route families; - inhibition protects route margins under context interference; - reward gating and eligibility traces become load-bearing under noisy or delayed feedback. Experiment 10 now probes the stability-plasticity tradeoff. The model first learns rule set A, then the mode meanings are changed to rule set B. We measure new-rule adaptation,

Source path: `experiments/experiment10_adaptive_reversal/EXPERIMENT_10_ADAPTIVE_REVERSAL.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment10_adaptive_reversal/EXPERIMENT_10_ADAPTIVE_REVERSAL.md`
- Task/design clue: Experiment 10 tests the next unresolved question after Experiment 9: > Can a graph change a learned route system without destroying itself? Experiments 7-9 established the mechanism stack: - clean route fields compose recurrently; - local structural plasticity can self-organize those route fields from one-step experience; - context binding separates route families; - inhibition protects route margins under context interference; - reward gating and eligibility traces become load-bearing under noisy or delayed feedback. Experiment 10 now probes the stability-plasticity tradeoff. The model first learns rule set A, then the mode meanings are changed to rule set B. We measure new-rule adaptation,
- Run scripts detected: `experiments/experiment10_adaptive_reversal/run_exp10_adaptive_reversal.py`, `experiments/experiment10_adaptive_reversal/run_exp10_suite.py`, `experiments/experiment10_adaptive_reversal/start.ps1`, `experiments/experiment10_adaptive_reversal/start.sh`, `experiments/experiment10_adaptive_reversal/start_exp10.ps1`
- Analysis CSVs detected: 20; plot files detected: 18; generated/design reports detected: 4.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment10_adaptive_reversal/EXPERIMENT_10_ADAPTIVE_REVERSAL.md`: Experiment 10 tests the next unresolved question after Experiment 9: > Can a graph change a learned route system without destroying itself? Experiments 7-9 established the mechanism stack: - clean route fields compose recurrently; - local structural plasticity can self-organize those route fields from one-step experience; - context binding separates route families; - inhibition protects route margins under context in
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_report.md`: Experiment 10 tests whether a route field learned under rule A can adapt when the meaning of mode labels is changed to rule B. It also tests whether consolidation, inhibition, reward gating, eligibility traces, and dual world context affect the stability-plasticity tradeoff. - `eval_rule=A` measures old-rule retention. `eval_rule=B` measures new-rule adaptation. - `checkpoint=0` in the reversal phase is immediately a
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_report.md`: Experiment 10 tests whether a route field learned under rule A can adapt when the meaning of mode labels is changed to rule B. It also tests whether consolidation, inhibition, reward gating, eligibility traces, and dual world context affect the stability-plasticity tradeoff. - `eval_rule=A` measures old-rule retention. `eval_rule=B` measures new-rule adaptation. - `checkpoint=0` in the reversal phase is immediately a

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp10_dual_context_worlds | Uses separated context/worlds for reversal | TODO: import intended expectation from thread digest | final acc=0.0379 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_full_adaptive_reversal | Reference/full mechanism | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_consolidation | Removes consolidation | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_eligibility_trace | Removes delayed-credit trace | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | final acc=0.2895 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | final acc=0.0292 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |
| exp10_strong_consolidation | Raises consolidation strength | TODO: import intended expectation from thread digest | final acc=0.9276 | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| route_table_accuracy | Direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_target_rank | Average rank of the true target. | Generated analysis CSV/report | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_correct_margin | Correct target score margin over the strongest wrong target. | Generated analysis CSV/report | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_context_margin | Correct context/world support margin over competing contexts/worlds. | Generated analysis CSV/report | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_wrong_route_activation | Activation assigned to competing routes. | Generated analysis CSV/report | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Adaptive reversal changes final rule performance in local summary

Claim: The main Exp10 adaptation-threshold summary reports high final B accuracy for the full adaptive-reversal variant and lower final A retention.
Evidence: `exp10_full_adaptive_reversal`: final B accuracy=0.9996, B adaptation_threshold_80=3.0; final A accuracy=0.2895.
Caveat: This does not prove non-destructive continual learning; it shows adaptation with old-rule loss in this summary.
Source path: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`

### Result 2: Strong consolidation shifts the reversal tradeoff

Claim: The strong-consolidation row retains A substantially more than the full adaptive-reversal row but has low final B accuracy.
Evidence: `exp10_strong_consolidation`: final A accuracy=0.9276, final B accuracy=0.2897.
Caveat: Validation-full outputs are smaller and differ in magnitude; treat as preliminary until reviewed.
Source path: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`; `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_adaptation_thresholds.csv`

### Result 3: No structural plasticity does not adapt in the main summary

Claim: The no-structural-plasticity row has low final B accuracy.
Evidence: `exp10_no_structural_plasticity` final B accuracy=0.0305.
Caveat: The summary uses generated aggregate values; inspect run profiles before manuscript use.
Source path: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`

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
| `experiments/experiment10_adaptive_reversal/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/run_exp10_adaptive_reversal.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/run_exp10_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/start_exp10.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/EXPERIMENT_10_ADAPTIVE_REVERSAL.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/TRACKER_UPDATE_EXP10.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_adaptation_thresholds.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_failure_taxonomy_final_new_rule.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_new_rule_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_old_rule_retention.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_composition_dual_rule.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_correct_margin_dual_rule.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_route_table.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_old_rule_retention.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_route_table_dual_rule.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_failure_taxonomy_final_new_rule.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 18 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp10 failure taxonomy final new rule | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_failure_taxonomy_final_new_rule.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 final new rule composition | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_new_rule_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 final old rule retention | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_old_rule_retention.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal composition dual rule | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_composition_dual_rule.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal correct margin dual rule | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_correct_margin_dual_rule.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal new rule composition | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal new rule route table | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_route_table.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal old rule retention | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_old_rule_retention.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 reversal route table dual rule | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_route_table_dual_rule.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 failure taxonomy final new rule | `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_failure_taxonomy_final_new_rule.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 final new rule composition | `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_new_rule_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp10 final old rule retention | `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_old_rule_retention.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (6) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread says Exp10 demonstrated adaptive route rebinding and a measurable stability-plasticity tradeoff: the full model adapted to rule B while old A dropped toward overlap baseline; strong consolidation retained A but blocked B; no-consolidation adapted quickly but switchback behavior was poor.
Caveat: The full model mostly overwrote old A under the same context labels; this is not non-destructive memory.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`; `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_report.md`
Status: Promising

## Key results (thread-integrated)

### Result 1: Adaptive rebinding, not non-destructive memory

Claim: Exp10 supports adaptive route rebinding after rule reversal, but not preservation of both rules under the same context.
Evidence: Local adaptation thresholds show full B final accuracy near 1.0 while A final accuracy is about 0.2895; the thread interprets this as overwrite/adaptation.
Caveat: Do not present as solved continual retention.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`
Manuscript status: Promising

### Result 2: Consolidation exposes a stability-plasticity tradeoff

Claim: Strong consolidation preserves old A but blocks new B in Exp10.
Evidence: Local threshold summary shows `exp10_strong_consolidation` final A accuracy about 0.9276 and final B accuracy about 0.2897.
Caveat: Consolidation levels may be too strong and require tuning.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`
Manuscript status: Promising

### Result 3: Dual-context result is ambiguous

Claim: Exp10 dual-context worlds hint at recoverable separated memories but do not prove non-destructive retention.
Evidence: The thread reports B reached 1.0 and A recovered after switchback, but A was not retained during initial B learning.
Caveat: Could reflect retraining, latent recoverability, or context-access issues.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_report.md`; `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_composition_dual_rule.png`
Manuscript status: Preliminary

## What this experiment supports (thread-integrated)

- Adaptive rebinding and stability-plasticity tradeoff framing.

## What this experiment does not prove (thread-integrated)

- It does not prove non-destructive multi-world memory; Exp11 addresses that directly.

## Follow-up actions (thread-integrated)

- Use Exp10 as precursor/supplemental support for the consolidation framing, not as the central memory result.
