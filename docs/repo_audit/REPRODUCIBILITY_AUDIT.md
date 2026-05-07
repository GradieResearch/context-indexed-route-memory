# Reproducibility Audit

## Goal

Can a new researcher clone the repo, run key experiments, regenerate metrics, regenerate plots, and reproduce manuscript claims?

## Current Summary

Current status: partially reproducible, excluding Exp13.2.

Existing artifacts are present for Exp11, Exp12, Exp13, and Exp13.1. Launchers and validation commands were inspected in this cleanup pass, but no long experiment reruns were executed. Manuscript-critical experiments still need fresh command verification, runtime/hardware logs, seed-level uncertainty tables, and final figure-regeneration scripts before submission.

Exp13.2 is intentionally excluded and deferred to a separate analysis/import/alignment pass.

## Environment

Python version: no formal repository-wide Python version is pinned. Python 3.10+ is recommended for current utility scripts.

Package installation:

- There is no root-level requirements file.
- Each experiment has its own `requirements.txt`.
- Exp11 requirements: `experiments/experiment11_context_memory/requirements.txt`.
- Exp12 requirements: `experiments/experiment12_capacity_generalization/requirements.txt`.
- Exp13 requirements: `experiments/experiment13_breaking_point/requirements.txt`.
- Exp13.1 requirements: `experiments/experiment13_1_publication_hardening/requirements.txt`.

GPU expectations:

- Exp11-Exp13.1 are table-based or NumPy/Pandas/Matplotlib style workloads, not deep-learning GPU workloads.
- Exp13 explicitly documents that it does not require PyTorch, TensorFlow, torchvision, MNIST downloads, or internet access. Source path: `experiments/experiment13_breaking_point/README.md`.
- Exp13.1 documents that it is table-based and CPU-oriented, with no PyTorch or dataset downloads. Source path: `experiments/experiment13_1_publication_hardening/README.md`.
- Exp13.1 full-run manifest records configuration but not explicit device/runtime metadata. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`.

## Manuscript-Critical Experiments

| Experiment | Directory | Primary launcher | Validation/smoke command | Full/standard command | Expected outputs | Validation/report artifact | Executed in this pass? | Known caveats | GPU/runtime notes | Manifest metadata |
|---|---|---|---|---|---|---|---|---|---|---|
| Exp11 | `experiments/experiment11_context_memory/` | `experiments/experiment11_context_memory/start_exp11.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1 -ValidationOnly` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1` | `experiments/experiment11_context_memory/analysis/exp11_validation/`; `experiments/experiment11_context_memory/analysis/exp11/` | `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md` | No, inspected only. | Uses `-ValidationOnly` rather than `-Profile smoke`; full command runs validation before full run. | Table/NumPy style; no GPU use documented. | No dedicated run manifest found; `runs.csv` and logs exist. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | `experiments/experiment12_capacity_generalization/start_exp12.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile validate -OutDir analysis/exp12_validation` or `-ValidateOnly` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile full -OutDir analysis/exp12` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/`; `experiments/experiment12_capacity_generalization/analysis/exp12/` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md` | No, inspected only. | Profiles are `validate`, `full`, and `custom`, not the later `smoke` / `standard` / `full` convention. | CPU/table-oriented; no GPU use documented. | No dedicated run manifest found; `runs.csv` and `progress.jsonl` exist. |
| Exp13 | `experiments/experiment13_breaking_point/` | `experiments/experiment13_breaking_point/start_exp13.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile smoke -Clean` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile standard -Clean`; `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile full -Clean` | `experiments/experiment13_breaking_point/analysis/metrics.csv`; summary CSVs; `experiments/experiment13_breaking_point/analysis/plots/` | `experiments/experiment13_breaking_point/analysis/exp13_report.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/validation_results.json` | No, inspected only. | Current artifact appears to be a standard/boundary run; holdout metric cleanup remains if C9 is central. | README says no deep-learning stack or internet required. | `runs.csv` exists; no dedicated run manifest found. |
| Exp13.1 | `experiments/experiment13_1_publication_hardening/` | `experiments/experiment13_1_publication_hardening/start_exp13_1_run.ps1`; wrapper scripts for standard/full/validate | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_validate.ps1 -RunId latest` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_standard.ps1`; `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_full.ps1` | per-run SQLite under `experiments/experiment13_1_publication_hardening/runs/`; per-run analysis under `experiments/experiment13_1_publication_hardening/analysis/<run_id>/` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_results.json` | No, inspected only. Existing validation report says PASS 27, WARN 0, FAIL 0. | Targeted lesion diagnostic failed expected positive pattern; do not cite as positive evidence without audit/rerun. | README documents CPU-only/table-based rationale; no GPU use. | `run_manifest.json` exists but lacks explicit device/runtime metadata. |

## Historical And Supporting Experiments

Exp1-Exp6 remain historical/exploratory. Exp7-Exp10 are supporting mechanism-building experiments. Their entry points and artifacts are indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`, but this cleanup did not execute their commands or promote them to central evidence.

## Artifact Regeneration

Generated artifacts are preserved in the owning experiment directories as historical records. They should not be overwritten to make documentation tidier.

Final paper figures should eventually be regenerated from scripts with fixed input paths and documented source-data tables. Review-friendly source-data mirrors may exist under `docs/source_data/`, but the original `experiments/...` artifacts remain authoritative unless a future document explicitly says otherwise.

## Utility Checks

Path verification:

```bash
python scripts/verify_doc_source_paths.py
```

Generic seed-summary helper:

```bash
python scripts/compute_seed_metric_summary.py --help
```

The seed-summary helper requires explicit input/output paths and grouping columns. Its output is marked `human_review_required_before_citation`.

## Required Before Manuscript Submission

- Verify Exp11, Exp12, Exp13, and Exp13.1 commands on a fresh checkout.
- Document runtime, expected outputs, seed counts, and hardware expectations for manuscript-critical runs.
- Add final figure regeneration commands and source-data manifests.
- Add seed-level confidence intervals and effect sizes for core claims.
- Complete separate Exp13.2 import/alignment for baselines.
- Keep completed generated outputs immutable and create new run files for reruns.
