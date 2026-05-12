#!/usr/bin/env python
"""Verify local source paths cited by active documentation.

The verifier is intentionally conservative: it checks paths that look like
repository-local source artifacts, reports missing active paths, and skips
paths whose surrounding text explicitly marks them as planned, future, missing,
or local-verification-pending.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

ROOT_DOCS = [
    "README.md",
    "AGENTS.md",
    "EXPERIMENT_TRACKER.md",
    "Experiment.md",
]

KNOWN_ROOTS = {
    "docs",
    "experiments",
    "scripts",
}

LEGACY_EXPERIMENT_ROOTS = {
    "experiment1",
    "experiment2",
    "experiment3",
    "experiment4_successor",
    "experiment5_contextual_successor",
    "experiment6_route_audit_successor",
    "experiment7_route_field_diagnostics",
    "experiment8_self_organizing_route_acquisition",
    "experiment9_robust_adaptive_route_plasticity",
    "experiment10_adaptive_reversal",
    "experiment11_context_memory",
    "experiment12_capacity_generalization",
    "experiment13_breaking_point",
    "plastic_graph_mnist_exp1",
    "plastic_graph_mnist_exp2",
    "plastic_graph_mnist_exp3",
    "plastic_graph_mnist_experiment4_successor",
    "plastic_graph_mnist_experiment5_contextual_successor",
    "plastic_graph_mnist_experiment6_route_audit_successor",
    "plastic_graph_mnist_experiment7_route_field_diagnostics",
    "plastic_graph_mnist_experiment8_self_organizing_route_acquisition",
    "plastic_graph_mnist_experiment9_robust_adaptive_route_plasticity",
}

DOC_EXTENSIONS = {
    ".md",
    ".csv",
    ".txt",
    ".json",
    ".jsonl",
    ".yml",
    ".yaml",
}

KNOWN_PATH_EXTENSIONS = {
    ".csv",
    ".db",
    ".json",
    ".jsonl",
    ".md",
    ".png",
    ".ps1",
    ".py",
    ".sh",
    ".sqlite",
    ".sqlite3",
    ".txt",
    ".yaml",
    ".yml",
    ".zip",
}

PLANNED_MARKERS = (
    "future",
    "planned",
    "for example",
    "not yet created",
    "to be created",
    "pending",
    "todo",
    "before submission",
    "if implemented",
)

LOCAL_PENDING_MARKERS = (
    "local verification pending",
    "missing",
    "stale paths such as",
    "do not cite stale paths",
    "not present",
    "not indexed",
    "no matching local artifact",
    "no baseline run artifact",
    "source artifact is not present",
    "does not exist locally",
)

HISTORICAL_MARKERS = (
    "historical thread",
    "thread export preserves",
    "historical conversation",
)

URL_PREFIXES = ("http://", "https://", "mailto:")


@dataclass(frozen=True)
class Finding:
    doc: str
    line: int
    path: str
    note: str = ""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_doc_files() -> list[Path]:
    files: list[Path] = []
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        for path in docs_dir.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in DOC_EXTENSIONS:
                continue
            # Generated thread transcripts are historical source text. Active
            # thread indexes and templates are still scanned.
            if (
                path.parent == docs_dir / "threads"
                and path.name.startswith("experiment")
                and path.name.endswith("_export.md")
            ):
                continue
            files.append(path)

    for name in ROOT_DOCS:
        path = ROOT / name
        if path.exists():
            files.append(path)

    return sorted(set(files))


def split_candidate_text(text: str) -> Iterable[str]:
    # Backtick spans and CSV cells often contain semicolon-separated paths.
    for part in re.split(r"[;\n]", text):
        part = part.strip()
        if part:
            if " " in part and ("/" in part or "\\" in part):
                for token in part.split():
                    yield token
            yield part


def normalize_candidate(raw: str, line: str = "") -> str | None:
    value = raw.strip()
    if not value:
        return None

    value = value.strip(" \t\r\n`'\"<>[](){}")
    value = value.rstrip(".,;:")
    value = value.replace("\\", "/")

    if " " in value and "/" in value:
        return None

    if not value or value.startswith(URL_PREFIXES):
        return None

    if value.startswith("#"):
        return None

    if any(ch in value for ch in "*?"):
        return None

    if re.search(r"<[^>]+>", value):
        return None

    if value in {"TODO", "none", "None", "local verification pending"}:
        return None

    if re.fullmatch(r"C\d+", value) or re.fullmatch(r"Exp\d+(?:\.\d+)?", value):
        return None

    if "#" in value:
        value = value.split("#", 1)[0]

    # Drop markdown line suffixes like path.md:25 only after preserving Windows
    # drive letters. Repo paths in these docs are relative, so this is safe.
    value = re.sub(r":\d+$", "", value)

    if value.startswith("./"):
        value = value[2:]

    while value.startswith("/"):
        value = value[1:]

    if not value or value.startswith(URL_PREFIXES):
        return None

    suffix = Path(value).suffix
    has_path_separator = "/" in value
    has_known_extension = suffix in KNOWN_PATH_EXTENSIONS
    is_root_doc = value in ROOT_DOCS or value == ".gitattributes"

    if not (has_path_separator or has_known_extension or is_root_doc):
        return None

    if has_path_separator:
        first = value.split("/", 1)[0]
        if first not in KNOWN_ROOTS and first not in LEGACY_EXPERIMENT_ROOTS:
            return None
    elif not is_root_doc:
        lower_line = line.lower()
        explicitly_missing = any(marker in lower_line for marker in LOCAL_PENDING_MARKERS)
        if value != "Pasted text.txt" and not explicitly_missing:
            return None

    return value


def candidates_from_markdown_line(line: str) -> Iterable[str]:
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", line):
        yield match.group(1)

    for match in re.finditer(r"`([^`]+)`", line):
        for part in split_candidate_text(match.group(1)):
            yield part

    if re.search(r"\b(Source path|Source artifact|Source materials|Source thread|Expected outputs|Command/script|Validation command)\b", line, re.I):
        for match in re.finditer(r"(?<![\w.-])(?:\.?/)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_. -]+)+", line.replace("\\", "/")):
            yield match.group(0)


def candidates_from_csv_line(line: str) -> Iterable[str]:
    try:
        row = next(csv.reader([line]))
    except csv.Error:
        row = [line]

    for cell in row:
        for part in split_candidate_text(cell):
            yield part


def is_staged_import_bundle(path: str) -> bool:
    """Return true for zip bundles used only during analysis import.

    Thread digests and import reports intentionally record the source zip that was
    staged under docs/imports/. Those bundles are handoff inputs, not durable
    repository artifacts, so their historical references should not fail the
    active source-path verifier.
    """

    normalized = path.replace("\\", "/")
    return normalized.startswith("docs/imports/") and normalized.endswith(".zip")


def classify_missing(path: str, line: str) -> tuple[str, str]:
    if is_staged_import_bundle(path):
        return "local_pending", "staged import bundle reference; not retained as active repo artifact"

    lower = line.lower()
    if any(marker in lower for marker in LOCAL_PENDING_MARKERS):
        return "local_pending", "explicitly marked missing/local verification pending"
    if any(marker in lower for marker in PLANNED_MARKERS):
        return "planned", "explicitly marked planned/future/pending"
    if any(marker in lower for marker in HISTORICAL_MARKERS):
        return "historical", "historical source text"
    return "missing", ""


def path_exists(candidate: str) -> bool:
    path = ROOT / candidate
    if path.exists():
        return True

    # Accept directory references with a trailing slash after normalization.
    if candidate.endswith("/") and (ROOT / candidate.rstrip("/")).exists():
        return True

    return False


def scan_file(path: Path) -> tuple[list[Finding], list[Finding], list[Finding], list[Finding]]:
    ok: list[Finding] = []
    missing: list[Finding] = []
    planned: list[Finding] = []
    local_pending: list[Finding] = []

    text = path.read_text(encoding="utf-8", errors="replace")
    for line_no, line in enumerate(text.splitlines(), start=1):
        raw_candidates = list(candidates_from_markdown_line(line))
        if path.suffix.lower() == ".csv":
            raw_candidates.extend(candidates_from_csv_line(line))

        seen_on_line: set[str] = set()
        for raw in raw_candidates:
            candidate = normalize_candidate(raw, line)
            if candidate is None or candidate in seen_on_line:
                continue
            seen_on_line.add(candidate)

            finding = Finding(rel(path), line_no, candidate)
            if path_exists(candidate):
                ok.append(finding)
                continue

            category, note = classify_missing(candidate, line)
            finding = Finding(rel(path), line_no, candidate, note)
            if category == "planned":
                planned.append(finding)
            elif category in {"local_pending", "historical"}:
                local_pending.append(finding)
            else:
                missing.append(finding)

    return ok, missing, planned, local_pending


def print_group(title: str, findings: list[Finding], limit: int | None = None) -> None:
    print(f"\n## {title}")
    if not findings:
        print("None")
        return

    shown = findings if limit is None else findings[:limit]
    for item in shown:
        note = f" ({item.note})" if item.note else ""
        print(f"{item.doc}:{item.line}: {item.path}{note}")
    if limit is not None and len(findings) > limit:
        print(f"... {len(findings) - limit} more")


def main() -> int:
    scanned = iter_doc_files()
    ok: list[Finding] = []
    missing: list[Finding] = []
    planned: list[Finding] = []
    local_pending: list[Finding] = []

    for path in scanned:
        file_ok, file_missing, file_planned, file_local_pending = scan_file(path)
        ok.extend(file_ok)
        missing.extend(file_missing)
        planned.extend(file_planned)
        local_pending.extend(file_local_pending)

    print("# Documentation Source Path Verification")
    print(f"Files scanned: {len(scanned)}")
    print(f"OK paths: {len(ok)}")
    print(f"Missing active paths: {len(missing)}")
    print(f"Skipped planned/future paths: {len(planned)}")
    print(f"Skipped local-verification-pending paths: {len(local_pending)}")

    print_group("Missing Active Paths", missing)
    print_group("Skipped Planned/Future Paths", planned, limit=200)
    print_group("Skipped Local-Verification-Pending Paths", local_pending, limit=200)

    print("\n## Files Scanned")
    for path in scanned:
        print(rel(path))

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
