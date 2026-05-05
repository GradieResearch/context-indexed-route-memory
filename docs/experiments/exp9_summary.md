# Experiment 9: Robust Adaptive Route Plasticity

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; robustness thread imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Candidate robustness supplement or secondary result after review.

## Purpose

Experiment 8 showed that a local plastic graph can acquire a context-conditioned route field from one-step transition exposure, then use recurrence to compose unseen multi-step paths. Experiment 9 asks the next question: > Can the graph preserve, repair, and adapt those routes when context is unreliable and feedback is imperfect or delayed? This experiment is intentionally still symbolic. The goal is not to make the problem more semantically rich. The goal is to stress the mechanism that Experiment 8 validated. Does inhibition protect context-bound routes when competing context assemblies are partially active? The main stressor is `context_bleed`: a fraction of the wrong mode and wrong sourc

Source path: `experiments/experiment9_robust_adaptive_route_plasticity/EXPERIMENT_9_ROBUST_ADAPTIVE_ROUTE_PLASTICITY.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment9_robust_adaptive_route_plasticity/EXPERIMENT_9_ROBUST_ADAPTIVE_ROUTE_PLASTICITY.md`
- Task/design clue: Experiment 8 showed that a local plastic graph can acquire a context-conditioned route field from one-step transition exposure, then use recurrence to compose unseen multi-step paths. Experiment 9 asks the next question: > Can the graph preserve, repair, and adapt those routes when context is unreliable and feedback is imperfect or delayed? This experiment is intentionally still symbolic. The goal is not to make the problem more semantically rich. The goal is to stress the mechanism that Experiment 8 validated. Does inhibition protect context-bound routes when competing context assemblies are partially active? The main stressor is `context_bleed`: a fraction of the wrong mode and wrong sourc
- Run scripts detected: `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_robust_adaptive_route_plasticity.py`, `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_suite.py`, `experiments/experiment9_robust_adaptive_route_plasticity/start.ps1`, `experiments/experiment9_robust_adaptive_route_plasticity/start.sh`, `experiments/experiment9_robust_adaptive_route_plasticity/start_exp9.ps1`
- Analysis CSVs detected: 18; plot files detected: 41; generated/design reports detected: 4.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment9_robust_adaptive_route_plasticity/EXPERIMENT_9_ROBUST_ADAPTIVE_ROUTE_PLASTICITY.md`: Experiment 8 showed that a local plastic graph can acquire a context-conditioned route field from one-step transition exposure, then use recurrence to compose unseen multi-step paths. Experiment 9 asks the next question: > Can the graph preserve, repair, and adapt those routes when context is unreliable and feedback is imperfect or delayed? This experiment is intentionally still symbolic. The goal is not to make the
- `experiments/experiment9_robust_adaptive_route_plasticity/TRACKER_UPDATE_EXP9.md`: Date: 2026-05-02 Experiment: Exp9 Robust Adaptive Route Plasticity Run names: - exp9_full_interference_robust - exp9_no_inhibition - exp9_no_context_binding - exp9_no_structural_plasticity - exp9_full_reward_robust - exp9_no_reward_gate - exp9_no_eligibility_trace - exp9_no_recurrence Config highlights: Context interference sweep plus feedback noise / delayed reward sweep. Training remains one-step only. Composition
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_report.md`: Experiment 9 stresses the self-organizing route acquisition mechanism discovered in Experiment 8. It asks two questions: whether inhibition protects context-bound routes under interference, and whether reward gating / eligibility traces protect route acquisition under noisy or delayed feedback. - `transition_accuracy`: local one-step route acquisition. - `composition_accuracy`: unseen multi-step recurrent traversal f
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_report.md`: Experiment 9 stresses the self-organizing route acquisition mechanism discovered in Experiment 8. It asks two questions: whether inhibition protects context-bound routes under interference, and whether reward gating / eligibility traces protect route acquisition under noisy or delayed feedback. - `transition_accuracy`: local one-step route acquisition. - `composition_accuracy`: unseen multi-step recurrent traversal f

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp9_full_reward_robust | Reference/full mechanism | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_eligibility_trace | Removes delayed-credit trace | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | comp=0.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | comp=0.0287; route=0.0297; transition=0.0297 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_full_interference_robust | Reference/full mechanism | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | comp=0.0526; route=0.3478; transition=0.3478 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |
| exp9_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | comp=1.0; route=1.0; transition=1.0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| route_table_accuracy | Direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_target_rank | Average rank of the true target. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_correct_margin | Correct target score margin over the strongest wrong target. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_context_margin | Correct context/world support margin over competing contexts/worlds. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| mean_wrong_route_activation | Activation assigned to competing routes. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy_mean | Mean one-step route learning accuracy across seeds/conditions. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_accuracy_mean | Mean multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| route_table_accuracy_mean | Mean direct route-table correctness. | Generated analysis CSV/report | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Clean full reward-robust condition succeeds locally

Claim: The main Exp9 summary reports 1.0 transition, route-table, and composition accuracy for the full reward-robust variant under clean immediate feedback.
Evidence: `exp9_full_reward_robust` at feedback_noise=0.0/reward_delay_steps=0: transition_accuracy_mean=1.0, route_table_accuracy_mean=1.0, composition_accuracy_mean=1.0.
Caveat: Robustness interpretation requires reviewing the full stress grid.
Source path: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`

