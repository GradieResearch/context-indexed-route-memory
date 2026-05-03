# Workspace Rules

This workspace stores experiments as isolated, self-contained directories.

## Directory Rules

- Every experiment must live in its own top-level directory.
- Do not implement a new experiment by extending a previous experiment directory in place.
- When starting a new experiment, create a new directory and copy or reimplement everything that experiment needs inside it.
- An experiment directory should contain its own code, runner scripts, analysis scripts, docs, `runs/`, and `analysis/` outputs as needed.
- Every experiment directory must include its own `README.md`.
- Each experiment `README.md` must include a dedicated section for tracking completed runs and their results.
- Treat previous experiment directories as historical records. Do not mix a newer experiment's code or outputs into an older experiment directory.

## Naming

- Use clear top-level directory names such as `plastic_graph_mnist_expN` or `plastic_graph_mnist_experimentN_description`.
- Keep experiment-specific docs in that directory, for example `EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`.

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

## Run Logging And Immutability

- Experimental runs are immutable records.
- Do not append multiple runs into a shared SQLite database for an experiment.
- Each completed run must write to its own separate SQLite database file.
- Store that per-run SQLite database inside the owning experiment directory, typically under that experiment's `runs/` folder.
- Treat a completed run database as read-only historical output. If a new run is needed, create a new database file rather than reusing or overwriting an old one.
- After completing a run, update that experiment's `README.md` run-results section with the run name, database path, key configuration notes, and summarized results.

## Migration Rule

- If an experiment was started in the wrong directory, migrate it into its own top-level directory and remove the newer experiment's files from the older one.
