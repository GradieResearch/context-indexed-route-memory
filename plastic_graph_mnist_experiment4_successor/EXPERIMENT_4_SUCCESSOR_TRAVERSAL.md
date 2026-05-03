# Experiment 4 — Successor Traversal

Experiment 4 moves beyond MNIST because MNIST did not strongly require recurrent graph traversal. The previous ablations showed that recurrence was measurable but not clearly useful; the no-recurrence model performed about as well as the full recurrent model. That suggested the task was too perceptual and one-shot.

This experiment asks a sharper question:

> Can a sparse recurrent plastic graph learn a local transition rule and then compose that rule repeatedly to solve a task it was not directly trained on?

The task is successor arithmetic:

```text
Learn local transition:
  0 -> 1
  1 -> 2
  2 -> 3
  ...

Evaluate compositional addition:
  start at 2, take 3 successor steps -> 5
  start at 7, take 4 successor steps -> 11
```

The model is trained on one-step transitions only. Multi-step addition is a held-out traversal test.

---

## Why this matters

MNIST can be solved by a shallow mapping:

```text
pixels -> sparse features -> class readout
```

That does not force the recurrent graph to be useful.

Experiment 4 forces the issue:

```text
symbolic start state -> recurrent transition -> recurrent transition -> ... -> decoded answer
```

If the full recurrent graph beats the no-recurrence control on multi-step addition, that supports the claim that recurrent plastic pathways are doing work.

---

## Dense network versus plastic traversal graph

### Typical feed-forward classifier

```text
Input
  |
  v
Dense/static learned transform
  |
  v
Dense/static learned transform
  |
  v
Output

Learning mostly occurs during a separate training phase.
Inference does not alter the substrate.
```

### Experiment 4 plastic traversal graph

```text
Concept assembly: 2
  |
  | recurrent learned edge field
  v
Concept assembly: 3
  |
  | recurrent learned edge field
  v
Concept assembly: 4
  |
  | recurrent learned edge field
  v
Concept assembly: 5

Feedback strengthens or weakens the active transition paths.
Structural plasticity can replace weak outgoing edges with useful targets.
Homeostasis prevents runaway recurrent spread.
```

---

## Model components

- `ConceptAssemblyBook`: assigns each number to a sparse distributed assembly of hidden units.
- `SparseRecurrentAssemblyGraph`: holds sparse hidden-to-hidden recurrent edges.
- `SuccessorTask`: produces one-step transition training examples and multi-step addition tests.
- `SuccessorExperimentTrainer`: trains transitions, evaluates compositional traversal, and persists metrics/checkpoints.

---

## Controlled variants

The suite runs these variants:

| Variant | Purpose |
|---|---|
| `exp4_full_traversal` | Full recurrent plastic graph |
| `exp4_no_recurrence` | Tests whether recurrence is necessary |
| `exp4_no_structural_plasticity` | Tests whether edge rewiring/growth matters |
| `exp4_no_homeostasis` | Tests whether activity regulation prevents collapse |
| `exp4_no_reward_gate` | Tests whether the reward gate helps or hurts |

---

## Expected interpretation

A strong result would look like:

```text
exp4_full_traversal >> exp4_no_recurrence on multi-step addition
```

Especially on:

```text
addition/accuracy_steps_2
addition/accuracy_steps_3
addition/accuracy_steps_4
addition/accuracy_steps_5
```

If `no_recurrence` performs well, the task is still too easy or the decoder is leaking information. If `no_structural_plasticity` performs about the same as full traversal, then the current structural update rule is not load-bearing. If `no_homeostasis` collapses or shows high recurrent drive, that supports the need for biological-style stabilizers.

---

## Run it

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python run_exp4_suite.py \
  --max-number 24 \
  --max-addend 5 \
  --train-transition-repeats 120 \
  --hidden-units 4096 \
  --assembly-size 96 \
  --active-units 96 \
  --recurrent-edges-per-unit 48

python analyze_exp4_suite.py \
  --db runs/exp4_successor_suite.sqlite3 \
  --output-dir analysis/exp4
```

```powershell
python -m venv ..\.venv
..\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python .\run_exp4_suite.py `
  --max-number 24 `
  --max-addend 5 `
  --train-transition-repeats 120 `
  --hidden-units 4096 `
  --assembly-size 96 `
  --active-units 96 `
  --recurrent-edges-per-unit 48

python .\analyze_exp4_suite.py `
  --db .\runs\exp4_successor_suite.sqlite3 `
  --output-dir .\analysis\exp4
```

Helper scripts are available too:

```bash
./start.sh
```

```powershell
.\start.ps1
```

For a quick smoke test:

```bash
python run_exp4_suite.py \
  --max-number 12 \
  --max-addend 3 \
  --train-transition-repeats 10 \
  --hidden-units 512 \
  --assembly-size 32 \
  --active-units 32 \
  --recurrent-edges-per-unit 16 \
  --eval-every 50

python analyze_exp4_suite.py \
  --db runs/exp4_successor_suite.sqlite3 \
  --output-dir analysis/exp4_smoke
```

```powershell
python .\run_exp4_suite.py `
  --max-number 12 `
  --max-addend 3 `
  --train-transition-repeats 10 `
  --hidden-units 512 `
  --assembly-size 32 `
  --active-units 32 `
  --recurrent-edges-per-unit 16 `
  --eval-every 50

python .\analyze_exp4_suite.py `
  --db .\runs\exp4_successor_suite.sqlite3 `
  --output-dir .\analysis\exp4_smoke
```

---

## What success means

This experiment does not try to beat standard neural networks. It tries to demonstrate a different mechanism:

```text
local transition learning
+ recurrent path traversal
+ reward/feedback reinforcement
+ structural edge replacement
+ homeostatic stabilization
= compositional behavior
```

The key claim is not “better MNIST accuracy.” The key claim is that a persistent plastic graph can learn a reusable pathway and apply it repeatedly.