### Result 2: Noisy delayed feedback lowers full-model composition and exposes ablations

Claim: Under feedback_noise=0.2 and reward_delay_steps=2, the full row degrades and no-eligibility-trace is much lower.
Evidence: Full reward-robust composition_accuracy_mean=0.3677; `exp9_no_eligibility_trace` composition_accuracy_mean=0.0312.
Caveat: This is a local stress-grid observation; causal interpretation needs thread/human review.
Source path: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`

### Result 3: No recurrence again separates route table from composition

Claim: The no-recurrence feedback row keeps route-table accuracy at 1.0 but composition accuracy is 0.0 under clean feedback.
Evidence: `exp9_no_recurrence`: route_table_accuracy_mean=1.0, composition_accuracy_mean=0.0.
Caveat: Same synthetic route-memory benchmark family; avoid broad generalization language.
Source path: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`

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
| `experiments/experiment9_robust_adaptive_route_plasticity/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_robust_adaptive_route_plasticity.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/start_exp9.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/EXPERIMENT_9_ROBUST_ADAPTIVE_ROUTE_PLASTICITY.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/TRACKER_UPDATE_EXP9.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_route_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_transition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_failure_taxonomy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_0.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_2.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_4.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_0.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_2.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_4.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_0.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 41 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp9 clean composition accuracy | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 clean transition accuracy | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_transition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 failure taxonomy | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_failure_taxonomy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback composition noise delay 0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_0.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback composition noise delay 2 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_2.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback composition noise delay 4 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_4.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback margin noise delay 0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_0.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback margin noise delay 2 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_2.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback margin noise delay 4 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_4.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback route table noise delay 0 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_0.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback route table noise delay 2 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_2.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp9 feedback route table noise delay 4 | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_4.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (29) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread says inhibition becomes load-bearing under context interference, and reward/eligibility mechanisms matter under noisy or delayed feedback.
Caveat: Effects are stress-dependent; inhibition is not required in clean deterministic settings.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_report.md`
Status: Promising

## Key results (thread-integrated)

### Result 1: Inhibition protects margins under context bleed

Claim: Exp9 supports inhibition as a stress-dependent route-margin protection mechanism.
Evidence: The thread reports full composition around 0.777 versus no-inhibition around 0.524 at context bleed 0.35, with matching route-table and margin trends.
Caveat: Thread-derived numerical comparison should be checked against the local stress-grid rows before final manuscript use.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_composition_by_bleed.png`
Manuscript status: Promising

### Result 2: Eligibility traces matter under delayed feedback

Claim: Exp9 suggests eligibility traces protect route acquisition when reward is delayed.
Evidence: The thread says the no-eligibility-trace variant collapsed when reward delay was introduced, while the full model remained strong under zero-noise delayed reward.
Caveat: This is a stressor-specific result; do not claim eligibility is always necessary.
Source thread: `docs/threads/experiment5to10_export.md`
Source artifact: `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_2.png`
Manuscript status: Promising

## What this experiment supports (thread-integrated)

- Robustness mechanisms become visible under the right stressors.

## What this experiment does not prove (thread-integrated)

- It does not prove inhibition, reward gating, or eligibility traces are required in clean tasks.

## Follow-up actions (thread-integrated)

- Use Exp9 as a supplementary robustness mechanism result unless the manuscript expands beyond the Exp11-Exp13 spine.
