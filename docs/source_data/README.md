# Source Data Mirrors

This directory contains small, review-friendly mirrors of selected aggregate evidence tables. They exist so manuscript reviewers can inspect key tables on GitHub even when the authoritative generated experiment CSVs remain in Git LFS.

These files are convenience copies or docs-derived tables, not new experimental outputs. The authoritative source remains the original artifact path in the owning experiment directory. Date copied: 2026-05-05.

| Mirror file | Source artifact path | Type | Notes |
|---|---|---|---|
| `exp12_capacity_final_summary.csv` | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | direct copy | Exp12 capacity and ablation aggregate summary. |
| `exp12_heldout_generalization_summary.csv` | `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv` | direct copy | Exp12 held-out composition aggregate summary. |
| `exp13_capacity_pressure_summary.csv` | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | direct copy | Exp13 global capacity-pressure aggregate summary. |
| `exp13_context_corruption_summary.csv` | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` | direct copy | Exp13 adversarial context-corruption aggregate summary. |
| `exp13_true_holdout_generalization_summary.csv` | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | direct copy | Exp13 true-holdout aggregate summary. |
| `exp13_continuous_frontend_bridge_summary.csv` | `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | direct copy | Exp13 noisy continuous-front-end bridge aggregate summary. |
| `exp13_local_capacity_pressure_summary.csv` | `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | direct copy | Exp13 local capacity-pressure aggregate summary. |
| `exp13_local_vs_global_budget_comparison.csv` | `docs/experiments/exp13_local_vs_global_budget_comparison.md` plus `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` and `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | derived docs table | CSV form of the docs-only aggregate comparison table; not a paired seed-level analysis. |

Do not treat these mirrors as a replacement for the original artifacts. When citing evidence, cite the experiment artifact and use the mirror only as a readable convenience copy.
