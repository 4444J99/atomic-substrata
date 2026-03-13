---
title: "Re-Refinement Protocol"
artifact_id: uaks_v1_re_refinement_protocol_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Re-Refinement Protocol

Document ID: uaks_v1_re_refinement_protocol_20260311

## 1. Purpose

The Re-Refinement Protocol defines when and how atoms should be re-processed through the refinement pipeline to improve quality, incorporate new extraction methods, or fix identified issues.

## 2. Triggers

### 2.1 Automatic Triggers

| Trigger | Condition | Priority |
|---------|-----------|----------|
| Source update | New version detected | High |
| Parser upgrade | New parser version | Medium |
| Schema change | New atom schema | High |
| Quality flag | Low confidence score | Medium |

### 2.2 Manual Triggers

| Trigger | Initiator | Priority |
|---------|-----------|----------|
| Audit request | Auditor | High |
| Bug report | User | High |
| Bulk re-refine | Admin | Low |

## 3. Re-Refinement Modes

### 3.1 Full Re-Refinement

- Complete pipeline re-execution
- New hash generated
- New atom created
- Old atom marked as superseded

### 3.2 Incremental Re-Refinement

- Only affected components
- Preserve unchanged data
- Faster, lower impact

### 3.3 Selective Re-Refinement

- Specific atom families
- Specific source types
- Granular control

## 4. Processing Pipeline

### 4.1 Workflow

```
Identify Atoms → Assess Impact → Plan Re-refine → Execute → Verify → Update
```

### 4.2 Impact Assessment

Before re-refinement:

1. Count affected atoms
2. Estimate processing time
3. Identify relation impacts
4. Check dependent recipes

### 4.3 Execution

1. Lock affected atom IDs
2. Create new atom versions
3. Update relations (if needed)
4. Verify integrity
5. Release locks
6. Update superseded chain

## 5. Versioning

### 5.1 Atom Versioning

```
Original:   atom_abc123_000001
Re-refined: atom_abc123_000002
```

### 5.2 Supersession Chain

```
atom_abc123_000001
  ↓ superseded_by
atom_abc123_000002
  ↓ superseded_by
atom_abc123_000003
```

## 6. Rollback

### 6.1 Failure Handling

If re-refinement fails:

1. Preserve original atom
2. Log failure details
3. Alert operators
4. Manual intervention required

## 7. Source Lineage

Derived from the UAKS architecture conversation artifact set.
