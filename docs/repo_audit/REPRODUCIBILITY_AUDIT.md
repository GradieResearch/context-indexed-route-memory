# Reproducibility Audit

## Goal

Can a new researcher clone the repo, run key experiments, regenerate metrics, regenerate plots, and reproduce manuscript claims?

## Current status

Initial status: partially reproducible from local scripts and existing artifacts, but not yet manuscript-ready. This pass indexed discovered commands and outputs without executing experiments or validating regenerated results.

## Experiment run commands found

| Experiment | Command/script | Profile options | Expected outputs | Validation command | Notes |
| --- | --- | --- | --- | --- | --- |
| exp1 | `python ./experiments/experiment1/run_mnist_experiment.py` | TODO: inspect script options | `experiments/experiment1/runs/` | TODO | Discovered but not executed in this audit. |
| exp1 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment1/start.ps1` | TODO: inspect script options | `experiments/experiment1/runs/` | TODO | Discovered but not executed in this audit. |
| exp1 | `bash ./experiments/experiment1/start.sh` | TODO: inspect script options | `experiments/experiment1/runs/` | TODO | Discovered but not executed in this audit. |
| exp2 | `python ./experiments/experiment2/run_mnist_experiment.py` | TODO: inspect script options | `experiments/experiment2/analysis/`, `experiments/experiment2/runs/` | TODO | Discovered but not executed in this audit. |
| exp2 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment2/start.ps1` | TODO: inspect script options | `experiments/experiment2/analysis/`, `experiments/experiment2/runs/` | TODO | Discovered but not executed in this audit. |
| exp2 | `bash ./experiments/experiment2/start.sh` | TODO: inspect script options | `experiments/experiment2/analysis/`, `experiments/experiment2/runs/` | TODO | Discovered but not executed in this audit. |
| exp3 | `python ./experiments/experiment3/run_experiment_suite.py` | TODO: inspect script options | `experiments/experiment3/analysis/`, `experiments/experiment3/runs/` | TODO | Discovered but not executed in this audit. |
| exp3 | `python ./experiments/experiment3/run_mnist_experiment.py` | TODO: inspect script options | `experiments/experiment3/analysis/`, `experiments/experiment3/runs/` | TODO | Discovered but not executed in this audit. |
| exp3 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment3/start.ps1` | TODO: inspect script options | `experiments/experiment3/analysis/`, `experiments/experiment3/runs/` | TODO | Discovered but not executed in this audit. |
| exp3 | `bash ./experiments/experiment3/start.sh` | TODO: inspect script options | `experiments/experiment3/analysis/`, `experiments/experiment3/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `python ./experiments/experiment4_successor/run_exp4_successor_experiment.py` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `python ./experiments/experiment4_successor/run_exp4_suite.py` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `python ./experiments/experiment4_successor/run_experiment_suite.py` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `python ./experiments/experiment4_successor/run_mnist_experiment.py` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment4_successor/start.ps1` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp4 | `bash ./experiments/experiment4_successor/start.sh` | TODO: inspect script options | `experiments/experiment4_successor/analysis/`, `experiments/experiment4_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp5 | `python ./experiments/experiment5_contextual_successor/run_exp5_contextual_successor.py` | TODO: inspect script options | `experiments/experiment5_contextual_successor/analysis/`, `experiments/experiment5_contextual_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp5 | `python ./experiments/experiment5_contextual_successor/run_exp5_suite.py` | TODO: inspect script options | `experiments/experiment5_contextual_successor/analysis/`, `experiments/experiment5_contextual_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp5 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment5_contextual_successor/start.ps1` | TODO: inspect script options | `experiments/experiment5_contextual_successor/analysis/`, `experiments/experiment5_contextual_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp5 | `bash ./experiments/experiment5_contextual_successor/start.sh` | TODO: inspect script options | `experiments/experiment5_contextual_successor/analysis/`, `experiments/experiment5_contextual_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp6 | `python ./experiments/experiment6_route_audit_successor/run_exp6_route_audit_successor.py` | TODO: inspect script options | `experiments/experiment6_route_audit_successor/analysis/`, `experiments/experiment6_route_audit_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp6 | `python ./experiments/experiment6_route_audit_successor/run_exp6_suite.py` | TODO: inspect script options | `experiments/experiment6_route_audit_successor/analysis/`, `experiments/experiment6_route_audit_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp6 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment6_route_audit_successor/start.ps1` | TODO: inspect script options | `experiments/experiment6_route_audit_successor/analysis/`, `experiments/experiment6_route_audit_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp6 | `bash ./experiments/experiment6_route_audit_successor/start.sh` | TODO: inspect script options | `experiments/experiment6_route_audit_successor/analysis/`, `experiments/experiment6_route_audit_successor/runs/` | TODO | Discovered but not executed in this audit. |
| exp7 | `python ./experiments/experiment7_route_field_diagnostics/run_exp7_route_field_diagnostics.py` | TODO: inspect script options | `experiments/experiment7_route_field_diagnostics/analysis/`, `experiments/experiment7_route_field_diagnostics/runs/` | TODO | Discovered but not executed in this audit. |
| exp7 | `python ./experiments/experiment7_route_field_diagnostics/run_exp7_suite.py` | TODO: inspect script options | `experiments/experiment7_route_field_diagnostics/analysis/`, `experiments/experiment7_route_field_diagnostics/runs/` | TODO | Discovered but not executed in this audit. |
| exp7 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment7_route_field_diagnostics/start.ps1` | TODO: inspect script options | `experiments/experiment7_route_field_diagnostics/analysis/`, `experiments/experiment7_route_field_diagnostics/runs/` | TODO | Discovered but not executed in this audit. |
| exp7 | `bash ./experiments/experiment7_route_field_diagnostics/start.sh` | TODO: inspect script options | `experiments/experiment7_route_field_diagnostics/analysis/`, `experiments/experiment7_route_field_diagnostics/runs/` | TODO | Discovered but not executed in this audit. |
| exp8 | `python ./experiments/experiment8_self_organizing_route_acquisition/run_exp8_self_organizing_route_acquisition.py` | TODO: inspect script options | `experiments/experiment8_self_organizing_route_acquisition/analysis/`, `experiments/experiment8_self_organizing_route_acquisition/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp8 | `python ./experiments/experiment8_self_organizing_route_acquisition/run_exp8_suite.py` | TODO: inspect script options | `experiments/experiment8_self_organizing_route_acquisition/analysis/`, `experiments/experiment8_self_organizing_route_acquisition/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp8 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment8_self_organizing_route_acquisition/start.ps1` | TODO: inspect script options | `experiments/experiment8_self_organizing_route_acquisition/analysis/`, `experiments/experiment8_self_organizing_route_acquisition/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp8 | `bash ./experiments/experiment8_self_organizing_route_acquisition/start.sh` | TODO: inspect script options | `experiments/experiment8_self_organizing_route_acquisition/analysis/`, `experiments/experiment8_self_organizing_route_acquisition/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp8 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment8_self_organizing_route_acquisition/start_exp8.ps1` | TODO: inspect script options | `experiments/experiment8_self_organizing_route_acquisition/analysis/`, `experiments/experiment8_self_organizing_route_acquisition/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp9 | `python ./experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_robust_adaptive_route_plasticity.py` | TODO: inspect script options | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/`, `experiments/experiment9_robust_adaptive_route_plasticity/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp9 | `python ./experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_suite.py` | TODO: inspect script options | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/`, `experiments/experiment9_robust_adaptive_route_plasticity/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp9 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment9_robust_adaptive_route_plasticity/start.ps1` | TODO: inspect script options | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/`, `experiments/experiment9_robust_adaptive_route_plasticity/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp9 | `bash ./experiments/experiment9_robust_adaptive_route_plasticity/start.sh` | TODO: inspect script options | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/`, `experiments/experiment9_robust_adaptive_route_plasticity/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp9 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment9_robust_adaptive_route_plasticity/start_exp9.ps1` | TODO: inspect script options | `experiments/experiment9_robust_adaptive_route_plasticity/analysis/`, `experiments/experiment9_robust_adaptive_route_plasticity/runs/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp10 | `python ./experiments/experiment10_adaptive_reversal/run_exp10_adaptive_reversal.py` | TODO: inspect script options | `experiments/experiment10_adaptive_reversal/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp10 | `python ./experiments/experiment10_adaptive_reversal/run_exp10_suite.py` | TODO: inspect script options | `experiments/experiment10_adaptive_reversal/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp10 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment10_adaptive_reversal/start.ps1` | TODO: inspect script options | `experiments/experiment10_adaptive_reversal/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp10 | `bash ./experiments/experiment10_adaptive_reversal/start.sh` | TODO: inspect script options | `experiments/experiment10_adaptive_reversal/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp10 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment10_adaptive_reversal/start_exp10.ps1` | TODO: inspect script options | `experiments/experiment10_adaptive_reversal/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp11 | `python ./experiments/experiment11_context_memory/run_exp11_context_memory.py` | TODO: inspect script options | `experiments/experiment11_context_memory/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp11 | `python ./experiments/experiment11_context_memory/run_exp11_suite.py` | TODO: inspect script options | `experiments/experiment11_context_memory/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp11 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment11_context_memory/start.ps1` | TODO: inspect script options | `experiments/experiment11_context_memory/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp11 | `bash ./experiments/experiment11_context_memory/start.sh` | TODO: inspect script options | `experiments/experiment11_context_memory/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp11 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment11_context_memory/start_exp11.ps1` | ValidationOnly switch; SkipDependencyInstall switch | `experiments/experiment11_context_memory/analysis/` | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment11_context_memory/start_exp11.ps1 -ValidationOnly` | Discovered but not executed in this audit. |
| exp12 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment12_capacity_generalization/start_exp12.ps1` | full, validate, custom | `experiments/experiment12_capacity_generalization/analysis/` | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment12_capacity_generalization/start_exp12.ps1 -Profile validate` | Discovered but not executed in this audit. |
| exp13 | `python ./experiments/experiment13_breaking_point/run_experiment13.py` | TODO: inspect script options | `experiments/experiment13_breaking_point/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |
| exp13 | `powershell -ExecutionPolicy Bypass -File ./experiments/experiment13_breaking_point/start_exp13.ps1` | smoke, standard, full | `experiments/experiment13_breaking_point/analysis/` | TODO: validation outputs exist; command not confirmed | Discovered but not executed in this audit. |

## Missing reproducibility items

- Standard run interface is inconsistent across experiments. Source path: launcher scripts indexed above.
- Validation commands are not uniformly documented. Source path: `docs/repo_audit/MISSING_ARTIFACTS.md`.
- Per-run database immutability is visible in several `runs/` folders but not yet audited against every launcher. Source path: `docs/repo_audit/ARTIFACT_INDEX.csv`.
- Environment/GPU expectations need a single documented path. Source path: `check_gpu_status.py`.

## Recommended standard run interface

Propose a consistent pattern, for example:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp<N>.ps1 -Profile smoke -Clean
powershell -ExecutionPolicy Bypass -File .\start_exp<N>.ps1 -Profile standard -Clean
powershell -ExecutionPolicy Bypass -File .\start_exp<N>.ps1 -Profile full -Clean
```

## Required before manuscript submission

- Confirm exact run and validation commands for every experiment used in the manuscript.
- Document expected runtime, GPU usage, seeds, and output paths.
- Verify that completed runs write separate immutable SQLite files where applicable.
- Add smoke/standard/full profiles for manuscript-critical experiments or document why unavailable.
