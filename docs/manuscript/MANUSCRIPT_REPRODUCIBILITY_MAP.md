# Manuscript Reproducibility Map

Purpose: give reviewers and future work a claim-scoped route from manuscript claims to committed source artifacts, validation artifacts, rerun commands, and statistical caveats.

This document is the reviewer-facing companion to the machine-readable map at `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`.

## Current standard

The manuscript should target a reproducibility standard stronger than preserved outputs alone:

1. **Artifact auditability** - every manuscript claim points to exact committed inputs, outputs, tables, figures, and validation artifacts.
2. **Computational repeatability** - manuscript-critical experiments can be rerun from a clean checkout using documented commands.
3. **Manuscript asset regeneration** - final figures and tables can be rebuilt from committed experiment outputs and source-data mirrors without rerunning all experiments.
4. **Claim-scoped statistical robustness** - stochastic or seed-sensitive claims have seed-level summaries, confidence intervals/effect sizes where appropriate, and explicit comparison-family caveats.
5. **Boundary discipline** - historical, exploratory, boundary, and non-claim artifacts remain visible but are not used as central evidence.

## Claim tiers

### Tier A - manuscript-critical retained claims

These require the strongest reproducibility support before submission:

- C1 structural route storage, benchmark/model-family-specific.
- C2 context/world indexing for incompatible local transitions and first-step/full-route disambiguation.
- C3 recurrent execution for multi-step route composition.
- C4 separation of route-table storage, endpoint memorization, and composition.
- C5 clean supplied-context ceiling performance through tested world counts.
- C6 observed finite-budget degradation.
- C13 symbolic transition-cue context selection.
- C12 discussion/table baseline posture: symbolic/algorithmic baselines and minimal fixed-profile neural comparator are present, but non-exhaustive.

### Tier B - boundary/supplement evidence

These remain visible but should not be promoted without additional analysis:

- C7 local-versus-global pressure.
- C8 consolidation/stability-plasticity discussion.
- C10 context/cue corruption sensitivity.
- C11 continuous/noisy bridge.

### Tier C - non-claims or dropped claims

These must not be used as central evidence in V3:

- C9 seen/unseen primitive boundary until metric cleanup exists.
- Exp13.1 positive lesion evidence.
- Exp15 replay collapse.
- Broad CIRM-over-neural claims.
- Raw sensory latent-world discovery.
- Biological validation.

## Reviewer-facing claim map

| Claim | Role | Evidence assets | What must reproduce | Current status |
|---|---|---|---|---|
| C1 | Main | Figure 2; compact Table 3 | Exp13.1/Exp13.2 ablation pattern and Exp15 narrowing; structural storage requirement remains benchmark/model-family-specific. | Source artifacts exist; final seed-level grouping pending. |
| C2 | Main | Figures 2 and 5; Table 4 | Context/no-context conflict-sensitive first-step and full-route disambiguation, not blanket suffix-composition necessity. | Source artifacts exist; C2-wide seed grouping pending. |
| C3 | Main | Figure 2; compact Table 3 | No-recurrence separation between one-step access and multi-step composition. | Source artifacts exist; grouping pending. |
| C4 | Main | Figure 2; Table 4 | Endpoint memorization, reusable transition learning, and recurrent composition dissociate. | Table 4 source-data-backed; C4-wide grouping pending. |
| C5 | Main | Figure 3; compact Table 3 | Ceiling performance through tested supplied-context world counts only. | Source artifacts exist; no capacity-law claim. |
| C6 | Main | Figure 4; compact Table 3 | Observed finite-budget degradation curve. | Source artifacts exist; no fitted law. |
| C13 | Main-narrow | Figure 5; compact Table 3 | Symbolic transition-cue context selection before route execution. | Source artifacts and effect-size artifact exist; grouping pending. |
| C12 | Discussion/table | Table 4 | Baseline coverage exists but is fixed-profile/non-exhaustive. | Table 4 exists; optional broader neural comparator remains venue-dependent. |

