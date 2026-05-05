# Experiment 13: Breaking Point, Context Corruption, and Continuous Front-End Bridge

## Evidence status

- Local artifacts indexed: yes
- Local artifacts checked for key claims: partial
- Thread digest imported: yes; Exp13 result and hardening-plan thread imported
- Human/manuscript validation pending: yes
- Claims fully validated for publication: no

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment12to13_export.md`
- Manuscript relevance: Candidate main boundary-mapping result after review.

## Purpose

Experiment 13 is designed as the first serious **boundary-mapping** experiment after Experiment 12. Experiment 12 showed that the current mechanism can remain saturated at perfect accuracy across many incompatible worlds. That was important, but a manuscript cannot rely only on ceiling effects. Experiment 13 deliberately pushes the model into regimes where it should fail. The purpose is to make the first manuscript harder to attack: 1. show where the full mechanism succeeds; 2. show where it breaks; 3. show that ablations fail for specific, mechanistically interpretable reasons; 4. separate memory composition from true unseen-transition inference; 5. bridge from symbolic route tables into a

Source path: `experiments/experiment13_breaking_point/README.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment13_breaking_point/README.md`
- Task/design clue: Experiment 13 is designed as the first serious **boundary-mapping** experiment after Experiment 12. Experiment 12 showed that the current mechanism can remain saturated at perfect accuracy across many incompatible worlds. That was important, but a manuscript cannot rely only on ceiling effects. Experiment 13 deliberately pushes the model into regimes where it should fail. The purpose is to make the first manuscript harder to attack: 1. show where the full mechanism succeeds; 2. show where it breaks; 3. show that ablations fail for specific, mechanistically interpretable reasons; 4. separate memory composition from true unseen-transition inference; 5. bridge from symbolic route tables into a
- Run scripts detected: `experiments/experiment13_breaking_point/run_experiment13.py`, `experiments/experiment13_breaking_point/start_exp13.ps1`
- Analysis CSVs detected: 8; plot files detected: 36; generated/design reports detected: 3.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment13_breaking_point/analysis/exp13_report.md`: Experiment 13 deliberately pushes the Experiment 12 mechanism out of the ceiling regime. It asks where context-indexed structural route memory breaks when memory capacity, context integrity, primitive transition coverage, and perceptual input quality are degraded. - profile: `standard` - seeds: `5` - nodes: `32` - modes: `3` - capacity world counts: `[4, 8, 16, 32]` - capacity route lengths: `[1, 4, 8, 12]` - global
- `experiments/experiment13_breaking_point/analysis/validation_report.md`: Found phases: ['capacity_pressure', 'context_corruption', 'continual_retention_pressure', 'continuous_frontend_bridge', 'local_capacity_pressure', 'true_holdout_generalization'] mean=1.0000 low=0.3939, exact=1.0000 route_table=1.0000, multi_comp=0.0427 no_world_context=0.0694, full=1.0000 low=1.0000, high=0.0000 seen=0.8924, unseen=0.0747 low=1.0000, high=0.3841 no_consolidation=0.7661, strong=0.7676, delta=0.0016 -
- `experiments/experiment13_breaking_point/analysis/validation_report.md`: Found phases: ['capacity_pressure', 'context_corruption', 'continual_retention_pressure', 'continuous_frontend_bridge', 'local_capacity_pressure', 'true_holdout_generalization'] mean=1.0000 low=0.3939, exact=1.0000 route_table=1.0000, multi_comp=0.0427 no_world_context=0.0694, full=1.0000 low=1.0000, high=0.0000 seen=0.8924, unseen=0.0747 low=1.0000, high=0.3841 no_consolidation=0.7661, strong=0.7676, delta=0.0016 -

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp13_full_context_separated_memory | Reference/full mechanism | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_world_gated_plasticity | Restricts plastic updates by world | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_no_consolidation | Removes consolidation | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_strong_consolidation | Raises consolidation strength | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_no_world_context | Removes context or world indexing | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | configuration indexed in runs.csv | `experiments/experiment13_breaking_point/analysis/runs.csv` |
| exp13_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | near-chance route-table and composition in capacity-pressure summary | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| composition_accuracy_mean | Mean multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| route_route_table_accuracy_mean | Mean route-table correctness in summary files. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_route_gap_mean | Route table accuracy minus composition accuracy, or reported composition-route gap. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| top1_world_accuracy_mean | Top-1 world selection accuracy. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_accuracy | Multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/metrics.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy | One-step route learning accuracy. | Generated analysis CSV/report | `experiments/experiment13_breaking_point/analysis/metrics.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Finite memory pressure creates an observed degradation curve

Claim: Exp13 validation and capacity summaries report perfect composition at exact budget and lower composition under low budget.
Evidence: Validation report states exact=1.0000 and low=0.3939. For world_count=32, route_length=12: budget_ratio=1.0 composition_accuracy_mean=1.0; budget_ratio=0.25 composition_accuracy_mean=0.2755.
Caveat: Validation PASS language is local to this generated validation script; manuscript claims still need review.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

### Result 2: Local budget pressure is visibly harsher for long routes in the local summary

Claim: The local-capacity summary shows very low composition at local_budget_ratio=0.25 for route_length=12.
Evidence: `exp13_full_context_separated_memory`, world_count=32, route_length=12, local_budget_ratio=0.25: composition_accuracy_mean=0.0417, route_route_table_accuracy_mean=0.2721.
Caveat: A formal local-vs-global comparison still needs a reviewed analysis table; keep this as preliminary.
Source path: `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`

### Result 3: Primitive holdout separates composition over seen primitives from unseen primitive transitions

Claim: The validation report explicitly marks primitive holdout as PASS and reports seen=0.8924, unseen=0.0747.
Evidence: CSV examples: compositions_from_seen_primitives route_length=8 composition_accuracy_mean=1.0; routes_requiring_unseen_primitives at primitive_holdout_rate=0.1 composition_accuracy_mean=0.1143.
Caveat: This is a boundary result, not broad abstract rule generalization.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`

