# Experiment 11 Analysis - Context-Separated Memory and Non-Destructive Rebinding

Experiment 11 tests whether higher-order world context can separate multiple route systems over the same source/mode substrate. It measures old-world retention while a new world is learned, alternating-world stability, multi-world scaling, and retrieval robustness under world-context bleed/dropout.

## Final sequential memory indices

| run_name                            |   retention_A_after_B |   acquisition_B_after_A |   route_retention_A_after_B |   route_acquisition_B_after_A |   world_margin_A_after_B |   world_margin_B_after_A |
|:------------------------------------|----------------------:|------------------------:|----------------------------:|------------------------------:|-------------------------:|-------------------------:|
| exp11_full_context_separated_memory |             1         |               1         |                    1        |                       1       |              0.410064    |              2.16018     |
| exp11_no_structural_plasticity      |             0.0972222 |               0.0902778 |                    0.046875 |                       0.03125 |             -3.17908e-06 |             -5.35534e-06 |
| exp11_no_world_context              |             0.25      |               1         |                    0.375    |                       1       |            nan           |            nan           |
| exp11_world_gated_plasticity        |             1         |               1         |                    1        |                       1       |              0.387551    |              3.00865     |


## Generated outputs

- `exp11_alternating_composition.png`
- `exp11_alternating_route_table.png`
- `exp11_alternating_world_margin.png`
- `exp11_context_bleed_composition.png`
- `exp11_context_bleed_world_margin.png`
- `exp11_context_bleed_wrong_world_activation.png`
- `exp11_context_dropout_composition.png`
- `exp11_context_dropout_world_margin.png`
- `exp11_context_dropout_wrong_world_activation.png`
- `exp11_failure_taxonomy_final_sequential.png`
- `exp11_scaling_final_composition.png`
- `exp11_scaling_final_route_table.png`
- `exp11_scaling_final_world_margin.png`
- `exp11_scaling_final_wrong_world_activation.png`
- `exp11_sequential_composition.png`
- `exp11_sequential_correct_margin.png`
- `exp11_sequential_route_table.png`
- `exp11_sequential_world_margin.png`
- `exp11_sequential_wrong_world_activation.png`


## Interpretation guide

- `retention_A_after_B` measures whether world A remains accessible after world B training without A rehearsal.

- `acquisition_B_after_A` measures whether the new world is acquired after A.

- `composition_mean_world_margin` and `composition_mean_wrong_world_activation` indicate whether the correct world context suppresses other route worlds.

- `exp11_no_world_context` and `exp11_shared_edges_only` should overwrite/collide.

- `exp11_world_gated_plasticity` is the strongest test of non-destructive world-specific updates.
