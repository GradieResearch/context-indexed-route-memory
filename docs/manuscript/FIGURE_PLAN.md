# Candidate Main Figures

Purpose: Track candidate figures and panels while preserving a source path and caveat for every claim.

The canonical thread-integrated figure entries are below. The older artifact inventory retained later in this file is a convenience list, not the claim-bearing figure plan.

Selected small aggregate tables also have readable mirrors under `docs/source_data/`. Figure source paths below continue to cite the authoritative `experiments/...` artifacts.

## Figure 1 - Conceptual Architecture and Task

Purpose: Define the continual compositional route-memory benchmark and the model decomposition.
Panels: task worlds with incompatible transitions; one-step route table; world/context index; recurrent multi-step execution; evidence-level legend.
Claim supported: Framing for C1-C4, not a result claim.
Source materials: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md`.
Source thread: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Status: Manuscript framing decision.
Caveat: Conceptual figure must not imply biological completeness or latent-world inference.

## Figure 2 - Core Mechanism / Ablation Decomposition

Purpose: Show that structural plasticity, world context, and recurrence play separable roles.
Likely experiments: Exp11, Exp12, Exp13.
Panels: full model; no structural plasticity; no world context; no recurrence; route-table vs composition dissociation.
Claim supported: C1, C2, C3, C4.
Source materials: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
Source thread: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Status: Strong internal evidence.
Caveat: Internal ablations require external baselines before submission.

## Figure 3 - Capacity Scaling and Continual Retention

Purpose: Show clean-context capacity scaling and sequential retention before pushing the system to failure.
Likely experiment: Exp12.
Panels: world-count scaling; route length / held-out composition; continual retention heatmap; wrong-world activation or world margin.
Claim supported: C2, C5, C9 with caveats.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_wrong_world_activation.png`.
Source thread: `docs/threads/experiment12to13_export.md`.
Status: Strong but ceiling-limited.
Caveat: Exp12 context-bleed/dropout curves were judged inconclusive; do not use them as strong robustness evidence.

## Figure 4 - Breaking Point Under Finite Structural Capacity

Purpose: Show the observed finite-budget performance degradation curve.
Likely experiment: Exp13.
Panels: global budget curve; local budget curve; route-table/composition divergence; local damage effect on long-route execution.
Claim supported: C6, C7.
Source materials: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png`.
Source thread: `docs/threads/experiment12to13_export.md`.
Status: C6 promising; C7 preliminary.
Caveat: Docs-only local-vs-global comparison exists; formal paired seed-level comparison and capacity-law fitting remain pending.

## Figure 5 - Consolidation as Stability-Plasticity Bias

Purpose: Reframe consolidation as a retention bias under pressure rather than an essential accuracy mechanism.
Likely experiments: Exp12, Exp13, planned Exp13.1.
Panels: consolidation pressure margin; old-vs-new retention heatmaps; TODO dose-response panel.
Claim supported: C8.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_world_margin.png`; `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`.
Source thread: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Status: Preliminary.
Caveat: Exp13 validation reports only a small consolidation delta; dose-response is P0 follow-up.

## Figure 6 - Held-Out Composition Boundary

Purpose: Separate composition over stored primitives from unseen primitive-transition inference.
Likely experiments: Exp12, Exp13, planned Exp13.1.
Panels: seen-primitives composition; unseen primitive failure; route-table accuracy split TODO.
Claim supported: C9.
Source materials: `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_compositions_from_seen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_routes_requiring_unseen_primitives.png`.
Source thread: `docs/threads/experiment12to13_export.md`.
Status: Needs metric cleanup.
Caveat: Do not describe as broad abstract rule generalization.

## Figure 7 - Context Corruption Failure Boundary

Purpose: Show adversarial context corruption as the main local failure evidence for context selection.
Likely experiment: Exp13.
Panels: adversarial mixture composition; top-1 world accuracy or world margin across mixture level; caveat panel distinguishing diagnostic Exp11/Exp12 noise plots.
Claim supported: C10.
Source materials: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_top1_world.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png`.
Source thread: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.
Status: Promising.
Caveat: Exp13 adversarial corruption is threshold-like; Exp11/Exp12 context bleed/dropout artifacts are supplementary diagnostics only.

## Figure 8 - Continuous / Perceptual Bridge

Purpose: Show that noisy continuous decoding can feed the route-memory mechanism.
Likely experiment: Exp13.
Panels: continuous noise versus decode accuracy; composition accuracy downstream of noisy decoding; caveat that this is not end-to-end perception.
Claim supported: C11.
Source materials: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_composition_vs_noise.png`.
Source thread: `docs/threads/experiment12to13_export.md`.
Status: Preliminary or supplementary.
Caveat: Not a learned perceptual system.

