# P0 Remediation Report

## Summary

This cleanup addressed the two P0 repo-readiness issues without modifying experiment logic, rerunning experiments, deleting generated artifacts, or changing scientific conclusions.

Fixed:

- Active manuscript/evidence/source paths now use the `experiments/...` prefix.
- Documentation/evidence CSVs under `docs/` are staged as normal Git text instead of LFS pointer files.
- `scripts/verify_doc_source_paths.py` now verifies active documentation source paths.
- `AGENTS.md`, `README.md`, and `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` now align with the current `experiments/` repository structure.
- Small review-friendly source-data mirrors were added under `docs/source_data/`.

## Path Migration

Do not cite stale paths such as `experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; this is an old-pattern example, not an active source path.

Current pattern: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`

Active documentation paths were updated in the manuscript docs, synthesis docs, experiment summaries, experiment registry, audit docs, root tracker docs, and selected experiment READMEs. Historical thread export transcripts were left untouched unless they were active index material.

Actual experiment directories detected during remediation:

- `experiments/experiment1/`
- `experiments/experiment2/`
- `experiments/experiment3/`
- `experiments/experiment4_successor/`
- `experiments/experiment5_contextual_successor/`
- `experiments/experiment6_route_audit_successor/`
- `experiments/experiment7_route_field_diagnostics/`
- `experiments/experiment8_self_organizing_route_acquisition/`
- `experiments/experiment9_robust_adaptive_route_plasticity/`
- `experiments/experiment10_adaptive_reversal/`
- `experiments/experiment11_context_memory/`
- `experiments/experiment12_capacity_generalization/`
- `experiments/experiment13_breaking_point/`

Path verifier result: zero missing active paths.

## Git LFS Docs CSV Cleanup

Old `.gitattributes` behavior sent every `*.csv` file to Git LFS, including evidence-critical CSVs under `docs/`.

New `.gitattributes` behavior:

- `*.sqlite3` remains in LFS.
- `experiments/**/runs/**/*.csv` remains in LFS.
- `experiments/**/analysis/**/*.csv` remains in LFS.
- `docs/**/*.csv` is plain text with LF endings.

Docs CSVs migrated out of LFS in the staged index:

- `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv`
- `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`
- `docs/repo_audit/ARTIFACT_INDEX.csv`

Generated experiment CSVs under `experiments/**/analysis/**/*.csv` and `experiments/**/runs/**/*.csv` remain in LFS intentionally.

## Source-Data Mirrors

| Mirror file | Original artifact path | Type | Notes |
|---|---|---|---|
| `docs/source_data/exp12_capacity_final_summary.csv` | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | direct copy | Review-friendly Exp12 capacity aggregate. |
| `docs/source_data/exp12_heldout_generalization_summary.csv` | `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv` | direct copy | Review-friendly Exp12 heldout aggregate. |
| `docs/source_data/exp13_capacity_pressure_summary.csv` | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | direct copy | Review-friendly Exp13 capacity-pressure aggregate. |
| `docs/source_data/exp13_context_corruption_summary.csv` | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` | direct copy | Review-friendly Exp13 context-corruption aggregate. |
| `docs/source_data/exp13_true_holdout_generalization_summary.csv` | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | direct copy | Review-friendly Exp13 true-holdout aggregate. |
| `docs/source_data/exp13_continuous_frontend_bridge_summary.csv` | `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | direct copy | Review-friendly Exp13 continuous-front-end bridge aggregate. |
| `docs/source_data/exp13_local_capacity_pressure_summary.csv` | `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | direct copy | Review-friendly Exp13 local-capacity aggregate. |
| `docs/source_data/exp13_local_vs_global_budget_comparison.csv` | `docs/experiments/exp13_local_vs_global_budget_comparison.md` plus Exp13 global/local capacity summaries | derived docs table | CSV form of the docs-only aggregate comparison; not a paired seed-level analysis. |

The original experiment artifacts remain authoritative.

## Remaining Issues

- Novelty assessment artifact `Pasted text.txt` remains missing/local verification pending.
- Exp13.1 has not been run.
- External baselines are not implemented.
- Statistical hardening and final reproducible figure scripts remain pending.
- Generated experiment CSVs may remain in LFS intentionally.
- Reproducibility commands were discovered but not executed in this audit.

## Verification

Command used:

```bash
python scripts/verify_doc_source_paths.py
```

Result: zero missing active paths. Remaining unresolved paths are explicitly marked planned/future or local verification pending.

Additional checks:

- `git lfs pull` completed before docs CSV migration.
- Staged docs CSV blobs were inspected and contain real CSV content, not Git LFS pointer text.
- `git check-attr` confirms `docs/**/*.csv` resolves to plain text with `eol=lf`, while generated experiment analysis CSVs still resolve to LFS.

## Files Changed

Major files changed:

- `.gitattributes`
- `AGENTS.md`
- `README.md`
- `EXPERIMENT_TRACKER.md`
- `Experiment.md`
- `scripts/verify_doc_source_paths.py`
- `docs/repo_audit/PATH_VERIFICATION_REPORT.md`
- `docs/repo_audit/P0_REMEDIATION_REPORT.md`
- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv`
- `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`
- `docs/repo_audit/ARTIFACT_INDEX.csv`
- `docs/source_data/`

Many additional active docs and experiment summaries received mechanical path-prefix updates from stale experiment-directory paths to `experiments/...` paths.
