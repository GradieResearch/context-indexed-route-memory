# Table 4: Exp15 Minimal Neural Comparator Hard-Slice Summary

Status: source-data-backed draft table for manuscript V2 hardening.

Source data:

- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
- Derived from `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`

Hard-slice definition:

- `world_count = 32`
- `route_length = 12`
- `n_seeds = 10`

| Variant | First-step context conflict | Retention after sequential worlds | Seen-route composition | Suffix-route composition | Transition accuracy | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `neural_gru_endpoint_context` | 0.0000 | 0.7015 | 0.9990 | 0.4040 | 0.0232 | Endpoint model memorizes seen supplied-context routes but shows weak reusable transition structure. |
| `neural_gru_endpoint_no_context` | 0.0000 | 0.0231 | 0.0312 | 0.0149 | 0.0009 | Endpoint model collapses without context. |
| `neural_gru_rollout_context` | 0.8794 | 0.0612 | 0.0448 | 0.0777 | 0.5122 | Learns some conflict-sensitive transition behavior but fails long rollout/composition in the fixed profile. |
| `neural_gru_rollout_no_context` | 0.0312 | 0.0222 | 0.0008 | 0.0437 | 0.4350 | Some transition learning, but no context-conflict resolution. |
| `neural_transformer_sequence_context` | 0.0000 | 0.3309 | 0.5435 | 0.1184 | 0.0070 | Partial endpoint learning with weak suffix/transition behavior. |
| `neural_transition_mlp_context` | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | Context-conditioned transition learner solves the clean hard slice. |
| `neural_transition_mlp_no_context` | 0.0312 | 0.5156 | 0.0312 | 1.0000 | 0.9193 | Solves many suffix transitions but fails first-step/full-route disambiguation. |
| `neural_transition_mlp_replay_context` | 0.0086 | 0.0005 | 0.0005 | 0.0004 | 0.0120 | Near-zero hard-slice performance; audit before scientific interpretation. |
| `neural_transition_mlp_world_heads_context` | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | Parameter-isolated transition learner solves the clean hard slice. |

Draft caption:

Minimal neural comparator on the hardest Exp15 summarized slice. Endpoint sequence models can perform well on seen full routes without learning reusable transition structure, while context-conditioned transition MLPs solve the clean transition-composition problem. No-context transition learning fails conflict-sensitive first-step and seen-route disambiguation despite solving suffix composition, showing that context is required for deliberately incompatible local mappings rather than for every suffix transition. The replay variant is shown for completeness but should not be interpreted until audited. Exp15 is a fixed-profile comparator, not an exhaustive neural architecture search.