# Candidate Supplementary Figures

| Supplement | Source artifact path | Source thread path | Claim supported | Caveat |
|---|---|---|---|---|
| Exp5 contextual successor failure plots | `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_best_composition_accuracy.png`; `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_context_confusion.png` | `docs/threads/experiment5to10_export.md`; `docs/threads/experiment6_export.md` | Historical motivation for raw route audits | Low accuracy and methodological caveat; historical only. |
| Exp6 route-audit failure plots | `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_best_composition_accuracy.png`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_route_margin.png`; `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_context_confusion.png` | `docs/threads/experiment6_export.md` | Context identity is not route execution | Needs seed/rerun if exact numbers are used. |
| Exp7 diagnostic route-field plots | `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_composition_accuracy.png`; `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_transition_accuracy.png` | `docs/threads/experiment5to10_export.md` | Clean route fields compose recurrently | Diagnostic, not self-organized acquisition. |
| Exp8 acquisition plots | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_composition_accuracy.png`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_route_table.png` | `docs/threads/experiment5to10_export.md` | Local plasticity can acquire route fields | Symbolic task and exposure-curve caveat. |
| Exp9 interference/noise plots | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_composition_by_bleed.png`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_2.png` | `docs/threads/experiment5to10_export.md` | Inhibition/reward mechanisms under stress | Stress-dependent; not required in clean tasks. |
| Exp10 reversal plots | `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_composition.png`; `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_old_rule_retention.png` | `docs/threads/experiment5to10_export.md` | Adaptive rebinding and consolidation tradeoff | Not non-destructive memory. |
| Exp11 context-noise plots | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_world_margin.png`; `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_wrong_world_activation.png` | `docs/threads/experiment11_export` | Supplementary diagnostics only, not C10 failure evidence | No formal slope/confidence interval yet. |
| Exp12 context-noise plots | `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_composition.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_composition.png` | `docs/threads/experiment12to13_export.md` | Supplementary diagnostics only, not C10 failure evidence | Thread judged curves too flat/inconclusive. |
| Exp13 context corruption plots | `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png` | `docs/threads/experiment12to13_export.md` | C10 context selection failure under adversarial evidence | Hard threshold, not stochastic robustness. |

# Pre-Import Figure Sketch And Artifact Inventory

Legacy inventory - claim IDs in this section are not authoritative. Use the canonical entries above for current C1-C12 mapping.

## Figure 1 - Conceptual model
Purpose: Explain the synthetic route-memory benchmark, context-indexed structural route fields, and recurrent traversal.
Panels: task world; one-step route field; context/world indexing; recurrent multi-step execution; ablation map.
Source: Superseded by the canonical Figure 1 entry above; use `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`, `experiments/experiment12_capacity_generalization/README.md`, and `experiments/experiment13_breaking_point/README.md`.
Status: needs manual figure creation.

## Figure 2 - Core mechanism and ablations
Purpose: Show that one-step route memory and multi-step execution separate under recurrence/structural-plasticity ablations.
Candidate experiments: Exp7, Exp8, Exp9, Exp12, Exp13.
Candidate artifacts: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_composition_accuracy.png`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_transition_accuracy.png`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_route_table.png`; `experiments/experiment13_breaking_point/analysis/validation_report.md`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 2 above.
Caveat: Keep benchmark-specific; verify canonical run profile.

## Figure 3 - Capacity scaling and retention
Purpose: Show context-separated memory scaling, retention, and ceiling effects before boundary mapping.
Candidate experiments: Exp11 and Exp12.
Candidate artifacts: `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_route_table_accuracy.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png`; `experiments/experiment11_context_memory/analysis/exp11/exp11_final_sequential_summary.csv`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 3 above.
Caveat: Exp12 full model is at ceiling; Exp13 is needed for breaking points.

## Figure 4 - Breaking point under memory pressure
Purpose: Show finite capacity and route-length pressure as an observed degradation curve.
Candidate experiments: Exp13.
Candidate artifacts: `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 4 above.
Caveat: Docs-only local-vs-global comparison exists; formal paired analysis remains pending.

