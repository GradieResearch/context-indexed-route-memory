# Experiment 2: Persistent Plastic Graph MNIST Prototype

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; no non-empty Exp2-specific result digest was available
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: empty `docs/threads/experiment1to4_export.md`; background mentions only
- Manuscript relevance: Historical/supplemental MNIST learning evidence.

## Purpose

This is a research prototype for a **persistent plastic graph network**: a sparse, stateful, reward-modulated learning substrate trained on MNIST. It is intentionally not a giant monolithic neural-network script. The core pieces are separated: - `config.py` - experiment configuration - `storage.py` - SQLite/SQLAlchemy persistence for runs, metrics, checkpoints - `data.py` - MNIST loading - `plastic_graph.py` - sparse adaptive graph substrate - `modulators.py` - reward/novelty/confidence plasticity gates - `trainer.py` - experiment loop - `run_mnist_experiment.py` - composition/root script Or use the included helper scripts: Results are persisted to `runs/plastic_graph_mnist.sqlite3` by defau

Source path: `experiments/experiment2/README.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment2/README.md`
- Task/design clue: This is a research prototype for a **persistent plastic graph network**: a sparse, stateful, reward-modulated learning substrate trained on MNIST. It is intentionally not a giant monolithic neural-network script. The core pieces are separated: - `config.py` - experiment configuration - `storage.py` - SQLite/SQLAlchemy persistence for runs, metrics, checkpoints - `data.py` - MNIST loading - `plastic_graph.py` - sparse adaptive graph substrate - `modulators.py` - reward/novelty/confidence plasticity gates - `trainer.py` - experiment loop - `run_mnist_experiment.py` - composition/root script Or use the included helper scripts: Results are persisted to `runs/plastic_graph_mnist.sqlite3` by defau
- Run scripts detected: `experiments/experiment2/run_mnist_experiment.py`, `experiments/experiment2/start.ps1`, `experiments/experiment2/start.sh`
- Analysis CSVs detected: 1; plot files detected: 4; generated/design reports detected: 1.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment2/analysis/analysis_report.md`: - Name: `plastic_graph_mnist` - Status: `completed` - Started: `2026-05-01 12:54:33.292616` - Completed: `2026-05-01 12:55:21.868298` - Recorded best accuracy: `0.9225` - Best test accuracy: **0.9225** at step `27500` / epoch `3` - Latest test/accuracy: `0.9190` at step `30000` - Latest test/average_confidence: `0.8309` at step `30000` - Latest train/average_confidence: `0.8979` at step `30000` - Latest train/window_

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| TODO | TODO: no summary metrics detected | TODO | TODO | Metrics may exist only inside SQLite or require analysis regeneration. |

## Key results

### Result 1: Completed MNIST prototype run

Claim: Exp2 has a completed MNIST prototype run with best reported test accuracy 0.9225.
Evidence: The generated analysis report states best test accuracy 0.9225 at step 27500 and latest test accuracy 0.9190 at step 30000.
Caveat: Single prototype run; MNIST does not test route-memory composition.
Source path: `experiments/experiment2/analysis/analysis_report.md`

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
| `experiments/experiment2/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment2/run_mnist_experiment.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment2/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment2/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/analysis_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/test_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/test_average_confidence.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/train_average_confidence.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment2/analysis/train_window_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| test accuracy | `experiments/experiment2/analysis/test_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| test average confidence | `experiments/experiment2/analysis/test_average_confidence.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| train average confidence | `experiments/experiment2/analysis/train_average_confidence.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| train window accuracy | `experiments/experiment2/analysis/train_window_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment1to4_export.md`

Completed result / design / caveat / decision: No importable content.
Evidence: The digest file is present but empty.
Caveat: No Exp2 scientific claim was imported from this file.
Source thread: `docs/threads/experiment1to4_export.md`
Related local artifact path: `experiments/experiment2/analysis/analysis_report.md`
Status: Historical only

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Background only.
Evidence: The thread lists Exp1/Exp2 as sparse plastic MNIST baseline experiments and does not analyze them.
Caveat: Thread-derived claim; local artifact support pending for detailed Exp2 interpretation.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment2/analysis/analysis_report.md`
Status: Historical only

## Key results (thread-integrated)

No thread-derived route-memory result is imported for Exp2.

## What this experiment supports (thread-integrated)

- Historical MNIST/plastic-graph context only.

## What this experiment does not prove (thread-integrated)

- It does not support the manuscript's context-indexed route-memory claims.

## Follow-up actions (thread-integrated)

- Keep Exp2 as historical/supplemental unless early MNIST results are separately reviewed.
