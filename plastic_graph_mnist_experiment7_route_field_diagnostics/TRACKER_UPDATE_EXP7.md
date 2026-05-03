```text
Date: 2026-05-02
Experiment: Exp7 Route Field Diagnostics
Run names:
- exp7_full_route_field
- exp7_no_recurrence
- exp7_no_context_binding
- exp7_no_structural_plasticity
- exp7_no_inhibition
- exp7_context_bleed
- exp7_noisy_plasticity

Config highlights:
A small bounded contextual successor world with explicit route-field diagnostics. The suite separates one-step transition learning from recurrent multi-step composition and reports target-rank, correct-route margin, context margin, wrong-route activation, deterministic baselines, and learned transition-table inspection.

Key result:
Implementation completed. The included default run shows the diagnostic scaffold can clearly separate local transition learning, recurrent composition, context binding, and structural plasticity failure modes.

What changed our belief:
Experiment 7 is now a mechanism-inspection bridge between Exp5 and any harder follow-up. It should be used before escalating to noisy feedback, rule reversal, or multimodal grounding.

Next action:
Run Experiment 7 in the real repository environment, inspect analysis/exp7/exp7_report.md, then port the same diagnostics back onto the richer Experiment 5 hidden-assembly implementation.
```
