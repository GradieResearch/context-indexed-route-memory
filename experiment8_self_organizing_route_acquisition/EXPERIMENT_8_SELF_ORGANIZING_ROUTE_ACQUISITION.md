# Experiment 8 - Self-Organizing Contextual Route Acquisition

Experiment 7 showed that a clean context-conditioned route field can be composed recurrently. Experiment 8 asks the missing bridge question:

> Can a local plastic graph acquire that clean context-conditioned route field from one-step transition experience, then solve unseen multi-step traversal queries by recurrence?

The model trains only on local transitions such as:

```text
mode=plus_one,  source=4 -> target=5
mode=plus_two,  source=4 -> target=6
mode=minus_one, source=4 -> target=3
```

It is then evaluated on held-out composition tasks such as:

```text
mode=plus_two,  start=4,  steps=7 -> 18
mode=minus_one, start=20, steps=6 -> 14
```

The main experiment should keep `--path-train-repeats 0`, so the model never directly trains on the final multi-step answers.

## Hypothesis

A recurrent graph with context-bound structural plasticity can acquire local transition routes from sparse experience, and once those routes reach sufficient margin, recurrent traversal composes them to solve unseen multi-step queries.

Sub-hypotheses:

1. Structural plasticity is required to form the route table.
2. Recurrence is required to compose the local route table.
3. Context binding is required to keep multiple route families from colliding.
4. Inhibition is not required in easy clean settings, but protects margins and route purity.
5. Reward gating should matter most under feedback noise or delayed reward.
6. Accuracy alone is insufficient; margins and target rank expose brittleness before accuracy collapses.

## Architecture

The graph uses sparse distributed assemblies over a latent hidden population:

- number assemblies represent symbolic numbers;
- mode assemblies represent transition families;
- a recurrent matrix `W[pre_unit, post_unit]` is locally updated when a source+mode assembly predicts a target assembly.

Training uses a simple local update:

```text
source number assembly
+ active context assembly
+ reward/error gating
+ structural plasticity update toward target number assembly
+ optional inhibition of competing targets and contexts
= learned recurrent route field
```

Composition is performed by repeatedly decoding the next number and feeding it back into the same learned route field under the same context.

## Variants

| Variant | Purpose |
|---|---|
| `exp8_full_self_organizing_route_field` | Main model |
| `exp8_no_recurrence` | Should learn one-step transitions but fail multi-step composition |
| `exp8_no_structural_plasticity` | Should fail route acquisition |
| `exp8_no_context_binding` | Should show route collisions between modes |
| `exp8_no_inhibition` | Should preserve simple accuracy but lose route purity/margins under stress |
| `exp8_no_reward_gate` | Should become fragile under noisy feedback |
| `exp8_no_homeostasis` | Tests whether clipping/stabilization matters under larger repetition or noise |
| `exp8_context_bleed` | Tests stale/competing context contamination |

## Metrics

Performance:

- `transition/accuracy`
- `composition/accuracy`
- `composition/accuracy_mode_*`
- `composition/accuracy_steps_*`

Route field:

- `route_table/accuracy`
- `route_table/mean_target_rank`
- `route_table/mean_correct_margin`
- `route_table/mean_context_margin`
- `route_table/mean_wrong_route_activation`

Composition diagnostics:

- `composition/mean_target_rank`
- `composition/mean_correct_margin`
- `composition/mean_context_margin`
- `composition/mean_wrong_route_activation`

Failure taxonomy:

- `first_step_failure`
- `mid_route_drift`
- `no_recurrence_single_step_only`
- `decoder_or_endpoint_failure`

## Success criteria

Strong evidence for the bridge hypothesis would look like:

| Metric | Desired direction |
|---|---:|
| Full model transition accuracy | high |
| Full model route-table accuracy | high |
| Full model composition accuracy | high on unseen steps |
| No recurrence composition | near zero despite good transition accuracy |
| No structural plasticity | near random route acquisition |
| No context binding | severe route collision and margin collapse |
| No inhibition | accuracy may survive, but wrong-route activation/margins worsen |

## Run

```powershell
.\start.ps1
```

The script intentionally uses the shared virtual environment one directory up:

```powershell
..\.venv\Scripts\python.exe
```

## Manual command

```powershell
..\.venv\Scripts\python.exe .\run_exp8_suite.py `
  --max-number 31 `
  --max-steps 8 `
  --transition-train-repeats 1 `
  --path-train-repeats 0 `
  --seeds 30 `
  --hidden-units 2048 `
  --number-assembly-size 72 `
  --mode-assembly-size 24 `
  --force
```
