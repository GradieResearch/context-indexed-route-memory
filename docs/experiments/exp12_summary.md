# Experiment 12: Capacity, Interference, and Compositional Generalization

## Evidence status

- Local artifacts indexed: yes
- Local artifacts checked for key claims: partial
- Thread digest imported: yes; Exp12 result/design threads imported
- Human/manuscript validation pending: yes
- Claims fully validated for publication: no

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`
- Manuscript relevance: Candidate main/supplement capacity and generalization result; ceiling-effect caveat.

## Purpose

Experiment 12 extends Experiment 11 from a successful context-separated memory demonstration into a paper-facing stress test. The experiment asks four questions: 1. **Capacity:** how many incompatible route worlds can the model retain? 2. **Continual retention:** after each new world is learned, do previous worlds remain accessible? 3. **Compositional generalization:** after training only one-step transitions, can recurrence execute held-out multi-step routes? 4. **Context robustness:** what happens when world context is noisy, blended, or partially dropped out? 5. **Consolidation pressure:** is consolidation actually useful under heavier capacity/noise pressure, or merely optional in the ea

Source path: `experiments/experiment12_capacity_generalization/README.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment12_capacity_generalization/README.md`
- Task/design clue: Experiment 12 extends Experiment 11 from a successful context-separated memory demonstration into a paper-facing stress test. The experiment asks four questions: 1. **Capacity:** how many incompatible route worlds can the model retain? 2. **Continual retention:** after each new world is learned, do previous worlds remain accessible? 3. **Compositional generalization:** after training only one-step transitions, can recurrence execute held-out multi-step routes? 4. **Context robustness:** what happens when world context is noisy, blended, or partially dropped out? 5. **Consolidation pressure:** is consolidation actually useful under heavier capacity/noise pressure, or merely optional in the ea
- Run scripts detected: `experiments/experiment12_capacity_generalization/start_exp12.ps1`
- Analysis CSVs detected: 18; plot files detected: 24; generated/design reports detected: 3.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment12_capacity_generalization/HANDOFF.md`: A complete local experiment package for Experiment 12: - `experiment12.py` - main experiment runner. - `start_exp12.ps1` - PowerShell launcher for Windows. - `requirements.txt` - minimal dependencies. - `README.md` - design, expected behavior, outputs, and run instructions. - `analysis/exp12_validation/` - completed validation pass outputs. Command executed: Validation profile: - seeds: `2` - world counts: `2, 4` - r
- `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md`: Experiment 12 stress-tests the Experiment 11 mechanism by scaling the number of incompatible worlds, measuring continual retention after each new world, testing held-out multi-step compositions, and sweeping world-context noise plus consolidation strength. - profile: `full` - seeds: `30` - world counts: `[2, 4, 8, 16, 32]` - route lengths: `[1, 2, 4, 8, 12]` - nodes: `32` - modes: `3` - variants: `['exp12_full_contex
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`: Experiment 12 stress-tests the Experiment 11 mechanism by scaling the number of incompatible worlds, measuring continual retention after each new world, testing held-out multi-step compositions, and sweeping world-context noise plus consolidation strength. - profile: `validate` - seeds: `2` - world counts: `[2, 4]` - route lengths: `[1, 2, 4]` - nodes: `16` - modes: `3` - variants: `['exp12_full_context_separated_mem

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp12_full_context_separated_memory | Reference/full mechanism | TODO: import intended expectation from thread digest | final comp=1.0; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_no_consolidation | Removes consolidation | TODO: import intended expectation from thread digest | final comp=1.0; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | final comp=1.0; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | final comp=0.0535; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | final comp=0.0363; final route=0.0323 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_no_world_context | Removes context or world indexing | TODO: import intended expectation from thread digest | final comp=0.5194; final route=0.5134 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_strong_consolidation | Raises consolidation strength | TODO: import intended expectation from thread digest | final comp=1.0; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |
| exp12_world_gated_plasticity | Restricts plastic updates by world | TODO: import intended expectation from thread digest | final comp=1.0; final route=1.0 | `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| composition_accuracy_mean | Mean multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| route_route_table_accuracy_mean | Mean route-table correctness in summary files. | Generated analysis CSV/report | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_route_gap_mean | Route table accuracy minus composition accuracy, or reported composition-route gap. | Generated analysis CSV/report | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| composition_accuracy | Multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy | One-step route learning accuracy. | Generated analysis CSV/report | `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Full context-separated memory remains at ceiling through 32 worlds locally

Claim: The Exp12 final memory index reports full-model final composition and route-table accuracy of 1.0 at world_count=32.
Evidence: `exp12_full_context_separated_memory`, world_count=32: final_composition_accuracy=1.0, final_route_table_accuracy=1.0.
Caveat: Ceiling effects limit mechanism discrimination; Exp13 was designed to map breaking points.
Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md`

### Result 2: No recurrence keeps route memory but loses multi-step execution at scale

