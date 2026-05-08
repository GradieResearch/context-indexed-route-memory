# Candidate Main Figures

Purpose: Track candidate figures and panels while preserving a source path and caveat for every claim.

Scope note: Exp13.2 is intentionally excluded from this cleanup pass. Any baseline figure or table is deferred to a separate Exp13.2 import/alignment pass and is not included as a current manuscript-ready panel here.

## Post-Freeze Generated Asset Status

Step 4 manuscript asset generation has produced a reproducible candidate figure/table pipeline.

Build command: `python scripts/manuscript_assets/build_manuscript_assets.py`

Generated asset manifest: `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`

Generation report: `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`

Freeze-document numbering supersedes the older candidate numbering below:

| Freeze figure | Generated file(s) | Source data | Claim(s) | Status | Caveat |
|---|---|---|---|---|---|
| Figure 1 - Conceptual route-memory schematic | `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/figures/figure_01_conceptual_route_memory.svg` | `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv` | C1-C4 framing; C13 boundary wording | Generated candidate schematic | Conceptual only; not empirical evidence. |
| Figure 2 - Structural plasticity and recurrence ablation | `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg` | `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv` | C1-C4 | Generated candidate main figure | Internal symbolic ablation; uncertainty uses aggregate normal approximation. |
| Figure 3 - Clean capacity scaling | `docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/figures/figure_03_capacity_scaling.svg` | `docs/manuscript/source_data/figure_03_capacity_scaling.csv` | C5 | Generated candidate main figure | Ceiling-limited clean supplied-context result; no fitted capacity law. |
| Figure 4 - Finite structural budget/local-global pressure | `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg` | `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv` | C6-C7 | Generated candidate narrow-main/supplement figure | Observed degradation curve only; paired seed-level local/global inference remains deferred. |
| Figure 5 - Symbolic context selection from transition cues | `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/figures/figure_05_symbolic_context_selection.svg` | `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv` | C13 | Generated candidate main-or-supplement figure | Symbolic transition-cue selection only; oracle remains an upper bound. |

Generated manuscript tables:

| Table | File(s) | Role | Caveat |
|---|---|---|---|
| Table 1 - Claim evidence | `docs/manuscript/tables/table_01_claim_evidence.csv`; `docs/manuscript/tables/table_01_claim_evidence.md` | Frozen-claim evidence map for C1-C7, C13, and C12 discussion posture. | Headline values require human caption/prose review. |
| Table 2 - Run integrity | `docs/manuscript/tables/table_02_run_integrity.csv`; `docs/manuscript/tables/table_02_run_integrity.md` | Run/source provenance for manuscript-relevant artifacts. | Older Exp11/Exp12 layouts lack validation JSON and SQLite manifests. |
| Table 3 - Statistical summary | `docs/manuscript/tables/table_03_statistical_summary.csv`; `docs/manuscript/tables/table_03_statistical_summary.md` | Figure and baseline statistical source table. | Effect-size grouping still needs human review before exact manuscript citation. |

Exp13.2 baseline evidence is generated as `docs/manuscript/source_data/table_exp13_2_symbolic_baseline_suite.csv` and the manuscript tables above, rather than as a main Figure 4, because `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` assigns Figure 4 to finite structural budget/local-vs-global pressure.

## Figure 1 - Conceptual Architecture and Task

Purpose: Define the continual compositional route-memory benchmark and the model decomposition.
Panels: task worlds with incompatible transitions; one-step route table; world/context index; recurrent multi-step execution; evidence-level legend.
Claim supported: Framing for C1-C4, not a result claim.
Source materials: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md`.
Status: Manuscript framing decision.
Caveat: Conceptual figure must not imply biological completeness, novelty of context gating alone, or latent-world inference.

## Figure 2 - Core Mechanism / Ablation Decomposition

Purpose: Show that structural plasticity, world context, and recurrence play separable roles.
Likely experiments: Exp11, Exp12, Exp13, Exp13.1.
Claim supported: C1, C2, C3, C4.
Source materials: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_recurrence_ablation.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_composition_accuracy.png`.
Status: Strong internal evidence.
Caveat: Internal ablations require external baselines before submission.

## Figure 3 - Capacity Scaling and Continual Retention

Purpose: Show clean-context capacity scaling and sequential retention before pushing the system to failure.
Likely experiment: Exp12.
Claim supported: C2, C5, C9 with caveats.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_wrong_world_activation.png`.
Status: Strong but ceiling-limited.
Caveat: Exp12 context-bleed/dropout curves were judged inconclusive; do not use them as strong robustness evidence.

## Figure 4 - Breaking Point Under Finite Structural Capacity

Purpose: Show the observed finite-budget performance degradation curve.
Likely experiment: Exp13 and Exp13.1.
Claim supported: C6, C7.
Source materials: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_budget_consolidation.png`.
Status: Promising internal evidence.
Caveat: Seed-level confidence intervals, final figure scripts, and capacity-law fitting remain pending.

## Figure 5 - Consolidation as Stability-Plasticity Bias

