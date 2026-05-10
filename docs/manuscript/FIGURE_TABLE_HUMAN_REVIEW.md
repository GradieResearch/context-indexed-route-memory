# Figure and Table Human-Review Checklist

Status: post-human-decision placement tracker; still not a final journal art approval.

Purpose: record the required human review for generated Figures 1-5 and Tables 1-4 before treating them as final manuscript assets.

Controlling inputs:

- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/tables/table_01_claim_evidence.md`
- `docs/manuscript/tables/table_02_run_integrity.md`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`

## Summary

Claim: Figures 1-5 and Tables 1-4 form a coherent candidate V2 manuscript package, but they still require label/caption polishing and final venue formatting before submission.

Evidence: The manuscript asset pipeline generated candidate Figures 1-5, source-data mirrors, and Tables 1-3; Exp15 Table 4 has also been generated as a source-data-backed compact neural comparator table. The human placement decision has now been made for Figures 1-5 and Tables 3-4.

Caveat: Candidate assets are not automatically final submission figures. The retained claim posture after Pass 15A is narrow, and every figure/table caption should preserve that narrow posture. Table 3 remains candidate until grouping/effect-size review is completed.

## Human placement decision

- Figures 1-3: main.
- Figure 4: supplement by default unless the manuscript intentionally emphasizes the finite-budget story.
- Figure 5: main-narrow, because Exp14 helps reduce the oracle-context criticism.
- Table 3: candidate until grouping/effect-size review is done.
- Table 4: compact main-text table, because Exp15 materially shapes the paper's claims.

## Figures 1-5

| Asset | Retained placement | Claim role | Caption caveat required | Source-data status | Remaining review |
|---|---|---|---|---|---|
| Figure 1 - Conceptual route-memory schematic | Main | Framing for C1-C4 and C13 boundary language; not empirical evidence. | Must explicitly avoid implying biological validation, raw latent-world discovery, or novelty of context gating/recurrence alone. | Candidate schematic and source-data mirror exist: `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/figures/figure_01_conceptual_route_memory.svg`; `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`. | Approve labels and legend. Decide whether the schematic needs a human-redrawn polished version before submission. |
| Figure 2 - Structural plasticity and recurrence ablation | Main | C1-C4: structural storage, context separation, recurrence, and storage/execution dissociation in the tested symbolic contracts. | Must say benchmark/model-family-specific. Must not imply universal structural-plasticity necessity for all neural models, because Exp15 transition MLP variants solve the clean hard slice. Mention uncertainty/grouping status if Table 3 remains candidate. | Candidate figure and source-data mirror exist: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg`; `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`. | Approve selected rows/variants and decide final Table 3 grouping before citing exact intervals/effect sizes in prose. |
| Figure 3 - Clean capacity scaling | Main | C5: clean supplied-context ceiling scaling through tested world counts. | Must say ceiling-limited, supplied-context, tested range only. Must not claim a fitted capacity law or broad generalization. | Candidate figure and source-data mirror exist: `docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/figures/figure_03_capacity_scaling.svg`; `docs/manuscript/source_data/figure_03_capacity_scaling.csv`. | Approve caption language that makes the oracle/supplied-context limitation obvious. |
| Figure 4 - Finite structural budget/local-global pressure | Supplement by default unless finite-budget story is intentionally emphasized | C6 boundary evidence: finite structural budget produces observed degradation. C7 local/global remains boundary-only unless paired seed-level analysis is added. | Must say observed degradation curve only. Must not claim fitted law. Must keep local-vs-global pressure caveated unless paired seed-level local/global inference is added. | Candidate figure and source-data mirror exist: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg`; `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`. | If later promoted back to main text, make the finite-budget story explicit and preserve C7 as boundary wording unless paired analysis is added. |
| Figure 5 - Symbolic context selection from transition cues | Main-narrow | C13: symbolic transition-cue context selection before route execution. Narrows but does not eliminate the oracle-context limitation. | Must say symbolic transition-cue selection only; not raw sensory latent-world discovery. Must state oracle context-gated table remains an upper-bound control. | Candidate figure and source-data mirror exist: `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/figures/figure_05_symbolic_context_selection.svg`; `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`. | Approve cue-corruption/cue-count caption wording and whether the oracle upper-bound caveat is prominent enough. |

