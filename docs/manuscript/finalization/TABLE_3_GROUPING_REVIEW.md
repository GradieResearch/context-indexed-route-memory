# Table 3 Grouping / Effect-Size Review

Date: 2026-05-10

Status: completed for the current manuscript pass via **Option B: compact final-safe main-text Table 3 plus retained detailed candidate statistical map**.

This document records the outcome of the Table 3 grouping/effect-size cleanup requested by `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`.

No experiments were rerun. No effect sizes, confidence intervals, seed counts, or statistical comparisons were invented. The current pass deliberately keeps the manuscript on descriptive, final-safe wording instead of pretending the full generated statistical map is a final inferential statistics table.

## Decision implemented

The safest Table 3 path is **Option B**:

1. Add a compact final-safe descriptive main-text Table 3:
   - `docs/manuscript/tables/table_03_compact_final_safe.md`
   - `docs/manuscript/source_data/table_03_compact_final_safe.csv`
2. Retain the generated detailed statistical map as a candidate/supplementary artifact:
   - `docs/manuscript/tables/table_03_statistical_summary.md`
   - `docs/manuscript/tables/table_03_statistical_summary.csv`

The compact table is final-safe for descriptive manuscript use because it only includes claim-level summaries whose slice definitions and caveats are explicit. It does **not** claim final effect-size comparisons.

## Inputs reviewed

- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_03_statistical_summary.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/source_data/figure_03_capacity_scaling.csv`
- `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`
- `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`
- `docs/threads/experiment14_analysis_digest.md`

## Compact final-safe Table 3 rows

| Claim | Source slice | Final-safe use | Status |
|---|---|---|---|
| C1-C4 | Exp13.1 core symbolic ablation rows: full model, no context binding, no recurrence at eval, and no structural plasticity. | Descriptive support for Figure 2 and the storage/context/recurrence/execution decomposition in the tested symbolic model family. | `final_safe_descriptive` |
| C5 | Exp12 clean supplied-context scaling across explicit world-count and route-length settings mirrored in Figure 3 source data. | Descriptive ceiling-limited supplied-context scaling through the tested range. | `final_safe_descriptive` |
| C6 | Exp13 global finite structural budget at explicit budget ratios for world_count=32 and route_length=12. | Descriptive observed finite-budget degradation. Figure 4 remains supplement-default unless the finite-budget story is intentionally emphasized. | `final_safe_descriptive_supplement_default` |
| C13 | Exp14 symbolic transition-cue selection at explicit world_count, route_length, cue_count, and corruption-rate slices. | Narrow descriptive support for symbolic transition-cue context selection and Figure 5. | `final_safe_descriptive` |

## Material intentionally kept out of final main-text Table 3

### C7 local-vs-global pressure

C7 remains boundary/supplement only. The current evidence can support caveated discussion or Figure 4 caption wording, but it should not become a standalone main statistical comparison without paired seed-level local-vs-global grouping.

### Full generated Table 3 statistical map

The generated table remains useful as a detailed candidate/supplementary statistical map, but it is not the final main-text statistics table. It still contains rows that require caution, including repeated-looking Exp14 rows, aggregate-normal confidence intervals, `nan` effect-size cells, and rows whose slice-defining fields are not visible in the rendered table.

### Effect sizes

Effect-size artifacts exist for some experiments, but this pass does not insert final effect-size comparisons into the manuscript. Exact comparison families must be approved before inferential effect-size wording is added.

### Exp15 replay collapse

Exp15 replay collapse remains a non-claim pending implementation/training-regime audit.

## Manuscript wording allowed after this pass

Allowed:

- “Table 3 summarizes final-safe descriptive statistics for the retained manuscript claims.”
- “Detailed candidate statistical-map rows are retained separately for audit and supplement planning.”
- “The compact Table 3 does not make final effect-size claims.”

Not allowed:

- Treating `table_03_statistical_summary.md` as the final manuscript statistics table.
- Promoting C7 local-vs-global pressure into a main inferential claim.
- Claiming fitted capacity laws from C6.
- Treating C13 as raw sensory latent-world discovery.
- Interpreting Exp15 replay collapse scientifically before audit.

## Remaining blockers after Table 3 split

- Run `python scripts/verify_doc_source_paths.py` in a clean checkout or CI-capable environment.
- Polish final captions and manuscript prose so they refer to the compact Table 3 path and keep the detailed statistical map as candidate/supplementary support.
- Decide final citation/export convention after venue selection.
- Add final effect sizes only if the manuscript needs inferential comparison wording rather than descriptive claim-level summaries.