### Result 4: Continuous front-end bridge degrades under noise

Claim: The validation report marks continuous front-end degradation under perceptual noise as PASS.
Evidence: Validation report states low=1.0000 and high=0.3841; the full-model summary row at continuous_noise=1.0 has composition_accuracy_mean=0.3471.
Caveat: Preliminary bridge only; does not prove end-to-end perception.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`

## What this experiment supports

- Local evidence summarized above; final supported-claim language must be imported into `docs/manuscript/CLAIMS_AND_EVIDENCE.md` after human/thread review.

## What this experiment does not prove

- Does not establish novelty by itself.
- Does not remove the need for baseline and reproducibility review.

## Known implementation or interpretation caveats

- Thread digest imported. Local artifacts have been partially checked for key claims. Manuscript-level validation and external baseline comparison remain pending.
- Check run profile, seeds, and aggregation before manuscript use.

## Artifacts

| Path | Type | Description | Manuscript relevance | Notes |
| --- | --- | --- | --- | --- |
| `experiments/experiment13_breaking_point/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/run_experiment13.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/start_exp13.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/exp13_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/validation_report.md` | validation | Generated report | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/continual_retention_pressure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_1.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_4.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_8.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_wrong_world_activation_budget_1.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_top1_world.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 36 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp13 budget breaking curve full vs consolidation | `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 capacity accuracy route len 1 | `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_1.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 capacity accuracy route len 12 | `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 capacity accuracy route len 4 | `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_4.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 capacity accuracy route len 8 | `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_8.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 capacity wrong world activation budget 1 | `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_wrong_world_activation_budget_1.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context adversarial mixture composition | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context adversarial mixture top1 world | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_top1_world.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context adversarial mixture world margin | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context dropout composition | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context dropout top1 world | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_top1_world.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp13 context dropout world margin | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (24) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment12to13_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread analyzes Exp13 global/local capacity pressure, recurrence dissociation, consolidation retention asymmetry, adversarial context corruption, true primitive holdout, and continuous/noisy bridge.
Caveat: The same thread identifies major hardening needs: no-context-binding was not a pure ablation, holdout metrics were confusing, context corruption used a hard threshold, external baselines are missing, and consolidation needs dose-response.
Source thread: `docs/threads/experiment12to13_export.md`
Related local artifact path: `experiments/experiment13_breaking_point/analysis/exp13_report.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md`
Status: Promising

## Key results (thread-integrated)

### Result 1: Global budget pressure creates an observed degradation curve

Claim: Under global memory pressure, Exp13 degrades below exact capacity and recovers at exact/surplus capacity.
Evidence: Local capacity summary for full model at 32 worlds and route length 12 rises from composition about 0.276 at budget 0.25 to 1.0 at budgets 1.0 and 1.25.
Caveat: Capacity-law fitting and confidence intervals remain required.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`
Manuscript status: Promising

