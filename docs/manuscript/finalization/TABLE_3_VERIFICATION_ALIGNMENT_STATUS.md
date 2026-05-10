# Table 3 Verification And Alignment Status

Date: 2026-05-10

Purpose: record the status of the compact Table 3 manuscript-placeholder and source-path verification pass requested after the compact final-safe Table 3 split.

## Status

Result: **complete for the compact Table 3 manuscript-placeholder and source-path verification blocker**.

The compact Table 3 split itself is complete. `docs/manuscript/draft/MANUSCRIPT_V2.md` now distinguishes the compact descriptive main-text Table 3 from the detailed generated statistical map.

## Manuscript Table 3 alignment

`docs/manuscript/draft/MANUSCRIPT_V2.md` now uses this main-text placeholder:

```md
[Table 3 here: compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Detailed generated statistical map retained as candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`. Caveat: descriptive only; do not treat as final inferential effect-size evidence or approved comparison-family statistics.]
```

The main-text Table 3 path is:

- `docs/manuscript/tables/table_03_compact_final_safe.md`
- `docs/manuscript/source_data/table_03_compact_final_safe.csv`

The detailed generated statistical map remains candidate/supplementary audit support only:

- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_03_statistical_summary.csv`

Do not add final effect-size language or approved comparison-family statistics unless those groupings are explicitly reviewed later.

## Verification result

Command:

```bash
python scripts/verify_doc_source_paths.py
```

Execution environment: GitHub Actions pull-request checkout for branch `finalize-table3-placeholder-verification`.

Result: **passed**.

Output:

```text
# Documentation Source Path Verification
Files scanned: 133
OK paths: 6030
Missing active paths: 0
Skipped planned/future paths: 13
Skipped local-verification-pending paths: 56

## Missing Active Paths
None

## Skipped Planned/Future Paths
AGENTS.md:22: experiments/exp13_1_publication_hardening/ (explicitly marked planned/future/pending)
AGENTS.md:22: experiments/experimentNN_descriptive_name/ (explicitly marked planned/future/pending)
docs/manuscript/draft/MANUSCRIPT_V1.md:533: docs/manuscript/PRIOR_ART_LIVE_SEARCH_20260508.md (explicitly marked planned/future/pending)
docs/manuscript/draft/MANUSCRIPT_V1.md:533: docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md (explicitly marked planned/future/pending)
docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md:7: docs/manuscript/BASELINE_RESULTS.md (explicitly marked planned/future/pending)
docs/repo_audit/P0_REMEDIATION_QA.md:21: experiments/expNN_descriptive_name/ (explicitly marked planned/future/pending)
docs/repo_audit/P0_REMEDIATION_QA.md:38: experiments/exp13_1_publication_hardening/ (explicitly marked planned/future/pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:19: experiments/expNN_descriptive_name/ (explicitly marked planned/future/pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:19: experiments/experimentNN_descriptive_name/ (explicitly marked planned/future/pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:20: docs/manuscript/BASELINE_RESULTS.md (explicitly marked planned/future/pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:22: docs/manuscript/BASELINE_RESULTS.md (explicitly marked planned/future/pending)
docs/threads/experiment13_2_analysis_digest.md:537: docs/manuscript/BASELINE_RESULTS.md (explicitly marked planned/future/pending)
docs/threads/experiment13_2_analysis_digest.md:656: docs/manuscript/BASELINE_RESULTS.md (explicitly marked planned/future/pending)

## Skipped Local-Verification-Pending Paths
AGENTS.md:61: experiment12_capacity_generalization/analysis/ (explicitly marked missing/local verification pending)
docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv:40: Pasted text.txt (explicitly marked missing/local verification pending)
docs/manuscript/CITATION_PRIOR_ART_AUDIT.md:30: Pasted text.txt (explicitly marked missing/local verification pending)
docs/manuscript/CLAIMS_AND_EVIDENCE.md:44: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md:5: docs/imports/experiment13_1_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md:9: docs/imports/experiment13_1_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md:5: docs/imports/experiment13_2_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md:9: docs/imports/experiment13_2_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md:16: docs/imports/experiment14_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md:115: experiments/experiment14_latent_context_inference/e14_analysis.zip (explicitly marked missing/local verification pending)
docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md:6: docs/imports/experiment15_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md:8: docs/imports/experiment15_analysis_digest.zip (staged import bundle reference; not retained as active repo artifact)
docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md:41: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md:115: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/MISSING_ARTIFACTS.md:43: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md:37: experiments/experiment14_latent_context_inference/e14_analysis.zip (explicitly marked missing/local verification pending)
docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md:72: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:15: CLAIMS_AND_EVIDENCE.md (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:15: FIGURE_PLAN.md (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:15: PUBLICATION_READINESS.md (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:15: REPRODUCIBILITY_AUDIT.md (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:18: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_QA.md:32: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_REPORT.md:17: experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv (explicitly marked missing/local verification pending)
docs/repo_audit/P0_REMEDIATION_REPORT.md:77: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P1_REMEDIATION_QA.md:23: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/P2_REMEDIATION_REPORT.md:186: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:26: Pasted text.txt (explicitly marked missing/local verification pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:27: docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md (explicitly marked missing/local verification pending)
docs/repo_audit/PATH_VERIFICATION_REPORT.md:37: Pasted text.txt (explicitly marked missing/loca
... [truncated]
```

## Remaining blocker

The Table 3 placeholder/source-path verification loop is closed. The next blocker is final figure/table caption polish and manuscript TODO cleanup, especially Figures 1-3, Figure 5, compact Table 3, and Table 4.
