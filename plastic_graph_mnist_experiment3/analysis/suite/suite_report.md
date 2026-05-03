# Plastic Graph Experiment Suite Analysis

This report compares controlled variants of the sparse plastic graph model. The goal is not merely to maximize MNIST accuracy; the goal is to identify which architectural mechanisms actually contribute to stable, generalizable online learning.

## How to read this

- **Best accuracy**: best recorded test accuracy. This is the headline performance metric.
- **Generalization gap**: latest train window accuracy minus latest test accuracy. A large positive gap suggests memorization or over-specialization.
- **Unique active**: average number of unique hidden units recruited across the recurrent traversal. If recurrence is active, this should usually exceed `active_hidden`.
- **Recurrent drive**: magnitude of hidden-to-hidden contribution. If this is near zero, the recurrent graph is present but not functionally important yet.

## Results

| Rank | Run | Best test acc | Latest test acc | Train acc | Gap | Unique active | Recurrent drive |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `no_reward_modulation` | 0.9285 | 0.9235 | 0.9820 | 0.0585 | 143.9700 | 5.9411 |
| 2 | `no_reward_modulation` | 0.9285 | 0.9235 | 0.9820 | 0.0585 | 143.9700 | 5.9411 |
| 3 | `no_recurrence_sparse_plastic_readout` | 0.9255 | 0.9240 | 0.9860 | 0.0620 | 128.0000 | 0.0000 |
| 4 | `no_recurrence_sparse_plastic_readout` | 0.9255 | 0.9240 | 0.9860 | 0.0620 | 128.0000 | 0.0000 |
| 5 | `full_recurrent_plastic_graph` | 0.9230 | 0.9205 | 0.9840 | 0.0635 | 134.5820 | 2.5558 |
| 6 | `full_recurrent_plastic_graph` | 0.9230 | 0.9205 | 0.9840 | 0.0635 | 134.5820 | 2.5558 |
| 7 | `frozen_input_projection` | 0.9225 | 0.9190 | 0.9840 | 0.0650 | 134.5040 | 2.5024 |
| 8 | `frozen_input_projection` | 0.9225 | 0.9190 | 0.9840 | 0.0650 | 134.5040 | 2.5024 |
| 9 | `no_homeostasis` | 0.8875 | 0.7555 | 0.7820 | 0.0265 | 241.4340 | 154.1024 |
| 10 | `no_homeostasis` | 0.8875 | 0.7595 | 0.7780 | 0.0185 | 241.1660 | 153.2890 |

## Interpretation framework

A variant is interesting if it improves test accuracy, improves learning speed, reduces the train/test gap, or demonstrates meaningful recurrent traversal without collapse. A higher training accuracy alone is not enough.

### What would support the biological/plastic-graph thesis?

1. The recurrent model beats the no-recurrence control or reaches the same accuracy with fewer active units.
2. The recurrent model shows non-trivial recurrent drive and higher unique-active recruitment.
3. The no-homeostasis variant has worse collapse, worse accuracy, or a larger generalization gap.
4. The frozen-input variant underperforms the full model, suggesting that input-side plasticity is doing real work.
5. The no-reward-modulation variant becomes less stable, less accurate, or overconfident.

### What would weaken the thesis?

If `no_recurrence_sparse_plastic_readout` performs essentially the same as the full recurrent model, then the current recurrent graph is not yet adding much. That would not kill the idea, but it would mean the next design needs stronger hidden-to-hidden dynamics, better recurrent credit assignment, or a task that requires multi-step traversal.
