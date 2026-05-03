python -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt

python run_experiment_suite.py \
  --epochs 3 \
  --hidden-units 4096 \
  --active-hidden 128 \
  --input-edges-per-hidden 64 \
  --max-train 10000 \
  --max-test 2000

python analyze_experiment_suite.py \
  --db runs/plastic_graph_suite.sqlite3 \
  --output-dir analysis/suite