# Persistent Plastic Graph MNIST Prototype

This is a research prototype for a **persistent plastic graph network**: a sparse, stateful, reward-modulated learning substrate trained on MNIST.

It is intentionally not a giant monolithic neural-network script. The core pieces are separated:

- `config.py` — experiment configuration
- `storage.py` — SQLite/SQLAlchemy persistence for runs, metrics, checkpoints
- `data.py` — MNIST loading
- `plastic_graph.py` — sparse adaptive graph substrate
- `modulators.py` — reward/novelty/confidence plasticity gates
- `trainer.py` — experiment loop
- `run_mnist_experiment.py` — composition/root script

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```bash
python run_mnist_experiment.py --epochs 3 --hidden-units 4096 --active-hidden 128 --max-train 10000 --max-test 2000
```

```powershell
python .\run_mnist_experiment.py --epochs 3 --hidden-units 4096 --active-hidden 128 --max-train 10000 --max-test 2000
```

Or use the included helper scripts:

```bash
./start.sh
```

```powershell
.\start.ps1
```

Results are persisted to `runs/plastic_graph_mnist.sqlite3` by default.

## Design note

This prototype keeps the conceptual model object-oriented but avoids heavyweight object-per-neuron runtime storage. Neurons and synapses have identity and lifecycle, but are stored in compact NumPy arrays for speed.

## Analyze experiment results

After a run finishes, inspect the SQLite database and latest checkpoint:

```bash
python analyze_results.py --db runs/plastic_graph_mnist.sqlite3 --list-runs

python analyze_results.py \
  --db runs/plastic_graph_mnist.sqlite3 \
  --output-dir analysis
```

For a specific run:

```bash
python analyze_results.py \
  --db runs/plastic_graph_mnist.sqlite3 \
  --run-id 1 \
  --output-dir analysis/run_1
```

```powershell
python .\analyze_results.py --db .\runs\plastic_graph_mnist.sqlite3 --list-runs

python .\analyze_results.py `
  --db .\runs\plastic_graph_mnist.sqlite3 `
  --output-dir .\analysis

python .\analyze_results.py `
  --db .\runs\plastic_graph_mnist.sqlite3 `
  --run-id 1 `
  --output-dir .\analysis\run_1
```

The analyzer writes:

- `analysis_report.md` — plain-English interpretation of the run
- `metrics.csv` — all recorded metric rows
- `latest_checkpoint_summary.json` — shapes and statistics for saved graph arrays
- `*.png` plots — accuracy and confidence curves when `matplotlib` is installed
