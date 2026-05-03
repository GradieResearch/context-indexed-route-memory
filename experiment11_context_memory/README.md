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

## Smoke test recommendation

Before running the full suite, run a tiny all-variant smoke test so every ablation path is exercised:

```powershell
& $Python .\run_exp11_suite.py --output-dir analysis/exp11_smoke --max-number 9 --max-steps 3 --worlds "A B C" --seeds 1 --new-world-exposure-schedule "0 1" --alternation-cycles 1 --alternation-eval-schedule "0 1" --scaling-exposure-repeats 1 --context-bleed-sweep "0" --context-dropout-sweep "0" --force
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
