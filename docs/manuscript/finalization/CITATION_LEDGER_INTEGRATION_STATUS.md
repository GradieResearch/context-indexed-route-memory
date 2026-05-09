# Citation Ledger Integration Status

Date: 2026-05-09

Status: citation-ledger integration partially completed; final manuscript export convention and closest-prior-art insertion remain human decisions.

## Summary

This pass followed `docs/manuscript/finalization/NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md` after the citation-ledger artifacts were present.

The repository now treats `docs/manuscript/REFERENCES.md` as the checked venue-neutral bibliography ledger and `docs/manuscript/closest_prior_art_table.md` as the checked closest-prior-art companion artifact. The older `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` has been updated so it no longer carries the stale `Eichenbaum2017` DOI/title mismatch as candidate metadata.

## Citation convention decision

No final citation/export convention is chosen yet.

Current decision:

- Preserve bracketed placeholder keys in `docs/manuscript/draft/MANUSCRIPT_V2.md`.
- Treat `docs/manuscript/REFERENCES.md` as the authoritative checked metadata ledger.
- Do not add fake BibTeX, fake CSL JSON, or journal-specific formatting before a target convention is chosen.

Acceptable next convention choices remain:

- Pandoc-style citation keys;
- BibTeX;
- CSL JSON;
- numbered references;
- target-journal author-year style.

## Closest-prior-art table decision

No human decision has been made to inline the table into the manuscript.

Current decision:

- Preserve `docs/manuscript/closest_prior_art_table.md` as the manuscript-facing companion artifact.
- Keep Section 2.7 insertion pending until the human chooses whether the final manuscript should include a compact table or prose derived from the table.
- Preserve the explicit structure: what is inherited / what is not claimed / narrow contribution.

Recommended compact insertion source remains `docs/manuscript/closest_prior_art_table.md`.

## Citation-risk wording status

`docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` now records manuscript-facing replacement language for the two main risky phrases:

1. Narrow `modern transformer memory systems` to memory-augmented neural systems covered by the current ledger unless exact transformer-memory references are added later.
2. Narrow `task masks, adapters, parameter isolation` to architectural expansion, path/module selection, parameter isolation, and sparse expert routing unless exact task-mask/adapter references are added later.

Biological citations remain motivational only. Exp15 remains minimal fixed-profile neural comparator evidence, not exhaustive neural benchmarking.

## Eichenbaum correction

The checked entry is:

- Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. *Neuron*, 95(5), 1007-1018. DOI: `10.1016/j.neuron.2017.06.036`.

The older audit pairing of this title with DOI `10.1038/nrn.2017.74` is superseded and should not be used for final bibliography export.

## Figure/table decisions

No new human figure/table placement decisions were available in this pass.

Conservative defaults therefore remain:

- Figures 1-3 stay main.
- Figure 4 stays main-narrow for C6, with C7 boundary caveat.
- Figure 5 stays main-narrow for V2 hardening, movable to supplement by venue decision.
- Table 4 stays compact main-text neural comparator, movable to supplement by venue decision.
- Table 3 remains candidate until grouping/effect-size review is completed.
- Exp15 analysis plots are not promoted into final figures.

## Operational doc updates in this pass

Updated:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`

Not rewritten in this pass:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` because no citation/export convention or closest-prior-art insertion decision is available.
- `docs/manuscript/FIGURE_PLAN.md` because no figure/table placement decision changed.
- `docs/manuscript/NOVELTY_POSITIONING.md` because prior-art posture did not change beyond the already-added closest-prior-art companion artifact.

## Remaining blockers

- Choose citation/export convention.
- Convert `docs/manuscript/REFERENCES.md` into the chosen convention.
- Mechanically format or replace `MANUSCRIPT_V2.md` placeholder citations once the convention is chosen.
- Decide whether to inline `docs/manuscript/closest_prior_art_table.md` into Section 2.7 or keep it as a companion source artifact.
- Human-review `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, especially Figure 4, Figure 5, Table 3, and Table 4 decisions.
- Run `python scripts/verify_doc_source_paths.py` in a local checkout or CI environment.

## Verification

The documentation path verifier was not run in this tool session because the repository could not be cloned into the execution container. No experiment code was modified and no new paths were introduced except this report file.