## Tables 1-4

| Asset | Retained placement | Claim role | Caption caveat required | Source-data status | Remaining review |
|---|---|---|---|---|---|
| Table 1 - Claim evidence | Main/supporting | Evidence map for retained main claims C1-C6, C13, and C12 discussion/table baseline posture. | Must distinguish retained main, boundary/supplement, blocked, and non-claim evidence. Must not re-promote C9, Exp13.1 lesion evidence, Exp15 replay collapse, broad neural superiority, raw latent-world discovery, or biological validation. | Generated table exists: `docs/manuscript/tables/table_01_claim_evidence.csv`; `docs/manuscript/tables/table_01_claim_evidence.md`. | Approve headline wording and decide whether table length is suitable for main text or should become supplementary with a condensed main version. |
| Table 2 - Run integrity | Main/supporting or supplement | Provenance summary for manuscript-relevant experiments and source artifacts. | Must preserve older-run caveats: Exp11/Exp12 have older/nonstandard validation/provenance layouts; Exp15 has reconstructed-manifest/SQLite-tail caveat. | Generated table exists: `docs/manuscript/tables/table_02_run_integrity.csv`; `docs/manuscript/tables/table_02_run_integrity.md`. | Decide whether this belongs in main text, supplement, or repository-only reproducibility appendix. |
| Table 3 - Statistical summary | Candidate only until grouping/effect-size review is complete | Statistical support table for retained figures and baseline comparisons. | Must state that grouping/effect-size choices are candidate until human reviewed. Do not cite exact intervals/effects as final until retained-claim comparison grouping is approved. | Generated table exists: `docs/manuscript/tables/table_03_statistical_summary.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`. | Review row grouping claim-by-claim, especially C1/C2/C4/C13 comparisons and Exp13.2/Exp14/Exp15 effect-size grouping. |
| Table 4 - Exp15 neural comparator | Compact main-text table | C12 discussion/table baseline posture; strengthens C2/C4 caveats and narrows C1/C2 overclaiming. | Must say Exp15 is minimal fixed-profile and non-exhaustive. Must state context-conditioned transition MLP and world-head MLP solve the clean hard slice. Must keep replay collapse non-claim pending audit. Must not imply broad CIRM-over-neural superiority. | Source-data-backed table exists: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`. | Decide later whether optional memory-augmented/key-value neural baseline is needed for the eventual target venue. |

## Required caption-review checklist

For each final figure/table caption, verify:

- The caption names the exact task slice or experimental condition where relevant.
- The caption states whether the asset is conceptual, empirical, candidate, source-data-backed, or supplementary.
- The caption does not broaden CIRM into a general continual-learning, biological, perceptual, or neural-superiority claim.
- The caption distinguishes supplied context, selected symbolic context, and no-context variants.
- The caption distinguishes endpoint memorization, transition learning, suffix composition, first-step conflict accuracy, and recurrent execution.
- The caption preserves Exp15 as minimal fixed-profile neural comparator evidence.
- The caption keeps Exp15 replay collapse and Exp13.1 positive lesion evidence out of the claim set.

## Recommended next review order

1. Apply the Section 2.7 closest-prior-art prose in `docs/manuscript/draft/MANUSCRIPT_V2.md` if not already applied.
2. Update `docs/manuscript/FIGURE_PLAN.md` to mirror these placement decisions.
3. Review Table 3 grouping before citing exact intervals or effect sizes in manuscript prose.
4. Polish captions for Figures 1-3, Figure 5, and Table 4.
5. Decide later, based on venue/reviewer strategy, whether Table 1/Table 2 remain main/supporting or move to supplement/repository appendix.
