# Experiment 9 — Robust Adaptive Route Plasticity

This directory contains Experiment 9, the robustness follow-up to Experiment 8.

Experiment 8 established that a local plastic graph can acquire a clean context-conditioned route field from one-step transition examples and compose it recurrently. Experiment 9 now stresses that mechanism using context interference, noisy feedback, and delayed feedback.

## Run

PowerShell:

```powershell
.\start.ps1
```

The script uses a virtual environment one directory up:

```powershell
..\.venv\Scripts\python.exe
```

Bash:

```bash
./start.sh
```

## Outputs

The default run writes:

```text
runs/exp9_robust_adaptive_route_plasticity.sqlite3
analysis/exp9/
```

Upload `analysis/exp9/` for review, especially:

- `exp9_report.md`
- `exp9_summary.csv`
- `exp9_route_summary.csv`
- `predictions.csv`
- `route_diagnostics.csv`
- generated PNGs

## Main scripts

- `run_exp9_suite.py`: executes the experiment suite.
- `analyze_exp9_suite.py`: generates CSV summaries, plots, and report.
- `exp9/core.py`: model, task generation, route learning, and diagnostics.