The exact source artifacts and validation artifacts are in `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`.

## Required reproducibility package before submission

### 1. Artifact validation

A reviewer should be able to run one command that checks:

- all manuscript-cited artifacts exist;
- required CSV schemas are present;
- key metric columns are finite;
- expected variants/seeds/world counts are present;
- source-data mirrors match their authoritative experiment artifacts;
- historical/non-claim artifacts are not accidentally promoted.

Planned future command to implement:

```bash
python scripts/reproduce_manuscript.py --profile validate-artifacts
```

### 2. Manuscript asset regeneration

A reviewer should be able to rebuild candidate manuscript figures/tables from committed artifacts without rerunning expensive experiments.

Planned future command to implement:

```bash
python scripts/reproduce_manuscript.py --profile rebuild-manuscript-assets
```

Expected outputs:

- refreshed manuscript source-data mirrors;
- candidate figure/table files;
- a regeneration report with commit SHA, command, runtime, and pass/fail.

### 3. Smoke rerun

A reviewer should be able to run a quick smoke profile that verifies the executable path for manuscript-critical experiments.

Planned future command to implement:

```bash
python scripts/reproduce_manuscript.py --profile smoke
```

This should not run the expensive full experiment suite. It should confirm that entry points, dependencies, and minimal output generation work.

### 4. Critical rerun profile

The authors should run a fresh-checkout rerun of manuscript-critical experiments before submission.

Planned future command to implement:

```bash
python scripts/reproduce_manuscript.py --profile rerun-critical --jobs 1
```

This should write new timestamped outputs and compare claim-level summaries to committed evidence. It should not overwrite preserved historical outputs.

### 5. Full critical profile

A motivated reviewer or future author should be able to run the full critical suite, but this should not be the default CI path.

Planned future command to implement:

```bash
python scripts/reproduce_manuscript.py --profile full-critical --jobs 1
```

## Statistical reproducibility plan

Do not build one giant undifferentiated matrix across all 15 experiments. Build a claim-scoped reproducibility summary.

Planned future outputs:

- reproducibility claim summary CSV;
- seed-level core-claim metrics CSV;
- reproducibility claim summary Markdown table.

For each retained claim, report:

- experiment IDs;
- source artifacts;
- seed/run count;
- metric names;
- mean/median where applicable;
- spread or confidence interval where appropriate;
- effect size only when the comparison family is approved;
- whether a fresh rerun was performed;
- whether the claim should remain main, boundary, supplement, or non-claim.

## Rerun policy

- Do not rerun all 15 experiments blindly.
- Rerun manuscript-critical experiments or smoke profiles only.
- Rerun an experiment fully only if it directly supports a retained claim and either lacks fresh-checkout verification or has weak/ambiguous statistics.
- Keep historical outputs immutable.
- Write reruns to new timestamped directories.
- Compare reruns at the claim-summary level, not by overwriting original artifacts.

## Current gaps

The repository currently has preserved artifacts and several validation reports, but it still needs:

- a master reproducibility driver;
- a fresh-checkout validation report;
- final figure/table regeneration report;
- claim-scoped seed-level reproducibility summary;
- explicit runtime/hardware reporting for fresh reruns;
- final decision on whether optional memory-augmented/key-value neural baselines are needed for the target venue.

## Definition of done for reproducibility before V3 submission

- `docs/manuscript/source_data/manuscript_claim_artifact_map.csv` is complete and source-path verified.
- The planned future validate-artifacts profile passes from a clean checkout.
- The planned future rebuild-manuscript-assets profile regenerates the manuscript figures/tables from committed artifacts.
- The planned future smoke profile confirms manuscript-critical experiment entry points.
- A fresh manuscript reproducibility report records commit SHA, hardware, environment, commands, runtimes, and pass/fail.
- Claim-scoped statistical summaries exist for retained claims.
- V3 manuscript claims match only the reproducibility-backed retained claim set.
