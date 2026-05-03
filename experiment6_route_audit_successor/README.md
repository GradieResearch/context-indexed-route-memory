# Experiment 6 - Route Audit Successor World

This directory is the isolated implementation home for Experiment 6.

Experiment 5 exposed an important ambiguity: the contextual-successor setup was interesting, but its traversal loop reconstructed the symbolic state after each step, which made several routing metrics look stronger than the underlying recurrent dynamics justified.

Experiment 6 asks the corrected question:

> Can the graph still choose among competing transition systems based on context when we audit the raw recurrent trajectory instead of resetting the symbolic state after every step?

The contextual modes are:

```text
plus_one:  n -> n + 1
plus_two:  n -> n + 2
minus_one: n -> n - 1
```

The same starting number can therefore produce different answers depending on the active mode.

See [EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md](EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md) for the detailed design and interpretation framework.

## Layout

```text
plastic_graph_mnist_experiment6_route_audit_successor/
  run_exp6_route_audit_successor.py
  run_exp6_suite.py
  analyze_exp6_suite.py
  EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md
  runs/
  analysis/
  plastic_graph_mnist/
```

This directory intentionally contains its own implementation rather than extending the Experiment 5 directory in place.

## Run the suite

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

## Optional stressors

- `--feedback-noise`
- `--delayed-reward`
- `--rule-reversal`

## Completed Runs And Results

- Pending first Experiment 6 run. This section will be updated with the run name, database path, key configuration notes, and summarized results after execution.

## Helper scripts

```bash
./start.sh
```

```powershell
.\start.ps1
```

These helper scripts use the shared workspace virtualenv at `../.venv`.
