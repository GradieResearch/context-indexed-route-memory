# Experiment 13.1 Review Notes

## Review verdict

The uploaded implementation was a strong start: the core table-based route-field model was syntactically valid, included the historical `modes + 1` guard, separated eval-only recurrence from recurrence-disabled-throughout, and covered context corruption, freeze, lesion, and budget/consolidation controls.

However, it was lacking against the implementation prompt and repository discipline in four important ways:

1. **Run artifacts were flat, not per-run immutable records.**
   - Original output defaulted to `analysis/exp13_1/`.
   - Revised output defaults to `analysis/<run_id>/`.

2. **No SQLite run database was produced.**
   - Revised implementation writes `runs/<run_id>.sqlite3` with `metrics`, `metadata`, and `variants` tables.

3. **Validation and experiment execution were coupled in one launcher.**
   - Revised implementation separates run and validation scripts:
     - `start_exp13_1_run.ps1`
     - `start_exp13_1_full.ps1`
     - `start_exp13_1_standard.ps1`
     - `start_exp13_1_validate.ps1`

4. **Progress logging was too coarse to estimate runtime.**
   - Original logging marked phase starts/completions.
   - Revised logging records row/evaluation units with elapsed time, rate, percent complete, and ETA in both console output and `progress.jsonl`.

## Additional hardening added

- `run_manifest.json` is emitted before execution rows are written.
- `metrics.csv` and `exp13_1_metrics.csv` are both written for compatibility.
- Plots are written under `analysis/<run_id>/plots/`.
- `experiment_report.md` and `exp13_1_report.md` are both written for compatibility.
- The validator can validate `--run-id latest`, an explicit `--run-id`, or an exact `--analysis-dir`.
- The validator checks progress ETA fields, SQLite tables, required phases, required variants, required plots, metric bounds, context corruption deltas, recurrence metadata, lesion controls, and report anti-overclaiming.

## Execution note

This package was statically checked with Python compilation only. The experiment/validation scripts were not executed here.
