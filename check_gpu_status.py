from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPERIMENT_DIRS = [
    ROOT / "plastic_graph_mnist_exp1",
    ROOT / "plastic_graph_mnist_exp2",
    ROOT / "plastic_graph_mnist_exp3",
    ROOT / "plastic_graph_mnist_experiment4_successor",
    ROOT / "plastic_graph_mnist_experiment5_contextual_successor",
]


def print_header(title: str) -> None:
    print(f"\n=== {title} ===")


def try_import_torch():
    try:
        import torch  # type: ignore

        return torch, None
    except Exception as exc:  # pragma: no cover - diagnostic path
        return None, exc


def run_nvidia_smi() -> None:
    print_header("nvidia-smi")
    exe = shutil.which("nvidia-smi")
    if not exe:
        print("nvidia-smi not found on PATH.")
        return
    try:
        result = subprocess.run(
            [
                exe,
                "--query-gpu=index,name,driver_version,memory.total,utilization.gpu",
                "--format=csv,noheader",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        output = result.stdout.strip()
        print(output if output else "No GPU rows returned.")
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Failed to run nvidia-smi: {exc}")


def check_torch_gpu() -> bool:
    print_header("PyTorch")
    torch, exc = try_import_torch()
    if torch is None:
        print(f"PyTorch import failed: {exc}")
        print("Run this script from the shared workspace venv if you want a full runtime check.")
        return False

    print(f"Python: {sys.executable}")
    print(f"Torch version: {torch.__version__}")
    print(f"CUDA build: {getattr(torch.version, 'cuda', None)}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"CUDA device count: {torch.cuda.device_count()}")

    if not torch.cuda.is_available():
        return False

    for index in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(index)
        total_gb = props.total_memory / (1024 ** 3)
        print(f"GPU {index}: {props.name} ({total_gb:.1f} GiB)")

    try:
        device = torch.device("cuda:0")
        a = torch.randn((2048, 2048), device=device)
        b = torch.randn((2048, 2048), device=device)
        c = a @ b
        torch.cuda.synchronize()
        print(f"GPU tensor smoke test passed on {device}: result shape={tuple(c.shape)}")
        allocated_mb = torch.cuda.memory_allocated(device) / (1024 ** 2)
        print(f"CUDA memory allocated after smoke test: {allocated_mb:.1f} MiB")
        return True
    except Exception as runtime_exc:  # pragma: no cover - diagnostic path
        print(f"GPU runtime test failed: {runtime_exc}")
        return False


def scan_experiment_code() -> None:
    print_header("Experiment Code Scan")
    torch_pattern = re.compile(r"\bimport torch\b|\bfrom torch\b|torch\.")
    cuda_pattern = re.compile(r"\bcuda\b|\bmps\b|torch\.device|\.to\(|torch\.cuda", re.IGNORECASE)

    torch_hits: list[str] = []
    gpu_hits: list[str] = []

    for exp_dir in EXPERIMENT_DIRS:
        if not exp_dir.exists():
            continue
        for path in exp_dir.rglob("*.py"):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = path.read_text(encoding="utf-8", errors="ignore")
            rel = path.relative_to(ROOT)
            if torch_pattern.search(text):
                torch_hits.append(str(rel))
            if cuda_pattern.search(text):
                gpu_hits.append(str(rel))

    if torch_hits:
        print("Files mentioning torch:")
        for item in torch_hits:
            print(f"  {item}")
    else:
        print("No Python files mention torch.")

    if gpu_hits:
        print("Files mentioning CUDA/device transfer concepts:")
        for item in gpu_hits:
            print(f"  {item}")
    else:
        print("No Python files mention CUDA, MPS, torch.device, or tensor .to(...) calls.")

    print("\nTrainer summary:")
    print("The experiment trainers in this workspace operate on NumPy-based graph code.")
    print("That means GPU availability alone does not make the experiment runs use CUDA.")


def print_conclusion(gpu_runtime_ok: bool) -> None:
    print_header("Conclusion")
    if gpu_runtime_ok:
        print("A CUDA GPU is available and PyTorch can execute work on it.")
        print("However, these experiments appear CPU-oriented as currently written.")
        print("You would need explicit torch/CUDA tensor usage in the graph and trainer code for runs to use the GPU.")
    else:
        print("This script could not confirm active CUDA execution for the current Python environment.")
        print("Even if you fix that environment, these experiments still look CPU-oriented as currently written.")


def main() -> None:
    print(f"Workspace: {ROOT}")
    run_nvidia_smi()
    gpu_runtime_ok = check_torch_gpu()
    scan_experiment_code()
    print_conclusion(gpu_runtime_ok)


if __name__ == "__main__":
    main()
