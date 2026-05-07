# Experiment 14 Summary

## Purpose

Experiment 14 tests whether Context-Indexed Route Memory can select the active symbolic world from partial transition cues before executing a route, rather than receiving an oracle world/context label at evaluation time.

## Design

- Experiment directory: `experiments/experiment14_latent_context_inference/`
- Primary run: `exp14_full_20260507_210712`
- Sanity runs: `exp14_smoke_20260507_210610`; `exp14_validation_20260507_210649`
- Full profile: 20 seeds; world counts 4, 8, 16, 32; route lengths 4, 8, 12, 16; cue counts 1, 2, 4, 8; corruption rates 0.0, 0.1, 0.25, 0.5.
- Main model: `exp14_cirm_latent_selector`, a world-indexed structural route table selected from transition cues followed by recurrent route execution.
- Comparators: oracle context-gated table, shared no-context table, endpoint memorizer with the same latent selector, random selector, recency selector, and compact hash-slot selectors.

## Run IDs And Artifacts

| Run ID | Profile | Validation | Main artifact paths |
|---|---|---|---|
| `exp14_smoke_20260507_210610` | smoke | PASS: 27 pass, 0 warn, 0 fail | `experiments/experiment14_latent_context_inference/analysis/exp14_smoke_20260507_210610/validation_report.md`; `experiments/experiment14_latent_context_inference/runs/exp14_smoke_20260507_210610.sqlite3` |
| `exp14_validation_20260507_210649` | validation | PASS: 27 pass, 0 warn, 0 fail | `experiments/experiment14_latent_context_inference/analysis/exp14_validation_20260507_210649/validation_report.md`; `experiments/experiment14_latent_context_inference/runs/exp14_validation_20260507_210649.sqlite3` |
| `exp14_full_20260507_210712` | full | PASS: 27 pass, 0 warn, 0 fail | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/runs/exp14_full_20260507_210712.sqlite3` |

## Key Results

Claim -> Evidence -> Caveat -> Source path:

- Claim: CIRM-style route memory can infer the active symbolic world from clean partial transition cues. -> Evidence: in the full run hard clean slice `world_count=32`, `route_length=16`, `cue_count=8`, CIRM reaches 1.0000 seen-route world selection, seen-route composition, suffix-route composition, and first-step context accuracy. -> Caveat: this is symbolic transition-cue inference, not raw sensory latent-world discovery. -> Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
- Claim: corrupted cue evidence creates a measurable latent-selection cost relative to oracle context gating. -> Evidence: at the same hard slice, CIRM seen-route composition and world selection drop to about 0.9416 at `corruption_rate=0.5`, while the oracle context-gated table remains at 1.0000. -> Caveat: the oracle is an upper bound, not a fair non-oracle selector; the corruption process is synthetic. -> Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
- Claim: multiple cues protect symbolic latent-context selection under moderate corruption. -> Evidence: at `world_count=32`, `route_length=16`, `corruption_rate=0.25`, CIRM seen-route composition rises from about 0.7473 with one cue to about 0.9992 with eight cues. -> Caveat: exact curve shape should not be over-generalized without an implementation/theory note. -> Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
- Claim: endpoint memorization is separable from recurrent suffix composition. -> Evidence: the endpoint memorizer reaches 1.0000 seen-route composition in the hard clean slice but 0.0000 suffix-route composition. -> Caveat: it uses the same latent selector and remains a symbolic control. -> Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`

## Caveats

- Exp14 is a symbolic/table-based experiment and does not require GPU acceleration; the run manifest explicitly records `gpu_used=false` with a CPU-only rationale.
- The oracle context-gated table remains an upper bound and should not be described as defeated by CIRM.
- Shared no-context suffix-route accuracy can be misleading because suffix probes may bypass first-step context conflicts.
- Hash-slot selectors expose compact context collision limits and should be interpreted carefully.
- Generated plots are candidate analysis outputs, not final manuscript figures.

## Manuscript Status

Promising candidate main or supplement evidence for a new latent symbolic context-inference claim, currently mapped as C13 in `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.

## Next Action

Decide whether Exp14 belongs in the first manuscript main results, supplement, or follow-up framing. If retained, create final figure scripts and source-data mirrors for the selected panels.
