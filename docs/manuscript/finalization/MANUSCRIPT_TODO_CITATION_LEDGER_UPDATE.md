# Manuscript TODO Update: Citation Ledger Pass

Status: update note for the operational work queue after the citation-ledger / closest-prior-art table pass.

Date: 2026-05-09

## Completed in this pass

| Completed item | Result | Source path |
|---|---|---|
| Citation metadata ledger. | V2 placeholder keys are now mapped to checked, venue-neutral metadata in a local manuscript reference ledger. | `docs/manuscript/REFERENCES.md` |
| Closest-prior-art positioning table. | Section 2.7 now has a compact source artifact that separates inherited prior art, non-novel claims, and the manuscript's narrow contribution. | `docs/manuscript/closest_prior_art_table.md` |
| Citation insertion report. | Records what was completed, what was deliberately deferred, and the corrected `Eichenbaum2017` metadata. | `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` |
| Next-step prompt. | The next finalization session should choose a citation/export convention and decide whether to inline the closest-prior-art table. | `docs/manuscript/finalization/NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md` |

## Changes to current priority

The previous P0 item, "verify citation placeholders against real metadata," is now partially satisfied by the references ledger. It should no longer be treated as a blank audit task.

The new P0 item is:

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Choose citation/export convention and mechanically integrate citation placeholders. | The repository now has checked metadata, but no selected output convention. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | BibTeX / CSL JSON / Pandoc / numbered / author-year citation format applied consistently. |
| Decide whether to inline the closest-prior-art table into Section 2.7. | The table source now exists, but manuscript insertion is a style/length decision. | `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Compact table inserted into V2, or explicit decision to keep it as companion/supplement. |
| Preserve conservative figure/table defaults until human decision. | No new human placement decision was made during the citation ledger pass. | `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` | Figures 1-3 main; Figure 4 main-narrow; Figure 5 main-narrow; Table 4 compact main; Table 3 candidate pending grouping review. |

## Remaining blockers before submission

- Citation/export convention is still undecided.
- `MANUSCRIPT_V2.md` still uses bracketed placeholder keys by design.
- The closest-prior-art table has not yet been inlined into Section 2.7.
- Human figure/table placement and caption decisions remain unresolved.
- Table 3 grouping/effect-size review remains unresolved.
- `python scripts/verify_doc_source_paths.py` still needs to be run in a checked-out repository after this branch is available locally.

## Guardrails carried forward

- Do not add fake BibTeX or unsupported metadata.
- Do not broaden novelty beyond the route-memory decomposition/evidence-map posture.
- Do not cite Exp15 as exhaustive neural benchmarking.
- Do not cite Exp15 replay collapse or Exp13.1 lesion evidence as positive mechanism evidence.
- Do not claim biological validation from hippocampal/CLS motivation citations.
