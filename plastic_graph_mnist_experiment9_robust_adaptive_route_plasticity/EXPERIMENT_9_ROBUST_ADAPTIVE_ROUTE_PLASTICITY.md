# Experiment 9 — Robust Adaptive Route Plasticity

Experiment 8 showed that a local plastic graph can acquire a context-conditioned route field from one-step transition exposure, then use recurrence to compose unseen multi-step paths.

Experiment 9 asks the next question:

> Can the graph preserve, repair, and adapt those routes when context is unreliable and feedback is imperfect or delayed?

This experiment is intentionally still symbolic. The goal is not to make the problem more semantically rich. The goal is to stress the mechanism that Experiment 8 validated.

## Research questions

### 9A — Interference robustness

Does inhibition protect context-bound routes when competing context assemblies are partially active?

The main stressor is `context_bleed`: a fraction of the wrong mode and wrong source-mode pair assemblies are injected into the active context.

Expected pattern:

| Variant | Expected result |
|---|---|
| `exp9_full_interference_robust` | Best preservation of route-table accuracy, margins, and composition |
| `exp9_no_inhibition` | Similar at low bleed, earlier margin/accuracy degradation at higher bleed |
| `exp9_no_context_binding` | Route collision and poor composition |
| `exp9_no_structural_plasticity` | Near-random route acquisition |

### 9B — Noisy and delayed feedback

Does reward gating and eligibility-style credit assignment matter when feedback becomes unreliable or delayed?

The stressors are:

- `feedback_noise`: probability of corrupting a transition target during training.
- `reward_delay_steps`: number of training events by which feedback is delayed.

Expected pattern:

| Variant | Expected result |
|---|---|
| `exp9_full_reward_robust` | Robust under noise/delay because bad feedback is gated and delayed feedback is assigned to the eligible source-mode pair |
| `exp9_no_reward_gate` | Learns wrong edges under noisy feedback |
| `exp9_no_eligibility_trace` | Misassigns delayed feedback to the wrong active source-mode pair |
| `exp9_no_structural_plasticity` | Near-random acquisition |
| `exp9_no_recurrence` | Learns one-step transitions but fails multi-step composition |

## Metrics

- `transition/accuracy`: one-step route acquisition.
- `composition/accuracy`: unseen multi-step recurrent traversal.
- `route_table/accuracy`: direct inspection of the learned local route field.
- `mean_target_rank`: whether the correct target is near the top even when argmax is wrong.
- `mean_correct_margin`: correct target score minus strongest wrong target.
- `mean_context_margin`: correct-mode support minus strongest wrong-mode support for the same target.
- `mean_wrong_route_activation`: bounded proxy for competing route activation.
- Failure taxonomy: first-step failures, mid-route drift, no-recurrence single-step-only failures.

## Default legitimate run

The provided `start.ps1` runs both phases:

```powershell
python .\run_exp9_suite.py `
  --max-number 31 `
  --max-steps 8 `
  --transition-train-repeats 1 `
  --seeds 30 `
  --context-bleed-sweep "0 0.05 0.10 0.20 0.35 0.50" `
  --feedback-noise-sweep "0 0.05 0.10 0.20 0.30" `
  --reward-delay-sweep "0 2 4" `
  --force
```

This is a heavier run than Experiment 8 because it sweeps stress levels.
