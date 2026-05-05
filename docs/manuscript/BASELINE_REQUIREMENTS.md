# Baseline Requirements

Purpose: Track the baselines and controls required before manuscript claims are submission-ready.

Evidence status: planning document only. This file records locally imported thread guidance and is not itself evidence for novelty or baseline performance. The novelty assessment artifact named in the thread as `Pasted text.txt` is not present locally; local verification pending.

## Required Baseline Families

| Baseline family | Local source path | Reason to include | Local status | Caveat |
|---|---|---|---|---|
| Context-dependent gating / XdG-style comparator | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Tests whether supplied context labels and gating alone explain retention. | planned | Thread-derived requirement; no baseline run artifact is present. |
| Synaptic stabilization / SI or stabilization-plus-gating comparator | `docs/threads/experiment12to13_export.md` | Tests whether stabilization without the proposed route-memory structure explains the effect. | planned | Source thread names XdG/SI or stabilization-plus-gating; no local novelty artifact or baseline result is present. |
| Replay comparator | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Tests whether replay-based continual-learning controls match retention and composition. | planned | The local thread names replay but not DER/CLEAR specifically; do not cite those variants until sourced. |
| Task masks / HAT-style comparator | `docs/threads/experiment12to13_export.md` | Tests whether task-mask isolation explains incompatible-world retention. | planned | No implementation or literature citation imported locally in this pass. |
| Parameter isolation / PackNet / PathNet-style comparator | `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` | Tests whether isolated capacity explains retention and composition. | planned | Progressive Nets are not locally source-backed in the reviewed docs; keep them out until sourced. |
| Task-conditioned weights / hypernetwork comparator | `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` | Tests compact context-conditioned storage against the proposed structural route memory. | planned | No hypernetwork baseline artifact is present. |
| Superposition comparator | `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` | Tests whether superposed context-specific weights can reproduce retention/composition behavior. | planned | No superposition baseline artifact is present. |
| Cognitive-map / CSCG / TEM-style comparator | `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` | Tests relation to cloned-state and temporal-map models. | planned | Source is thread-level planning; no local comparison or bibliography is imported. |

## Internal Controls Already Represented

These are internal ablations, not external baselines.

| Control | Local evidence path | Caveat |
|---|---|---|
| No recurrence | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Supports storage/execution dissociation within the benchmark only. |
| No structural plasticity | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Internal ablation; not an external literature comparator. |
| No context binding or no world context | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/validation_report.md` | Exp13 no-context-binding variant definition remains caveated in the conflict log. |
| Capacity or memory-budget controls | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Observed aggregate curves only; fitted capacity-law analysis is pending. |
| Context noise/corruption controls | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv` | Exp13 adversarial corruption is failure evidence; Exp12 bleed/dropout is diagnostic only. |
