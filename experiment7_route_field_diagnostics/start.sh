#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="$SCRIPT_DIR/../.venv/bin/python"
if [[ ! -x "$PYTHON" ]]; then
  echo "Expected Python virtual environment at '$PYTHON'. Create the shared venv one directory above this experiment folder, then install requirements.txt." >&2
  exit 1
fi

"$PYTHON" -m pip install -r ./requirements.txt

"$PYTHON" ./run_exp7_suite.py \
  --max-number 11 \
  --max-steps 3 \
  --train-repeats 40 \
  --path-train-repeats 2 \
  --seeds 5 \
  --force

"$PYTHON" ./analyze_exp7_suite.py \
  --db ./runs/exp7_route_field_diagnostics.sqlite3 \
  --output-dir ./analysis/exp7

echo "Experiment 7 complete. Open ./analysis/exp7/exp7_report.md"
