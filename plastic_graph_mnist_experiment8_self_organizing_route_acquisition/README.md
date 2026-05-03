# Experiment 8 - Self-Organizing Contextual Route Acquisition

This directory contains the bridge experiment after Experiment 7.

Experiment 7 showed that if a clean context-conditioned route field exists, recurrence can compose it. Experiment 8 asks whether a local plastic graph can acquire that route field from one-step transition experience, then generalize to unseen multi-step traversal.

## Layout

```text
plastic_graph_mnist_experiment8_self_organizing_route_acquisition/
  exp8/
    core.py
  run_exp8_suite.py
  run_exp8_self_organizing_route_acquisition.py
  analyze_exp8_suite.py
  EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md
  README.md
  requirements.txt
  start_exp8.cmd
  start_exp8.ps1
  start.ps1
  start.sh
```

## Quick validation

```powershell
..\.venv\Scripts\python.exe .\run_exp8_suite.py `
  --max-number 12 `
  --max-steps 4 `
  --transition-train-repeats 1 `
  --seeds 3 `
  --hidden-units 1024 `
  --number-assembly-size 32 `
  --mode-assembly-size 12 `
  --pair-assembly-size 24 `
  --force
```

## Main local run

```powershell
.\start_exp8.cmd
```

If PowerShell blocks `start_exp8.ps1` because the file is not digitally signed, use the `.cmd` launcher above. It starts PowerShell for this run only with `-ExecutionPolicy Bypass`, which avoids changing the machine-wide policy.

If you specifically want to run the PowerShell script directly, either of these also works:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp8.ps1
Unblock-File .\start_exp8.ps1
```

Outputs are written to:

```text
runs/exp8_self_organizing_route_acquisition.sqlite3
analysis/exp8/
```

The important files to upload back for analysis are:

```text
analysis/exp8/exp8_report.md
analysis/exp8/exp8_summary.csv
analysis/exp8/exp8_route_summary.csv
analysis/exp8/exp8_baseline_summary.csv
analysis/exp8/predictions.csv
analysis/exp8/route_diagnostics.csv
analysis/exp8/*.png
```
