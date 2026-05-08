from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]


def repo_path(path: str | Path) -> Path:
    return REPO_ROOT / Path(path)


def rel_path(path: str | Path) -> str:
    return Path(path).resolve().relative_to(REPO_ROOT).as_posix()


def read_csv(rel: str) -> pd.DataFrame:
    return pd.read_csv(repo_path(rel))


def read_json(rel: str) -> Any:
    return json.loads(repo_path(rel).read_text(encoding="utf-8"))


def count_csv_rows(rel: str) -> int:
    path = repo_path(rel)
    if not path.exists():
        return 0
    return int(pd.read_csv(path).shape[0])


def count_files(rel_dir: str, pattern: str) -> int:
    path = repo_path(rel_dir)
    if not path.exists():
        return 0
    return len(list(path.glob(pattern)))


def normal_ci(mean: float, std: float, n: float) -> tuple[float | None, float | None, float | None]:
    if pd.isna(mean) or pd.isna(std) or pd.isna(n) or n <= 0:
        return (None, None, None)
    sem = float(std) / math.sqrt(float(n))
    return (sem, float(mean) - 1.96 * sem, float(mean) + 1.96 * sem)


def table_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows generated._\n"
    return df.to_markdown(index=False)


def write_csv_and_md(df: pd.DataFrame, csv_path: Path, md_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)
    md_path.write_text(table_to_markdown(df) + "\n", encoding="utf-8")


def summarize_validation(rel_json: str | None) -> tuple[str, int | None, int | None, int | None]:
    if not rel_json:
        return ("not available", None, None, None)
    path = repo_path(rel_json)
    if not path.exists():
        return ("missing", None, None, None)
    obj = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(obj, dict):
        return (
            str(obj.get("status", "unknown")),
            obj.get("pass_count"),
            obj.get("warn_count"),
            obj.get("fail_count"),
        )
    if isinstance(obj, list):
        pass_count = sum(1 for item in obj if item.get("status") == "PASS")
        warn_count = sum(1 for item in obj if item.get("status") == "WARN")
        fail_count = sum(1 for item in obj if item.get("status") == "FAIL")
        status = "PASS" if fail_count == 0 else "FAIL"
        return (status, pass_count, warn_count, fail_count)
    return ("unknown", None, None, None)


@dataclass(frozen=True)
class RequiredInput:
    path: str
    status: str
    purpose: str
    claims: str


def validate_inputs(inputs: Iterable[RequiredInput]) -> tuple[list[str], list[str]]:
    missing_required: list[str] = []
    warnings: list[str] = []
    for item in inputs:
        exists = repo_path(item.path).exists()
        if exists:
            continue
        message = f"{item.path} ({item.purpose}; claims {item.claims})"
        if item.status == "required":
            missing_required.append(message)
        else:
            warnings.append(f"Missing deferred/optional input: {message}")
    return missing_required, warnings


def format_num(value: Any, digits: int = 4) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, (int,)) and not isinstance(value, bool):
        return str(value)
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def choose_existing(paths: Iterable[str]) -> list[str]:
    return [p for p in paths if repo_path(p).exists()]
