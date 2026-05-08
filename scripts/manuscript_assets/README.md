# Manuscript Asset Pipeline

This directory contains the reproducible manuscript figure/table build for the first-manuscript claim freeze.

Run from the repository root:

```bash
python scripts/manuscript_assets/build_manuscript_assets.py
```

The build reads `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` plus local experiment artifacts under `experiments/...`, then writes:

- figure source data to `docs/manuscript/source_data/`
- manuscript figures to `docs/manuscript/figures/`
- manuscript tables to `docs/manuscript/tables/`
- the asset manifest at `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- the generation report at `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`

The script does not rerun experiments and does not modify experiment artifacts. It fails if a required main-manuscript input artifact is missing and records warnings for deferred/supplementary inputs.

After editing manuscript/source-path-heavy docs, run:

```bash
python scripts/verify_doc_source_paths.py
```
