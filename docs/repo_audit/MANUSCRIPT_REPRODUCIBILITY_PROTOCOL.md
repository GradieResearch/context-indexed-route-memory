# Manuscript Reproducibility Protocol

Purpose: define the concrete reproducibility package required before the V3 manuscript is submitted for review.

This protocol is scoped to the current narrow manuscript claim set. It does not require rerunning every historical experiment. It requires claim-scoped validation, manuscript asset regeneration, and fresh-checkout verification for manuscript-critical experiments.

## Inputs

Canonical claim map:

- `docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md`
- `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`

Current reproducibility audit:

- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

Retained claim and statistical-hardening controls:

- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`

Manuscript asset pipeline:

- `scripts/manuscript_assets/build_manuscript_assets.py`
- `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`

## Required command surface

Implement the planned future master driver with these profiles:

```bash
python scripts/reproduce_manuscript.py --profile validate-artifacts
python scripts/reproduce_manuscript.py --profile rebuild-manuscript-assets
python scripts/reproduce_manuscript.py --profile smoke
python scripts/reproduce_manuscript.py --profile rerun-critical --jobs 1
python scripts/reproduce_manuscript.py --profile full-critical --jobs 1
```

The script should be conservative by default:

- Do not overwrite preserved experiment outputs.
- Write reruns to new timestamped directories.
- Do not run expensive full profiles unless requested.
- Do not require GPU unless the selected profile explicitly needs it.
- Produce machine-readable JSON plus Markdown reports.

Planned future outputs:

- manuscript reproducibility Markdown report;
- manuscript reproducibility JSON report.

## Profile definitions

### validate-artifacts

Purpose: check that the committed evidence package is internally consistent.

Must check:

- every source path in `docs/manuscript/source_data/manuscript_claim_artifact_map.csv` exists unless explicitly marked non-claim/boundary/future;
- required validation artifacts exist;
- manuscript source-data mirrors exist;
- required CSVs can be parsed;
- required metric columns exist for each retained claim;
- required variants for Exp15 Table 4 exist;
- no retained claim depends only on a missing, planned, or historical-only artifact.

Should run quickly and be CI-suitable.

### rebuild-manuscript-assets

Purpose: regenerate manuscript candidate assets from committed experiment outputs.

Must run:

```bash
python scripts/manuscript_assets/build_manuscript_assets.py
```

Must report:

- files generated or updated;
- source artifacts consumed;
- whether regenerated source-data mirrors match committed mirrors;
- whether Figure 1-5 / Table 1-4 candidates are present.

### smoke

Purpose: verify executable paths for manuscript-critical experiments without running expensive full experiments.

Should invoke smoke/validation entry points where available:

- Exp11 validation-only launcher, if retained in V3.
- Exp12 validate profile.
- Exp13 smoke profile.
- Exp13.1 validation wrapper.
- Exp13.2 validation or artifact-validation path.
- Exp14 smoke or validation wrapper.
- Exp15 validation wrapper.

The smoke profile may skip experiments that lack quick launchers, but it must record the skip with a reason.

### rerun-critical

Purpose: rerun manuscript-critical experiments at a standard or validation-heavy level from a fresh checkout.

This is author-facing, not CI-default.

Must:

- write outputs to new timestamped directories;
- preserve original committed outputs;
- record command, runtime, environment, and hardware;
- compare claim-level metrics to committed evidence using explicit tolerances;
- report qualitative agreement/disagreement with each retained claim.

### full-critical

Purpose: provide a full rerun path for authors or highly motivated reviewers.

This may take hours. It should be opt-in only.

Must:

- document expected runtime range;
- support `--jobs` for bounded parallelism;
- support CPU/GPU choice where relevant;
- never silently overwrite historical outputs.

## Claim-level validation requirements

### C1

- Verify Exp13.1 full-run ablation metrics exist and parse.
- Verify Exp13.2 summary exists and parse.
- Verify Exp15 summary exists and parse so the C1 boundary is visible.
- Confirm the report states C1 is benchmark/model-family-specific.

### C2

- Verify context/no-context and conflict-sensitive metrics for Exp13.2/Exp14/Exp15.
- Verify Table 4 source data exists and includes first-step context conflict, seen-route composition, suffix-route composition, retention, and transition accuracy columns.
- Confirm the report states context necessity is conflict-specific, not blanket suffix necessity.

### C3

- Verify no-recurrence and full-model route-table/composition evidence exists.
- Confirm recurrence is framed as execution mechanism, not novelty by itself.

### C4

- Verify endpoint, transition, rollout, suffix, and seen-route evidence exists where Table 4 is used.
- Confirm decomposition, not architecture ranking.

### C5

- Verify Exp12 capacity summary and metrics exist.
- Confirm no fitted capacity law is claimed.

### C6

- Verify Exp13 capacity-pressure summary and metrics exist.
- Confirm observed degradation only.

### C13

- Verify Exp14 summary, metrics, effect sizes, and Figure 5 source data exist.
- Confirm symbolic transition-cue context selection only.

### C12

- Verify Exp13.2 and Exp15 baseline summaries/effect-size artifacts exist.
- Confirm baseline coverage is non-exhaustive.

## Statistical output requirements

Add these planned future outputs in a follow-up implementation pass:

- reproducibility claim summary CSV;
- seed-level core-claim metrics CSV;
- reproducibility claim summary Markdown table.

These should be claim-scoped, not a giant all-experiment matrix.

Minimum columns for reproducibility claim summary:

```text
claim_id,role,experiment_ids,metric_family,source_artifacts,n_units,summary_value,interval_or_spread,effect_size,status,caveat,fresh_rerun_status
```

Minimum columns for seed-level core-claim metrics:

```text
claim_id,experiment_id,run_id,seed,variant,world_count,route_length,metric_name,metric_value,source_artifact
```

## Report requirements

The planned future manuscript reproducibility report should include:

- repository commit SHA;
- branch/ref;
- date/time;
- OS;
- Python version;
- relevant package versions;
- CPU/GPU/hardware summary;
- selected profile;
- command executed;
- runtime;
- per-claim pass/fail/warn;
- per-experiment pass/fail/warn;
- source-path verification result;
- artifact validation result;
- manuscript asset regeneration result;
- known caveats;
- whether the report is author-generated or CI-generated.

## Acceptance criteria before V3 submission

- `python scripts/verify_doc_source_paths.py` passes.
- The planned future validate-artifacts profile passes.
- The planned future rebuild-manuscript-assets profile passes or records exact generated-file differences for review.
- The planned future smoke profile passes or records justified skips.
- A fresh manuscript reproducibility report is committed.
- Claim-scoped statistical summaries exist for retained claims.
- V3 wording matches only claims marked reproducibility-backed or explicitly caveated.

## Non-goals

- Do not rerun all 15 experiments by default.
- Do not promote boundary/supplement claims to main claims.
- Do not interpret Exp15 replay collapse without audit.
- Do not add broader memory-augmented/key-value neural baselines unless a human target-venue/reviewer decision requires them.
- Do not overwrite existing historical outputs.
