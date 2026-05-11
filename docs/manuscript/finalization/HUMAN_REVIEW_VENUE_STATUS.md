# Human Review, Venue, And Release Decision Status

Date: 2026-05-11

Purpose: record the manuscript decision state after caption/TODO cleanup and before any target-venue or release-metadata decisions are made.

## Status

Result: **pre-venue documentation state tied off; human decisions still required**.

The repository has moved past the Table 3 alignment, path-verification, caption-placeholder, and manuscript-TODO cleanup blockers. The remaining work is no longer primarily experiment import or source-path repair. It is now submission-package decision work: human manuscript review, venue/citation formatting, release metadata, and optional reviewer-strategy baseline decisions.

This status intentionally does **not** invent a target venue, bibliography convention, license, `CITATION.cff`, or new neural-baseline requirement.

## Current manuscript-readiness assessment

The manuscript is close to a submission candidate, but not yet submission-ready.

The current draft is suitable for human flow review because it now has:

- the conservative post-Exp15 claim posture;
- Section 2.7 closest-prior-art prose;
- compact descriptive Table 3 as the main statistical table;
- compact Exp15 Table 4 as the minimal neural-comparator table;
- final-safe figure/table placeholder captions with caveats;
- no known source-path verification blocker.

However, the manuscript is not yet final because these human choices remain open:

- target venue and citation/export convention;
- whether to keep the manuscript venue-neutral for now;
- final bibliography style and verified metadata formatting;
- final figure/table placement and supplement split;
- whether reviewer strategy requires a memory-augmented/key-value neural comparator beyond Exp15;
- human-chosen `LICENSE` and `CITATION.cff`;
- final release/archive strategy.

## Known minor cleanup item

A later duplicate in-section Table 4 placeholder still uses older bracketed manuscript-placeholder wording. This is not a path-verification blocker and does not change the claim posture, but it should be normalized during the next manuscript flow/edit pass. It is deliberately called out here so it does not get lost.

## Recommendation

If no target venue has been chosen yet, keep the manuscript package venue-neutral and do not generate BibTeX/CSL/numbered references or journal-specific formatting. The next useful human decision is one of:

1. choose a target venue and citation convention;
2. explicitly stay venue-neutral for one more pass and perform a prose-only manuscript flow edit;
3. decide whether a broader neural comparator is strategically necessary before submission.

## Remaining work estimate

Minimum path without new experiments:

1. Normalize the duplicate Table 4 placeholder and do one full manuscript flow edit.
2. Choose venue/citation convention or explicitly keep the package venue-neutral.
3. Finalize bibliography formatting only after that venue decision.
4. Add `LICENSE` and `CITATION.cff` after human choices.
5. Run final source-path verification and a fresh-checkout command/reproducibility pass.
6. Optionally tag/archive after manuscript stabilization.

That is likely **2-4 small documentation PRs** if no new experiment is added.

If a memory-augmented/key-value neural comparator is required, add one experiment-design/implementation run, one analysis/import pass, and one manuscript integration pass. That would turn the remaining work into roughly **4-7 PRs plus the runtime of the new experiment**.

## Next blocker

Human decision: target venue/citation convention versus one more venue-neutral flow-edit pass.
