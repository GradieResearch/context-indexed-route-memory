# Reproducibility Audit

## Goal

Can a new researcher clone the repo, run key experiments, regenerate metrics, regenerate plots, and reproduce manuscript claims?

## Current Summary

Current status: partially reproducible.

Existing artifacts are present for Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15. Launchers and validation commands have been documented or inspected, but no long experiment reruns were executed in this documentation cleanup pass. Manuscript-critical experiments still need fresh command verification, runtime/hardware logs, seed-level uncertainty tables, and final figure-regeneration scripts before submission.

Exp13.2 is now treated as imported symbolic/algorithmic baseline evidence. Exp14 is now treated as imported symbolic transition-cue context-selection evidence. Exp15 is now treated as imported minimal fixed-profile neural-comparator evidence, with a reconstructed-manifest/empty-SQLite-`run_manifest` caveat.

## Environment

Python version: no formal repository-wide Python version is pinned. Python 3.10+ is recommended for current utility scripts. Exp14 reports Python 3.12.10 in its run metadata. Exp15 records runtime/hardware/library metadata in its reconstructed `run_manifest.json`.

Package installation:

- There is no root-level requirements file.
- Each experiment has its own `requirements.txt` where needed.
- Exp11 requirements: `experiments/experiment11_context_memory/requirements.txt`.
- Exp12 requirements: `experiments/experiment12_capacity_generalization/requirements.txt`.
- Exp13 requirements: `experiments/experiment13_breaking_point/requirements.txt`.
- Exp13.1 requirements: `experiments/experiment13_1_publication_hardening/requirements.txt`.
- Exp14 requirements and launchers are local to `experiments/experiment14_latent_context_inference/`.
- Exp15 requirements and launchers are local to `experiments/experiment15_neural_baseline_comparator/`.

GPU expectations:

- Exp11-Exp14 are table-based or NumPy/Pandas/Matplotlib style workloads, not deep-learning GPU workloads.
- Exp15 is a neural comparator and may use CPU or GPU depending on local environment and launcher arguments.
- Exp13 explicitly documents that it does not require PyTorch, TensorFlow, torchvision, MNIST downloads, or internet access. Source path: `experiments/experiment13_breaking_point/README.md`.
- Exp13.1 documents that it is table-based and CPU-oriented, with no PyTorch or dataset downloads. Source path: `experiments/experiment13_1_publication_hardening/README.md`.
- Exp13.1 full-run manifest records configuration but not explicit device/runtime metadata. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`.
- Exp14 validation reports CPU/device metadata and an explicit CPU-only GPU rationale. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`.
- Exp15 records runtime/hardware metadata in `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`, but the manifest was reconstructed after a final SQLite manifest-write failure.

## Manuscript-Critical Experiments