### Result 2: Local budget pressure appears to damage long-route execution more than global pressure

Claim: Local structural budget pressure appears more damaging to long-route composition than global pressure in the aggregate Exp13 summaries.
Evidence: At 32 worlds and route length 12, the docs-only comparison table reports local budget 0.75 route-table about 0.757 and composition about 0.138, while the matched global budget 0.75 row has composition about 0.758.
Caveat: The comparison table is aggregate-only; formal paired seed-level comparison and confidence intervals remain required.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`
Manuscript status: Preliminary

### Result 3: No-recurrence storage/execution dissociation replicates

Claim: Exp13 confirms recurrence is required for multi-step execution even when one-step route memory is intact.
Evidence: Local exact-capacity no-recurrence at 32 worlds and route length 12 has route-table accuracy 1.0 and composition about 0.0449.
Caveat: Symbolic benchmark; external recurrent baselines needed.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`
Manuscript status: Strong

### Result 4: Consolidation is a preliminary stability-plasticity bias

Claim: Exp13 suggests consolidation can bias which worlds survive under finite sequential capacity.
Evidence: Thread analysis cites retention heatmaps for full/consolidated versus no-consolidation at budget 0.5.
Caveat: Local validation reports only a small finite-pressure consolidation delta; dose-response is required.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`
Manuscript status: Preliminary

### Result 5: Context corruption has a hard selection threshold

Claim: Exp13 adversarial context corruption fails when wrong-world evidence dominates.
Evidence: Local context corruption summary shows composition/top-1 world accuracy 1.0 through positive world margins and collapse to about 0.032 composition with top-1 world 0.0 when the margin becomes negative.
Caveat: This is deterministic threshold-like corruption, not realistic stochastic noise.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`
Manuscript status: Promising

### Result 6: Seen primitive composition and unseen primitive inference separate

Claim: Exp13 shows the model composes seen primitives but does not infer unseen primitive transitions.
Evidence: Local true-holdout summary shows one-step unseen primitive composition near chance while compositions from seen primitives remain high until severe holdout.
Caveat: Route-table all/seen/unseen metric split is required.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`
Manuscript status: Needs metric cleanup

### Result 7: Continuous/noisy bridge is preliminary

Claim: Exp13 shows noisy continuous decoding can feed route memory, with downstream composition degrading as noise increases.
Evidence: Local continuous bridge summary shows full-model composition 1.0 at noise 0.0 and about 0.347 at noise 1.0.
Caveat: Not end-to-end perception.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`
Manuscript status: Preliminary

### Result 8: No structural plasticity remains near chance in capacity-pressure data

Claim: Exp13 capacity-pressure data include a no-structural-plasticity variant with near-chance route-table formation and composition.
Evidence: At 32 worlds and route length 12, `exp13_no_structural_plasticity` has route-table accuracy about 0.030 and composition about 0.035 across the reported budget ratios.
Caveat: This claim is supported by `capacity_pressure_summary.csv`; the Exp13 validation report does not mention no-structural-plasticity and should not be cited for this subclaim.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`
Manuscript status: Strong internal ablation evidence

## What this experiment supports (thread-integrated)

- Boundary mapping under finite capacity.
- Route-table/execution dissociation under pressure.
- Generalization boundary between seen primitives and unseen transitions.
- Preliminary continuous-input compatibility.

## What this experiment does not prove (thread-integrated)

- It does not prove a clean no-context-binding ablation.
- It does not prove consolidation is essential.
- It does not prove stochastic context-noise robustness.
- It does not prove end-to-end perception or unseen primitive inference.

## Follow-up actions (thread-integrated)

- Run Exp13.1 as a new top-level publication-hardening experiment.
- Add external baselines before submission.
- Add metric cleanup and capacity-law summaries.
