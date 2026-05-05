# Context-Indexed Route Memory

## What This Repository Contains

This repository contains a research project on context-indexed route-memory experiments. The work studies a controlled continual compositional route-memory benchmark where a model must store and execute multiple incompatible transition systems over the same state/action space.

Experiments live under `experiments/`. Each experiment directory is intended to be self-contained, with its own code, runner scripts, analysis scripts, `runs/`, generated artifacts, and README/run notes. Generated artifacts are preserved in the owning experiment directory as historical evidence.

Manuscript, evidence, synthesis, and repo-audit documents live under `docs/`. Active manuscript/evidence paths should use the current `experiments/...` prefix, for example `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`.

Detected experiment directories in this checkout:

- `experiments/experiment1/`
- `experiments/experiment2/`
- `experiments/experiment3/`
- `experiments/experiment4_successor/`
- `experiments/experiment5_contextual_successor/`
- `experiments/experiment6_route_audit_successor/`
- `experiments/experiment7_route_field_diagnostics/`
- `experiments/experiment8_self_organizing_route_acquisition/`
- `experiments/experiment9_robust_adaptive_route_plasticity/`
- `experiments/experiment10_adaptive_reversal/`
- `experiments/experiment11_context_memory/`
- `experiments/experiment12_capacity_generalization/`
- `experiments/experiment13_breaking_point/`

## Current Manuscript Status

The internal evidence is promising, but the manuscript is not submission-ready. Current blockers include Exp13.1 publication hardening, external baselines, statistical hardening, reproducible final figures, and careful prior-art positioning.

The current strongest internal result is the route-table/composition dissociation: no-recurrence variants can preserve one-step route memory while failing multi-step execution. This remains benchmark-specific and needs external comparison before submission claims are appropriate.

## Where To Start

- [Claims and evidence](docs/manuscript/CLAIMS_AND_EVIDENCE.md)
- [Figure plan](docs/manuscript/FIGURE_PLAN.md)
- [Limitations and threats](docs/manuscript/LIMITATIONS_AND_THREATS.md)
- [Publication readiness](docs/synthesis/PUBLICATION_READINESS.md)
- [Reproducibility audit](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)
- [Experiment registry](docs/experiments/EXPERIMENT_REGISTRY.md)

For documentation path checks, run:

```bash
python scripts/verify_doc_source_paths.py
```

## Non-Claims

The current repository does not claim solved continual learning, novelty of context gating by itself, a complete hippocampal theory, end-to-end perception, or broad abstract rule induction.

## Working Rules

See [AGENTS.md](AGENTS.md) for repository rules. In short: keep experiments under `experiments/`, keep runs immutable, do not modify older experiment directories to answer new scientific questions, and keep active documentation source paths resolvable or explicitly marked as planned/missing/local verification pending.

## License

TODO: Add license. Until a license is added, reuse rights are not formally granted.
