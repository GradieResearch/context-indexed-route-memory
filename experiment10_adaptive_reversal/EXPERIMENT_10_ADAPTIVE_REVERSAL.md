# Experiment 10 — Rule Reversal, Retention, and Adaptive Rebinding

## Purpose

Experiment 10 tests the next unresolved question after Experiment 9:

> Can a graph change a learned route system without destroying itself?

Experiments 7–9 established the mechanism stack:

- clean route fields compose recurrently;
- local structural plasticity can self-organize those route fields from one-step experience;
- context binding separates route families;
- inhibition protects route margins under context interference;
- reward gating and eligibility traces become load-bearing under noisy or delayed feedback.

Experiment 10 now probes the stability-plasticity tradeoff. The model first learns rule set A, then the mode meanings are changed to rule set B. We measure new-rule adaptation, old-rule retention, interference, and switchback behavior.

## Rule sets

Rule set A:

```text
minus_one -> n - 1
plus_one  -> n + 1
plus_two  -> n + 2
```

Rule set B:

```text
minus_one -> n + 1
plus_one  -> n - 1
plus_two  -> n + 2
```

`plus_two` remains unchanged as an anchor. This lets us distinguish targeted mode remapping from global route-field collapse.

## Phases

### 10A — Clean abrupt reversal

The graph learns rule A from one-step transitions, then receives one-step rule B transitions. Multi-step rule B composition is evaluated without direct multi-step training.

### 10B — Consolidation tradeoff

Variants compare no consolidation, balanced consolidation, and strong consolidation. The goal is to measure whether old routes are preserved at the cost of slower new-rule adaptation.

### 10C — Dual-context worlds

The `exp10_dual_context_worlds` variant adds a higher-level rule context so the graph can potentially preserve both A and B instead of overwriting the same route field.

### 10D — Switchback

After learning B, the graph trains again on A. This tests whether old routes were retained latently and whether reacquisition is faster or cleaner than first learning.

## Core variants

| Variant | Purpose |
|---|---|
| `exp10_full_adaptive_reversal` | Main balanced model |
| `exp10_no_consolidation` | Fast adaptation but likely catastrophic forgetting |
| `exp10_strong_consolidation` | Old-route protection but slower adaptation |
| `exp10_dual_context_worlds` | Preserve A and B through hierarchical context |
| `exp10_no_inhibition` | Test old-route interference |
| `exp10_no_reward_gate` | Test noisy reversal feedback |
| `exp10_no_eligibility_trace` | Test delayed feedback assignment |
| `exp10_no_homeostasis` | Test stability under repeated updates |
| `exp10_no_structural_plasticity` | Negative control for route acquisition/adaptation |

## Main metrics

- old-rule route-table accuracy;
- new-rule route-table accuracy;
- old-rule composition accuracy;
- new-rule composition accuracy;
- correct-route margin;
- context margin;
- wrong-route activation;
- adaptation half-life;
- threshold to 80% new-rule composition;
- failure taxonomy;
- switchback reacquisition.

## Important interpretation

This experiment should not be judged only by final new-rule accuracy. The shape of the adaptation curve matters. A model that instantly overwrites B but fully destroys A is different from one that learns B while retaining latent A structure. The best result would show a measurable, controllable tradeoff between plasticity and retention.
