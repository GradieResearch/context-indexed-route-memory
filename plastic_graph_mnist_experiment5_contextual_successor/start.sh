if [ -f "../.venv/Scripts/python.exe" ] && [ ! -f "../.venv/pyvenv.cfg" ]; then
  rm -rf ../.venv
fi

python -m venv ../.venv
source ../.venv/bin/activate  # Windows: ..\.venv\Scripts\activate
pip install -r requirements.txt

python run_exp5_suite.py \
  --max-number 24 \
  --max-steps 5 \
  --train-sequence-repeats 120 \
  --hidden-units 4096 \
  --assembly-size 72 \
  --mode-assembly-size 24 \
  --active-units 96 \
  --recurrent-edges-per-unit 48

python analyze_exp5_suite.py \
  --db runs/exp5_contextual_successor_suite.sqlite3 \
  --output-dir analysis/exp5
