#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
PYTHON="$SCRIPT_DIR/../.venv/bin/python"
if [[ ! -x "$PYTHON" ]]; then
  echo "Could not find shared virtualenv Python at: $PYTHON"
  echo "Create it from the workspace root with: python -m venv .venv"
  exit 1
fi

"$PYTHON" -m pip install -r ./requirements.txt
"$PYTHON" ./run_exp9_suite.py \
  --db ./runs/exp9_robust_adaptive_route_plasticity.sqlite3 \
  --output-dir ./analysis/exp9 \
  --max-number 31 \
  --max-steps 8 \
  --transition-train-repeats 1 \
  --seeds 30 \
  --hidden-units 4096 \
  --number-assembly-size 72 \
  --mode-assembly-size 24 \
  --pair-assembly-size 48 \
  --phases interference feedback \
  --context-bleed-sweep "0 0.05 0.10 0.20 0.35 0.50" \
  --feedback-noise-sweep "0 0.05 0.10 0.20 0.30" \
  --reward-delay-sweep "0 2 4" \
  --force

echo "Experiment 9 complete. Upload ./analysis/exp9 for review."
