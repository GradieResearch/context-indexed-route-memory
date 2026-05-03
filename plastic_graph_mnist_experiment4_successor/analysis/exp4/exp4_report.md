# Experiment 4 Analysis — Successor Traversal

This experiment asks a sharper question than MNIST: can a recurrent plastic graph learn a local successor transition and compose it repeatedly to solve addition-like tasks it was not directly trained on?

## Summary table

|   run_id | run_name                      | status    |   best_accuracy |   best_addition_accuracy |   best_transition_accuracy |   addition/accuracy |   addition/accuracy_steps_2 |   addition/accuracy_steps_3 |   addition/accuracy_steps_4 |   addition/accuracy_steps_5 |   addition/average_confidence |   addition/average_recurrent_drive |   addition/average_steps |   addition/average_unique_active |   train/recent_after_transition_accuracy |   transition/accuracy |   transition/average_confidence |   transition/average_recurrent_drive |   transition/average_unique_active |
|---------:|:------------------------------|:----------|----------------:|-------------------------:|---------------------------:|--------------------:|----------------------------:|----------------------------:|----------------------------:|----------------------------:|------------------------------:|-----------------------------------:|-------------------------:|---------------------------------:|-----------------------------------------:|----------------------:|--------------------------------:|-------------------------------------:|-----------------------------------:|
|        1 | exp4_full_traversal           | completed |       1         |                1         |                  1         |           1         |                   1         |                   1         |                    1        |                           1 |                      0.999516 |                            811.363 |                  3.44186 |                          407.105 |                                     1    |             1         |                       0.999566  |                              814.488 |                            189.792 |
|        5 | exp4_no_reward_gate           | completed |       1         |                1         |                  1         |           1         |                   1         |                   1         |                    1        |                           1 |                      1        |                            812.869 |                  3.44186 |                          407.093 |                                     1    |             1         |                       1         |                              815.903 |                            189.792 |
|        4 | exp4_no_homeostasis           | completed |       1         |                1         |                  1         |           1         |                   1         |                   1         |                    1        |                           1 |                      1        |                            825.62  |                  3.44186 |                          407.093 |                                     1    |             1         |                       1         |                              828.09  |                            189.792 |
|        3 | exp4_no_structural_plasticity | completed |       0.0348837 |                0.0348837 |                  0.0416667 |           0.0348837 |                   0.0434783 |                   0.0454545 |                    0.047619 |                           0 |                      0.014656 |                            128.721 |                  3.44186 |                          402.43  |                                     0.04 |             0.0416667 |                       0.0230035 |                              130.299 |                            191.917 |
|        2 | exp4_no_recurrence            | completed |       0         |                0         |                  0         |           0         |                   0         |                   0         |                    0        |                           0 |                      1        |                              0     |                  3.44186 |                           96     |                                     0    |             0         |                       1         |                                0     |                             96     |

## Interpretation framework

A strong result would show `exp4_full_traversal` beating `exp4_no_recurrence` on multi-step addition, not merely matching it on one-step transitions.

Key things to inspect:

- `best_addition_accuracy`: whether traversal composes beyond single-step memory.
- `addition/accuracy_steps_2+`: whether performance degrades gracefully with path length.
- `addition/average_recurrent_drive`: whether recurrent edges are functionally active.
- `addition/average_unique_active`: whether recurrence recruits additional assemblies rather than collapsing.
- `exp4_no_structural_plasticity`: tests whether edge rewiring/growth is load-bearing.
- `exp4_no_homeostasis`: tests whether activity regulation prevents runaway spread.
