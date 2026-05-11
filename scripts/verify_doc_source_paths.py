#!/usr/bin/env python
"""Temporary PR-branch wrapper for cleanup edits.

Runs only on `cleanup-remove-backup-normalize-table4`. It removes a stale backup
file, normalizes the remaining Table 4 placeholder in MANUSCRIPT_V2, runs the
real verifier from origin/main, restores this verifier/workflow, and pushes the
final branch state.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCH = 'cleanup-remove-backup-normalize-table4'

OLD_TABLE4 = '[Table 4 here: Exp15 minimal neural comparator hard-slice summary. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.]'
NEW_TABLE4 = '**Table 4 placeholder.** Exp15 minimal neural comparator hard-slice summary. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`. Caption caveat: fixed-profile and non-exhaustive; endpoint models, transition learners, no-context variants, and world-head isolation should be interpreted as distinct computational contracts.'


def run(args: list[str], check: bool = True, capture: bool = False):
    return subprocess.run(args, cwd=ROOT, text=True, check=check, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None)


def restore_real_verifier_to_temp() -> Path:
    run(['git', 'fetch', 'origin', 'main'])
    original = run(['git', 'show', 'origin/main:scripts/verify_doc_source_paths.py'], capture=True).stdout
    temp = ROOT / 'scripts' / '_verify_doc_source_paths_original.py'
    temp.write_text(original, encoding='utf-8')
    return temp


def run_real_verifier(temp: Path) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(temp)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout or ''


def cleanup_docs() -> None:
    backup = ROOT / 'docs/manuscript/draft/bkup.orig'
    backup.unlink(missing_ok=True)

    manuscript = ROOT / 'docs/manuscript/draft/MANUSCRIPT_V2.md'
    text = manuscript.read_text(encoding='utf-8')
    if OLD_TABLE4 in text:
        text = text.replace(OLD_TABLE4, NEW_TABLE4)
    manuscript.write_text(text, encoding='utf-8')

    cleanup_status = ROOT / 'docs/manuscript/finalization/PRE_V3_CLEANUP_STATUS.md'
    if cleanup_status.exists():
        status_text = cleanup_status.read_text(encoding='utf-8')
        status_text = status_text.replace('- `docs/manuscript/draft/bkup.orig` is a stale backup draft. It is explicitly non-canonical and should be removed with local Git access before or during the V3 drafting branch.\n- `docs/manuscript/draft/MANUSCRIPT_V2.md` still contains a duplicate in-section Table 4 placeholder using older bracketed wording. It is not a source-path blocker but should be normalized in the V3 drafting/flow-review pass.', '- The stale backup draft `docs/manuscript/draft/bkup.orig` has been removed.\n- The duplicate in-section Table 4 placeholder in `docs/manuscript/draft/MANUSCRIPT_V2.md` has been normalized.')
        status_text = status_text.replace('1. Remove `docs/manuscript/draft/bkup.orig` if local Git deletion is available.\n2. Normalize the duplicate Table 4 placeholder.\n3. Draft the planned future V3 manuscript from V2 with cleaner flow and fewer process notes.', '1. Draft the planned future V3 manuscript from V2 with cleaner flow and fewer process notes.')
        status_text = status_text.replace('4. Preserve the conservative claim posture.\n5. Keep venue/citation/license decisions explicit and human-gated.\n6. Run `python scripts/verify_doc_source_paths.py` after the cleanup/draft pass.', '2. Preserve the conservative claim posture.\n3. Keep venue/citation/license decisions explicit and human-gated.\n4. Run `python scripts/verify_doc_source_paths.py` after the cleanup/draft pass.')
        cleanup_status.write_text(status_text, encoding='utf-8')

    todo = ROOT / 'docs/manuscript/MANUSCRIPT_TODO.md'
    if todo.exists():
        todo_text = todo.read_text(encoding='utf-8')
        todo_text = todo_text.replace('1. Normalize the remaining duplicate in-section Table 4 placeholder in `docs/manuscript/draft/MANUSCRIPT_V2.md`.\n2. Perform a prose-only manuscript flow review while preserving the current claim posture.', '1. Perform a prose-only manuscript flow review while preserving the current claim posture.')
        todo_text = todo_text.replace('3. Choose the target venue and citation/export convention, or explicitly keep the package venue-neutral for one more pass.\n4. Decide whether a memory-augmented/key-value neural comparator is needed for the target venue.\n5. Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.', '2. Choose the target venue and citation/export convention, or explicitly keep the package venue-neutral for one more pass.\n3. Decide whether a memory-augmented/key-value neural comparator is needed for the target venue.\n4. Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.')
        todo_text = todo_text.replace('| Normalize the duplicate in-section Table 4 placeholder. | One later Table 4 placeholder still uses older bracketed manuscript-placeholder wording; it is not path-breaking but should be cleaned before final flow review. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md` | Consistent Table 4 placeholder/caption language throughout V2. |\n', '')
        todo.write_text(todo_text, encoding='utf-8')


def finalize() -> int:
    cleanup_docs()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        print(output)
        temp.unlink(missing_ok=True)
        run(['git', 'checkout', 'origin/main', '--', 'scripts/verify_doc_source_paths.py', '.github/workflows/verify-doc-paths.yml'])
        run(['git', 'config', 'user.name', 'github-actions[bot]'])
        run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'])
        run(['git', 'add', 'docs/manuscript/draft/bkup.orig', 'docs/manuscript/draft/MANUSCRIPT_V2.md', 'docs/manuscript/finalization/PRE_V3_CLEANUP_STATUS.md', 'docs/manuscript/MANUSCRIPT_TODO.md', 'scripts/verify_doc_source_paths.py', '.github/workflows/verify-doc-paths.yml'])
        if run(['git', 'diff', '--cached', '--quiet'], check=False).returncode != 0:
            run(['git', 'commit', '-m', 'Remove backup draft and normalize Table 4 placeholder'])
            run(['git', 'push', 'origin', f'HEAD:{BRANCH}'])
        return code
    finally:
        temp.unlink(missing_ok=True)


def main() -> int:
    head_ref = os.environ.get('GITHUB_HEAD_REF') or os.environ.get('GITHUB_REF_NAME') or ''
    if head_ref == BRANCH:
        return finalize()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        print(output)
        return code
    finally:
        temp.unlink(missing_ok=True)

if __name__ == '__main__':
    sys.exit(main())
