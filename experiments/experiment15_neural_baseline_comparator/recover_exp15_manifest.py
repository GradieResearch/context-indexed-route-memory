import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

run_dir = Path(r".\analysis\exp15_full_20260508_092811")

metrics = pd.read_csv(run_dir / "exp15_seed_metrics.csv")
runtime = pd.read_csv(run_dir / "exp15_model_runtime.csv")
config = json.loads((run_dir / "exp15_config.json").read_text(encoding="utf-8"))

progress = []
for line in (run_dir / "progress.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        try:
            progress.append(json.loads(line))
        except Exception:
            pass

def git_value(args):
    try:
        return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None

try:
    import torch
    gpu_available = bool(torch.cuda.is_available())
    gpu_name = torch.cuda.get_device_name(0) if gpu_available else None
    cuda_version = torch.version.cuda
    torch_version = torch.__version__
except Exception:
    gpu_available = None
    gpu_name = None
    cuda_version = None
    torch_version = None

try:
    import psutil
    ram_gb = round(psutil.virtual_memory().total / (1024 ** 3), 3)
except Exception:
    ram_gb = None

start_time = progress[0].get("timestamp_utc") if progress else datetime.now(timezone.utc).isoformat()
end_time = progress[-1].get("timestamp_utc") if progress else datetime.now(timezone.utc).isoformat()
duration_seconds = progress[-1].get("elapsed_seconds") if progress else None

manifest = {
    "experiment": "exp15_neural_baseline_comparator",
    "run_id": run_dir.name,
    "profile": "full",
    "schema_version": "exp15_neural_metrics_v1",
    "analysis_dir": str(run_dir),
    "metric_rows": int(len(metrics)),
    "runtime_rows": int(len(runtime)),
    "requested_seeds": config.get("seeds", sorted(metrics["seed"].dropna().astype(int).unique().tolist())),
    "completed_seeds": sorted(metrics["seed"].dropna().astype(int).unique().tolist()),
    "requested_world_counts": config.get("world_counts", sorted(metrics["world_count"].dropna().astype(int).unique().tolist())),
    "completed_world_counts": sorted(metrics["world_count"].dropna().astype(int).unique().tolist()),
    "requested_route_lengths": config.get("route_lengths", sorted(metrics["route_length"].dropna().astype(int).unique().tolist())),
    "completed_route_lengths": sorted(metrics["route_length"].dropna().astype(int).unique().tolist()),
    "requested_variants": config.get("required_variants", sorted(metrics["variant"].dropna().unique().tolist())),
    "completed_variants": sorted(metrics["variant"].dropna().unique().tolist()),
    "start_time_utc": start_time,
    "end_time_utc": end_time,
    "duration_seconds": duration_seconds,
    "python_version": sys.version.replace("\n", " "),
    "platform": platform.platform(),
    "processor": platform.processor(),
    "cpu_count": os.cpu_count(),
    "ram_gb": ram_gb,
    "gpu_available": gpu_available,
    "gpu_name": gpu_name,
    "cuda_version": cuda_version,
    "torch_version": torch_version,
    "numpy_version": np.__version__,
    "pandas_version": pd.__version__,
    "git_commit": git_value(["rev-parse", "HEAD"]),
    "git_branch": git_value(["rev-parse", "--abbrev-ref", "HEAD"]),
    "command": "recovered after Exp15 completed all units but failed during final SQLite manifest write",
    "recovered_after_failed_sqlite_tail": True,
    "recovery_note": "Training/evaluation completed. CSV artifacts were preserved. Manifest was reconstructed without rerunning.",
}

(run_dir / "run_manifest.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True),
    encoding="utf-8"
)

print(f"Wrote {run_dir / 'run_manifest.json'}")
print(f"metric_rows={manifest['metric_rows']}")
print(f"runtime_rows={manifest['runtime_rows']}")
print(f"completed_seeds={manifest['completed_seeds']}")
print(f"completed_variants={len(manifest['completed_variants'])}")