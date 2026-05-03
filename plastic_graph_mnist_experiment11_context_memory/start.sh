#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
PYTHON="$SCRIPT_DIR/../.venv/bin/python"
if [ ! -x "$PYTHON" ]; then
  PYTHON="python"
fi
"$PYTHON" ./run_exp11_suite.py \
  --output-dir analysis/exp11 \
  --max-number 31 \
  --max-steps 8 \
  --worlds "A B C D" \
  --seeds 30 \
  --initial-exposure-repeats 1 \
  --new-world-exposure-schedule "0 1 2 3 5 8 13 21" \
  --alternation-cycles 21 \
  --alternation-eval-schedule "0 1 2 3 5 8 13 21" \
  --scaling-exposure-repeats 3 \
  --context-bleed-sweep "0 0.05 0.10 0.20 0.35" \
  --context-dropout-sweep "0 0.05 0.10 0.20" \
  --phases sequential alternating scaling context_noise \
  --log-level INFO \
  --force
