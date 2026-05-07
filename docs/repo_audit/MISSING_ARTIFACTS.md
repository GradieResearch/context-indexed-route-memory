# Missing Artifacts

Purpose: Conservatively track missing, nonstandard, or deferred artifacts for manuscript-readiness, excluding Exp13.2.

Scope: Exp13.2 is intentionally excluded from this pass. Existing Exp13.2 artifacts are not inspected, summarized, or used to close baseline blockers here.

## Summary

Claim: The repository has enough local artifacts to support a conservative internal manuscript spine, but not enough for submission readiness.
Evidence: Exp11, Exp12, Exp13, and Exp13.1 contain generated analysis CSVs, plots, and reports; audit manifests now index those paths.
Caveat: Baselines, seed-level uncertainty/effect sizes, final figure scripts, prior-art import, command verification, and license/citation metadata remain missing or incomplete.
Source path: `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`

## Manuscript-Critical Experiments

| Experiment | Present artifacts | Missing or nonstandard artifacts | Manuscript impact | Recommended action |
|---|---|---|---|---|
| Exp11 | README, launchers, code, `analysis/exp11/metrics.csv`, `runs.csv`, `progress.jsonl`, summary CSVs, report, plots. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md` | No dedicated `validation_report.md`; no run manifest with device/runtime metadata; no final figure script; no CI/effect-size table. | Strong internal evidence, not submission-ready alone. | Verify validation command on fresh checkout and add reviewed uncertainty/figure outputs. |
| Exp12 | README, launcher, `analysis/exp12/metrics.csv`, `runs.csv`, summaries, report, plots. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md` | Validation exists as `exp12_report.md` under `analysis/exp12_validation/`, not a standardized validation report; no run manifest/device metadata; no final figure script; no CI/effect-size table. | Strong but ceiling-limited scaling evidence. | Verify commands, add source-data/figure script, keep context-noise caveat. |
| Exp13 | README, launcher, validation script, `analysis/validation_report.md`, validation JSON, metrics, summaries, plots. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md` | No per-run SQLite database detected; no run manifest; holdout seen/unseen metric cleanup missing; no final figure script; no CI/effect-size table. | Boundary evidence remains useful but caveated. | Add metric cleanup if C9 remains central; add uncertainty and final scripts. |
| Exp13.1 | README, run wrappers, validator, per-run SQLite DB, `run_manifest.json`, validation report/JSON, metrics, summaries, plots. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md` | Manifest lacks explicit device/runtime metadata; lesion diagnostic failed expected pattern; no final figure script; no CI/effect-size table. | Strong internal hardening evidence with important caveats. | Do not cite lesion as positive evidence; audit/rerun only if needed; add device/runtime metadata to future manifests. |

## Supporting Experiments

Exp7-Exp10 have local generated artifacts and summaries, but they are supporting evidence only. They are not blockers unless a manuscript claim cites an exact supporting result.

| Tier | Missing or nonstandard item | Impact | Action |
|---|---|---|---|
| Supporting Exp7-Exp10 | Validation artifacts are nonstandard and commands were not rerun in this pass. | Not a blocker for the current internal spine unless elevated. | Keep as supporting/historical or verify before exact citation. |
| Supporting Exp7-Exp10 | No manuscript-grade CI/effect-size tables. | Limits use as quantitative support. | Add only if retained in figures/tables. |

## Historical Experiments

Exp1-Exp6 are historical or methodological precursor material. Missing validation reports, thread digests, or standardized run manifests are not submission blockers unless a current manuscript claim elevates them.

## Cross-Cutting Missing Artifacts

| Missing artifact | Why it matters | Current status | Source path |
|---|---|---|---|
| Separate Exp13.2 import/alignment | C12 baseline blocker cannot be marked complete in this pass. | Deferred. | `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md` |
| Seed-level CI/effect-size tables | Manuscript-grade reporting needs uncertainty and effect sizes. | Missing for C1-C11. | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py` |
| Final paper figure scripts | Current plots are generated analysis outputs, not reproducible manuscript panels. | Missing for all candidate main figures. | `docs/manuscript/FIGURE_PLAN.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv` |
| Prior-art/novelty local source artifact | C12 and novelty framing need local source support. | `Pasted text.txt` remains local verification pending. | `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md` |
| License and citation metadata | Public reuse and citation instructions are unclear. | `LICENSE` and `CITATION.cff` missing. | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` |
| Command verification log | Reproducibility claims require commands actually executed on a fresh checkout. | Commands inspected, not rerun. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` |

## Non-Blockers In This Pass

- Messy generated historical artifacts are preserved and not deleted.
- Historical experiment validation gaps are not blockers unless claims cite them centrally.
- Exp13.2 artifacts are neither fixed nor summarized here because they are out of scope.