## Figure 5 - Consolidation / stability-plasticity tradeoff
Purpose: Present consolidation as a bias/tradeoff, not as proven necessity.
Candidate experiments: Exp10, Exp12, Exp13.
Candidate artifacts: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_old_rule_retention.png`; `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_new_rule_composition.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_accuracy.png`; `experiments/experiment13_breaking_point/analysis/validation_report.md`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 5 above.
Caveat: Exp13 validation includes a consolidation WARN with small delta; do not overstate.

## Figure 6 - Held-out composition and primitive holdout boundary
Purpose: Separate held-out composition over seen primitives from unseen primitive-transition inference.
Candidate experiments: Exp12 and Exp13.
Candidate artifacts: `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_compositions_from_seen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_routes_requiring_unseen_primitives.png`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 6 above.
Caveat: Boundary result only; not broad abstract rule generalization.

## Figure 7 - Continuous/perceptual bridge, if retained
Purpose: Present continuous/noisy input decoding as a preliminary bridge.
Candidate experiments: Exp13.
Candidate artifacts: `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_composition_vs_noise.png`; `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
Legacy claim note: claim IDs removed from this pre-import inventory; use canonical Figure 8 above.
Caveat: Does not prove end-to-end perception.

## Pre-Import Supplementary Artifact List

## exp2 - Persistent Plastic Graph MNIST Prototype

- `experiments/experiment2/analysis/test_accuracy.png`
- `experiments/experiment2/analysis/test_average_confidence.png`
- `experiments/experiment2/analysis/train_average_confidence.png`
- `experiments/experiment2/analysis/train_window_accuracy.png`

## exp3 - Persistent Plastic Graph MNIST Experiments

- `experiments/experiment3/analysis/suite/suite_best_accuracy.png`

## exp4 - Successor Traversal

- `experiments/experiment4_successor/analysis/exp4/exp4_best_addition_accuracy.png`
- `experiments/experiment4_successor/analysis/exp4/exp4_recurrent_drive.png`
- `experiments/experiment4_successor/analysis/exp4/exp4_unique_active.png`

## exp5 - Contextual Successor World

- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_mode.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_accuracy_by_path_length.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_adaptation_curve.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_best_composition_accuracy.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_context_confusion.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_recurrent_drive.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_wrong_route_activation.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_mode.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_accuracy_by_path_length.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_adaptation_curve.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_best_composition_accuracy.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_context_confusion.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_recurrent_drive.png`
- `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_wrong_route_activation.png`

## exp6 - Route Audit Successor World

- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_mode.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_accuracy_by_path_length.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_adaptation_curve.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_best_composition_accuracy.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_context_confusion.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_recurrent_drive.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_route_margin.png`
- `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_wrong_route_activation.png`

## exp7 - Route Field Diagnostics

- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_mode.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_accuracy_by_steps.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_composition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_context_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_correct_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_target_rank.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_transition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_accuracy_by_mode.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_accuracy_by_steps.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_composition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_context_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_correct_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_target_rank.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_transition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_accuracy_by_mode.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_accuracy_by_steps.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_composition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_context_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_correct_margin.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_target_rank.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_transition_accuracy.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png`
- `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png`

## exp8 - Self-Organizing Contextual Route Acquisition

- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_mode.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_accuracy_by_steps.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_composition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_context_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_correct_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_composition.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_exposure_curve_route_table.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_failure_taxonomy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_target_rank.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_transition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_minus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_two_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_accuracy_by_mode.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_accuracy_by_steps.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_composition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_context_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_correct_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_exposure_curve_composition.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_exposure_curve_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_exposure_curve_route_table.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_failure_taxonomy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_target_rank.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_transition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_minus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_two_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_accuracy_by_mode.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_accuracy_by_steps.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_composition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_context_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_correct_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_exposure_curve_composition.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_exposure_curve_margin.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_exposure_curve_route_table.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_failure_taxonomy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_target_rank.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_transition_accuracy.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_minus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_one_exp1.png`
- `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/route_margin_heatmap_exp8_full_self_organizing_route_field_seed0_plus_two_exp1.png`

