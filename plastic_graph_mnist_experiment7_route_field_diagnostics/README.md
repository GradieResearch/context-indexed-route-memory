# Experiment 7 - Route Field Diagnostics

This directory contains the isolated implementation for Experiment 7.

Experiment 7 is a diagnostic follow-up to the contextual successor work. It tests whether contextual traversal failures come from local transition learning, recurrent composition, context binding, route contamination, or structural plasticity.

See [`EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md`](EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md) for the full design.

## Layout

```text
plastic_graph_mnist_experiment7_route_field_diagnostics/
  exp7/
    __init__.py
    core.py
  run_exp7_suite.py
  analyze_exp7_suite.py
  EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md
  README.md
  requirements.txt
  start.ps1
  start.sh
  runs/
  analysis/exp7/
```

## Quick start

PowerShell:

```powershell
.\start.ps1
```

Bash:

```bash
./start.sh
```

The PowerShell script intentionally uses the virtual environment one directory above this experiment folder:

```text
..\.venv\Scripts\python.exe
```

## Manual run

```bash
python run_exp7_suite.py \
  --max-number 11 \
  --max-steps 3 \
  --train-repeats 40 \
  --path-train-repeats 2 \
  --seeds 5 \
  --force

python analyze_exp7_suite.py \
  --db runs/exp7_route_field_diagnostics.sqlite3 \
  --output-dir analysis/exp7
```

## Main outputs

```text
runs/exp7_route_field_diagnostics.sqlite3
analysis/exp7/exp7_report.md
analysis/exp7/exp7_summary.csv
analysis/exp7/exp7_route_summary.csv
analysis/exp7/exp7_baseline_summary.csv
analysis/exp7/*.png
```

## Interpretation

Start with `analysis/exp7/exp7_report.md`.

The most important comparison is:

```text
full route field
vs no recurrence
vs no context binding
vs no structural plasticity
```

The key diagnostic is not just accuracy. Look at:

```text
mean_target_rank
mean_correct_margin
mean_context_margin
mean_wrong_route_activation
```

These metrics tell us whether the correct route is dominant, merely nearby, or not represented at all.
