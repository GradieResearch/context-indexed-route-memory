# Plastic Graph MNIST Analysis — Run 1

## Run summary

- Name: `plastic_graph_mnist`
- Status: `completed`
- Started: `2026-05-01 12:54:33.292616`
- Completed: `2026-05-01 12:55:21.868298`
- Recorded best accuracy: `0.9225`

## Key metrics

- Best test accuracy: **0.9225** at step `27500` / epoch `3`
- Latest test/accuracy: `0.9190` at step `30000`
- Latest test/average_confidence: `0.8309` at step `30000`
- Latest train/average_confidence: `0.8979` at step `30000`
- Latest train/window_accuracy: `0.9820` at step `30000`
- Train window accuracy delta: `0.7280` → `0.9820` = `+0.2540`
- Test accuracy delta: `0.8815` → `0.9190` = `+0.0375`

## Configuration highlights

- hidden_units: `4096`
- input_edges_per_hidden: `64`
- active_hidden: `128`
- learning_rate_hidden_output: `0.035`
- learning_rate_input_hidden: `0.002`
- trace_decay: `0.92`
- threshold_lr: `0.002`
- epochs: `3`
- max_train: `10000`
- max_test: `2000`

## Latest checkpoint

- Artifact: `final`
- Epoch/step: `3` / `30000`
- Arrays:
  - `hidden_excitability` shape=(4096,), mean=1.000000, std=0.000000, p95=1.000000, nonzero=1.0000
  - `hidden_thresholds` shape=(4096,), mean=0.859271, std=0.291728, p95=1.396188, nonzero=1.0000
  - `hidden_traces` shape=(4096,), mean=0.178311, std=0.202062, p95=0.590352, nonzero=1.0000
  - `input_indices` shape=(4096, 64), mean=391.243221, std=226.665199, p95=744.000000, nonzero=0.9986
  - `input_weights` shape=(4096, 64), mean=0.000135, std=0.149810, p95=0.246195, nonzero=1.0000
  - `output_weights` shape=(4096, 10), mean=0.000011, std=0.111162, p95=0.209607, nonzero=1.0000

## Interpretation guide

- Rising `test/accuracy` means the plastic graph is learning pathways that generalize beyond the online training stream.
- Rising `train/window_accuracy` with flat test accuracy suggests memorization or unstable routing rather than generalizable reasoning.
- Very high confidence with poor accuracy suggests runaway reinforcement or an overly aggressive plasticity gate.
- Very low confidence and poor accuracy suggests the readout is not consolidating useful hidden pathways.
- Large threshold drift or very high trace concentration suggests the active population may be collapsing onto too few units.

## Generated files

- `metrics.csv`
- `latest_checkpoint_summary.json`
- `test_accuracy.png`
- `train_window_accuracy.png`
- `test_average_confidence.png`
- `train_average_confidence.png`
