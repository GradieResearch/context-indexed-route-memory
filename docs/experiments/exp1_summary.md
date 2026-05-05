# Experiment 1: Persistent Plastic Graph MNIST Prototype

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; no non-empty Exp1-specific result digest was available
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: no
- Validation present: no
- Thread digest present: empty `docs/threads/experiment1to4_export.md`; background mentions only
- Manuscript relevance: Historical implementation background; not a manuscript result without analysis.

## Purpose

This is a research prototype for a **persistent plastic graph network**: a sparse, stateful, reward-modulated learning substrate trained on MNIST. It is intentionally not a giant monolithic neural-network script. The core pieces are separated: - `config.py` - experiment configuration - `storage.py` - SQLite/SQLAlchemy persistence for runs, metrics, checkpoints - `data.py` - MNIST loading - `plastic_graph.py` - sparse adaptive graph substrate - `modulators.py` - reward/novelty/confidence plasticity gates - `trainer.py` - experiment loop - `run_mnist_experiment.py` - composition/root script Or use the included helper scripts: Results are persisted to `runs/plastic_graph_mnist.sqlite3` by defau

Source path: `experiments/experiment1/README.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment1/README.md`
- Task/design clue: This is a research prototype for a **persistent plastic graph network**: a sparse, stateful, reward-modulated learning substrate trained on MNIST. It is intentionally not a giant monolithic neural-network script. The core pieces are separated: - `config.py` - experiment configuration - `storage.py` - SQLite/SQLAlchemy persistence for runs, metrics, checkpoints - `data.py` - MNIST loading - `plastic_graph.py` - sparse adaptive graph substrate - `modulators.py` - reward/novelty/confidence plasticity gates - `trainer.py` - experiment loop - `run_mnist_experiment.py` - composition/root script Or use the included helper scripts: Results are persisted to `runs/plastic_graph_mnist.sqlite3` by defau
- Run scripts detected: `experiments/experiment1/run_mnist_experiment.py`, `experiments/experiment1/start.ps1`, `experiments/experiment1/start.sh`
- Analysis CSVs detected: 0; plot files detected: 0; generated/design reports detected: 0.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- TODO: no generated report/design doc summary detected.

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| TODO | TODO: no summary metrics detected | TODO | TODO | Metrics may exist only inside SQLite or require analysis regeneration. |

## Key results

### Result 1: No generated local result report detected

Claim: TODO: no result claim is made for Exp1 in this pass.
Evidence: README and run database are present, but no generated metrics/report files were detected in the local artifact inventory.
Caveat: A SQLite run artifact may contain results, but no report/CSV has been consolidated here.
Source path: `experiments/experiment1/README.md`; `experiments/experiment1/runs/plastic_graph_mnist.sqlite3`

## What this experiment supports

- Local evidence summarized above; final supported-claim language must be imported into `docs/manuscript/CLAIMS_AND_EVIDENCE.md` after human/thread review.

## What this experiment does not prove

- Does not establish novelty by itself.
- Does not remove the need for baseline and reproducibility review.

## Known implementation or interpretation caveats

- Thread digest has not been reviewed.
- Check run profile, seeds, and aggregation before manuscript use.

## Artifacts

| Path | Type | Description | Manuscript relevance | Notes |
| --- | --- | --- | --- | --- |
| `experiments/experiment1/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment1/run_mnist_experiment.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment1/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment1/start.sh` | script | Launcher | low | Indexed locally; review before citing. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| TODO | TODO | TODO | No plot artifact detected. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment1to4_export.md`

Completed result / design / caveat / decision: No importable content.
Evidence: The digest file is present but empty.
Caveat: No Exp1 scientific claim was imported from this file.
Source thread: `docs/threads/experiment1to4_export.md`
Related local artifact path: `experiments/experiment1/README.md`
Status: Historical only

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Background only.
Evidence: The thread lists Exp1/Exp2 as sparse plastic MNIST baseline experiments and does not analyze them.
Caveat: Thread-derived claim; local artifact support pending for any detailed Exp1 result.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment1/README.md`
Status: Historical only

## Key results (thread-integrated)

No thread-derived result is imported for Exp1.

## What this experiment supports (thread-integrated)

- Historical background for the project only.

## What this experiment does not prove (thread-integrated)

- It does not support route-memory, context-indexing, recurrence-composition, or capacity claims in the first manuscript.

## Follow-up actions (thread-integrated)

- Keep Exp1 out of central manuscript claims unless a non-empty Exp1 digest or local analysis is added.
