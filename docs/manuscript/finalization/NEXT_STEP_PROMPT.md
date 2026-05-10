# Next Step Prompt: Polish Figure/Table Captions And Clear Manuscript TODOs

Use this prompt after compact Table 3 manuscript-placeholder alignment and source-path verification have been recorded.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: complete the next manuscript-finalization pass: final-safe figure/table caption polish and manuscript TODO cleanup. Do not start new experiments.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification status capture.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists and carries the conservative post-Exp15 manuscript posture.
- Section 2.7 contains closest-prior-art positioning prose, with `docs/manuscript/closest_prior_art_table.md` retained as a companion artifact.
- `docs/manuscript/tables/table_03_compact_final_safe.md` is the compact descriptive main-text Table 3.
- `docs/manuscript/source_data/table_03_compact_final_safe.csv` is the compact Table 3 source-data mirror.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv` remain detailed candidate/supplementary statistical-map artifacts, not final inferential statistics.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` points main-text Table 3 at the compact final-safe descriptive table and keeps the detailed statistical map candidate/supplementary.
- `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records the Table 3 manuscript-placeholder patch and source-path verifier result.
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` identify caption/prose polish and TODO cleanup as the next active blocker.

Immediate work:

1. Review:
   - `docs/manuscript/draft/MANUSCRIPT_V2.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`

2. Polish manuscript figure/table placeholder and caption prose for:
   - Figures 1-3 as main figures.
   - Figure 5 as main-narrow symbolic transition-cue context-selection evidence.
   - Figure 4 as supplement-default unless a human explicitly emphasizes the finite-budget story.
   - Compact Table 3 as descriptive main-text statistics only.
   - Table 4 as compact main-text Exp15 neural comparator evidence.

3. Remove or clearly mark remaining submission-blocking TODOs in `docs/manuscript/draft/MANUSCRIPT_V2.md`.

4. Sync operational docs after the caption/TODO pass:
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
   - this `NEXT_STEP_PROMPT.md`

5. Run `python scripts/verify_doc_source_paths.py` if any active source paths are added or edited. Record the result exactly if run.

Preserve the current claim posture:

- Do not add final effect-size language unless explicit comparison families are approved.
- Keep compact Table 3 descriptive only.
- Keep C1 benchmark/model-family-specific.
- Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
- Keep C5 ceiling-limited and supplied-context only.
- Keep C6 as observed finite-budget degradation only; no fitted capacity law.
- Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
- Keep C13 symbolic transition-cue context selection only.
- Keep Exp15 replay collapse as non-claim pending audit.
- Do not claim broad neural superiority, solved continual learning, raw sensory latent-world discovery, or biological validation.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` has final-safe caption/placeholder prose for the current figure/table package and no unreviewed submission-blocking TODOs.
- Compact Table 3 remains descriptive and source-data-backed.
- Table 4 remains minimal fixed-profile neural-comparator evidence with caveats.
- Operational docs point to the next real blocker after caption/TODO cleanup.
- Final response summarizes changed files, verifier status if run, final caption/TODO status, and remaining blockers.
```
