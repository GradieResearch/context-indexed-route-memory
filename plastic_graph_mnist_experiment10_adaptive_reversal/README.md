# Experiment 10 — Adaptive Reversal

This package runs Experiment 10 for the Biological Neural Nets project.

The experiment trains a self-organizing contextual route field on rule set A, reverses mode meanings into rule set B, and evaluates whether the graph adapts, forgets, retains, or contextually separates the two rules.

## Run

PowerShell:

```powershell
.\start.ps1
```

Bash:

```bash
./start.sh
```

By default, `start.ps1` uses the shared virtual environment one directory up:

```powershell
..\.venv\Scripts\python.exe
```

## Outputs

Results are written to:

```text
analysis/exp10/
```

Most important files:

```text
exp10_report.md
exp10_summary.csv
exp10_route_summary.csv
metrics_wide.csv
route_diagnostics.csv
failure_taxonomy.csv
exp10_reversal_*.png
exp10_switchback_*.png
route_margin_heatmap_*.png
```

The suite intentionally does **not** save full per-task predictions by default. Use `--save-predictions` only for forensic debugging, because the file can become large.
