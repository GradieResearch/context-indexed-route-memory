# Experiment 14: Latent Context Inference

This is a self-contained successor experiment for the Context-Indexed Route Memory manuscript.

## Why this experiment is next

Experiment 13.2 completed the first baseline suite and showed an important reviewer-facing truth: when the correct world/context label is supplied, an explicit context-gated lookup table can solve the clean symbolic route-composition benchmark as well as the proposed mechanism. That does **not** invalidate CIRM, but it means the manuscript must be precise: raw clean-task accuracy is not the novelty claim.

Experiment 14 therefore targets the next manuscript-critical limitation: **oracle context labels**. It removes the supplied world label at evaluation time and requires models to infer the active context from partial transition evidence before composing a route.

## Scientific purpose

Experiment 14 asks whether context-indexed route memory can support latent context/world selection from observed transition cues, and how that selection degrades under stochastic cue corruption.

The purpose is not to claim solved latent-world discovery or perception. The benchmark remains symbolic and controlled. The manuscript value is narrower:

- separate oracle context-gated lookup from latent context selection;
- measure whether route execution succeeds when the active world is inferred from cues;
- compare against random, recency, shared no-context, endpoint-memorization, oracle, and compact hash-slot selector baselines;
- quantify cue-count sensitivity and stochastic corruption sensitivity;
- produce seed-level confidence intervals, effect sizes, plots, run manifests, progress logs, validation reports, and SQLite records.

## Experiment directory

Expected repository path:

```text
experiments/experiment14_latent_context_inference/
```

## Run profiles

| Profile | Purpose | Seeds | World counts | Route lengths | Cue counts | Corruption rates | Use first |
|---|---:|---:|---:|---:|---:|---:|---|
| `smoke` | Fast command/artifact check | 2 | 4 | 4, 8 | 1, 2 | 0.0, 0.5 | Yes |
| `validation` | Medium sanity run | 5 | 4, 8 | 4, 8 | 1, 2, 4 | 0.0, 0.25, 0.5 | After smoke |
| `full` | Manuscript-facing latent-context run | 20 | 4, 8, 16, 32 | 4, 8, 12, 16 | 1, 2, 4, 8 | 0.0, 0.10, 0.25, 0.50 | After validation passes |

## How to run on Windows PowerShell

From this experiment directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp14_smoke.ps1
powershell -ExecutionPolicy Bypass -File .\start_exp14_validation.ps1
powershell -ExecutionPolicy Bypass -File .\start_exp14_full.ps1
```

Each start script runs the experiment and then validates the generated artifacts.

For advanced usage:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp14_run.ps1 -Profile validation
powershell -ExecutionPolicy Bypass -File .\start_exp14_run.ps1 -Profile full -ProgressEvery 25
powershell -ExecutionPolicy Bypass -File .\start_exp14_run.ps1 -Profile smoke -SkipValidation -NoSqlite
```

## Python-only usage

```bash
python run_exp14_latent_context_inference.py --profile smoke
python validate_exp14.py --analysis-root analysis
```

## Output layout

Each run writes a new run directory:

```text
analysis/<run_id>/
  exp14_metrics.csv
  metrics.csv
  exp14_summary.csv
  exp14_effect_sizes.csv
  exp14_config.json
  exp14_report.md
  experiment_report.md
  run_manifest.json
  progress.jsonl
  validation_report.md
  validation_results.json
  plots/
    exp14_world_selection_vs_corruption.png
    exp14_seen_composition_vs_corruption.png
    exp14_suffix_composition_vs_corruption.png
    exp14_margin_vs_corruption.png
    exp14_cue_count_selection_sensitivity.png
    exp14_cue_count_composition_sensitivity.png
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

## Model variants

| Variant | Role | Interpretation |
|---|---|---|
| `exp14_cirm_latent_selector` | Main model | World-indexed structural table selected from transition cues, then recurrent route execution. |
| `baseline_oracle_context_gated_table` | Upper bound | Same clean table task with true world supplied; not a fair latent-selector baseline. |
| `baseline_shared_no_context_table` | No-context lower bound | Tests whether context/world indexing is required under incompatible first-step transitions. |
| `baseline_route_endpoint_memorizer_with_latent_selector` | Memorization control | Can memorize seen whole-route endpoints but should fail unseen suffix route probes. |
| `baseline_random_context_selector` | Chance selector | Estimates chance context selection and downstream composition. |
| `baseline_recency_context_selector` | Sequential recency control | Always selects the most recently learned world. |
| `baseline_hash_slot_selector_div*` | Compact context control | Tests context compression/collision behavior with fewer slots than worlds. |

## Primary metrics

- `world_selection_accuracy_seen_route`
- `world_selection_accuracy_suffix_route`
- `composition_accuracy_seen_route`
- `composition_accuracy_suffix_route`
- `first_step_context_accuracy`
- `route_table_selected_accuracy_seen_route`
- `route_table_selected_accuracy_suffix_route`
- `mean_world_margin_seen_route`
- `mean_world_confidence_seen_route`
- seed-level CI95 summaries and CIRM-vs-baseline effect sizes

## Interpretation guardrails

1. Clean cue success supports context selection from symbolic transition evidence, not autonomous context discovery from raw sensory data.
2. The oracle context-gated table should remain an upper-bound control, not a defeated competitor.
3. If stochastic corruption degrades CIRM, frame it as cue-evidence sensitivity unless richer noise models are added.
4. If hash-slot selectors succeed when slots are sufficient and fail under collisions, that refines the resource/capacity interpretation rather than proving biological plausibility.
5. This experiment does not resolve the Exp13.1 targeted-lesion diagnostic failure and does not replace prior-art discussion.

## Manuscript value

If the expected sanity relationships hold, this experiment should refine the manuscript spine after Exp13.2:

- C2 becomes more precise: world/context indexing can be selected from partial symbolic evidence, but oracle labels remain a limitation.
- C10 becomes more precise: wrong or corrupted context evidence degrades selection and route execution.
- C12 becomes less blocking: the context-gated lookup baseline is now explicitly represented as an oracle upper bound rather than an unexamined competitor.
- The limitations section should still state that the task is symbolic and not an end-to-end latent-world or perceptual learning demonstration.
