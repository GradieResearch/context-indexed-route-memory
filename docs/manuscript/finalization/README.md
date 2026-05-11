# Manuscript Finalization

Purpose: provide a clean operating surface for moving from the V2 manuscript/finalization package into a real V3 manuscript draft.

This folder previously accumulated several one-off prompts and status captures while Exp15, citation hygiene, Table 3, caption cleanup, and pre-venue status were being integrated. Those artifacts are retained for traceability, but only a small subset should be treated as active.

## Active V3-facing files

Use these first:

- [`NEXT_STEP_PROMPT.md`](NEXT_STEP_PROMPT.md) - current agent-ready handoff for the next manuscript pass.
- [`FINALIZATION_CHECKLIST.md`](FINALIZATION_CHECKLIST.md) - active operational checklist.
- [`HUMAN_REVIEW_VENUE_STATUS.md`](HUMAN_REVIEW_VENUE_STATUS.md) - current pre-venue decision gate and remaining-work estimate.
- [`MANUSCRIPT_FINALIZATION_PLAN.md`](MANUSCRIPT_FINALIZATION_PLAN.md) - higher-level finalization plan.

Primary non-finalization companions:

- [`../draft/MANUSCRIPT_V2.md`](../draft/MANUSCRIPT_V2.md) - current draft to flow-review before V3.
- [`../MANUSCRIPT_TODO.md`](../MANUSCRIPT_TODO.md) - manuscript work queue.
- [`../SOURCE_OF_TRUTH.md`](../SOURCE_OF_TRUTH.md) - canonical document priority rules.
- [`../../synthesis/PUBLICATION_READINESS.md`](../../synthesis/PUBLICATION_READINESS.md) - current publication-readiness judgment.

## Current state

The repository is post:

- Exp15 import and post-Exp15 claim narrowing;
- Analysis Pass 15A retained-claim/statistical hardening;
- checked citation-ledger and closest-prior-art companion artifact creation;
- Section 2.7 closest-prior-art prose integration;
- compact descriptive Table 3 split and verification;
- caption/TODO cleanup;
- pre-venue human-review/venue/release decision-status capture;
- stale backup draft removal and duplicate Table 4 placeholder normalization.

The manuscript is **not submission-ready**, but it is close enough for a serious V3 drafting pass.

## Current next action

Do one of the following, in order of preference:

1. If no venue has been chosen, perform a venue-neutral V3 manuscript flow review.
2. Preserve the conservative claim posture while improving prose and manuscript flow.
3. Record any unresolved venue, citation, figure/table, license, and optional-baseline decisions.

Do **not** start a new experiment, choose a venue, choose a license, create final citation exports, or add a memory-augmented/key-value neural comparator unless a human explicitly asks for that.

## Historical audit trail

These files are retained as provenance for how the current state was reached. They should not be used as current instructions unless `NEXT_STEP_PROMPT.md` explicitly points to them.

- `CITATION_PRIOR_ART_INSERTION_REPORT.md` - checked citation-ledger and closest-prior-art creation pass.
- `CITATION_LEDGER_INTEGRATION_STATUS.md` - citation-ledger integration follow-up status.
- `HUMAN_DECISION_INTEGRATION_STATUS.md` - earlier human decisions on citation/export posture, closest-prior-art placement, and figure/table placement.
- `TABLE_3_GROUPING_REVIEW.md` - compact Table 3 decision record.
- `TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` - Table 3 manuscript placeholder/source-path verification record.
- `CAPTION_TODO_CLEANUP_STATUS.md` - caption/TODO cleanup verification record.
- `SECTION_2_7_PROSE_PATCH.md` - prose patch source for closest-prior-art Section 2.7 integration.
- `NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md` - superseded handoff prompt from the citation-ledger stage.
- `MANUSCRIPT_TODO_CITATION_LEDGER_UPDATE.md` - superseded TODO update note from the citation-ledger stage.

## Before V3

- Keep `docs/manuscript/REFERENCES.md` venue-neutral until a target venue/citation convention is chosen.
- Keep `LICENSE` and `CITATION.cff` unset until human choices are made.
