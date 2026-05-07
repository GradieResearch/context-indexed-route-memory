# Experiment 14 Report: Latent Context Inference

## Run identity

- Experiment: `exp14_latent_context_inference`
- Run ID: `exp14_smoke_20260507_210610`
- Profile: `smoke`
- Seeds: `(0, 1)`
- World counts: `(4,)`
- Route lengths: `(4, 8)`
- Cue counts: `(1, 2)`
- Corruption rates: `(0.0, 0.5)`
- Metrics rows: `112`
- SQLite DB: `runs\exp14_smoke_20260507_210610.sqlite3`

## Executive summary

This run removes the oracle world label used by the clean context-gated lookup baseline and asks each selector to infer the active world from partial transition cues before route composition.

At the hardest clean setting available in this run (worlds=4, route_length=8, cue_count=2):
- CIRM latent selector world-selection accuracy: 1.0000.
- CIRM latent selector seen-route composition accuracy: 1.0000.
- Oracle context-gated table seen-route composition accuracy: 1.0000.
- Shared no-context table seen-route composition accuracy: 0.2500.
- Route endpoint memorizer suffix-route composition accuracy: 0.0000.

At the same hardest setting with the highest corruption rate (0.5):
- CIRM latent selector world-selection accuracy: 0.5156.
- CIRM latent selector seen-route composition accuracy: 0.5156.

## Interpretation guardrails

- This is still a symbolic route-memory benchmark, not end-to-end perception or solved continual learning.
- The oracle context-gated table remains an upper bound, not a fair latent-selector baseline.
- Clean cue success supports context selection from observed transition evidence, not autonomous discovery of worlds from raw sensory streams.
- Corrupted cue collapse should be framed as context-evidence sensitivity, not generic robustness failure unless paired with richer noise models.

## Generated plots

- `analysis\exp14_smoke_20260507_210610\plots\exp14_world_selection_vs_corruption.png`
- `analysis\exp14_smoke_20260507_210610\plots\exp14_seen_composition_vs_corruption.png`
- `analysis\exp14_smoke_20260507_210610\plots\exp14_suffix_composition_vs_corruption.png`
- `analysis\exp14_smoke_20260507_210610\plots\exp14_margin_vs_corruption.png`
- `analysis\exp14_smoke_20260507_210610\plots\exp14_cue_count_selection_sensitivity.png`
- `analysis\exp14_smoke_20260507_210610\plots\exp14_cue_count_composition_sensitivity.png`

## Source artifacts

- `exp14_metrics.csv`
- `metrics.csv`
- `exp14_summary.csv`
- `exp14_effect_sizes.csv`
- `run_manifest.json`
- `progress.jsonl`
