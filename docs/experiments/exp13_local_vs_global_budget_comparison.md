# Exp13 Local vs Global Budget Comparison

Purpose: Make the local-vs-global budget comparison explicit using existing Exp13 aggregate summary CSVs only. This is a documentation/evidence artifact, not a rerun and not a new experiment.

## Method

- Source path, global budget: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`
- Source path, local budget: `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`
- Rows selected: `run_name=exp13_full_context_separated_memory`, `world_count=32`, `route_length=12`
- Join key: `budget_ratio` in the global CSV matched to `local_budget_ratio` in the local CSV.
- Reported values: aggregate means already present in the source CSVs. `local_minus_global_composition` is computed as local composition mean minus global composition mean.

## Comparison Table

| Budget ratio | Global composition mean | Local composition mean | Local minus global composition | Global route-table mean | Local route-table mean |
|---|---:|---:|---:|---:|---:|
| 0.25 | 0.2755 | 0.0417 | -0.2339 | 0.2723 | 0.2721 |
| 0.50 | 0.5173 | 0.0596 | -0.4577 | 0.5144 | 0.5148 |
| 0.75 | 0.7579 | 0.1379 | -0.6201 | 0.7571 | 0.7575 |
| 1.00 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |

## Conservative Interpretation

Claim: Local structural budget pressure appears more damaging to long-route composition than global budget pressure in this aggregate Exp13 slice.

Evidence: At 32 worlds and route length 12, local and global budget conditions have similar route-table means at budget ratios 0.25, 0.50, and 0.75, but local composition means are lower than the matched global composition means.

Caveat: This is a docs-only comparison from aggregate summaries. It is not a paired seed-level hypothesis test and does not include confidence intervals. Formal paired comparison remains an Exp13.1 follow-up.

Source path: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`
