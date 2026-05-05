# Results Storyboard

Purpose: Define a conservative first manuscript results sequence. Each block uses Claim -> Evidence -> Caveat -> Source path discipline.

## 1. Define the continual compositional route-memory problem

Claim: The manuscript studies a symbolic benchmark where incompatible local transition systems must be stored, selected by world/context, and executed as multi-step routes.
Experiments: Exp5-Exp13.
Primary artifacts: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md`.
Thread sources: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Caveats: Synthetic symbolic benchmark; not a full perceptual or biological task.
Figure candidate: Figure 1.
Manuscript status: Strong framing, but baseline context still required.

## 2. Show the full model can store incompatible route worlds

Claim: Full context-separated memory and world-gated variants retain old A while acquiring B in Exp11.
Experiments: Exp11.
Primary artifacts: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md`.
Thread sources: `docs/threads/experiment11_export`.
Caveats: Oracle world labels are supplied; synthetic task; external baselines absent.
Figure candidate: Figure 2 or Figure 3.
Manuscript status: Strong internal evidence.

## 3. Ablate structural plasticity, world context, and recurrence

Claim: The core mechanism decomposes into structural storage, world/context separation, and recurrent execution.
Experiments: Exp8, Exp11, Exp12, Exp13.
Primary artifacts: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
Thread sources: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Caveats: Internal ablations do not replace external baselines.
Figure candidate: Figure 2.
Manuscript status: Strong within benchmark.

## 4. Show route-table memory and composition dissociate

Claim: One-step route-table memory can remain intact while multi-step execution fails without recurrence.
Experiments: Exp7, Exp8, Exp11, Exp12, Exp13.
Primary artifacts: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
Thread sources: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Caveats: Does not imply recurrence is novel by itself.
Figure candidate: Figure 2.
Manuscript status: Strong.

## 5. Scale world count and route length

Claim: Under clean context and full capacity, Exp12 remains at ceiling through 32 worlds and route lengths up to 12.
Experiments: Exp12.
Primary artifacts: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`.
Thread sources: `docs/threads/experiment12to13_export.md`.
Caveats: Ceiling effects mean this does not establish a fitted capacity law; Exp13 is needed.
Figure candidate: Figure 3.
Manuscript status: Strong but caveated.

## 6. Show continual retention across sequential worlds

Claim: Continual retention can be visualized as world retention over learning checkpoints in the context-separated setting.
Experiments: Exp12, Exp13.
Primary artifacts: `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_continual_retention_heatmap_full_model.png`; `experiments/experiment13_breaking_point/analysis/continual_retention_pressure_summary.csv`.
Thread sources: `docs/threads/experiment12to13_export.md`.
Caveats: Exp13 retention interpretation for consolidation is still preliminary.
Figure candidate: Figure 3 or Figure 5.
Manuscript status: Promising.

## 7. Push model to failure under capacity pressure

Claim: Finite structural budget creates an observed performance degradation curve, and local budget pressure appears especially damaging for long routes.
Experiments: Exp13.
Primary artifacts: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_budget_breaking_curve_full_vs_consolidation.png`.
Thread sources: `docs/threads/experiment12to13_export.md`.
Caveats: Capacity-law fitting and formal paired local-vs-global confidence intervals are still required.
Figure candidate: Figure 4.
Manuscript status: C6 promising; C7 preliminary.

## 8. Explain consolidation as a stability-plasticity bias

Claim: Consolidation is not essential in easy/full-capacity regimes but may bias retention under finite pressure.
Experiments: Exp10, Exp11, Exp12, Exp13.
Primary artifacts: `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`.
Thread sources: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Caveats: Exp13 validation reports a small consolidation delta; dose-response is required.
Figure candidate: Figure 5.
Manuscript status: Preliminary.

## 9. Clarify generalization boundary

Claim: The model composes stored primitives but does not infer unseen primitive transitions.
Experiments: Exp12, Exp13.
Primary artifacts: `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
Thread sources: `docs/threads/experiment12to13_export.md`.
Caveats: Holdout metrics need seen/unseen/all route-table split.
Figure candidate: Figure 6.
Manuscript status: Needs metric cleanup.

## 10. Show adversarial context-corruption failure boundary

Claim: Adversarial context corruption can collapse route execution when world selection flips to the wrong context.
Experiments: Exp13.
Primary artifacts: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_composition.png`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png`.
Thread sources: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.
Caveats: Exp11/Exp12 context-noise artifacts are supplementary diagnostics only; stochastic/graded corruption remains required.
Figure candidate: Figure 7.
Manuscript status: Promising.

## 11. Show preliminary continuous-input bridge

Claim: A noisy continuous decoder can feed the route-memory mechanism, with downstream composition degrading as decode noise increases.
Experiments: Exp13.
Primary artifacts: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_continuous_frontend_decode_vs_noise.png`.
Thread sources: `docs/threads/experiment12to13_export.md`.
Caveats: Not end-to-end perception.
Figure candidate: Figure 8 or supplement.
Manuscript status: Preliminary.

## 12. State limitations and baseline requirements

Claim: The manuscript is not submission-ready until external baselines, metric cleanup, and statistical hardening are complete.
Experiments: All core experiments; Exp13.1 planned.
Primary artifacts: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; local verification pending for the missing novelty assessment artifact.
Thread sources: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Caveats: `docs/manuscript/BASELINE_REQUIREMENTS.md` is planning only; the novelty assessment source artifact is not local.
Figure candidate: none; Discussion and limitations.
Manuscript status: Needs baseline.
