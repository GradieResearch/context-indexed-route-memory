if [ -f "../.venv/Scripts/python.exe" ] && [ ! -f "../.venv/pyvenv.cfg" ]; then
  rm -rf ../.venv
fi

python -m venv ../.venv
source ../.venv/bin/activate  # Windows: ..\.venv\Scripts\activate
pip install -r requirements.txt

python run_exp4_suite.py \
  --max-number 24 \
  --max-addend 5 \
  --train-transition-repeats 120 \
  --hidden-units 4096 \
  --assembly-size 96 \
  --active-units 96 \
  --recurrent-edges-per-unit 48

python analyze_exp4_suite.py \
  --db runs/exp4_successor_suite.sqlite3 \
  --output-dir analysis/exp4
