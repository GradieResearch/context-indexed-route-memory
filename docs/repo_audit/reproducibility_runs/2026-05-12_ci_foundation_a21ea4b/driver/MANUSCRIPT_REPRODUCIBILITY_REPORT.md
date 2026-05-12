# Manuscript Reproducibility Report

Generated at: 2026-05-12T14:53:44+00:00

Overall status: **WARN**

## Environment

- commit_sha: `a21ea4b6bcd0732952d7964a81f073de72cf5299`
- branch: `fresh-foundation-repro-report-v2`
- python: `3.11.15 (main, Mar  3 2026, 16:10:12) [GCC 13.3.0]`
- platform: `Linux-6.17.0-1010-azure-x86_64-with-glibc2.39`
- machine: `x86_64`
- processor: `x86_64`
- command: `python scripts/reproduce_manuscript.py --profile foundation`

## Profile Summary

| Profile | Status | PASS | WARN | FAIL | Elapsed seconds |
|---|---:|---:|---:|---:|---:|
| validate-artifacts | PASS | 122 | 0 | 0 | 0.02 |
| rebuild-manuscript-assets | WARN | 6 | 1 | 0 | 0.03 |
| smoke | PASS | 6 | 0 | 0 | 0.00 |

## Profile: validate-artifacts

Status: **PASS**

Caveats:

- This profile validates committed artifacts and schemas; it does not rerun expensive experiments.
- Boundary and non-claim rows are checked but not promoted to manuscript evidence.

### Check counts

- PASS: 122
- WARN: 0
- FAIL: 0

## Profile: rebuild-manuscript-assets

Status: **WARN**

Caveats:

- This profile runs the manuscript asset build script from committed artifacts.
- Generated file differences should be reviewed before committing regenerated assets.

### Warnings and failures

| Status | Check | Claim | Path | Message |
|---|---|---|---|---|
| WARN | asset_build | - | `scripts/manuscript_assets/build_manuscript_assets.py` | Manuscript asset build did not complete in this environment; install experiment/asset dependencies and rerun locally. |

### Check counts

- PASS: 6
- WARN: 1
- FAIL: 0

## Profile: smoke

Status: **PASS**

Caveats:

- The smoke profile currently records the execution plan only.
- Full execution is intentionally opt-in so preserved historical outputs are not overwritten.

### Check counts

- PASS: 6
- WARN: 0
- FAIL: 0

## Interpretation

This report is claim-scoped. It validates the committed evidence package and/or records planned execution paths; it does not by itself promote boundary or non-claim evidence into the retained manuscript claim set.

Full manuscript submission readiness still requires human venue/citation decisions, final statistical comparison-family choices, and any target-venue reviewer-strategy baseline decision.
