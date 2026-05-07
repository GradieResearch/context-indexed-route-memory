# Experiment 13.2: Baseline Suite

This is a self-contained successor experiment for the Context-Indexed Route Memory manuscript.

## Why this experiment is next

After Experiment 13.1, the repository state identifies external baselines as a required manuscript blocker. The Exp13.1 lesion audit remains important only if route-critical lesion evidence will be cited, but baseline comparison is required regardless. Experiment 13.2 therefore implements a baseline suite rather than another conceptual expansion.

## Scientific purpose

Experiment 13.2 compares the Context-Indexed Route Memory mechanism against simpler baseline families on the same symbolic route-composition benchmark.

The goal is **not** to claim that CIRM beats an oracle lookup table. A context-gated table should solve a clean symbolic table task. The goal is to determine which simpler explanations account for which parts of the observed behavior:

- no-context shared lookup tests whether context/world indexing is required;
- context-gated lookup tests whether explicit gating alone can solve the clean benchmark;
- route-endpoint memorization tests whether seen-route memorization explains composition;
- suffix-route probes test whether reusable one-step primitives support unseen composed queries;
- recurrent non-plastic rules test whether recurrence alone is sufficient;
- superposition/hash lookup tests compact context-conditioned storage with collisions;
- bounded replay/LRU and parameter-isolation tables test conventional continual-learning controls under finite capacity.

## Experiment directory

Expected repository path:

```text
experiments/experiment13_2_baseline_suite/
```

## Run profiles

| Profile | Purpose | Seeds | World counts | Route lengths | Use first |
|---|---:|---:|---:|---:|---|
| `smoke` | Fast command/artifact check | 2 | 4 | 4, 8 | Yes |
| `validation` | Medium sanity run | 5 | 4, 8 | 4, 8 | After smoke |
| `full` | Manuscript-facing baseline run | 20 | 4, 8, 16, 32 | 4, 8, 12, 16 | After validation passes |

## How to run on Windows PowerShell

From this experiment directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_2_smoke.ps1
powershell -ExecutionPolicy Bypass -File .\start_exp13_2_validation.ps1
powershell -ExecutionPolicy Bypass -File .\start_exp13_2_full.ps1
```

Each start script runs the experiment and then validates the generated artifacts.

## Python-only usage

```bash
python run_exp13_2_baseline_suite.py --profile smoke
python validate_exp13_2.py --analysis-root analysis
```

## Output layout

Each run writes a new run directory:

```text
analysis/<run_id>/
  exp13_2_metrics.csv
  metrics.csv
  exp13_2_summary.csv
  exp13_2_effect_sizes.csv
  exp13_2_baseline_metrics.csv
  exp13_2_report.md
  experiment_report.md
  run_manifest.json
  progress.jsonl
  validation_report.md
  validation_results.json
  plots/
    exp13_2_seen_route_composition_accuracy.png
    exp13_2_suffix_generalization_accuracy.png
    exp13_2_route_table_accuracy.png
    exp13_2_first_step_context_accuracy.png
    exp13_2_capacity_pressure.png
    exp13_2_sequential_retention.png
runs/<run_id>.sqlite3
```

## Progress logging

The runner writes structured JSONL progress events to:

```text
analysis/<run_id>/progress.jsonl
```

Console output includes:

- phase name;
- completed units;
- total units;
- percent complete;
- elapsed time;
- units per second;
- ETA.

The manifest includes CPU/device metadata and an explicit note that this symbolic/table-based experiment does not require a GPU.

## Interpretation guardrails

Use these guardrails when analyzing the results:

1. If `baseline_context_gated_transition_table` matches CIRM, that is expected and should be reported honestly. It means the clean symbolic benchmark can be solved by explicit context-gated lookup.
2. If `baseline_shared_transition_table` fails on seen routes or first-step context probes, that supports context/world indexing under incompatible route systems.
3. If `baseline_route_endpoint_memorizer` solves seen routes but fails suffix routes, that supports reusable primitive composition rather than whole-route memorization.
4. If `exp13_2_cirm_no_recurrence_at_eval` preserves route-table accuracy while composition fails, that continues the Exp13.1 route-table/composition dissociation.
5. Capacity-pressure results should be treated as baseline failure-mode curves, not as proof of biological plausibility.

## Expected manuscript value

This experiment should contribute to C12: external baselines required. It may also strengthen/refine C2, C3, C4, C6, and C7 if the expected sanity relationships hold.

## Completed runs and results

### `exp13_2_smoke_20260507_165655`

Claim -> Root `.venv` start-script resolution was verified with a smoke run.
Evidence -> `start_exp13_2_run.ps1 -Profile smoke -SkipValidation -NoSqlite` completed 16/16 planned units and reported Python from `..\..\.venv\Scripts\python.exe`.
Caveat -> Validation and SQLite writing were intentionally skipped for this launch-script check.
Source path -> `experiments/experiment13_2_baseline_suite/analysis/exp13_2_smoke_20260507_165655/`

- Database path: not written (`-NoSqlite`).
- Key configuration: smoke profile, seeds `[0, 1]`, world counts `[4]`, route lengths `[4, 8]`, routes per world `8`.
- Summary: hardest tested CIRM suffix-composition accuracy was `1.0000`; context-gated lookup was also `1.0000`; whole-route endpoint memorizer suffix-route accuracy was `0.0000`.

## Known limitations

- These are symbolic/algorithmic baselines, not full neural baselines.
- The context-gated lookup baseline is oracle-like because world labels are supplied.
- This does not resolve the Exp13.1 targeted-lesion diagnostic failure.
- This does not replace prior-art/novelty source import.
