# Context-Indexed Route Memory

## What this repository contains

This repository contains a research project on context-indexed route-memory experiments. It studies a controlled continual compositional route-memory benchmark where a model must store and execute multiple incompatible transition systems over the same state and action space.

Experiments live under `experiments/`. Each experiment directory is intended to be self-contained, with its own code, runner scripts, analysis scripts, generated reports, `runs/`, and `analysis/` outputs as needed. Generated analysis artifacts are preserved as historical evidence rather than deleted or overwritten.

Manuscript, evidence, synthesis, and repo-audit documents live under `docs/`. This is an active manuscript-preparation repository, so active source paths in evidence docs should use the current `experiments/...` prefix and should resolve locally unless they are explicitly marked planned, missing, future, or local verification pending.

## Current status

The internal evidence is promising, but the repository is not submission-ready. Current blockers include the separate Exp13.2 baseline import/alignment pass, seed-level uncertainty reporting, final reproducible paper figures, prior-art import, command verification, and license/citation metadata.

The strongest internal result so far is benchmark-specific: context-indexed structural route memory can retain incompatible local transition systems, while recurrence is needed to turn one-step route memories into multi-step execution. This needs external comparison before submission-level claims are appropriate.

## Scientific question

The central question is whether a system can continually store many route memories that reuse the same states and actions but require different transitions in different contexts. For example, the same symbolic action can mean different successor transitions in world A, world B, and world C.

The benchmark separates three things that are easy to conflate: one-step route-table storage, selection of the right world/context, and recurrent multi-step execution over stored transitions. This lets the project ask whether failures come from storage, context interference, missing recurrence, finite capacity, corrupted context, or missing primitive transitions.

The narrow scientific question for the first manuscript is: in this controlled route-memory benchmark, does the conjunction of context-indexed structural plasticity and recurrent execution support non-destructive storage and compositional execution of incompatible route systems, and where does it fail?

## Repository layout

```text
experiments/  self-contained experiment directories and generated artifacts
docs/         manuscript, evidence, synthesis, source-data, and repo-audit docs
scripts/      repository utilities, including documentation path verification
AGENTS.md     repository working rules for local agents
README.md     external-facing repository entry point
```

## Where to start

- [Documentation index](docs/README.md)
- [Claims and evidence](docs/manuscript/CLAIMS_AND_EVIDENCE.md)
- [Source of truth](docs/manuscript/SOURCE_OF_TRUTH.md)
- [Figure plan](docs/manuscript/FIGURE_PLAN.md)
- [Limitations and threats](docs/manuscript/LIMITATIONS_AND_THREATS.md)
- [Publication readiness](docs/synthesis/PUBLICATION_READINESS.md)
- [Next experiments](docs/synthesis/NEXT_EXPERIMENTS.md)
- [Reproducibility audit](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)
- [Experiment registry](docs/experiments/EXPERIMENT_REGISTRY.md)
- [Historical experiment tiers](docs/experiments/HISTORICAL_EXPERIMENTS.md)

## Experiment overview

| Experiment | Directory | Role | Status / manuscript relevance |
|---|---|---|---|
| Exp1 | `experiments/experiment1/` | Early MNIST plastic-graph prototype. | Historical; not central to route-memory claims. |
| Exp2 | `experiments/experiment2/` | Persistent plastic-graph MNIST exploration. | Historical/local evidence only. |
| Exp3 | `experiments/experiment3/` | Recurrent MNIST and controlled variants. | Historical context for recurrence exploration. |
| Exp4 | `experiments/experiment4_successor/` | Successor traversal and route-composition foundation. | Precursor evidence; not the main context-memory result. |
| Exp5 | `experiments/experiment5_contextual_successor/` | Contextual successor attempt. | Caveated predecessor; useful for failure history. |
| Exp6 | `experiments/experiment6_route_audit_successor/` | Route-audit correction of contextual successor task. | Methodological precursor; caveated. |
| Exp7 | `experiments/experiment7_route_field_diagnostics/` | Clean route-field diagnostic. | Supports route-table versus execution distinction as diagnostic evidence. |
| Exp8 | `experiments/experiment8_self_organizing_route_acquisition/` | Self-organizing route acquisition. | Important internal ablation evidence; needs baselines before central claims. |
| Exp9 | `experiments/experiment9_robust_adaptive_route_plasticity/` | Robustness, context bleed, delayed/noisy feedback. | Supporting stress-test evidence; claims remain narrow. |
| Exp10 | `experiments/experiment10_adaptive_reversal/` | Adaptive reversal and consolidation tradeoff. | Supporting evidence for stability/plasticity caveats. |
| Exp11 | `experiments/experiment11_context_memory/` | Context-separated incompatible-world memory. | Manuscript-critical internal evidence. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | Capacity, retention, and held-out composition scaling. | Manuscript-critical internal evidence; ceiling-limited. |
| Exp13 | `experiments/experiment13_breaking_point/` | Breaking point, context corruption, holdout boundary, continuous bridge. | Manuscript-critical boundary evidence; holdout and context-corruption caveats remain. |
| Exp13.1 | `experiments/experiment13_1_publication_hardening/` | Publication-hardening ablations and mechanism audit. | Manuscript-critical internal evidence; lesion diagnostic failed expected pattern and must not be used as positive evidence without audit/rerun. |

## Current claim map

The canonical claim table is [CLAIMS_AND_EVIDENCE.md](docs/manuscript/CLAIMS_AND_EVIDENCE.md). At a high level:

| Claim IDs | Current interpretation | Status |
|---|---|---|
| C1-C4 | Structural plasticity, world/context indexing, recurrence, and route-table/execution separation are supported inside the route-memory benchmark. | Strong internal ablation evidence; needs external baselines. |
| C5-C7 | Exp12 shows clean-context scaling; Exp13 and Exp13.1 map finite-capacity/local-budget failure. | Promising but needs uncertainty, final scripts, and capacity-law cleanup. |
| C8 | Consolidation is best framed as a stability/plasticity bias. | Preliminary; needs dose-response. |
| C9 | The model composes stored primitives but does not infer unseen primitive transitions. | Needs metric cleanup. |
| C10 | Adversarial context corruption can break execution when world selection flips. | Promising; stochastic corruption remains pending. |
| C11 | Continuous/noisy inputs can feed route memory through a simple decoded bridge. | Preliminary or supplementary. |
| C12 | Baselines and prior-art positioning are required before submission readiness. | Needs separate Exp13.2 import/alignment and novelty-source import. |

Every manuscript-facing use should retain the discipline: Claim -> Evidence -> Caveat -> Source path.

## Non-claims

This repository does not yet show:

- solved continual learning;
- that context gating is novel by itself;
- a complete hippocampal or biological theory;
- end-to-end perceptual learning;
- broad abstract rule induction;
- inference of unseen primitive transitions.

## Reproducibility

See [REPRODUCIBILITY_AUDIT.md](docs/repo_audit/REPRODUCIBILITY_AUDIT.md). Commands are being standardized, but early experiments may not follow the final `smoke` / `standard` / `full` interface. Manuscript-critical experiments currently have clearer launch paths than historical experiments.

To check active documentation source paths, run:

```bash
python scripts/verify_doc_source_paths.py
```

## Planned next work

The next planned manuscript-readiness step is a separate Exp13.2 baseline analysis/import/alignment pass, followed by seed-level uncertainty reporting and final figure workflows. A richer applied visual-state bridge should wait until baseline integration, uncertainty reporting, prior-art positioning, and final figure workflows are hardened.

## License / citation

TODO: Add a license and citation instructions. Until a license is added, reuse rights are not formally granted.
