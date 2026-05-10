# Context-Indexed Route Memory

This repository contains a research project on context-indexed route-memory experiments. It studies a controlled compositional route-memory benchmark where a model must store and execute multiple incompatible transition systems over the same symbolic state and action space.

Experiments live under `experiments/`. Manuscript, evidence, synthesis, source-data, finalization, and repo-audit documents live under `docs/`.

## Current status

The repository is now in a **post-Exp15 / post-Manuscript-V2 / post-Analysis-Pass-15A / post-citation-ledger / post-human-decision / post-Section-2.7 / post-compact-Table-3-split finalization state**.

Completed manuscript-relevant imports and decisions:

- Exp13.2 is imported as completed symbolic/algorithmic baseline-suite evidence.
- Exp14 is imported as completed symbolic transition-cue context-selection evidence.
- Exp15 is imported as completed minimal fixed-profile neural-comparator evidence.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured.
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` narrows the claim posture after Exp15.
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` records the post-15A retained-claim/source-CSV posture.
- `docs/manuscript/REFERENCES.md` is the checked venue-neutral citation ledger until a target venue/convention is chosen.
- Section 2.7 of `MANUSCRIPT_V2.md` contains prose derived from `docs/manuscript/closest_prior_art_table.md`.
- `docs/manuscript/tables/table_03_compact_final_safe.md` and `docs/manuscript/source_data/table_03_compact_final_safe.csv` provide the compact descriptive main-text Table 3 path.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `.csv` remain detailed candidate/supplementary statistical-map artifacts, not final main-text inferential statistics.
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md` and `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` provide a compact V2 Exp15 comparator table.

The repository is **not submission-ready**. The current blocker is documentation/source-path verification plus manuscript/caption alignment for the compact Table 3 path.

## Scientific posture

The strongest current manuscript posture is deliberately narrow: this is a controlled symbolic/mechanistic benchmark and evidence map. It supports claims about context-indexed storage, recurrent execution, endpoint-vs-transition composition, finite-budget boundaries, symbolic transition-cue context selection, and minimal neural comparator behavior. It does **not** support broad CIRM-over-neural-model claims or solved continual-learning claims.

## Where to start

- [Documentation index](docs/README.md)
- [Source of truth](docs/manuscript/SOURCE_OF_TRUTH.md)
- [Manuscript V2 draft](docs/manuscript/draft/MANUSCRIPT_V2.md)
- [Post-Exp15 claim freeze addendum](docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md)
- [Retained claims/statistical hardening](docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md)
- [Claims and evidence](docs/manuscript/CLAIMS_AND_EVIDENCE.md)
- [Finalization checklist](docs/manuscript/finalization/FINALIZATION_CHECKLIST.md)
- [Next step prompt](docs/manuscript/finalization/NEXT_STEP_PROMPT.md)
- [Figure/table human review](docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md)
- [Publication readiness](docs/synthesis/PUBLICATION_READINESS.md)
- [Next experiments / next work](docs/synthesis/NEXT_EXPERIMENTS.md)
- [Reproducibility audit](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)
- [Experiment registry](docs/experiments/EXPERIMENT_REGISTRY.md)

## Reproducibility

To check active documentation source paths, run:

```bash
python scripts/verify_doc_source_paths.py
```

## Planned next work

The next planned manuscript-readiness step is **documentation/source-path verification plus compact Table 3 manuscript/caption alignment**. Use:

```text
docs/manuscript/finalization/NEXT_STEP_PROMPT.md
```

That pass should run or document the inability to run `python scripts/verify_doc_source_paths.py`, fix broken active paths only if found, and polish `MANUSCRIPT_V2.md` / caption prose so compact descriptive Table 3 is the main-text Table 3 path while the detailed generated statistical map remains candidate/supplementary support. Do not start another experiment by default.

## License / citation

TODO: Add a license and citation instructions. Until a license is added, reuse rights are not formally granted.