Purpose: Reframe consolidation as a retention/stability bias under pressure rather than an essential accuracy mechanism.
Likely experiments: Exp12, Exp13, Exp13.1.
Claim supported: C8.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_world_margin.png`; `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv`.
Status: Preliminary.
Caveat: Exp13.1 did not show an accuracy rescue from consolidation strength; keep as a caveated stability-plasticity bias.

## Figure 6 - Held-Out Composition Boundary

Purpose: Separate composition over stored primitives from unseen primitive-transition inference.
Likely experiments: Exp12 and Exp13.
Claim supported: C9.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_compositions_from_seen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_routes_requiring_unseen_primitives.png`.
Status: Needs metric cleanup.
Caveat: Do not describe as broad abstract rule generalization.

## Figure 7 - Context Corruption Failure Boundary

Purpose: Show adversarial/wrong-world context corruption as the main local failure evidence for context selection.
Likely experiment: Exp13 and Exp13.1.
Claim supported: C10.
Source materials: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_top1_world.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_context_confusion.png`.
Status: Promising for wrong-world/context-identity sensitivity.
Caveat: Not generic stochastic robustness; Exp13.1 dropout/bleed did not reduce composition.

## Figure 8 - Continuous / Perceptual Bridge

Purpose: Show that a decoded noisy continuous input can feed the route-memory mechanism.
Likely experiment: Exp13.
Claim supported: C11.
Source materials: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_composition_vs_noise.png`.
Status: Preliminary or supplementary.
Caveat: Not end-to-end perception or learned visual representation.

## Figure 9 - Latent Symbolic Context Inference

Purpose: Show that the active world/context can be inferred from partial symbolic transition cues before route execution.
Likely experiment: Exp14.
Claim supported: C13, with implications for C2 and C10 wording.
Source materials: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_world_selection_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_seen_composition_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_selection_sensitivity.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_composition_sensitivity.png`.
Status: Candidate manuscript panel or supplement; final rendering pending.
Caveat: Generated analysis plots are not final figures. This supports symbolic transition-cue selection, not raw sensory latent-world discovery, and the oracle context-gated table remains an upper bound.

## Deferred Baseline Figure

Claim: Baseline figure/table planning is required, but intentionally deferred.
Evidence: C12 remains `Needs baseline` in this pass.
Caveat: Do not create a baseline-results figure or table from Exp13.2 until the separate Exp13.2 import/alignment pass is complete.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`

## Final-Figure Readiness

| Figure | Claims supported | Authoritative source paths | Source-data mirror exists | Final script exists | Current plot status | Caveat | Required action |
|---|---|---|---|---|---|---|---|
| Figure 1 - Conceptual Architecture and Task | C1-C4 framing | `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md` | not applicable | no | not generated | Must not imply latent context inference or biological proof. | Create manuscript illustration with explicit non-claim legend. |
| Figure 2 - Core Mechanism / Ablation Decomposition | C1-C4 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` | yes, partial: `docs/source_data/SOURCE_DATA_MANIFEST.csv` | no | exploratory/generated analysis output | Internal ablations only; uncertainty missing. | Build final panel script from selected CSVs and add CI/effect-size table. |
| Figure 3 - Capacity Scaling and Continual Retention | C2, C5, C9 | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv` | yes | no | exploratory/generated analysis output | Ceiling-limited; context-noise plots inconclusive. | Select panels, add source-data table, and generate final script. |
| Figure 4 - Breaking Point Under Finite Structural Capacity | C6, C7 | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | yes | no | exploratory/generated analysis output | Capacity-law fitting and seed-level intervals missing. | Add paired local/global analysis and final plotting script. |
| Figure 5 - Consolidation as Stability-Plasticity Bias | C8 | `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv` | yes, partial | no | exploratory/generated analysis output | Preliminary; no accuracy-rescue claim. | Decide whether main or supplementary; add uncertainty before central use. |
| Figure 6 - Held-Out Composition Boundary | C9 | `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | yes | no | exploratory/generated analysis output | Seen/unseen route-table cleanup needed. | Keep supplementary or add metric cleanup before central use. |
| Figure 7 - Context Corruption Failure Boundary | C10 | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | yes | no | exploratory/generated analysis output | Wrong-world sensitivity only; not stochastic robustness. | Add stochastic corruption if claiming robustness. |
| Figure 8 - Continuous / Perceptual Bridge | C11 | `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | yes | no | exploratory/generated analysis output | Preliminary bridge, not perception. | Keep supplementary unless a stronger applied bridge is built. |
| Figure 9 - Latent Symbolic Context Inference | C13 | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_world_selection_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_seen_composition_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_selection_sensitivity.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_composition_sensitivity.png` | no | no | generated analysis output; candidate panel/supplement | Symbolic cues only; oracle upper bound remains; final rendering pending. | Decide main vs supplement, create final plotting script, and add source-data mirror if retained. |
| Deferred baseline table/figure | C12 | deferred to separate Exp13.2 pass | not reviewed in this pass | no | deferred | Baseline blocker remains active here. | Complete Exp13.2 import/alignment separately. |
