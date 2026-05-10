# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Complete the remaining **compact Table 3 manuscript-placeholder and source-path verification blocker**.

The current-pass Table 3 decision has been made: use **Option B**, a compact final-safe descriptive main-text Table 3, while retaining the full generated statistical map as a candidate/supplementary artifact.

New Table 3 artifacts:

- `docs/manuscript/tables/table_03_compact_final_safe.md`
- `docs/manuscript/source_data/table_03_compact_final_safe.csv`

Retained candidate/supplementary statistical map:

- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_03_statistical_summary.csv`

Status note: `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records that the verification/alignment pass is **not complete yet**. The manuscript draft still needs its stale main-text Table 3 placeholder patched, and `python scripts/verify_doc_source_paths.py` still needs to be run from a clean local checkout or CI-capable environment.

The current active work is therefore:

1. Patch `docs/manuscript/draft/MANUSCRIPT_V2.md` so the main-text Table 3 placeholder cites `docs/manuscript/tables/table_03_compact_final_safe.md` and `docs/manuscript/source_data/table_03_compact_final_safe.csv`.
2. Keep `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv` candidate/supplementary only.
3. Run `python scripts/verify_doc_source_paths.py` after the manuscript placeholder patch.
4. Record the verifier pass/failure/inability exactly; do not mark the verifier complete unless it actually passes.
5. Keep final effect-size wording out of the manuscript unless explicit comparison families are approved.

## Current retained V2 posture

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| Manuscript V2 capture. | V2 manuscript draft exists with conservative post-Exp15 posture. | `docs/manuscript/draft/MANUSCRIPT_V2.md` |
| Checked citation ledger. | Major placeholder-key metadata is checked in a venue-neutral reference ledger. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` |
| Closest-prior-art prose. | Section 2.7 contains closest-prior-art positioning prose and the companion table is retained. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md` |
| Human decision integration. | Citation/export convention, closest-prior-art placement, and figure/table placement are recorded. | `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` |
| Table 3 compact-safe split. | Compact final-safe descriptive Table 3 now exists; the detailed generated statistical map remains candidate/supplementary and not final inferential statistics. | `docs/manuscript/tables/table_03_compact_final_safe.md`; `docs/manuscript/source_data/table_03_compact_final_safe.csv`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` |
| Table 3 verification/alignment status capture. | Current blocker is documented: patch stale manuscript placeholder and run verifier from clean local/CI environment. | `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`; `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` |
| Exp15 Table 4 capture. | Compact source-data-backed V2 neural comparator table exists. | `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` |

## P0 - Current Next Pass

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Patch stale manuscript Table 3 placeholder. | The manuscript must not cite the generated detailed statistical map as the main Table 3 path. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/tables/table_03_compact_final_safe.md`; `docs/manuscript/source_data/table_03_compact_final_safe.csv`; `docs/manuscript/tables/table_03_statistical_summary.md` | Main-text placeholder names compact Table 3 as descriptive and keeps the detailed map candidate/supplementary. |
| Run documentation source-path verifier. | New compact Table 3 files and synchronized docs should not introduce broken active paths. | `scripts/verify_doc_source_paths.py` | Passing verifier output or exact failure/inability report. |
| Sync status docs after verifier result. | The next prompt should advance only after the Table 3 placeholder and verifier result are real. | `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`; `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` | Updated docs that either close this blocker or preserve the exact failure reason. |
| Decide whether target venue strategy requires a memory-augmented/key-value neural comparator. | Exp15 is intentionally minimal and fixed-profile; broader neural coverage is venue-dependent. | `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Explicit venue/reviewer decision; do not start a new experiment by default. |

## P0 - Required Before Manuscript Submission

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Apply final citation/export convention after target venue selection. | Placeholder keys should be converted only after a convention is chosen. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Chosen bibliography/citation format without invented metadata. |
| Add inferential effect sizes only if needed. | Compact Table 3 is descriptive and does not claim final inferential comparisons. | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings, if required. |
| Human-review generated candidate figures and captions. | Generated assets are reproducible candidates, not final journal figures. | `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` | Final captions, approved placement, and journal-specific formatting changes. |
| Verify manuscript-critical run commands on a fresh checkout. | Commands were inspected/documented, not freshly rerun in this pass. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Command log with pass/fail, runtime, hardware, and expected outputs. |
| Add license and citation metadata. | Reuse and citation terms are unclear. | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen `LICENSE` and `CITATION.cff`. |

## P1 - Strongly Recommended

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Add stochastic context corruption only if generic robustness is claimed. | Current evidence supports identity/selection sensitivity, not generic stochastic robustness. | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition. |
| Refine consolidation analysis only if consolidation becomes central. | Current evidence supports bias/tradeoff, not necessity. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Upgrade local-vs-global comparison if C7 is elevated. | C7 is boundary/supplement only after Pass 15A and the compact Table 3 split. | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Paired seed-level local-vs-global table with confidence intervals. |

## P2 - Future Work

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Richer latent-world inference. | Exp14 covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment14_analysis_digest.md` | New experiment directory only if the manuscript needs a stronger non-symbolic bridge. |
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | `docs/threads/experiment12to13_export.md` | Applied bridge experiment, not claimed by current C11. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | `docs/theory/BIOLOGICAL_FRAMING.md` | Theory note or discussion section with citations. |