## exp9 - Robust Adaptive Route Plasticity

- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_composition_accuracy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_clean_transition_accuracy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_failure_taxonomy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_composition_noise_delay_4.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_margin_noise_delay_4.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_feedback_route_table_noise_delay_4.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_composition_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_margin_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_route_table_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_wrong_route_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_feedback_exp9_full_reward_robust_minus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_feedback_exp9_full_reward_robust_plus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_feedback_exp9_full_reward_robust_plus_two.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_interference_exp9_full_interference_robust_minus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_interference_exp9_full_interference_robust_plus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/route_margin_heatmap_interference_exp9_full_interference_robust_plus_two.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_clean_composition_accuracy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_clean_transition_accuracy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_failure_taxonomy.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_composition_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_composition_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_margin_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_margin_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_route_table_noise_delay_0.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_feedback_route_table_noise_delay_2.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_interference_composition_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_interference_margin_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_interference_route_table_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_interference_wrong_route_by_bleed.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_feedback_exp9_full_reward_robust_minus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_feedback_exp9_full_reward_robust_plus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_feedback_exp9_full_reward_robust_plus_two.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_interference_exp9_full_interference_robust_minus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_interference_exp9_full_interference_robust_plus_one.png`
- `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/route_margin_heatmap_interference_exp9_full_interference_robust_plus_two.png`

## exp10 - Rule Reversal, Retention, and Adaptive Rebinding

- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_failure_taxonomy_final_new_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_new_rule_composition.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_final_old_rule_retention.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_composition_dual_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_correct_margin_dual_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_composition.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_new_rule_route_table.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_old_rule_retention.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_reversal_route_table_dual_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_failure_taxonomy_final_new_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_new_rule_composition.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_old_rule_retention.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_composition_dual_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_correct_margin_dual_rule.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_new_rule_composition.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_new_rule_route_table.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_old_rule_retention.png`
- `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_reversal_route_table_dual_rule.png`

## exp11 - Context-Separated Memory and Non-Destructive Rebinding

- `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_taxonomy_final_sequential.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_correct_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_bleed_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_bleed_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_bleed_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_dropout_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_dropout_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_dropout_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_failure_taxonomy_final_sequential.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_scaling_final_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_scaling_final_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_scaling_final_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_scaling_final_wrong_world_activation.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_sequential_composition.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_sequential_correct_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_sequential_route_table.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_sequential_world_margin.png`
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_sequential_wrong_world_activation.png`

## exp12 - Capacity, Interference, and Compositional Generalization

- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_composition_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_route_table_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_capacity_wrong_world_activation.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_consolidation_pressure_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_composition.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_bleed_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_composition.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_heldout_generalization_by_length.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_capacity_composition_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_capacity_route_table_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_capacity_wrong_world_activation.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_consolidation_pressure_accuracy.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_consolidation_pressure_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_context_bleed_composition.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_context_bleed_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_context_dropout_composition.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_context_dropout_world_margin.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_continual_retention_heatmap_full_model.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_heldout_generalization_by_length.png`
- `experiments/experiment12_capacity_generalization/analysis/exp12_validation/plots/exp12_route_table_composition_gap.png`

## exp13 - Breaking Point, Context Corruption, and Continuous Front-End Bridge

- `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_1.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_12.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_4.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_accuracy_route_len_8.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_capacity_wrong_world_activation_budget_1.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_top1_world.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_composition.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_top1_world.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_dropout_world_margin.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_uniform_bleed_composition.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_uniform_bleed_top1_world.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_context_uniform_bleed_world_margin.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_composition_vs_noise.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_compositions_from_seen_primitives.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_routes_requiring_unseen_primitives.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.375.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.75.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_1.0.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.375.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_0.75.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_consolidation_budget_1.0.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_world_context_budget_0.375.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_world_context_budget_0.5.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_world_context_budget_0.75.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_no_world_context_budget_1.0.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_strong_consolidation_budget_0.375.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_strong_consolidation_budget_0.5.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_strong_consolidation_budget_0.75.png`
- `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_strong_consolidation_budget_1.0.png`
