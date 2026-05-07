# Thread Import Staging

Place thread digest zip packages here before running `execution_tools/prompts/05_import_analysis_into_repo.md`.

Expected package shape:

- `docs/imports/<THREAD_DIGEST_FILENAME>.zip`
- The zip contains `<THREAD_DIGEST_FILENAME>.md` at the zip root.
- The import prompt extracts the digest to `docs/threads/<THREAD_DIGEST_FILENAME>.md`.

Zip packages are local staging inputs and are ignored by git.
