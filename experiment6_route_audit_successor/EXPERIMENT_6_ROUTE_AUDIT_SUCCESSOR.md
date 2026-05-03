# Experiment 6 - Route Audit Successor World

Experiment 5 introduced contextual successor rules, but the review pass uncovered a methodological problem: the traversal loop reconstituted the symbolic concept-plus-context state after every recurrent step. That made several context metrics partly tautological and weakened the meaning of the route-selection claims.

Experiment 6 asks:

> If we stop rebuilding the symbolic state after every step and instead audit the raw recurrent trajectory, can the graph still choose the right transition family under context and compose it across multiple steps?

The task introduces several context-dependent transition rules over the same number concepts:

```text
plus_one:  n -> n + 1
plus_two:  n -> n + 2
minus_one: n -> n - 1
```

The same start state can now map to different next states depending on context:

```text
mode=plus_one,  start=4, steps=3 -> 7
mode=plus_two,  start=4, steps=3 -> 10
mode=minus_one, start=4, steps=3 -> 1
```

The graph therefore has to do more than memorize one successor chain. It has to preserve context, keep competing routes apart, and repeatedly traverse the route that matches the active mode.

## Why this matters

Experiment 4 still allowed a single universal transition family:

```text
2 -> 3 -> 4 -> 5
```

Experiment 5 creates route ambiguity:

```text
4 + context(plus_one)  -> 5
4 + context(plus_two)  -> 6
4 + context(minus_one) -> 3
```

This matters because biological-style reasoning is not just replaying one chain. It is selecting the right chain under the current state and suppressing nearby but wrong alternatives.

## What changed from Experiment 5

Experiment 6 keeps the same contextual task family, but changes the evaluation contract and the update semantics:

- Traversal now advances on the actual recurrently selected active set instead of replacing it with `activate_state(predicted, mode)` after each step.
- Route metrics are measured from the per-step recurrent trajectory rather than from the reconstructed endpoint assembly.
- Structural rewiring distinguishes positive consolidation from negative corrective rewrites so the `no_reward_gate` ablation is no longer silently bypassed by a universally positive rewrite path.
- Training defaults are slightly stronger than Experiment 5 so multi-step behavior is not judged purely from one-step learning.

The control mechanisms remain:

- `PersistentContextRouter`: biases selection toward the currently relevant context assembly without explicitly rebuilding the symbolic state.
- `ContextualInhibitionController`: penalizes competing mode assemblies and stale activity so the graph is less likely to blend routes.

The local learning rule remains simple and inspectable, but now separates consolidation from correction more honestly:

```text
active source assembly
+ active mode assembly
+ reward/error modulation
+ positive consolidation on correct target links
+ corrective rewiring away from wrong route links toward the correct next concept
= updated recurrent route field
```

## Variants

The suite runs these controlled variants:

| Variant | Purpose |
|---|---|
| `exp6_full_route_audit` | Full recurrent contextual traversal graph with audited route metrics |
| `exp6_no_recurrence` | Tests whether recurrent traversal is necessary |
| `exp6_no_structural_plasticity` | Tests whether rewiring/growth remains load-bearing |
| `exp6_no_reward_gate` | Tests whether reward modulation matters once negative correction is explicit |
| `exp6_no_homeostasis` | Tests whether stabilization matters when routes compete |
| `exp6_no_context_routing` | Tests whether persistent context bias is necessary without symbolic resets |
| `exp6_no_inhibition` | Tests whether suppressing competing contexts reduces route confusion |

## Optional stressors

The package still exposes the next contextual stressors:

- `--feedback-noise`: flips a fraction of reward signals to test robustness under misleading feedback.
- `--delayed-reward`: applies one final reward to a whole traversal path instead of immediate stepwise correction.
- `--rule-reversal`: swaps the transition rules mid-training so we can measure adaptation and interference.

These are off by default in the baseline suite so the route-audit question stays interpretable.

## Key metrics

Performance:

- `transition/accuracy`
- `composition/accuracy`
- `composition/accuracy_mode_*`
- `composition/accuracy_steps_*`

Route selection:

- `composition/average_target_route_activation`
- `composition/average_wrong_route_activation`
- `composition/average_route_margin`
- `composition/average_context_margin`
- `composition/confusion_*`

Dynamics:

- `composition/average_recurrent_drive`
- `composition/average_unique_active`
- `composition/average_path_entropy`

## Run it

```bash
python run_exp6_suite.py \
  --max-number 24 \
  --max-steps 5 \
  --train-sequence-repeats 180 \
  --training-max-steps 3 \
  --hidden-units 4096 \
  --assembly-size 72 \
  --mode-assembly-size 24 \
  --active-units 96 \
  --recurrent-edges-per-unit 48

python analyze_exp6_suite.py \
  --db runs/exp6_route_audit_successor_suite.sqlite3 \
  --output-dir analysis/exp6
```

```powershell
python .\run_exp6_suite.py `
  --max-number 24 `
  --max-steps 5 `
  --train-sequence-repeats 180 `
  --training-max-steps 3 `
  --hidden-units 4096 `
  --assembly-size 72 `
  --mode-assembly-size 24 `
  --active-units 96 `
  --recurrent-edges-per-unit 48

python .\analyze_exp6_suite.py `
  --db .\runs\exp6_route_audit_successor_suite.sqlite3 `
  --output-dir .\analysis\exp6
```

For a quick smoke test:

```bash
python run_exp6_suite.py \
  --max-number 12 \
  --max-steps 3 \
  --train-sequence-repeats 8 \
  --training-max-steps 2 \
  --hidden-units 512 \
  --assembly-size 32 \
  --mode-assembly-size 12 \
  --active-units 48 \
  --recurrent-edges-per-unit 16 \
  --eval-every 40
```

## What success means

This experiment supports the thesis if the full model can maintain the right route under context and compose it across multiple steps while the audited route metrics show that the correct route beats competing routes along the actual recurrent path, not just in a reconstructed symbolic endpoint.

The central claim is not:

```text
"the model memorized one chain"
```

It is:

```text
"the model learned multiple competing transition families
and could route through the right one based on context
under an honest recurrent audit"
```
