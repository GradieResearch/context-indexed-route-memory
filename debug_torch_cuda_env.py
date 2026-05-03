from __future__ import annotations

import os
import sys
import time
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    print(f"workspace={root}")
    print(f"python={sys.executable}")
    print(f"EXP10_BACKEND={os.environ.get('EXP10_BACKEND', '')}")
    print(f"EXP10_DEVICE={os.environ.get('EXP10_DEVICE', '')}")

    try:
        import torch
    except Exception as exc:
        print(f"torch_import_failed={exc}")
        return 1

    print(f"torch_version={torch.__version__}")
    print(f"torch_cuda_build={getattr(torch.version, 'cuda', None)}")
    print(f"cuda_available={torch.cuda.is_available()}")
    print(f"cuda_device_count={torch.cuda.device_count()}")

    for index in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(index)
        total_gb = props.total_memory / (1024 ** 3)
        print(f"gpu_{index}_name={props.name}")
        print(f"gpu_{index}_total_gb={total_gb:.2f}")

    if not torch.cuda.is_available():
        print("cuda_runtime_test=skipped")
        return 2

    device = torch.device("cuda:0")
    start = time.time()
    a = torch.randn((4096, 4096), device=device)
    b = torch.randn((4096, 4096), device=device)
    c = a @ b
    torch.cuda.synchronize(device)
    elapsed = time.time() - start
    print(f"cuda_runtime_test=ok shape={tuple(c.shape)} elapsed_seconds={elapsed:.3f}")
    print(f"cuda_memory_allocated_mb={torch.cuda.memory_allocated(device) / (1024 ** 2):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
