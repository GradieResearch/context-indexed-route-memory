# Experiment 4: Successor Traversal

## Evidence status

- Local artifacts reviewed: README/design docs, generated reports, CSV summaries, validation outputs where present, and plot filenames
- Thread digest reviewed: yes; historical contrast imported
- Claims validated: local-only first pass; human review still required
- Needs human review: yes

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: no
- Thread digest present: `docs/threads/experiment6_export.md`; background in `docs/threads/experiment5to10_export.md`
- Manuscript relevance: Candidate supplement for first traversal mechanism result.

## Purpose

Experiment 4 moves beyond MNIST because MNIST did not strongly require recurrent graph traversal. The previous ablations showed that recurrence was measurable but not clearly useful; the no-recurrence model performed about as well as the full recurrent model. That suggested the task was too perceptual and one-shot. This experiment asks a sharper question: > Can a sparse recurrent plastic graph learn a local transition rule and then compose that rule repeatedly to solve a task it was not directly trained on? The task is successor arithmetic: The model is trained on one-step transitions only. Multi-step addition is a held-out traversal test. MNIST can be solved by a shallow mapping: That does 

Source path: `experiments/experiment4_successor/EXPERIMENT_4_SUCCESSOR_TRAVERSAL.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment4_successor/EXPERIMENT_4_SUCCESSOR_TRAVERSAL.md`
- Task/design clue: Experiment 4 moves beyond MNIST because MNIST did not strongly require recurrent graph traversal. The previous ablations showed that recurrence was measurable but not clearly useful; the no-recurrence model performed about as well as the full recurrent model. That suggested the task was too perceptual and one-shot. This experiment asks a sharper question: > Can a sparse recurrent plastic graph learn a local transition rule and then compose that rule repeatedly to solve a task it was not directly trained on? The task is successor arithmetic: The model is trained on one-step transitions only. Multi-step addition is a held-out traversal test. MNIST can be solved by a shallow mapping: That does 
- Run scripts detected: `experiments/experiment4_successor/run_exp4_successor_experiment.py`, `experiments/experiment4_successor/run_exp4_suite.py`, `experiments/experiment4_successor/run_experiment_suite.py`, `experiments/experiment4_successor/run_mnist_experiment.py`, `experiments/experiment4_successor/start.ps1`, `experiments/experiment4_successor/start.sh`
- Analysis CSVs detected: 1; plot files detected: 3; generated/design reports detected: 2.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment4_successor/EXPERIMENT_4_SUCCESSOR_TRAVERSAL.md`: Experiment 4 moves beyond MNIST because MNIST did not strongly require recurrent graph traversal. The previous ablations showed that recurrence was measurable but not clearly useful; the no-recurrence model performed about as well as the full recurrent model. That suggested the task was too perceptual and one-shot. This experiment asks a sharper question: > Can a sparse recurrent plastic graph learn a local transitio
- `experiments/experiment4_successor/analysis/exp4/exp4_report.md`: This experiment asks a sharper question than MNIST: can a recurrent plastic graph learn a local successor transition and compose it repeatedly to solve addition-like tasks it was not directly trained on? A strong result would show `exp4_full_traversal` beating `exp4_no_recurrence` on multi-step addition, not merely matching it on one-step transitions. Key things to inspect: - `best_addition_accuracy`: whether travers

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp4_full_traversal | Reference/full mechanism | TODO: import intended expectation from thread digest | best transition=1.0 | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` |
| exp4_no_reward_gate | Removes reward gating | TODO: import intended expectation from thread digest | best transition=1.0 | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` |
| exp4_no_homeostasis | Removes homeostatic regulation | TODO: import intended expectation from thread digest | best transition=1.0 | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` |
| exp4_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | best transition=0.0417 | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` |
| exp4_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | best transition=0.0 | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| best_accuracy | Best recorded task accuracy in a run. | Generated analysis CSV/report | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| best_transition_accuracy | Best recorded one-step transition accuracy. | Generated analysis CSV/report | `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Single successor traversal separates mechanism ablations

Claim: Exp4 locally reports perfect transition and addition accuracy for the full traversal variant, with collapse in no-recurrence and no-structural-plasticity ablations.
Evidence: `exp4_full_traversal` has best_addition_accuracy=1.0; `exp4_no_recurrence` has best_addition_accuracy=0.0; `exp4_no_structural_plasticity` has best_addition_accuracy=0.0349.
Caveat: Single controlled successor task; later experiments test harder contextual route systems.
Source path: `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv`; `experiments/experiment4_successor/analysis/exp4/exp4_report.md`

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
| `experiments/experiment4_successor/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment4_successor/run_exp4_successor_experiment.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment4_successor/run_exp4_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment4_successor/run_experiment_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment4_successor/run_mnist_experiment.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment4_successor/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment4_successor/EXPERIMENT_4_SUCCESSOR_TRAVERSAL.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment4_successor/analysis/exp4/exp4_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment4_successor/analysis/exp4/exp4_best_addition_accuracy.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment4_successor/analysis/exp4/exp4_recurrent_drive.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment4_successor/analysis/exp4/exp4_unique_active.png` | plot | Plot image | high | Indexed locally; review before citing. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp4 best addition accuracy | `experiments/experiment4_successor/analysis/exp4/exp4_best_addition_accuracy.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp4 recurrent drive | `experiments/experiment4_successor/analysis/exp4/exp4_recurrent_drive.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp4 unique active | `experiments/experiment4_successor/analysis/exp4/exp4_unique_active.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment6_export.md`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread treats Exp4 as a single universal successor-route contrast where route ambiguity was limited.
Caveat: Exp4 does not test incompatible context-conditioned worlds.
Source thread: `docs/threads/experiment6_export.md`
Related local artifact path: `experiments/experiment4_successor/analysis/exp4/exp4_report.md`
Status: Historical only

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Manuscript framing decision.
Evidence: The thread uses Exp4 as prior motivation for Exp5 because traversal made recurrence and structural plasticity more load-bearing than earlier MNIST tasks.
Caveat: The central manuscript mechanism is supported by later context/world experiments, not Exp4 alone.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv`
Status: Historical only

## Key results (thread-integrated)

### Result 1: First traversal contrast

Claim: Exp4 is useful as historical evidence that a traversal task made recurrence/structural plasticity more relevant than MNIST-style classification.
Evidence: The thread frames Exp4 as the predecessor motivating contextual successor experiments.
Caveat: This is a historical motivation claim, not a central manuscript result about context-separated memory.
Source thread: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment6_export.md`
Source artifact: `experiments/experiment4_successor/analysis/exp4/exp4_report.md`
Manuscript status: Historical only

## What this experiment supports (thread-integrated)

- Route-composition motivation for later experiments.

## What this experiment does not prove (thread-integrated)

- It does not prove world/context indexing or non-destructive memory.

## Follow-up actions (thread-integrated)

- Keep Exp4 in background or supplementary history unless the manuscript needs the early traversal contrast.
