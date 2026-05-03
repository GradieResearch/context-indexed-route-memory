# Experiment 5 - Contextual Successor World

Experiment 4 showed that recurrence and structural plasticity become load-bearing when the task actually requires traversal. The next question is whether the graph can do something more interesting than learn a single reusable chain.

Experiment 5 asks:

> Can the same recurrent plastic graph choose among multiple transition systems based on context, then compose the chosen route over several steps?

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

## Architecture additions

Experiment 5 adds two explicit control mechanisms on top of the successor graph:

- `PersistentContextRouter`: re-injects the current mode assembly during traversal so route identity can persist over multiple recurrent steps.
- `ContextualInhibitionController`: penalizes competing mode assemblies and stale activity so the graph is less likely to blend routes.

The local learning rule remains simple and inspectable:

```text
active source assembly
+ active mode assembly
+ reward/error modulation
+ structural rewiring toward the correct next concept
= updated recurrent route field
```

## Variants

The suite runs these controlled variants:

| Variant | Purpose |
|---|---|
| `exp5_full_contextual_traversal` | Full recurrent contextual traversal graph |
| `exp5_no_recurrence` | Tests whether recurrent traversal is necessary |
| `exp5_no_structural_plasticity` | Tests whether rewiring/growth remains load-bearing |
| `exp5_no_reward_gate` | Tests whether reward modulation matters |
| `exp5_no_homeostasis` | Tests whether stabilization matters when routes compete |
| `exp5_no_context_routing` | Tests whether persistent context injection is necessary |
| `exp5_no_inhibition` | Tests whether suppressing competing contexts reduces route confusion |

## Optional stressors for 5B and 5C

The package also exposes optional knobs for the next two roadmap steps:

- `--feedback-noise`: flips a fraction of reward signals to test robustness under misleading feedback.
- `--delayed-reward`: applies one final reward to a whole traversal path instead of immediate stepwise correction.
- `--rule-reversal`: swaps the transition rules mid-training so we can measure adaptation and interference.

These are off by default in the baseline suite so the clean contextual-routing question stays interpretable.

## Key metrics

Performance:

- `transition/accuracy`
- `composition/accuracy`
- `composition/accuracy_mode_*`
- `composition/accuracy_steps_*`

Route selection:

- `composition/average_wrong_route_activation`
- `composition/average_context_margin`
- `composition/confusion_*`

Dynamics:

- `composition/average_recurrent_drive`
- `composition/average_unique_active`
- `composition/average_path_entropy`

## Run it

```bash
python run_exp5_suite.py \
  --max-number 24 \
  --max-steps 5 \
  --train-sequence-repeats 120 \
  --hidden-units 4096 \
  --assembly-size 72 \
  --mode-assembly-size 24 \
  --active-units 96 \
  --recurrent-edges-per-unit 48

python analyze_exp5_suite.py \
  --db runs/exp5_contextual_successor_suite.sqlite3 \
  --output-dir analysis/exp5
```

```powershell
python .\run_exp5_suite.py `
  --max-number 24 `
  --max-steps 5 `
  --train-sequence-repeats 120 `
  --hidden-units 4096 `
  --assembly-size 72 `
  --mode-assembly-size 24 `
  --active-units 96 `
  --recurrent-edges-per-unit 48

python .\analyze_exp5_suite.py `
  --db .\runs\exp5_contextual_successor_suite.sqlite3 `
  --output-dir .\analysis\exp5
```

For a quick smoke test:

```bash
python run_exp5_suite.py \
  --max-number 12 \
  --max-steps 3 \
  --train-sequence-repeats 8 \
  --hidden-units 512 \
  --assembly-size 32 \
  --mode-assembly-size 12 \
  --active-units 48 \
  --recurrent-edges-per-unit 16 \
  --eval-every 40
```

## What success means

This experiment supports the thesis if the full model can maintain the right route under context and compose it across multiple steps, while controls that remove recurrence, rewiring, or context persistence fail noticeably more often.

The central claim is not:

```text
"the model memorized one chain"
```

It is:

```text
"the model learned multiple competing transition families
and could route through the right one based on context"
```
