# Citation and Prior-Art Audit

Status: superseded by the checked citation ledger and closest-prior-art table; retained as the audit trail for the post-Analysis-Pass-15A citation pass.

Purpose: identify citation placeholders, related-work risk areas, and the disposition of the missing novelty/prior-art source artifact before final manuscript citation hardening.

Controlling inputs:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/NOVELTY_POSITIONING.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

## Summary

Claim: The manuscript has plausible related-work placeholder keys and now has a checked, venue-neutral bibliography ledger, but it still does not have a chosen final citation/export convention.

Evidence: `docs/manuscript/REFERENCES.md` maps the current `MANUSCRIPT_V2.md` placeholder keys to checked metadata. `docs/manuscript/closest_prior_art_table.md` supplies the manuscript-facing closest-prior-art comparison structure. `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` records the citation-ledger pass and remaining human decisions.

Caveat: This audit is no longer the authoritative bibliography metadata source. Use `docs/manuscript/REFERENCES.md` for checked reference metadata and only convert it to BibTeX, CSL JSON, numbered references, or author-year references after a target export convention is chosen.

## Missing novelty/prior-art source artifact disposition

The earlier missing novelty/prior-art source artifact was referred to as `Pasted text.txt` or, more generally, the missing novelty/prior-art source artifact. Repository search found references to the artifact in audit/planning documents, but no durable local source file containing its original contents.

Disposition:

- The original artifact remains absent.
- Its contents are not reconstructed or invented here.
- The dependency on that artifact is retired as a blocker for the next pass.
- `docs/manuscript/REFERENCES.md` and `docs/manuscript/closest_prior_art_table.md` are now the checked replacement path for citation/prior-art hardening unless the original artifact is later recovered.

## Corrected citation metadata note

Do not propagate the earlier `Eichenbaum2017` DOI/title mismatch.

The checked ledger entry is:

- Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. *Neuron*, 95(5), 1007-1018. DOI: `10.1016/j.neuron.2017.06.036`.

The older audit entry that paired this title with DOI `10.1038/nrn.2017.74` is superseded by `docs/manuscript/REFERENCES.md` and should not be used in a final bibliography.

## Citation placeholder audit outcome

| Placeholder family | Current disposition | Authoritative metadata source |
|---|---|---|
| Continual learning and catastrophic interference | Real sources identified and checked in the ledger; retain as background/framing only. | `docs/manuscript/REFERENCES.md` |
| Memory-augmented computation and few-shot memory | Real sources identified and checked in the ledger; phrase as memory-augmented neural systems unless exact transformer-memory references are later added. | `docs/manuscript/REFERENCES.md` |
| Fast weights, associative memory, and differentiable plasticity | Real sources identified and checked in the ledger; do not claim dynamic memory or plasticity is novel in isolation. | `docs/manuscript/REFERENCES.md` |
| Context, gating, modularity, and latent task inference | Real sources identified and checked in the ledger; do not claim novelty for context gating, modular routing, parameter isolation, supplied task labels, or latent-cause inference. | `docs/manuscript/REFERENCES.md` |
| Compositional generalization, graph reasoning, and neural algorithmic reasoning | Real sources identified and checked in the ledger; retain route-memory decomposition as the contribution rather than broad graph reasoning. | `docs/manuscript/REFERENCES.md` |
| Hippocampal indexing, cognitive maps, and complementary learning systems | Real sources identified and checked in the ledger; keep neuroscience citations motivational only. | `docs/manuscript/REFERENCES.md` |
| Closest-prior-art comparison | Source-backed companion artifact exists; final manuscript insertion remains pending until the citation/export convention and table/prose placement are chosen. | `docs/manuscript/closest_prior_art_table.md` |

## Related-work wording risks still requiring manuscript-facing cleanup

| Risk | Current issue | Required fix before submission |
|---|---|---|
| `modern transformer memory systems` | Section 2.2 mentions modern transformer memory systems, but the current ledger mostly supports external memory, memory networks, matching networks, meta-learning, and fast-weight/linear-attention background. | Either add exact transformer-memory/long-context references in a later pass, or narrow the phrase to memory-augmented neural systems already covered by the ledger. |
| `task masks, adapters, parameter isolation` | Section 2.4 names several architectural families, but the current ledger supports progressive networks, PathNet, sparsely gated MoE, and mixture-of-experts more directly than task masks/adapters. | Add exact task-mask/adapter references if those words remain, or narrow to architectural expansion, path/module selection, parameter isolation, and sparse expert routing covered by current sources. |
| `closest prior-art risk table` | A checked companion table now exists, but manuscript insertion remains a formatting/placement decision. | Insert a compact Section 2.7 table or a prose version once final citation/export convention and manuscript placement are chosen. |
| `biological mechanism` | Neuroscience citations motivate indexing, CLS, and cognitive maps, but do not validate CIRM biologically. | Keep all biological statements as computational inspiration unless new evidence is added. |
| `broad neural comparison` | Exp15 is minimal fixed-profile; memory-augmented/key-value neural baselines are not present. | Keep C12 as discussion/table baseline posture unless the venue requires optional broader neural baselines. |

## Recommended manuscript-facing replacement language

Use this replacement for the risky Section 2.2 phrase unless a later pass adds exact transformer-memory references:

> Memory-augmented neural systems separate computation from storage by providing external or differentiable memory mechanisms. Neural Turing Machines, Differentiable Neural Computers, Memory Networks, End-to-End Memory Networks, memory-augmented meta-learning systems, and matching-network approaches all explore ways to read, write, retrieve, and reuse information.

Use this replacement for the risky Section 2.4 phrase unless a later pass adds exact task-mask/adapter references:

> Context-conditioned computation and modular routing are long-standing ideas. Mixture-of-experts models use gating to select specialized components, while architectural expansion, path/module selection, parameter isolation, and sparse expert routing seek to reduce interference by separating task- or context-relevant computation.

These snippets intentionally preserve bracketed placeholder keys in `MANUSCRIPT_V2.md` until the manuscript export convention is chosen.

## Current remaining citation tasks

1. Choose the manuscript export/citation convention: Pandoc-style keys, BibTeX, CSL JSON, numbered references, or target-journal author-year style.
2. Convert `docs/manuscript/REFERENCES.md` into that chosen convention without inventing metadata.
3. Mechanically replace or format `MANUSCRIPT_V2.md` placeholder citations according to the chosen convention.
4. Insert a compact closest-prior-art table or prose version into Section 2.7, or explicitly keep `docs/manuscript/closest_prior_art_table.md` as a companion artifact.
5. Keep novelty framed as the controlled route-memory decomposition and evidence map, not as novelty of context gating, recurrence, replay, task isolation, modular routing, or memory augmentation in isolation.
