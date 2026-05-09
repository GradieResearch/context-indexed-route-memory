# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Move from **post-15A audit capture** into **final citation insertion, closest-prior-art table writing, and human approval of generated candidate figures/tables**.

Analysis Pass 15A is captured in `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` and reflected in `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`. The next hardening pass has now produced:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

Claim: The repository has a conservative V2 manuscript draft, a post-Exp15 claim-narrowing layer, a retained-claim decision, candidate manuscript figures/tables, an updated statistical-readiness map, a citation/prior-art audit, and a human-review checklist for Figures 1-5 and Tables 1-4, but it is not submission-ready.

Evidence: Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 have local artifacts and imported summaries. Exp13.2 partially satisfies symbolic/algorithmic baseline coverage, Exp14 supports symbolic transition-cue context selection, Exp15 adds minimal fixed-profile neural comparator evidence, V2 Table 4 captures the Exp15 hard-slice comparator, and the post-15A audit documents citation placeholders plus candidate prior-art metadata.

Caveat: The manuscript still needs final bibliography insertion, final related-work prose, closest-prior-art table writing, human-reviewed captions/figure placement, final seed-level statistical grouping, fresh command verification, and license/citation metadata. Exp15 neural coverage is fixed-profile and non-exhaustive; optional memory-augmented neural baselines remain a venue/reviewer decision.

Source path: `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

## Step 4 Manuscript Asset Pipeline Status

Claim -> A reproducible candidate manuscript asset pipeline now exists for the frozen first-manuscript claim set.

Evidence -> `python scripts/manuscript_assets/build_manuscript_assets.py` generates candidate Figures 1-5, source-data CSVs, claim/run-integrity/statistical tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`. Exp15 Table 4 has also been generated as a source-data-backed V2 comparator table. `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` now records the required human decisions for these assets.

Caveat -> These are generated candidate manuscript assets, not human-approved final journal figures or final captions. Exp14 placement remains main-vs-supplement unresolved, Exp13.2 remains symbolic/algorithmic baseline evidence only, Exp15 is a minimal fixed-profile neural comparator, and prior-art/optional neural-baseline decisions remain open.

Source path: `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`.

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| Path verifier and CI workflow. | Active documentation paths can be checked locally and in GitHub Actions. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
| Exp13.1 publication-hardening import. | Exp13.1 artifacts are documented with caveats; lesion diagnostic remains non-positive. | `docs/experiments/exp13_1_summary.md`; `docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md` |
| Exp13.2 symbolic/algorithmic baseline import. | Exp13.2 artifacts are documented as partial baseline coverage; oracle context-gated lookup matches CIRM on clean supplied-context route memory. | `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment13_2_analysis_digest.md` |
| Exp14 latent-context digest import. | Exp14 full, validation, and smoke runs are documented; C13 is added as symbolic transition-cue context-selection evidence. | `docs/experiments/exp14_summary.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment14_analysis_digest.md` |
| Exp15 neural baseline comparator import. | Exp15 full run digest and local artifacts are imported; neural baseline comparator is completed as minimal fixed-profile evidence, with manifest/SQLite and replay caveats. | `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md` |
| Manuscript V2 capture. | V2 manuscript draft exists with conservative post-Exp15 posture. | `docs/manuscript/draft/MANUSCRIPT_V2.md` |
| Exp15 Table 4 capture. | Compact source-data-backed V2 neural comparator table exists. | `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` |
| Analysis Pass 15A retained-claim hardening. | Retained main claims and source CSVs are explicitly mapped; statistical-readiness tracker separates retained, boundary, supplement, blocked, and non-claim evidence. | `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` |
| Post-15A citation/prior-art audit. | Citation placeholders are mapped to prior-art families and candidate real metadata; the missing novelty/prior-art artifact is explicitly not invented and is retired as the only path forward. | `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/NOVELTY_POSITIONING.md` |
| Post-15A figure/table human-review checklist. | Figures 1-5 and Tables 1-4 have placement, claim role, caption caveat, source-data status, and unresolved decision rows. | `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md` |

## P0 - Current Next Pass

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Convert citation audit into final bibliography and manuscript citations. | Related-work/citation hygiene is now the most important manuscript blocker after retained-claim hardening. | `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Verified bibliography entries, replaced placeholders, and final related-work citations. |
| Write the closest-prior-art risk table if retained in Section 2.7. | The manuscript currently calls for this table but does not yet contain final source-backed content. | `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Compact table separating CIRM from task-gated lookup, MoE routing, fast weights, external memory, graph algorithms, and memory-augmented neural baselines. |
| Human-review generated candidate Figures 1-5 and Tables 1-4. | Candidate assets exist, but final captions, source-data statements, and main-vs-supplement placement require review. | `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` | Approved figure/table placement and caption caveats. |
| Decide whether target venue strategy requires a memory-augmented/key-value neural comparator. | Exp15 is intentionally minimal and fixed-profile; broader neural coverage is venue-dependent. | `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Explicit venue/reviewer decision; do not start a new experiment by default. |

## P0 - Required Before Manuscript Submission

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Finalize seed-level confidence intervals and effect sizes for retained claims. | Pass 15A mapped sources but did not certify every statistical comparison as final. | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings. |
| Human-review generated candidate figures and captions. | Generated assets are reproducible candidates, not final journal figures. | `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` | Final captions, approved placement, and journal-specific formatting changes. |
| Verify manuscript-critical run commands on a fresh checkout. | Commands were inspected/documented, not freshly rerun in this pass. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Command log with pass/fail, runtime, hardware, and expected outputs. |
| Fix holdout metrics if retaining Exp13 holdout claims centrally. | C9 remains out of the main claim set until seen/unseen/all metric cleanup is done. | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | Split metrics such as `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and matching composition splits. |
| Audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence. | Targeted critical-edge lesions were less damaging than random count-matched lesions. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md` | Corrected lesion diagnostic or explicit decision not to cite lesion evidence. |
| Audit Exp15 replay variant before citing it. | Replay collapse is a non-claim pending implementation/training-regime audit. | `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | Implementation/training-regime audit or explicit decision not to cite replay scientifically. |
| Add license and citation metadata. | Reuse and citation terms are unclear. | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen `LICENSE` and `CITATION.cff`. |

## P1 - Strongly Recommended

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Add stochastic context corruption only if generic robustness is claimed. | Current evidence supports identity/selection sensitivity, not generic stochastic robustness. | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition. |
| Refine consolidation analysis only if consolidation becomes central. | Current evidence supports bias/tradeoff, not necessity. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws only if C6/C7 become stronger quantitative claims. | Current evidence supports observed degradation, not a fitted capacity law. | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Capacity-law summaries and final figure panel if retained. |
| Upgrade local-vs-global comparison if C7 is elevated. | C7 is boundary/supplement only after Pass 15A. | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as outputs change. | Manuscript claims must remain traceable to source paths. | `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` | Updated indexes after any new run or source-data import. |

## P2 - Future Work

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Richer latent-world inference. | Exp14 covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment14_analysis_digest.md` | New experiment directory only if the manuscript needs a stronger non-symbolic bridge. |
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | `docs/threads/experiment12to13_export.md` | Applied bridge experiment, not claimed by current C11. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | `docs/theory/BIOLOGICAL_FRAMING.md` | Theory note or discussion section with citations. |
