from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TMP_EXP = ROOT / "plastic_graph_mnist_experiment10_adaptive_reversal.tmp"
if str(TMP_EXP) not in sys.path:
    sys.path.insert(0, str(TMP_EXP))

from exp10.core import AdaptiveRouteGraph, GraphConfig, generate_transition_tasks, make_reversal_variants  # noqa: E402


def run_once(backend: str, device: str, repeats: int) -> tuple[str, float]:
    os.environ["EXP10_BACKEND"] = backend
    os.environ["EXP10_DEVICE"] = device
    variant = make_reversal_variants()[0]
    graph = AdaptiveRouteGraph(GraphConfig(max_number=31, hidden_units=4096), variant, seed=0)
    tasks = generate_transition_tasks(31, "A")
    start = time.time()
    for _ in range(repeats):
        graph.train_curriculum(tasks, repeats=1, phase="initial")
        graph.finalize()
    elapsed = time.time() - start
    return graph.backend_name, elapsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=2)
    args = parser.parse_args()

    cases = [("numpy", "cpu"), ("torch", "cpu")]
    try:
        import torch
        if torch.cuda.is_available():
            cases.append(("torch", "cuda"))
    except Exception:
        pass

    for backend, device in cases:
        name, elapsed = run_once(backend, device, args.repeats)
        print(f"backend={name} repeats={args.repeats} elapsed_seconds={elapsed:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
