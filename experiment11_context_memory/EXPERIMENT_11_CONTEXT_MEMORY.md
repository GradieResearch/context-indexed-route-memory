# Experiment 11 — Context-Separated Memory and Non-Destructive Rebinding

## Motivation

Experiments 7–9 established a route-field mechanism:

```text
structural plasticity -> route acquisition
context binding       -> route separation
recurrence            -> route composition
inhibition            -> interference robustness
eligibility trace     -> delayed feedback assignment
reward gating         -> noisy feedback robustness
```

Experiment 10 showed adaptive rule reversal. A learned route field can be rebound when mode meanings change, and consolidation controls the stability-plasticity tradeoff. But the strongest ordinary reversal behavior was still mostly overwrite: new rule B replaced old rule A under the same context labels.

Experiment 11 tests whether a higher-level world context allows multiple rule systems to coexist without destructive overwrite.

## Hypothesis

A higher-order context signal can bind route fields into separable memory worlds, allowing the same mode labels to have different transition semantics in different task contexts.

## Rule worlds

```text
World A: minus_one=-1, plus_one=+1, plus_two=+2
World B: minus_one=+1, plus_one=-1, plus_two=+2
World C: minus_one=+1, plus_one=+2, plus_two=-1
World D: minus_one=-1, plus_one=-2, plus_two=+1
```

## Variants

| Variant | Purpose |
|---|---|
| `exp11_full_context_separated_memory` | Main model with world-specific route fields and modest shared substrate |
| `exp11_world_gated_plasticity` | Strongest non-destructive update: only active world-specific routes are modified |
| `exp11_no_world_context` | Tests collapse when world identity is unavailable |
| `exp11_no_recurrence` | Tests whether composition requires recurrent traversal rather than a single transition |
| `exp11_no_context_binding` | Tests route collision when mode/world binding is weakened |
| `exp11_no_inhibition` | Tests wrong-world and wrong-mode suppression |
| `exp11_no_structural_plasticity` | Tests whether route fields can form without plasticity |
| `exp11_no_consolidation` | Fast learning with weaker retention pressure |
| `exp11_strong_consolidation` | Strong retention, slower new-world acquisition |
| `exp11_shared_edges_only` | Tests collision when all worlds share route edges |

## Phases

### 11A — Sequential dual-world retention

Train A, consolidate, then train B while continuing to evaluate both A and B.

Success requires B acquisition without A collapse.

### 11B — Alternating worlds

Train A and B in alternating cycles.

Success requires both worlds to remain high simultaneously.

### 11C — Multi-world scaling

Sequentially add A, B, C, D and evaluate all worlds after each addition.

Success requires graceful degradation rather than catastrophic collapse.

### 11D — Retrieval robustness

Train A/B, then evaluate under world-context bleed and dropout.

Success requires high accuracy and strong world margins under moderate context corruption.

## Primary metrics

- `composition/accuracy`
- `route/route_table_accuracy`
- `composition/mean_correct_margin`
- `composition/mean_world_margin`
- `composition/mean_wrong_world_activation`
- `retention_A_after_B`
- `acquisition_B_after_A`
- failure taxonomy: first-step failure, mid-route drift, no-recurrence single-step only

## Interpretation

A strong result is not simply high final B accuracy. The important result is simultaneous high A retention and B acquisition under explicit world context, with failure in no-world-context/shared-edge controls.
