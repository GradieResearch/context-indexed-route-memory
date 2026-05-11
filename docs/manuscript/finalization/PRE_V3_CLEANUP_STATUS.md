# Pre-V3 Cleanup Status

Date: 2026-05-11

Purpose: record the repository cleanup/consolidation pass before drafting the planned future V3 manuscript.

## Status

Result: **pre-V3 documentation cleanup and consolidation pass recorded**.

This pass does not create V3, choose a venue, choose a license, generate citation exports, or start new experiments. It narrows the documentation surface so the next pass can focus on manuscript drafting rather than interpreting accumulated finalization artifacts.

## What is active now

Active manuscript/finalization operating docs:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/SOURCE_OF_TRUTH.md`
- `docs/manuscript/finalization/README.md`
- `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

## What was consolidated

- `docs/manuscript/finalization/README.md` now presents a V3-facing active-files list first, and demotes one-off status/prompt files to a historical audit trail.
- `docs/manuscript/SOURCE_OF_TRUTH.md` now separates canonical docs, historical/audit-trail docs, and non-authoritative debris.
- `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`, `docs/synthesis/PUBLICATION_READINESS.md`, `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md`, and `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` now agree that the next milestone is a V3 drafting/flow-review pass or an explicit human venue/citation decision.

## Historical audit-trail files intentionally retained

These are retained because they document important decisions and source-path verification results. They should not be used as active instructions unless a canonical doc points to them.

- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`
- `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`
- `docs/manuscript/finalization/CAPTION_TODO_CLEANUP_STATUS.md`
- `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`
- `docs/manuscript/finalization/NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md`
- `docs/manuscript/finalization/MANUSCRIPT_TODO_CITATION_LEDGER_UPDATE.md`

## Non-canonical debris / cleanup targets

- `docs/manuscript/draft/bkup.orig` is a stale backup draft. It is explicitly non-canonical and should be removed with local Git access before or during the V3 drafting branch.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` still contains a duplicate in-section Table 4 placeholder using older bracketed wording. It is not a source-path blocker but should be normalized in the V3 drafting/flow-review pass.

## Next recommended action

Create a V3 drafting branch from `main` after this cleanup PR merges. The first V3 pass should:

1. Remove `docs/manuscript/draft/bkup.orig` if local Git deletion is available.
2. Normalize the duplicate Table 4 placeholder.
3. Draft the planned future V3 manuscript from V2 with cleaner flow and fewer process notes.
4. Preserve the conservative claim posture.
5. Keep venue/citation/license decisions explicit and human-gated.
6. Run `python scripts/verify_doc_source_paths.py` after the cleanup/draft pass.
