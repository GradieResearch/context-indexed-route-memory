# Table 3 Verification And Alignment Status

Date: 2026-05-10

Purpose: record the status of the compact Table 3 verification/alignment pass requested after the compact final-safe Table 3 split.

## Status

Result: **not complete yet**.

The compact Table 3 split itself is complete, and the surrounding review/readiness docs mostly describe the correct posture. However, the manuscript draft still contains at least one stale main-text Table 3 placeholder that points to the detailed statistical map rather than the compact descriptive main-text Table 3.

## Found stale manuscript reference

`docs/manuscript/draft/MANUSCRIPT_V2.md` still contains this stale placeholder near the manuscript table list:

```md
[Table 3 here: statistical summary. Source: `docs/manuscript/tables/table_03_statistical_summary.md`. Caveat: effect-size grouping still needs human review.]
```

For the compact Table 3 path, replace it with wording equivalent to:

```md
[Table 3 here: compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Detailed generated statistical map retained as candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`. Caveat: descriptive only; do not treat as final inferential effect-size evidence or approved comparison-family statistics.]
```

Do not add final effect-size language or approved comparison-family statistics while making this replacement.

## Already aligned or mostly aligned docs

The following files already distinguish the compact descriptive Table 3 from the detailed candidate/supplementary statistical map:

- `docs/manuscript/tables/table_03_compact_final_safe.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`

These files should still be reviewed after the manuscript placeholder is patched, but they should not be treated as evidence that the manuscript draft itself is already aligned.

## Verification attempt status

`python scripts/verify_doc_source_paths.py` was **not run to completion** in this pass.

Exact reason: the available execution environment could not materialize a clean checkout from GitHub. The attempted clone failed with:

```text
Cloning into '/mnt/data/cirm'...
fatal: unable to access 'https://github.com/GradieResearch/context-indexed-route-memory.git/': Could not resolve host: github.com
```

Because no clean checkout was available, this pass must not be recorded as a successful source-path verification pass. Run the verifier from a local checkout or CI-capable environment before marking this item complete.

## Remaining blocker

1. Patch the stale `MANUSCRIPT_V2.md` Table 3 placeholder to reference `docs/manuscript/tables/table_03_compact_final_safe.md` as the main-text Table 3 path.
2. Run `python scripts/verify_doc_source_paths.py` from a clean local checkout or CI-capable environment.
3. If the verifier passes, record the pass in:
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, if caption-review status changes
4. If the verifier fails, fix only broken active paths and preserve the current conservative claim posture.
