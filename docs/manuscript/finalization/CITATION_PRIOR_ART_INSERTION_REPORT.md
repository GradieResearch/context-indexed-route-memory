# Citation / Prior-Art Finalization Report

Status: partial completion of the post-15A citation/prior-art finalization task.

Date: 2026-05-09

## What changed

- Added `docs/manuscript/REFERENCES.md` as a venue-neutral references ledger mapping the current `MANUSCRIPT_V2.md` placeholder keys to checked reference metadata.
- Added `docs/manuscript/closest_prior_art_table.md` as a compact manuscript-facing closest-prior-art positioning table for Section 2.7.
- Preserved the post-15A claim posture: controlled symbolic/mechanistic route-memory benchmark and evidence map, not broad neural superiority, raw latent-world discovery, biological validation, or solved continual learning.

## Citation metadata result

The references ledger covers the placeholder families currently used in `docs/manuscript/draft/MANUSCRIPT_V2.md`:

- continual learning and catastrophic interference;
- memory-augmented computation and few-shot memory;
- fast weights, associative memory, and differentiable plasticity;
- context, gating, modularity, and latent task inference;
- compositional generalization, graph reasoning, and neural algorithmic reasoning;
- hippocampal indexing, cognitive maps, and complementary learning systems.

The ledger intentionally remains venue-neutral because the repository did not appear to have an existing bibliography convention such as a `.bib`, CSL JSON, or target-journal reference style.

## Important correction

The prior audit carried an `Eichenbaum2017` metadata mismatch. The ledger corrects the entry to:

- Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. *Neuron*, 95(5), 1007-1018. DOI: `10.1016/j.neuron.2017.06.036`.

The previous audit pairing of this title with DOI `10.1038/nrn.2017.74` should not be propagated into a final bibliography without correction.

## Closest-prior-art table result

`docs/manuscript/closest_prior_art_table.md` supplies a source-backed table covering:

- continual learning and catastrophic interference;
- differentiable/external memory;
- fast weights and differentiable plasticity;
- mixture-of-experts, modular routing, and task/context gating;
- latent-cause/context inference;
- compositional generalization;
- graph neural networks and neural algorithmic reasoning;
- symbolic graph/path lookup and oracle context-gated baselines;
- hippocampal/CLS inspiration;
- Exp15 minimal neural comparator posture.

The table explicitly separates:

- what the manuscript inherits from prior work;
- what is not claimed as novel;
- what the manuscript contributes narrowly.

## Work deliberately not completed in this pass

- `MANUSCRIPT_V2.md` placeholder keys were not converted to a journal-specific citation style because no repository citation convention or target venue style exists yet.
- A `.bib` file was not added because doing so would prematurely choose a bibliography convention and would require a final BibTeX export pass.
- The manuscript was not rewritten wholesale.
- Figure/table placements were not changed because no new human venue decision was available.
- No experiments were rerun and no experimental record was modified.

## Remaining blockers

- Choose the manuscript export/citation convention: BibTeX, CSL JSON, Pandoc Markdown citations, numbered references, or target-journal author-year style.
- Convert the `REFERENCES.md` ledger into that chosen convention.
- Replace `MANUSCRIPT_V2.md` placeholder citations mechanically once the convention is chosen.
- Decide whether to inline the closest-prior-art table into Section 2.7 or keep it as a companion source for the final manuscript export.
- Complete human review of `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, especially Figure 4, Figure 5, Table 3, and Table 4 placement/grouping decisions.
- Run `python scripts/verify_doc_source_paths.py` in a checked-out repository before merging.

## Recommended next pass

The next finalization pass should be a human-decision pass rather than another citation-audit pass:

1. Decide the citation/export convention.
2. Decide whether the closest-prior-art table is inlined in Section 2.7.
3. Resolve figure/table placement defaults or preserve conservative defaults explicitly.
4. Run the doc path verifier locally.
