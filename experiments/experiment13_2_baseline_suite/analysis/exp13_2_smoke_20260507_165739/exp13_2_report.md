# Experiment 13.2 Report: Baseline Suite

## Run identity

- Experiment: `exp13_2_baseline_suite`
- Run ID: `exp13_2_smoke_20260507_165739`
- Profile: `smoke`
- Seeds: `[0, 1]`
- World counts: `[4]`
- Route lengths: `[4, 8]`
- Routes per world: `8`
- Metrics rows: `108`
- SQLite DB: `runs\exp13_2_smoke_20260507_165739.sqlite3`

## Executive summary

This run compares the Context-Indexed Route Memory mechanism against explicit symbolic baselines under the same route-composition benchmark. It is designed to reduce the manuscript's baseline blocker, not to claim that CIRM beats an oracle lookup table.

- CIRM suffix-composition accuracy at the hardest tested setting: 1.0000.
- Explicit context-gated lookup suffix-composition accuracy at the hardest tested setting: 1.0000. This is expected to be strong and is an oracle-style control.
- Shared no-context transition-table seen-route accuracy at the hardest tested setting: 0.2500; first-step context disambiguation accuracy: 0.2500. Suffix probes can be easier for this baseline because they start after the deliberately conflicting first step.
- Whole-route endpoint memorizer seen-route accuracy: 1.0000; suffix-route accuracy: 0.0000.
- CIRM no-recurrence-at-eval route-table accuracy: 1.0000; seen-route composition accuracy: 0.0000.

## Interpretation guardrails

- If the context-gated lookup table performs as well as CIRM, that does not invalidate CIRM; it means this symbolic benchmark needs baselines and the novelty claim must be mechanistic rather than raw accuracy superiority.
- If whole-route endpoint memorization solves seen routes but fails suffix routes, suffix probes support reusable primitive composition over route memorization.
- If shared no-context lookup fails while context-gated lookup succeeds, this supports the need for context/world indexing under incompatible route systems.
- If finite-capacity replay/isolation baselines fail gracefully or differently, those curves should be used to frame CIRM against conventional continual-learning controls.

## Generated plots

- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_seen_route_composition_accuracy.png`
- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_suffix_generalization_accuracy.png`
- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_route_table_accuracy.png`
- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_first_step_context_accuracy.png`
- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_capacity_pressure.png`
- `analysis\exp13_2_smoke_20260507_165739\plots\exp13_2_sequential_retention.png`

## Source artifacts

- `exp13_2_metrics.csv`
- `exp13_2_summary.csv`
- `exp13_2_effect_sizes.csv`
- `exp13_2_baseline_metrics.csv`
- `run_manifest.json`
- `progress.jsonl`
