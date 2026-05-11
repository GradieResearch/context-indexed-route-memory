# Next Step Prompt: Implement Manuscript Reproducibility Driver

Use this prompt after the manuscript reproducibility foundation docs have been added.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: implement the manuscript reproducibility driver and first validation report. Do not rerun expensive full experiments by default.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, post-Table-3 manuscript-placeholder/source-path verification, post-caption/TODO cleanup, post-pre-venue decision-status tie-off, and post-pre-V3 cleanup.

Reproducibility foundation now exists:

- `docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md`
- `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`
- `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md`
- Existing audit: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

Immediate work:

1. Implement the planned future manuscript reproducibility driver at `scripts/reproduce_manuscript.py`.
2. Support at least these profiles:
   - `validate-artifacts`
   - `rebuild-manuscript-assets`
   - `smoke`
   - `rerun-critical`
   - `full-critical`
3. In the first implementation, fully implement `validate-artifacts` and `rebuild-manuscript-assets`.
4. For `smoke`, `rerun-critical`, and `full-critical`, implement command planning and safe skip/reporting if the exact launchers cannot be run in the current environment.
5. Produce planned future report outputs:
   - a manuscript reproducibility Markdown report under `docs/repo_audit/`
   - a manuscript reproducibility JSON report under `docs/repo_audit/`
6. Validate source paths with `python scripts/verify_doc_source_paths.py`.
7. Do not overwrite historical experiment outputs.
8. Do not run expensive full experiments unless explicitly requested by a human.

Implementation guidance:

- Read `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`.
- Parse semicolon-separated source paths and validation artifact paths.
- Check all retained-claim source and validation paths exist.
- Parse required CSVs and check that they are non-empty.
- Add profile-specific checks for key source-data artifacts:
  - `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
  - `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`
  - `docs/manuscript/source_data/figure_03_capacity_scaling.csv`
  - `docs/manuscript/source_data/table_03_compact_final_safe.csv`
- Run `python scripts/manuscript_assets/build_manuscript_assets.py` for `rebuild-manuscript-assets` if available in the current environment.
- Record pass/warn/fail per claim and per profile.
- Include commit SHA, branch/ref, OS, Python version, command, runtime, and caveats in the report.

Preserve the current claim posture:

- Do not add final effect-size language unless explicit comparison families are approved.
- Keep compact Table 3 descriptive only.
- Keep C1 benchmark/model-family-specific.
- Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
- Keep C5 ceiling-limited and supplied-context only.
- Keep C6 as observed finite-budget degradation only; no fitted capacity law.
- Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
- Keep C13 symbolic transition-cue context selection only.
- Keep Exp15 replay collapse as non-claim pending audit.
- Do not claim broad neural superiority, solved continual learning, raw sensory latent-world discovery, or biological validation.

Definition of done:

- The planned future validate-artifacts profile runs successfully from a clean checkout or reports actionable failures.
- The planned future rebuild-manuscript-assets profile runs successfully or records exact environment/actionable failures.
- Manuscript reproducibility Markdown and JSON reports are generated under `docs/repo_audit/`.
- `python scripts/verify_doc_source_paths.py` passes.
- Final response summarizes changed files, profile results, verifier status, and remaining reproducibility blockers.
```
