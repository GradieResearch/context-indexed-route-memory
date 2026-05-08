# Experiment 15 Summary: Minimal Neural Baseline Comparator

Status: **completed minimal neural comparator import**.

This document summarizes the imported Experiment 15 full run. Treat it as minimal fixed-profile neural comparator evidence, not exhaustive neural benchmarking.

## Purpose

Experiment 15 implements a minimal neural baseline comparator for the Context-Indexed Route Memory manuscript.

The experiment asks whether ordinary neural sequence models trained under matched symbolic route-memory conditions reproduce, fail, or partially reproduce the same storage, context separation, retention, and compositional execution behavior observed in CIRM.

## Implementation and imported run

Implementation directory:

```text
experiments/experiment15_neural_baseline_comparator/
```

Implementation files:

- `experiments/experiment15_neural_baseline_comparator/README.md`
- `experiments/experiment15_neural_baseline_comparator/run_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/analyze_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/validate_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/start_exp15_validation.ps1`
- `experiments/experiment15_neural_baseline_comparator/start_exp15_full.ps1`

## Baseline variants

The implementation includes:

- GRU endpoint model with context;
- GRU endpoint model without context;
- GRU rollout model with context;
- GRU rollout model without context;
- small attention/Transformer-style endpoint model with context;
- one-step transition MLP with context;
- one-step transition MLP without context;
- sequential-world replay transition MLP;
- parameter-isolated transition MLP with world-specific heads.

The optional neural key-value / memory-augmented lookup baseline is intentionally omitted for scope control.

Imported run:

```text
run_id: exp15_full_20260508_092811
profile: full
analysis: experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/
sqlite: experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3
```

Validation status: PASS, with 42 PASS, 0 WARN, and 0 FAIL checks.

## Metrics

Generated metrics:

- one-step transition accuracy;
- seen-route composition accuracy;
- suffix-route composition accuracy;
- first-step context-conflict accuracy;
- retention after sequential worlds;
- route-length scaling;
- world-count scaling;
- runtime/training cost;
- seed-level summaries suitable for confidence intervals and effect sizes.

## Local artifacts

The imported full run contains:

```text
experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/
  validation_report.md
  validation_results.json
  run_manifest.json
  exp15_config.json
  progress.jsonl
  metrics.csv
  exp15_seed_metrics.csv
  exp15_summary.csv
  exp15_effect_sizes.csv
  exp15_model_runtime.csv
  exp15_report.md
  experiment_report.md
  plots/
    exp15_seen_vs_suffix_composition.png
    exp15_context_conflict_accuracy.png
    exp15_retention_after_sequential_worlds.png
    exp15_route_length_scaling.png
    exp15_world_count_scaling.png
experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3
```

## How to run locally

From the experiment directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_validation.ps1
```

If validation passes:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_full.ps1
```

## Result summary

Claim -> Exp15 completed a minimal neural comparator over 10 seeds, 9 variants, world counts 2, 8, 16, and 32, and route lengths 4, 8, and 12.
Evidence -> The validation report passes and the imported CSVs contain 5,400 seed metric rows, 540 summary rows, and 1,080 runtime rows.
Caveat -> The run manifest was reconstructed after a final SQLite manifest-write failure. The SQLite database is present, but local verification found its `run_manifest` table empty; use CSV artifacts as authoritative unless a later audit says otherwise.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_model_runtime.csv`.

Claim -> Exp15 narrows manuscript wording rather than supporting broad neural-superiority claims.
Evidence -> At the hard slice `world_count=32`, `route_length=12`, context-conditioned transition MLP and world-head transition MLP variants reach 1.0000 on all hard-slice metrics, while endpoint GRU/Transformer variants show seen-route/endpoint behavior that does not fully transfer to suffix composition or transition accuracy.
Caveat -> Exp15 is not an architecture search, uses fixed small hyperparameters, omits memory-augmented/key-value neural baselines, and treats the replay variant as requiring audit before interpretation.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_report.md`.
