# Distillation Input Manifest Plan

Date: 2026-03-12
Project: `/Users/4jp/Workspace/organvm-i-theoria/uaks`

## Objective

Create one authoritative manifest that tells the software-distillation layer exactly which Markdown files should be used as implementation inputs.

## Required Outcome

- Enumerate canonical mainline UAKS specs.
- Enumerate branch-only supplemental specs that add unique design data.
- Enumerate non-normative context that is useful for engineering orientation but should not be treated as normative substrate law.
- Enumerate placeholders to exclude from implementation ingestion.
- Make the selection reproducible from existing manifests rather than hand-curated only in chat.

## Approach

1. Read the current main artifact manifest, branch artifact manifest, and unresolved placeholder list.
2. Define a category mapping by path and artifact kind:
   - canonical mainline specs,
   - branch supplemental specs,
   - non-normative context,
   - excluded placeholders.
3. Generate:
   - `manifests/distillation_input_manifest.json`
   - `manifests/distillation_input_manifest.md`
4. Add tests that confirm:
   - placeholders are excluded from distillation inputs,
   - branch-only supplemental docs are included,
   - canonical mainline docs are included,
   - manifest categories are non-empty where expected.

## Validation

- Run the manifest builder.
- Run `pytest`.
- Spot-check the output paths and counts.
