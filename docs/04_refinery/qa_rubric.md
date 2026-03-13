---
title: "QA Rubric"
artifact_id: uaks_v1_qa_rubric_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# QA Rubric

Document ID: uaks_v1_qa_rubric_20260311

## 1. Quality Dimensions

### 1.1 Atom Quality

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Accuracy | 30% | Correct extraction from source |
| Completeness | 25% | All extractable content captured |
| Consistency | 25% | Same input produces same atom |
| Integrity | 20% | Hash verification passes |

### 1.2 Scoring

```
Quality Score = (Accuracy × 0.30) + (Completeness × 0.25) + 
                (Consistency × 0.25) + (Integrity × 0.20)
```

**Thresholds:**

| Score | Rating | Action |
|-------|--------|--------|
| 0.9-1.0 | Excellent | Auto-approve |
| 0.7-0.9 | Good | Auto-approve |
| 0.5-0.7 | Fair | Review required |
| <0.5 | Poor | Reject, re-extract |

## 2. Review Checklist

### 2.1 Atom Validation

- [ ] Hash matches canonical form
- [ ] Provenance chain complete
- [ ] Type classification correct
- [ ] Family assignment appropriate
- [ ] Metadata populated

### 2.2 Content Validation

- [ ] No truncation
- [ ] No corruption
- [ ] Encoding correct
- [ ] Structure preserved

### 2.3 Relation Validation

- [ ] Source atom exists
- [ ] Target atom exists
- [ ] Relation type valid
- [ ] No circular dependencies

## 3. Testing Procedures

### 3.1 Automated Tests

| Test | Frequency | Pass Criteria |
|------|-----------|---------------|
| Hash verification | Every atom | 100% match |
| Schema validation | Every atom | Valid JSON |
| Duplicate detection | Batch | <0.01% false positives |
| Integration test | Daily | All tests pass |

### 3.2 Manual Review

Sample-based manual review:

- 1% of atoms (random)
- All atoms below threshold
- All new atom types

## 4. Issue Classification

### 4.1 Severity Levels

| Level | Description | Response Time |
|-------|-------------|---------------|
| Critical | Data loss, integrity failure | 1 hour |
| High | Incorrect extraction | 24 hours |
| Medium | Quality below threshold | 1 week |
| Low | Improvement opportunity | Next sprint |

### 4.2 Issue Types

| Type | Example |
|------|---------|
| Extraction | Wrong content extracted |
| Classification | Wrong type/family |
| Provenance | Missing source reference |
| Hash | Mismatch detected |
| Relation | Broken or invalid relation |

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
