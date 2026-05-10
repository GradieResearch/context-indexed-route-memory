# Next Step Prompt: Patch Manuscript Table 3 Placeholder And Run Verifier

Use this prompt after the compact Table 3 split and the first verification/alignment status pass.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: complete the remaining compact Table 3 verification/alignment blocker. Do not start new experiments.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, and post-status capture for the attempted verification/alignment pass.

Already completed:

- `docs/manuscript/tables/table_03_compact_final_safe.md` is the compact final-safe descriptive main-text Table 3.
- `docs/manuscript/source_data/table_03_compact_final_safe.csv` is the compact Table 3 source-data mirror.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv` remain detailed candidate/supplementary statistical-map artifacts, not final inferential statistics.
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` records the Option B compact Table 3 decision and remaining caveats.
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, `docs/synthesis/PUBLICATION_READINESS.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`, and `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` mostly reflect the compact Table 3 split.
- `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records that this pass is **not yet complete**, because the manuscript still has a stale Table 3 placeholder and the verifier could not be run in the prior execution environment.

Immediate work:

1. Patch `docs/manuscript/draft/MANUSCRIPT_V2.md` so the main-text Table 3 placeholder points to compact descriptive Table 3:
   - Main table path: `docs/manuscript/tables/table_03_compact_final_safe.md`
   - Source-data mirror: `docs/manuscript/source_data/table_03_compact_final_safe.csv`
   - Detailed map retained only as candidate/supplementary audit support: `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`

   Replace stale wording equivalent to:

   `[Table 3 here: statistical summary. Source: `docs/manuscript/tables/table_03_statistical_summary.md`. Caveat: effect-size grouping still needs human review.]`

   with wording equivalent to:

   `[Table 3 here: compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Detailed generated statistical map retained as candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`. Caveat: descriptive only; do not treat as final inferential effect-size evidence or approved comparison-family statistics.]`

2. Run `python scripts/verify_doc_source_paths.py` from a clean local checkout or CI-capable environment.
   - If it passes, record the pass in the relevant finalization/readiness docs.
   - If it cannot run, document the exact reason and do not guess.
   - If it fails, fix broken active paths only; do not change scientific claims.

3. Sync status after the patch and verifier result:
   - `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` only if caption-review status changes
   - `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` only if statuses change

4. Update this `NEXT_STEP_PROMPT.md` at the end so it points to the next real blocker after manuscript Table 3 alignment and source-path verification.

Preserve the current claim posture:

- Do not add final effect-size language unless explicit comparison families are approved.
- Keep C1 benchmark/model-family-specific.
- Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
- Keep C5 ceiling-limited and supplied-context only.
- Keep C6 as observed finite-budget degradation only; no fitted capacity law.
- Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
- Keep C13 symbolic transition-cue context selection only.
- Keep Exp15 replay collapse as non-claim pending audit.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not broaden claims beyond the retained post-15A posture.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` distinguishes compact descriptive Table 3 from the detailed candidate/supplement statistical map.
- `python scripts/verify_doc_source_paths.py` passes, or inability/failure is documented with exact reason.
- Operational docs record the true verification/alignment status and no longer loop back to completed Table 3 grouping work.
- Final response summarizes changed files, verification status, final Table 3 status, and remaining blockers.
```
