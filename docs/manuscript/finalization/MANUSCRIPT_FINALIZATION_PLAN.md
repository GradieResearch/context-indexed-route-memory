# Manuscript Finalization Plan

Purpose: convert the current limitation/threat register into a practical post-Exp15/post-15A/post-citation-ledger manuscript-finalization plan.

Controlling inputs:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/exp14_summary.md`
- `docs/experiments/exp15_summary.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`

## Executive Strategy

Do not try to solve every limitation before submission. Split the remaining work into four tracks:

| Track | Purpose | Manuscript blocking? |
|---|---|---|
| A. Claim and manuscript hygiene | Prevent overclaiming and keep the manuscript scoped as a controlled symbolic/mechanistic benchmark. | Yes |
| B. Metric/statistical cleanup | Ensure every central claim has clean seed-level uncertainty, effect-size, source-data, and figure provenance. | Yes |
| C. Citation/prior-art and venue positioning | Use the checked citation ledger and closest-prior-art table without inventing metadata or broadening claims. | Yes |
| D. Optional boundary experiments | Address lesion, stochastic robustness, consolidation, applied bridge, or memory-augmented neural baselines only if those claims are elevated. | No |

Recommended immediate next action: **human decision checkpoint for citation/export convention, closest-prior-art placement, figure/table placement, and venue baseline strategy**.

The manuscript should continue to avoid claims of solved continual learning, broad neural-network superiority, raw sensory latent-world discovery, end-to-end perception, broad biological proof, broad abstract rule induction, or unseen primitive inference.

## 1. Retained Claim Posture After Analysis Pass 15A

Claim -> Analysis Pass 15A has completed the retained-claim decision and source-CSV mapping, but it has not made the statistical package final.
Evidence -> `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` records the retained main scientific spine as C1, C2, C3, C4, C5, C6, and C13; C12 as a discussion/table baseline claim; C7, C8, C10, and C11 as boundary or supplement only; and C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad neural-superiority, raw latent-world discovery, and biological validation as out-of-main/non-claims.
Caveat -> Candidate Table 3 and generated Figures 1-5 still need human review of grouping, captions, caveats, and main-vs-supplement placement.
Source path -> `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`.

## 2. Baseline Coverage

Claim -> Baseline coverage is no longer absent, but remains incomplete for broad ML-comparison or submission-readiness claims.
Evidence -> Exp13.2 provides symbolic/algorithmic baselines. Exp15 provides a completed minimal neural comparator with validation PASS, 10 seeds, 9 variants, 5,400 seed metric rows, and 1,080 runtime rows.
Caveat -> Exp15 is fixed-profile and non-exhaustive, omits memory-augmented/key-value neural baselines, and includes replay/provenance caveats. Analysis Pass 15A keeps C12 as a discussion/table baseline claim rather than a broad readiness claim.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.

Observed Exp15 consequences:

| Result | Manuscript consequence |
|---|---|
| Context-conditioned transition MLP and world-head transition MLP solve the clean hard slice. | Drop broad neural-superiority language; frame CIRM as interpretable mechanism and benchmark decomposition. |
| Endpoint GRU/Transformer variants show endpoint-vs-composition dissociation. | Supports route-table/composition/endpoint-memorization separation. |
| No-context transition MLP solves suffix composition but fails first-step/full-route disambiguation. | Narrow context-necessity wording to incompatible local transitions and first-step/full-route conflict. |
| Replay transition MLP collapses in the hard slice. | Treat as requiring implementation/training-regime audit before scientific interpretation. |

Required next decisions:

- Decide whether Exp15 remains a compact main-text baseline table or moves to supplement for the target venue.
- Decide whether a memory-augmented/key-value neural baseline is required for the target venue.
- Keep broad CIRM-over-neural-model claims out of the manuscript.

## 3. Citation And Prior-Art Positioning

Claim -> Citation/prior-art hardening has progressed from audit to checked metadata and a closest-prior-art companion table.
Evidence -> `docs/manuscript/REFERENCES.md` records checked venue-neutral metadata for the major manuscript placeholder keys. `docs/manuscript/closest_prior_art_table.md` separates inherited prior art, non-novel claims, and the manuscript's narrow contribution. `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` and `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md` record the completed passes and remaining decisions.
Caveat -> The manuscript still lacks a final chosen citation/export convention and has not yet inlined or prose-integrated the closest-prior-art table into Section 2.7.
Source path -> `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`; `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`.

Required next decisions:

- Choose citation/export convention: Pandoc-style keys, BibTeX, CSL JSON, numbered references, target-journal author-year style, or venue-neutral ledger for now.
- Decide whether closest-prior-art material is inserted as a compact Section 2.7 table, converted to prose, or retained as a companion artifact until venue formatting.
- Do not invent fake BibTeX, fake CSL JSON, fake DOIs, or target-journal metadata.
- Do not propagate the corrected `Eichenbaum2017` mismatch. The checked entry is in `docs/manuscript/REFERENCES.md`.

## 4. Symbolic Benchmark Limitation

Claim -> The benchmark remains synthetic and symbolic.
Evidence -> Exp11-Exp15 use symbolic nodes, modes, worlds, routes, contexts, or transition cues.
Caveat -> This is not end-to-end perceptual learning or naturalistic navigation.
Source path -> `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment15_analysis_digest.md`.

Safe language:

> This benchmark intentionally uses symbolic route systems to isolate storage, context indexing, and recurrent execution. It is not a claim about end-to-end perceptual learning or naturalistic navigation.

No new experiment is required unless the manuscript attempts to make applied or perceptual claims.

## 5. Oracle Context And Symbolic Context Selection

Claim -> Exp14 partially reduces the oracle-world-label limitation by selecting symbolic context from transition cues.
Evidence -> Exp14 validation and summary artifacts support symbolic transition-cue context selection; Exp13.2 oracle context-gated lookup remains a clean supplied-context upper bound.
Caveat -> Exp14 is not raw sensory latent-world discovery, and oracle context gating should not be described as a defeated competitor.
Source path -> `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.

