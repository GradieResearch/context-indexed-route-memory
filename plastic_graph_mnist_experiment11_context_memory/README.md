# Experiment 11 — Context-Separated Memory and Non-Destructive Rebinding

Experiment 11 tests whether higher-order world context can separate multiple learned route systems over the same symbolic substrate.

It follows the result of Experiment 10: rule reversal works, but the ordinary same-context reversal mostly overwrites old routes. Experiment 11 asks whether explicit world context can allow new rule worlds to be learned without destroying old ones.

## Core question

Can the graph learn:

```text
world_A + plus_one  -> n + 1
world_B + plus_one  -> n - 1
world_C + plus_one  -> n + 2
...
```

while keeping all worlds retrievable through their context?

## Main phases

- `sequential`: train world A, then train world B, evaluating both worlds during B learning.
- `alternating`: train A/B in alternating cycles and evaluate stability.
- `scaling`: sequentially add A/B/C/D and measure memory capacity.
- `context_noise`: train A/B, then corrupt retrieval context using world-context bleed/dropout.

## Logging

The runner writes detailed progress to:

```text
analysis/exp11/exp11_run.log
analysis/exp11/progress.jsonl
```

It also prints progress to the console, including seed, variant, phase, job counts, and elapsed time per job.

## Raw predictions

Raw per-task predictions are disabled by default to avoid huge files. To enable them, add:

```powershell
--save-predictions
```

## Local run

Use `start.ps1`. It expects the shared virtual environment one directory up:

```powershell
..\.venv\Scripts\python.exe
```

## Outputs to upload for analysis

Upload the contents of:

```text
analysis/exp11/
```

Important files:

```text
exp11_report.md
exp11_summary.csv
exp11_memory_indices.csv
metrics_wide.csv
route_diagnostics.csv
failure_taxonomy.csv
exp11_*.png
exp11_run.log
```
