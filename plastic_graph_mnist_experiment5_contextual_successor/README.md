# Experiment 5 - Contextual Successor World

This directory is the isolated implementation home for Experiment 5.

Experiment 4 showed that recurrent structural plasticity could learn and reuse a single traversal chain. Experiment 5 asks a harder routing question:

> Can the graph choose among multiple competing transition systems based on context, then compose the right one over several steps?

The contextual modes are:

```text
plus_one:  n -> n + 1
plus_two:  n -> n + 2
minus_one: n -> n - 1
```

The same starting number can therefore produce different answers depending on the active mode.

See [EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md](EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md) for the detailed design and interpretation framework.

## Layout

```text
plastic_graph_mnist_experiment5_contextual_successor/
  run_exp5_contextual_successor.py
  run_exp5_suite.py
  analyze_exp5_suite.py
  EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md
  runs/
  analysis/
  plastic_graph_mnist/
```

This directory intentionally contains its own implementation rather than extending the Experiment 4 directory in place.

## Run the suite

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

## Optional stressors

- `--feedback-noise`
- `--delayed-reward`
- `--rule-reversal`

## Helper scripts

```bash
./start.sh
```

```powershell
.\start.ps1
```

These helper scripts use the shared workspace virtualenv at `../.venv`.
