#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="../.venv/bin/python"
if [ ! -x "$PYTHON" ]; then
  echo "Could not find shared virtual environment at $PYTHON"
  echo "Create it one directory up, then install requirements."
  exit 1
fi
"$PYTHON" -m pip install -r requirements.txt
"$PYTHON" ./run_exp10_suite.py \
  --output-dir ./analysis/exp10 \
  --max-number 31 \
  --max-steps 8 \
  --initial-exposure-repeats 1 \
  --reversal-exposure-schedule "0 1 2 3 5 8 13 21" \
  --switchback-exposure-schedule "0 1 2 3 5 8 13" \
  --seeds 30 \
  --hidden-units 4096 \
  --number-assembly-size 72 \
  --mode-assembly-size 24 \
  --pair-assembly-size 48 \
  --world-assembly-size 24 \
  --feedback-noise 0.0 \
  --reward-delay-steps 0 \
  --phases reversal switchback \
  --force
