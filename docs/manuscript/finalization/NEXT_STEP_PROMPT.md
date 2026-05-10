# Next Step Prompt: Verify Compact Table 3 Split And Align Captions

Use this prompt after the compact Table 3 split has been completed.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Complete the next manuscript-finalization blocker: verify documentation/source paths and align manuscript/caption prose with the compact Table 3 path. Do not start new experiments.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, and post-current-pass Table 3 compact split.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` Section 2.7 contains closest-prior-art prose derived from `docs/manuscript/closest_prior_art_table.md`.
- `docs/manuscript/closest_prior_art_table.md` remains the companion source artifact.
- `docs/manuscript/REFERENCES.md` remains the venue-neutral citation ledger until target venue/convention selection.
- `docs/manuscript/tables/table_03_compact_final_safe.md` is the compact final-safe descriptive main-text Table 3.
- `docs/manuscript/source_data/table_03_compact_final_safe.csv` is the compact Table 3 source-data mirror.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv` remain detailed candidate/supplementary statistical-map artifacts, not final inferential statistics.
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` records the Option B compact Table 3 decision and remaining caveats.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`, `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` have been updated for the compact Table 3 split.

Immediate work:

1. Run `python scripts/verify_doc_source_paths.py` in a clean checkout or CI-capable environment.
   - If it passes, record the pass in the relevant finalization/readiness docs.
   - If it cannot run, document the exact reason and do not guess.
   - If it fails, fix broken active paths only; do not change scientific claims.

2. Align manuscript/caption/table references:
   - Ensure `docs/manuscript/draft/MANUSCRIPT_V2.md` refers to compact descriptive Table 3 if it cites Table 3 as main text.
   - Ensure captions do not treat `table_03_statistical_summary.md` as final inferential statistics.
   - Keep the detailed generated Table 3 map as candidate/supplement/audit support.

3. Preserve the current claim posture:
   - Do not add final effect-size language unless explicit comparison families are approved.
   - Keep C1 benchmark/model-family-specific.
   - Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
   - Keep C5 ceiling-limited and supplied-context only.
   - Keep C6 as observed finite-budget degradation only; no fitted capacity law.
   - Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
   - Keep C13 symbolic transition-cue context selection only.
   - Keep Exp15 replay collapse as non-claim pending audit.

4. Sync operational docs after verification/caption alignment:
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
   - `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` only if statuses change.

5. Update this `NEXT_STEP_PROMPT.md` at the end so the next prompt points to the next real blocker after verification/caption alignment, not back to completed Table 3 grouping work.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not broaden claims beyond the retained post-15A posture.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- `python scripts/verify_doc_source_paths.py` passes, or inability/failure is documented with exact reason.
- Manuscript/caption references distinguish compact descriptive Table 3 from the detailed candidate/supplement statistical map.
- Operational docs no longer loop back to Table 3 grouping as unfinished.
- Final response summarizes changed files, verification status, final Table 3 status, and remaining blockers.
```
