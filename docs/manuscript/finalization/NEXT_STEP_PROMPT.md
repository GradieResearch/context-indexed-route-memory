# Next Step Prompt: Venue-Neutral Manuscript Flow Review Or Venue Decision

Use this prompt after the pre-venue documentation state has been tied off.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: perform the next manuscript-finalization decision/action pass. Do not start new experiments by default.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, post-Table-3 manuscript-placeholder/source-path verification, post-caption/TODO cleanup, and post-pre-venue decision-status tie-off.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists and carries the conservative post-Exp15 manuscript posture.
- Section 2.7 contains closest-prior-art positioning prose, with `docs/manuscript/closest_prior_art_table.md` retained as a companion artifact.
- Compact Table 3 is descriptive and source-data-backed.
- Table 4 is a compact minimal fixed-profile neural-comparator table with caveats.
- The manuscript has final-safe figure/table placeholder captions and no unreviewed submission-blocking TODO markers for the current draft pass.
- `python scripts/verify_doc_source_paths.py` has passed after the caption/TODO cleanup pass.
- `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md` records that target venue, citation/export convention, release metadata, and optional neural-comparator expansion remain human decisions.

Immediate work:

1. If no venue has been chosen, keep the package venue-neutral and perform a prose-only manuscript flow review.
2. Normalize the remaining duplicate in-section Table 4 placeholder in `docs/manuscript/draft/MANUSCRIPT_V2.md`.
3. Review the manuscript for repeated caveats, awkward placeholder wording, and claim-posture drift without changing the scientific claims.
4. Record flow-review findings in a finalization status document.
5. If a target venue is chosen by a human, apply the selected citation/export convention, word count, figure/table placement, and supplement formatting.
6. If no target venue is chosen, do not create BibTeX, CSL JSON, numbered references, final journal formatting, `LICENSE`, or `CITATION.cff`.
7. Sync `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and this prompt after the pass.
8. Run `python scripts/verify_doc_source_paths.py` after edits.

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
- Do not choose a license, citation style, or target venue without a human decision.

Definition of done:

- The remaining duplicate Table 4 placeholder is normalized, or explicitly left as a known blocker if tooling prevents the edit.
- Manuscript flow-review findings are recorded and actioned or queued.
- Target-venue/citation/release decisions are recorded, or explicitly deferred.
- Operational docs point to the next real blocker after the flow/decision pass.
- Final response summarizes changed files, verifier status, and remaining blockers.
```