Claim: The no-recurrence row at 32 worlds has route-table accuracy 1.0 but low composition accuracy.
Evidence: `exp12_no_recurrence`, world_count=32: final_route_table_accuracy=1.0, final_composition_accuracy=0.0566.
Caveat: Route-table/composition split is local to this benchmark family.
Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv`

### Result 3: No structural plasticity and no world context degrade capacity summaries

Claim: At 32 worlds, no-structural-plasticity is near zero and no-world-context is far below the full model.
Evidence: `exp12_no_structural_plasticity`: final_composition_accuracy=0.0376; `exp12_no_world_context`: final_composition_accuracy=0.0706.
Caveat: No-world-context behavior varies with world count; avoid overstating complete failure.
Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv`

### Result 4: Held-out multistep compositions remain at ceiling for full model in Exp12

Claim: The held-out generalization summary reports 1.0 composition accuracy for full model at 32 worlds and route length 12.
Evidence: `exp12_full_context_separated_memory`, world_count=32, route_length=12: composition_accuracy_mean=1.0, route_route_table_accuracy_mean=1.0.
Caveat: This uses seen primitive transitions; Exp13 separately tests primitive holdout.
Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`

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
| `experiments/experiment12_capacity_generalization/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/start_exp12.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/HANDOFF.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/context_dropout_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/continual_retention_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12_validation/capacity_final_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12_validation/consolidation_pressure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12_validation/context_bleed_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12_validation/context_dropout_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_route_table_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_wrong_world_activation.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 24 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp12 capacity composition accuracy | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 capacity route table accuracy | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_route_table_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 capacity wrong world activation | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_wrong_world_activation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 consolidation pressure accuracy | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 consolidation pressure world margin | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 context bleed composition | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 context bleed world margin | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 context dropout composition | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 context dropout world margin | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 continual retention heatmap full model | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 heldout generalization by length | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_heldout_generalization_by_length.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp12 route table composition gap | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (12) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment11_export`

Completed result / design / caveat / decision: Design decision and validation smoke test.
Evidence: The thread designed Exp12 to test many-world capacity, continual retention, held-out composition, context bleed/dropout, and consolidation pressure; validation was explicitly only a smoke test.
Caveat: Do not treat the two-seed validation run as final evidence.
Source thread: `docs/threads/experiment11_export`
Related local artifact path: `experiments/experiment12_capacity_generalization/HANDOFF.md`; `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`
Status: Design only

### Analysis source: `docs/threads/experiment12to13_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread says Exp12 full context-separated memory scales cleanly to 32 worlds; no-recurrence preserves route table but fails composition; no-structural-plasticity stays near chance; no-world-context declines as worlds accumulate.
Caveat: Context-bleed/dropout sweeps were considered too flat or inconclusive, and "generalization" should mean held-out multi-step execution over learned primitives.
Source thread: `docs/threads/experiment12to13_export.md`
Related local artifact path: `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`
Status: Strong

## Key results (thread-integrated)

### Result 1: Clean capacity scaling to 32 worlds

Claim: Exp12 full context-separated memory preserves perfect composition and route-table accuracy through 32 incompatible worlds under clean context.
Evidence: Capacity summary shows `exp12_full_context_separated_memory` composition and route-table accuracy 1.0 at world counts 2, 4, 8, 16, and 32.
Caveat: Ceiling result; Exp13 is needed for breaking-point analysis.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png`
Manuscript status: Strong

### Result 2: No-recurrence reproduces the route-table/composition gap

Claim: Exp12 confirms that one-step route storage and multi-step execution dissociate.
Evidence: `exp12_no_recurrence` route-table accuracy remains 1.0 across world counts while composition stays around 0.05-0.06.
Caveat: Internal symbolic ablation; external baselines required.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`
Manuscript status: Strong

### Result 3: No-world-context collapses as worlds accumulate

Claim: Exp12 supports world/context indexing as necessary for incompatible route-world retention under scaling.
Evidence: Thread reports no-world-context composition dropping from about 0.519 at 2 worlds to about 0.071 at 32 worlds; local capacity summary contains the same pattern.
Caveat: Needs external comparison to known context-gating methods.
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`
Manuscript status: Strong

### Result 4: Held-out composition is over learned primitives

Claim: Exp12 supports held-out multi-step execution over stored one-step transitions, not inference of unseen primitive transitions.
Evidence: The thread cites `heldout_generalization_summary.csv` and the heldout-by-length plot; local summary shows full model at ceiling for held-out multistep paths.
Caveat: The safer wording is "held-out compositional execution over learned one-step transitions."
Source thread: `docs/threads/experiment12to13_export.md`
Source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_heldout_generalization_by_length.png`
Manuscript status: Promising

## What this experiment supports (thread-integrated)

- Clean context scaling and continued route execution up to the tested world counts.
- Strong recurrence and structural-plasticity ablation story.

## What this experiment does not prove (thread-integrated)

- It does not establish a fitted capacity law because it is mostly at ceiling.
- It does not prove graded context-noise robustness.
- It does not prove unseen primitive inference.

## Follow-up actions (thread-integrated)

- Use Exp13 for boundary claims.
- Treat context-bleed/dropout artifacts as diagnostic until stochastic corruption is added.
