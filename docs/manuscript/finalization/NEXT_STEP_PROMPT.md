# Next Step Prompt: Human Review, Venue Formatting, And Release Metadata

Use this prompt after the caption/TODO cleanup pass has been completed.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: complete the next manuscript-finalization decision pass. Do not start new experiments by default.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, post-Table-3 manuscript-placeholder/source-path verification, and post-caption/TODO cleanup.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists and carries the conservative post-Exp15 manuscript posture.
- Section 2.7 contains closest-prior-art positioning prose, with `docs/manuscript/closest_prior_art_table.md` retained as a companion artifact.
- Compact Table 3 is descriptive and source-data-backed.
- Table 4 is a compact minimal fixed-profile neural-comparator table with caveats.
- The manuscript has final-safe figure/table placeholder captions and no unreviewed submission-blocking TODO markers for the current draft pass.
- `python scripts/verify_doc_source_paths.py` has passed after the caption/TODO cleanup pass.

Immediate work:

1. Human-review `docs/manuscript/draft/MANUSCRIPT_V2.md` for flow, wording, and final claim posture.
2. Choose a target venue or explicitly keep the package venue-neutral.
3. If a venue is chosen, apply venue-specific citation/export convention, word count, figure/table placement, and supplement formatting.
4. Decide whether reviewer strategy requires a memory-augmented/key-value neural comparator beyond Exp15.
5. Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.
6. Sync `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and this prompt after decisions are made.

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

Definition of done:

- Target-venue/citation/release decisions are recorded, or explicitly deferred.
- Manuscript flow review findings are recorded and actioned or queued.
- Operational docs point to the next real blocker after venue/release decisioning.
- Final response summarizes changed files, verifier status if run, and remaining blockers.
```