Required asset work:

- Human-review whether Exp14 remains main-narrow Figure 5 or moves to supplement.
- Caption it as symbolic transition-cue context selection.
- Preserve the oracle-context-gated table as an upper-bound caveat.

## 6. Metric And Statistical Hardening

Claim -> Central claims still need final manuscript-grade statistics and source-data-backed figures/tables.
Evidence -> Current docs have candidate assets and many generated analysis summaries, but not all retained claims have final reviewed effect-size groupings or approved source-data manifests/captions.
Caveat -> Candidate analysis plots are not final manuscript figures.
Source path -> `docs/manuscript/FIGURE_PLAN.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.

Required outputs:

- Human-reviewed grouping for retained-claim CIs/effect sizes.
- Human-reviewed Figures 1-5 and Tables 1-4 captions.
- `docs/source_data/SOURCE_DATA_MANIFEST.csv` synchronized with final panel/table decisions.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` synchronized with retained claims.
- `docs/manuscript/tables/table_03_statistical_summary.md` reviewed and aligned.

Acceptance criteria for every retained central claim:

- mean;
- standard deviation or standard error;
- 95% confidence interval;
- seed count;
- effect size for direct comparisons where appropriate;
- source artifact path;
- figure/table reference.

C9 must stay out of the main claim set unless seen/unseen/all route-table and composition split metrics are cleaned.

## 7. Known Retained Scope Boundaries

Keep these as explicit limitations unless new evidence is added:

| Boundary | Posture |
|---|---|
| Exp13.1 lesion diagnostic | Do not use as positive mechanism evidence unless audited/rerun. |
| Consolidation | Frame as preliminary stability/plasticity bias, not required or accuracy-rescuing. |
| Context corruption | Frame as symbolic wrong-world/cue-evidence sensitivity, not generic stochastic robustness. |
| Continuous/noisy input bridge | Keep preliminary or supplementary; not end-to-end perception. |
| Biological framing | Computational inspiration only, not a validated hippocampal theory. |
| Exp15 replay variant | Audit before citing as scientific evidence about replay. |
| Exp15 neural scope | Minimal fixed-profile comparator, not architecture search. |
| Citation convention | Human/venue decision pending; keep `REFERENCES.md` as venue-neutral ledger until chosen. |
| Closest-prior-art placement | Human/venue decision pending; keep `closest_prior_art_table.md` as companion artifact until chosen. |

## 8. Reproducibility And Provenance

