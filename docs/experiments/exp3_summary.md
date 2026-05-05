# Experiment 3: Persistent Plastic Graph MNIST Experiments

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; background-only thread mentions imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: empty `docs/threads/experiment1to4_export.md`; background mentions in `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Historical/supplemental MNIST ablation evidence.

## Purpose

This project is a small experimental framework for testing a biologically inspired learning-machine idea: > Instead of treating a model as a dense static sea of matrices, treat it as a sparse persistent graph of adaptive units whose active pathways can be reinforced, weakened, and inspected over time. This is **not** intended to beat CNNs on MNIST. MNIST is used because it gives us a clean, cheap proving ground for the learning dynamics. Can a small sparse graph substrate learn useful behavior through online reward-modulated plasticity? More specifically, can it: 1. Activate only a small subset of units per example. 2. Learn from immediate `yes/no` correction. 3. Strengthen useful active pat

Source path: `experiments/experiment3/README.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment3/README.md`
- Task/design clue: This project is a small experimental framework for testing a biologically inspired learning-machine idea: > Instead of treating a model as a dense static sea of matrices, treat it as a sparse persistent graph of adaptive units whose active pathways can be reinforced, weakened, and inspected over time. This is **not** intended to beat CNNs on MNIST. MNIST is used because it gives us a clean, cheap proving ground for the learning dynamics. Can a small sparse graph substrate learn useful behavior through online reward-modulated plasticity? More specifically, can it: 1. Activate only a small subset of units per example. 2. Learn from immediate `yes/no` correction. 3. Strengthen useful active pat
- Run scripts detected: `experiments/experiment3/run_experiment_suite.py`, `experiments/experiment3/run_mnist_experiment.py`, `experiments/experiment3/start.ps1`, `experiments/experiment3/start.sh`
- Analysis CSVs detected: 1; plot files detected: 1; generated/design reports detected: 1.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment3/analysis/suite/suite_report.md`: This report compares controlled variants of the sparse plastic graph model. The goal is not merely to maximize MNIST accuracy; the goal is to identify which architectural mechanisms actually contribute to stable, generalizable online learning. - **Best accuracy**: best recorded test accuracy. This is the headline performance metric. - **Generalization gap**: latest train window accuracy minus latest test accuracy. A

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| full_recurrent_plastic_graph | Reference/full mechanism | TODO: import intended expectation from thread digest | TODO: inspect metric rows | `experiments/experiment3/analysis/suite/suite_comparison.csv` |
| no_recurrence_sparse_plastic_readout | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | TODO: inspect metric rows | `experiments/experiment3/analysis/suite/suite_comparison.csv` |
| frozen_input_projection | TODO: infer mechanism from design doc/thread digest | TODO: import intended expectation from thread digest | TODO: inspect metric rows | `experiments/experiment3/analysis/suite/suite_comparison.csv` |
| no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | TODO: inspect metric rows | `experiments/experiment3/analysis/suite/suite_comparison.csv` |
| no_reward_modulation | Removes reward gating | TODO: import intended expectation from thread digest | TODO: inspect metric rows | `experiments/experiment3/analysis/suite/suite_comparison.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| best_accuracy | Best recorded task accuracy in a run. | Generated analysis CSV/report | `experiments/experiment3/analysis/suite/suite_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: MNIST ablations do not isolate recurrent traversal

Claim: The Exp3 suite report shows no-recurrence and no-reward-modulation MNIST variants matching or exceeding the full recurrent variant on best test accuracy.
Evidence: The report table lists best test accuracy 0.9285 for `no_reward_modulation`, 0.9255 for `no_recurrence_sparse_plastic_readout`, and 0.9230 for `full_recurrent_plastic_graph`.
Caveat: This is a classification benchmark, not a route-memory benchmark; duplicate rows appear in the generated report table.
Source path: `experiments/experiment3/analysis/suite/suite_report.md`; `experiments/experiment3/analysis/suite/suite_comparison.csv`

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
| `experiments/experiment3/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment3/run_experiment_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment3/run_mnist_experiment.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment3/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment3/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment3/analysis/suite/suite_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment3/analysis/suite/suite_comparison.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment3/analysis/suite/suite_best_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| suite best accuracy | `experiments/experiment3/analysis/suite/suite_best_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment1to4_export.md`

Completed result / design / caveat / decision: No importable content.
Evidence: The digest file is present but empty.
Caveat: No Exp3 result was imported from this file.
Source thread: `docs/threads/experiment1to4_export.md`
Related local artifact path: `experiments/experiment3/analysis/suite/suite_report.md`
Status: Historical only

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Completed result with caveat, background only.
Evidence: The thread says Exp3 was a recurrent MNIST suite where recurrence was measurable but not clearly useful on MNIST.
Caveat: The thread did not reanalyze Exp3 artifacts in detail; keep this as background rather than a manuscript claim.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment3/analysis/suite/suite_report.md`
Status: Historical only

## Key results (thread-integrated)

No central route-memory result is imported for Exp3.

## What this experiment supports (thread-integrated)

- Historical motivation for moving beyond MNIST to tasks requiring traversal.

## What this experiment does not prove (thread-integrated)

- It does not prove recurrence is generally unnecessary; the caveat is specific to the MNIST suite discussed as background.

## Follow-up actions (thread-integrated)

- Mention Exp3 only as motivation if the manuscript needs a brief experimental history.
