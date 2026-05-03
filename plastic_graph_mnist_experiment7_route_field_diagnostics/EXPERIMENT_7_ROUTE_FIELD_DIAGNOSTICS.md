# Experiment 7 - Route Field Diagnostics

Experiment 7 is the diagnostic follow-up to the contextual successor problem.

Experiment 5 asked whether the graph could choose among multiple transition systems using context and then compose the selected route over several recurrent steps. The result was mechanistically useful but not yet a capability success: recurrence was clearly load-bearing, context routing helped, and structural plasticity helped, but the full model did not reliably compose contextual routes.

Experiment 7 therefore does **not** make the task harder. It makes the mechanism easier to inspect.

## Core question

> When contextual traversal fails, does it fail because the graph did not learn the local transition table, did not preserve context, could not recurrently compose the local transition, could not decode the final state, or allowed competing routes to remain active?

## Why this experiment exists

Experiment 5 gave us low absolute composition accuracy, while the full model still preserved the mode identity in the context-confusion matrix. That suggests a specific possible failure mode:

```text
context identity is preserved
but context is not strongly binding the transition field
```

In plain terms, the graph may know it is in `plus_two` mode while still allowing `plus_one` or `minus_one` route fragments to influence the next state.

Experiment 7 turns that hypothesis into measurable diagnostics.

## Task world

The world is deliberately small and bounded.

```text
minus_one: n -> n - 1
plus_one:  n -> n + 1
plus_two:  n -> n + 2
```

Only tasks whose final target stays inside the number range are evaluated. This removes boundary effects as an explanation for failure.

Example:

```text
mode=plus_two, start=4, steps=3 -> 10
mode=minus_one, start=4, steps=3 -> 1
```

## What is learned

The diagnostic model learns a mode-conditioned recurrent route field:

```text
route[mode, source_number, destination_number]
```

The local plastic update reinforces the correct one-step transition:

```text
active source assembly
+ active mode assembly
+ correct next assembly
= stronger route edge
```

Composition is not solved by directly memorizing final answers. If the graph learns the one-step route field, recurrent traversal should produce multi-step answers.

## Variants

| Variant | Purpose |
|---|---|
| `exp7_full_route_field` | Full context-bound recurrent route field with structural plasticity and inhibition. |
| `exp7_no_recurrence` | Learns local transitions but does not feed the predicted state back through the route field. Should do well on one-step and fail on composition. |
| `exp7_no_context_binding` | Collapses all modes into one shared transition table. Tests whether route ambiguity creates collisions. |
| `exp7_no_structural_plasticity` | Keeps the route field random. Tests whether learned rewiring/growth is necessary. |
| `exp7_no_inhibition` | Reinforces correct routes without suppressing wrong targets or wrong contexts. Tests whether inhibition matters in this simplified diagnostic world. |
| `exp7_context_bleed` | Blends wrong-mode route fields into the active mode. Simulates route contamination. |
| `exp7_noisy_plasticity` | Adds noise during local updates. Tests robustness of route-field formation. |

## Deterministic baselines

The suite also reports:

| Baseline | Purpose |
|---|---|
| `random_uniform` | True random floor. |
| `most_frequent_target` | Detects target imbalance. |
| `identity_start` | Detects whether the model is merely staying near the source. |
| `always_plus_one` | Detects mode imbalance or successor bias. |
| `always_plus_two` | Detects plus-two bias. |
| `always_minus_one` | Detects minus-one bias. |
| `lookup_oracle` | Direct target ceiling. |
| `transition_table_composition_oracle` | One-step table + exact repeated composition ceiling. |

## Key diagnostics

### Accuracy metrics

```text
transition/accuracy
composition/accuracy
composition/accuracy_mode_*
composition/accuracy_steps_*
```

These answer whether local transition learning and recurrent composition work.

### Target-rank metrics

```text
mean_step_target_rank
max_step_target_rank
```

These answer whether the correct next state is close to winning even when argmax is wrong.

A model with target rank near 2 may be much closer to working than a model with target rank near random.

### Correct-route margin

```text
correct_margin = score(correct_next_state) - score(best_wrong_next_state)
```

This is more informative than raw recurrent drive. More drive is not necessarily better; correct target dominance is better.

### Context margin

```text
context_margin = score(correct_mode, source, target) - max(score(wrong_mode, source, target))
```

This tells us whether context actually binds the transition edge, not merely whether the context label is preserved.

### Wrong-route activation

A bounded proxy for wrong-mode support of the correct target.

This metric should be interpreted alongside correct-route margin. Low wrong-route activation is not automatically good if the model is simply inactive.

## Success criteria

Experiment 7 is successful if it can clearly separate these failure modes:

1. local transition table not learned;
2. transition table learned but not recurrently composed;
3. context route collisions;
4. route contamination from wrong modes;
5. decoder/final-state failure;
6. noisy or unstable plasticity.

The expected clean pattern is:

| Variant | Expected outcome |
|---|---|
| Full route field | High transition and high composition accuracy. |
| No recurrence | High transition accuracy, poor composition accuracy. |
| No context binding | Lower composition because modes collide in one shared route table. |
| No structural plasticity | Near random route table accuracy. |
| Context bleed | Correct context exists but margins degrade. |

## Run

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

PowerShell:

```powershell
.\start.ps1
```

The PowerShell start script uses the shared virtual environment one directory above this experiment directory:

```text
..\.venv\Scripts\python.exe
```

## Outputs

```text
runs/exp7_route_field_diagnostics.sqlite3
analysis/exp7/runs.csv
analysis/exp7/metrics.csv
analysis/exp7/predictions.csv
analysis/exp7/route_diagnostics.csv
analysis/exp7/baselines.csv
analysis/exp7/exp7_report.md
analysis/exp7/*.png
```

## How to use the result

If the full diagnostic route field solves this small world but Experiment 5 remains weak, then the issue is probably in the richer hidden-unit implementation: assembly overlap, recurrent drive scaling, decoder readout, context injection, or plastic update timing.

If the diagnostic route field itself fails, then the contextual traversal thesis needs a simpler local learning rule before moving to larger tasks.