Claim -> Exp15 includes runtime/hardware metadata, but has a manifest/SQLite provenance caveat.
Evidence -> `run_manifest.json` records runtime/hardware fields and `recovered_after_failed_sqlite_tail: true`; local SQLite inspection found an empty `run_manifest` table.
Caveat -> Treat CSV artifacts as authoritative unless a later audit says otherwise.
Source path -> `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`; `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

Future manifests should preserve explicit runtime/hardware metadata:

```json
{
  "python_version": "...",
  "platform": "...",
  "processor": "...",
  "cpu_count": "...",
  "ram_gb": "...",
  "gpu_available": true,
  "gpu_name": "...",
  "cuda_version": "...",
  "torch_version": "...",
  "numpy_version": "...",
  "start_time_utc": "...",
  "end_time_utc": "...",
  "duration_seconds": "...",
  "git_commit": "...",
  "git_branch": "...",
  "command": "...",
  "profile": "validation|full"
}
```

## 9. License, Citation, And Release Metadata

Before public release or manuscript submission:

1. Choose a license.
2. Add `LICENSE`.
3. Add `CITATION.cff`.
4. Add repository citation instructions.
5. Optionally archive a release with Zenodo after manuscript/preprint stabilization.

License selection must remain a human decision.

## Recommended Work Order

1. Human decision checkpoint: choose citation/export convention.
2. Human decision checkpoint: decide closest-prior-art Section 2.7 placement.
3. Human-review generated Figures 1-5 and Tables 1-4 for caption wording, caveats, and main-vs-supplement placement.
4. Finalize retained-claim CI/effect-size grouping for Table 3.
5. Decide whether Exp15 remains a compact main-text baseline table or moves to supplement for the target venue.
6. Decide whether optional memory-augmented/key-value neural baselines are required for the target venue.
7. Apply the chosen citation convention and closest-prior-art placement to `MANUSCRIPT_V2.md`.
8. Add runtime metadata standards, license, and citation metadata.
9. Revisit whether optional Exp16-Exp20 work is still necessary.

## Numbering Posture

| Work item | Name | Required now? | Notes |
|---|---|---|---|
| Experiment 15 | Minimal Neural Baseline Comparator | Completed minimal evidence | Integrated with non-exhaustive, replay, and provenance caveats. |
| Analysis Pass 15A | Manuscript Statistical Hardening | Completed as control pass | Retained claims and source CSVs are mapped; final human-reviewed CI/effect-size grouping remains pending. |
| Post-15A citation audit | Citation/prior-art and figure/table review artifact creation | Completed as control pass | `CITATION_PRIOR_ART_AUDIT.md` and `FIGURE_TABLE_HUMAN_REVIEW.md` exist. |
| Citation ledger pass | Checked references and closest-prior-art companion table | Completed as control pass | `REFERENCES.md`, `closest_prior_art_table.md`, and insertion report exist. |
| Citation-ledger integration status | Current citation/placement decision status | Completed as control pass | `CITATION_LEDGER_INTEGRATION_STATUS.md` exists. |
| Human decision checkpoint | Citation convention, closest-prior-art placement, figure/table decisions | Yes | Current next documentation/manuscript-readiness item; not a new experiment. |
| Repository Pass 15B | Submission Metadata and Reproducibility Hardening | Yes, after human decisions / guarded manuscript integration | Not a new experiment. |
| Optional neural baseline successor | Memory-augmented/key-value neural comparator | Venue-dependent | Only if target venue/reviewer posture requires broader neural coverage. |
| Experiment 16 | Lesion Diagnostic Audit | No | Only if positive lesion evidence is desired. |
| Experiment 17 | Perceptual / Continuous Applied Bridge | No | Future applied bridge. |
| Experiment 18 | Stochastic Context Corruption and Selection Margins | Optional | Only if generic robustness is elevated. |
| Experiment 19 | Consolidation Dose-Response Under Interference Pressure | No | Only if consolidation becomes central. |
| Experiment 20 or analysis-only pass | Seen-vs-Unseen Primitive Metric Cleanup | Optional | Needed only if C9 becomes central. |

## Bottom Line

Exp15, Analysis Pass 15A, the citation/prior-art audit, the checked citation ledger, and the citation-ledger integration-status pass are complete as finalization control steps. Do not start additional new experiments by default. Most remaining limitations should be handled as human citation/placement decisions, guarded manuscript integration, final statistical grouping, source-data/caption discipline, and future-work framing rather than new experimental obligations.