| Experiment | Directory | Primary launcher | Validation/smoke command | Full/standard command | Expected outputs | Validation/report artifact | Executed in this pass? | Known caveats | GPU/runtime notes | Manifest metadata |
|---|---|---|---|---|---|---|---|---|---|---|
| Exp11 | `experiments/experiment11_context_memory/` | `experiments/experiment11_context_memory/start_exp11.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1 -ValidationOnly` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1` | `experiments/experiment11_context_memory/analysis/exp11_validation/`; `experiments/experiment11_context_memory/analysis/exp11/` | `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md` | No, inspected only. | Uses `-ValidationOnly` rather than `-Profile smoke`; full command runs validation before full run. | Table/NumPy style; no GPU use documented. | No dedicated run manifest found; `runs.csv` and logs exist. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | `experiments/experiment12_capacity_generalization/start_exp12.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile validate -OutDir analysis/exp12_validation` or `-ValidateOnly` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile full -OutDir analysis/exp12` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/`; `experiments/experiment12_capacity_generalization/analysis/exp12/` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md` | No, inspected only. | Profiles are `validate`, `full`, and `custom`, not the later `smoke` / `standard` / `full` convention. | CPU/table-oriented; no GPU use documented. | No dedicated run manifest found; `runs.csv` and `progress.jsonl` exist. |
| Exp13 | `experiments/experiment13_breaking_point/` | `experiments/experiment13_breaking_point/start_exp13.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile smoke -Clean` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile standard -Clean`; `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile full -Clean` | `experiments/experiment13_breaking_point/analysis/metrics.csv`; summary CSVs; `experiments/experiment13_breaking_point/analysis/plots/` | `experiments/experiment13_breaking_point/analysis/exp13_report.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/validation_results.json` | No, inspected only. | Current artifact appears to be a standard/boundary run; holdout metric cleanup remains if C9 is central. | README says no deep-learning stack or internet required. | `runs.csv` exists; no dedicated run manifest found. |
| Exp13.1 | `experiments/experiment13_1_publication_hardening/` | `experiments/experiment13_1_publication_hardening/start_exp13_1_run.ps1`; wrapper scripts for standard/full/validate | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_validate.ps1 -RunId latest` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_standard.ps1`; `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_1_publication_hardening\start_exp13_1_full.ps1` | per-run SQLite under `experiments/experiment13_1_publication_hardening/runs/`; per-run analysis under `experiments/experiment13_1_publication_hardening/analysis/<run_id>/` | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_results.json` | No, inspected only. Existing validation report says PASS 27, WARN 0, FAIL 0. | Targeted lesion diagnostic failed expected positive pattern; do not cite as positive evidence without audit/rerun. | README documents CPU-only/table-based rationale; no GPU use. | `run_manifest.json` exists but lacks explicit device/runtime metadata. |
| Exp13.2 | `experiments/experiment13_2_baseline_suite/` | local Exp13.2 start/run scripts | local validation documented by completed run artifacts | full run `exp13_2_full_20260507_165813` | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/`; `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3` | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md` | No, imported artifacts only. Existing import report says PASS 28, WARN 0, FAIL 0. | Symbolic/algorithmic baselines only; not neural baselines. Oracle context-gated lookup matches CIRM on clean supplied-context benchmark. | Table/algorithmic baseline suite. | `run_manifest.json` exists per import report. |
| Exp14 | `experiments/experiment14_latent_context_inference/` | `start_exp14_run.ps1`; wrappers for smoke/validation/full | `powershell -ExecutionPolicy Bypass -File .\start_exp14_smoke.ps1`; `powershell -ExecutionPolicy Bypass -File .\start_exp14_validation.ps1` from experiment directory | `powershell -ExecutionPolicy Bypass -File .\start_exp14_full.ps1` | per-run SQLite under `experiments/experiment14_latent_context_inference/runs/`; per-run analysis under `experiments/experiment14_latent_context_inference/analysis/<run_id>/` | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md` | No, imported artifacts only. Existing validation report says PASS 27, WARN 0, FAIL 0. | Symbolic transition-cue context selection only; not raw sensory latent-world discovery. Generated plots are not final figures. | CPU-only symbolic/table-based run; no GPU required. | `run_manifest.json` exists and validation confirms device metadata. |
| Exp15 | `experiments/experiment15_neural_baseline_comparator/` | `start_exp15_validation.ps1`; `start_exp15_full.ps1`; Python runner/analysis/validation scripts | `powershell -ExecutionPolicy Bypass -File .\start_exp15_validation.ps1` from experiment directory | `powershell -ExecutionPolicy Bypass -File .\start_exp15_full.ps1` from experiment directory | per-run SQLite under `experiments/experiment15_neural_baseline_comparator/runs/`; per-run analysis under `experiments/experiment15_neural_baseline_comparator/analysis/<run_id>/`; `exp15_summary.csv`; `exp15_seed_metrics.csv`; `exp15_effect_sizes.csv`; `exp15_model_runtime.csv`; diagnostic plots | `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md` | No, imported artifacts only. Existing validation report reports PASS for required artifacts/metrics. | Minimal fixed-profile neural comparator; not exhaustive architecture search. Replay variant requires audit before scientific interpretation. SQLite `run_manifest` table may be empty, and `run_manifest.json` was reconstructed after final SQLite tail failure. | Neural workload; CPU/GPU depends on launcher/device. Runtime rows are available in `exp15_model_runtime.csv`. | Reconstructed `run_manifest.json` exists with explicit provenance caveat. |

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

- Verify Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 commands on a fresh checkout where cited.
- Document runtime, expected outputs, seed counts, and hardware expectations for manuscript-critical runs.
- Add final figure regeneration commands and source-data manifests.
- Add seed-level confidence intervals and effect sizes for core claims.
- Import prior-art/novelty evidence as local source artifacts.
- Decide whether broader neural baselines are required for the intended target venue.
- Keep completed generated outputs immutable and create new run files for reruns.
