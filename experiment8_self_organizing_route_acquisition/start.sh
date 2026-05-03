#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
PYTHON="$SCRIPT_DIR/../.venv/bin/python"
if [ ! -x "$PYTHON" ]; then
  echo "Could not find Python at $PYTHON. Create the shared virtualenv one directory up first." >&2
  exit 1
fi

"$PYTHON" ./run_exp8_suite.py \
  --db ./runs/exp8_self_organizing_route_acquisition.sqlite3 \
  --output-dir ./analysis/exp8 \
  --max-number 31 \
  --max-steps 8 \
  --transition-train-repeats 1 \
  --path-train-repeats 0 \
  --seeds 30 \
  --hidden-units 2048 \
  --number-assembly-size 72 \
  --mode-assembly-size 24 \
  --pair-assembly-size 48 \
  --mode-overlap 0.0 \
  --context-bleed 0.0 \
  --feedback-noise 0.0 \
  --force
