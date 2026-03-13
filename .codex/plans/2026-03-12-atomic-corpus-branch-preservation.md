# Atomic Corpus Branch Preservation Plan

Date: 2026-03-12
Project: `/Users/4jp/Workspace/organvm-i-theoria/uaks`

## Objective

Preserve the `atomic-corpus` export variants inside `uaks` without disturbing the current main-thread reconstruction.

## Constraints

- The existing UAKS reconstruction remains anchored to the 21-pair main export.
- Branch exports must be preserved as distinct sources, not merged into the main chat-pair lineage.
- Raw copies, pair archives, and machine-readable lineage metadata must all be created.

## Work

1. Create a separate preservation subtree under `source_artifacts/atomic_corpus_variants/`.
2. Copy in all three JSON exports and all three Markdown exports from the Downloads corpus.
3. Generate pair archives for each JSON export in separate variant directories.
4. Generate a machine-readable manifest describing:
   - files,
   - message/pair counts,
   - shared exact pairs,
   - variant-only pairs,
   - notable branch-only design lines.
5. Keep the previously written unique-data report in `manifests/` as the operator-facing summary.

## Validation

- Confirm raw copies exist for all six source files.
- Confirm pair archive counts match each JSON export.
- Confirm manifest pair counts match the exported transcripts.
- Run `pytest` to ensure no existing UAKS tests regress.
