# Workspace Rules

This repository stores experiments as isolated, self-contained directories under `experiments/`.

## Directory Rules

- All experiment directories must live under `experiments/`.
- Each experiment must be self-contained inside its own directory.
- Do not implement a new experiment by extending an older experiment directory in place.
- New experiments should follow the repository's current naming style, for example `experiments/expNN_descriptive_name/` or `experiments/experimentNN_descriptive_name/`.
- Successor protocols or corrected experimental designs should get a new experiment directory, for example `experiments/exp13_1_publication_hardening/`.
- Do not rename or normalize existing experiment directories unless explicitly asked.
- Each experiment directory should contain its own code, runner scripts, analysis scripts, docs, `runs/`, and `analysis/` outputs as needed.
- Every experiment directory must include its own `README.md` with run instructions and a dedicated section for completed runs and results.
- Treat previous experiment directories as historical records. Do not mix a newer experiment's code or outputs into an older experiment directory.

## Run Logging And Immutability

- Experimental runs are immutable records.
- Do not append multiple completed runs into a shared SQLite database for an experiment.
- Each completed run must write to its own separate SQLite database file.
- Store per-run SQLite databases inside the owning experiment directory, typically under that experiment's `runs/` folder.
- Reruns of the same protocol should stay under the same experiment directory, preferably under `analysis/runs/<run_id>/` or the experiment's existing run-output convention.
- Treat a completed run database as read-only historical output. If a new run is needed, create a new database file rather than reusing or overwriting an old one.
- After completing a run, update that experiment's `README.md` run-results section with the run name, database path, key configuration notes, and summarized results.

## Documentation Paths

- Every active docs source path must use the current `experiments/...` prefix.
- Do not cite stale paths such as `experiment12_capacity_generalization/analysis/...` in active manuscript or evidence docs.
- Every manuscript/evidence/source path cited in docs should either resolve to an existing local file or be explicitly marked as future, planned, missing, or local verification pending.
- Use `python scripts/verify_doc_source_paths.py` to check active documentation source paths before repo-readiness handoff.
- Historical thread exports may preserve old conversation text, but active evidence maps and indexes should use current paths.

## Shared Root Files

- Cross-experiment planning docs may live at the workspace root.
- The experiment tracker may live at the workspace root.
- Shared utilities at the root should stay minimal and should not become the implementation home for a specific experiment.

## GPU Usage

- Build new experiments to use the available GPUs on the system by default rather than assuming CPU-only execution.
- When multiple GPUs are available, design the experiment so it can make practical use of them when the workload supports it.
- Treat GPU support as part of the experiment design, not as a later optimization pass.
- Use `check_gpu_status.py` as a workspace reference when validating device visibility and runtime expectations.
- If an experiment cannot reasonably use the available GPUs, document the reason in that experiment's `README.md`.
- If GPU support is partial, document what is accelerated, what still runs on CPU, and any known limitations in the experiment `README.md`.

## Migration Rule

- If an experiment was started in the wrong directory, migrate it into its own directory under `experiments/` and remove the newer experiment's files from the older one.
