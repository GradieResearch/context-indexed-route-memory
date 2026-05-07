# Source Data Mirrors

This directory contains small, review-friendly mirrors of selected aggregate evidence tables. They exist so manuscript reviewers can inspect key tables on GitHub even when the authoritative generated experiment CSVs remain in Git LFS.

These files are convenience copies or docs-derived tables, not new experimental outputs. The authoritative source remains the original artifact path in the owning experiment directory. Date copied for Exp12/Exp13 mirrors: 2026-05-05. Date copied for Exp13.1 mirrors: 2026-05-07.

Scope note: Exp13.2 source-data files may exist in this directory from a prior import, but they are intentionally excluded from the current P0/P1 cleanup manifest and should not be used to update claims until the separate Exp13.2 import/alignment pass is completed.

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
| `exp13_1_variant_metrics.csv` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` | direct copy | Exp13.1 variant and core ablation aggregate summary. |
| `exp13_1_context_corruption.csv` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | direct copy | Exp13.1 context corruption aggregate summary. |
| `exp13_1_lesion_metrics.csv` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv` | direct copy | Exp13.1 lesion diagnostic aggregate summary; targeted-lesion positive claim not supported. |
| `exp13_1_budget_consolidation.csv` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | direct copy | Exp13.1 local/global budget and consolidation aggregate summary. |
| `exp13_1_freeze_plasticity.csv` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv` | direct copy | Exp13.1 freeze-plasticity aggregate summary. |

Do not treat these mirrors as a replacement for the original artifacts. When citing evidence, cite the experiment artifact and use the mirror only as a readable convenience copy.

Machine-readable manifests:

- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
