# Manuscript Spine

Purpose: Define the provisional structure of the first manuscript and keep every section tied to explicit evidence rather than thread memory.

## Provisional Framing

Claim: The current manuscript framing is benchmark-specific and internally supported, but not submission-ready without baselines and hardening:

> A synthetic continual compositional route-memory benchmark shows that context-indexed structural plasticity can store incompatible local transition systems without destructive overwriting, while recurrent dynamics are required to convert one-step route memories into multi-step execution.

Evidence: C1-C5 in the central evidence map are supported by Exp8/Exp11/Exp12/Exp13 internal ablation and capacity artifacts.
Caveat: External baselines, statistical hardening, and novelty-source import remain pending; do not present this as solved continual learning or biological theory.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

## Working outline

1. Motivation and benchmark definition. Source path: `Experiment.md`; `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md`.
2. Mechanism: structural plasticity, context indexing, recurrence, and route fields. Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
3. Core ablations. Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
4. Continual memory and capacity. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
5. Breaking points and caveats. Source path: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md`.
6. Limitations and non-claims. Source path: `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
