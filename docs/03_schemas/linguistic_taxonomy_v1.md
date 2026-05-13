# Linguistic Taxonomy v1 — `linguisticKind` Schema Extension

**Status:** Active (2026-04-26)
**Scope:** Additive extension to UAKS v1 (see `uaks_v1_schema_pack_20260311.md`).
**Implementation:** `~/.local/bin/substrate-check` (chezmoi source: `dot_local/bin/executable_substrate-check`).
**Persistence:** `~/Workspace/organvm/organvm-corpvs-testamentvm/data/atoms/utterance-atoms.jsonl`

---

## Why this exists

UAKS v1 classifies atoms by **content semantics** — `atomType` (TEXT/CODE/EVIDENCE/…) and `atomClass` (AXIOM/RULE/PROCEDURE/…). It cannot distinguish:

- a `$NEXT_ARTIFACT = "PITCH_DECK"` declaration from a free-form sentence
- a rhetorical filler ("okay", "so", "right?") from a substantive content unit
- an imperative phrase that *acts* ("dispatch fleet", "review recursive") from a passive description
- a question seeking closure ("safe to close?", "are we certain, Sisyphus?") from a statement

The user's directive (2026-04-26):

> *"Every word, put it on the scale, and measure whether it is an element, a non, a space filler, or a sequence of elements that act."*

This taxonomy fills that gap. It is **orthogonal** to `atomType`/`atomClass` — every existing atom can be back-classified without schema breakage.

---

## The seven kinds

| Kind | Definition | Detection rule | Example |
|---|---|---|---|
| `ELEMENT` | Substantive content unit (noun phrase, named entity, file path, ID, code identifier). The default kind for content. | Default fallthrough — passes content filter, not in stop-list, not a recognized filler/verb head. | `repository`, `agentic-titan`, `ATM-013811`, `Maddie's site` |
| `NON_WORD` | Grammatical glue: articles, prepositions, conjunctions, auxiliaries, pronouns. The "non" in the user's vocabulary. | Single-token match against `NON_WORDS` set (a, an, the, of, and, or, to, in, on, at, for, with, by, from, as, is, are, was, were, be, been, being, has, have, had, this, that, these, those, my, your, etc.). | `the`, `of`, `and`, `is` |
| `SPACE_FILLER` | Rhetorical filler / hesitation / emphasis. Carries no propositional content. | Single-token match against `SPACE_FILLERS` set (okay, so, um, uh, hmm, well, right, like, just, anyway, basically…) **OR** a run of `?!.…` of length ≥ 2. | `okay`, `so`, `?????????`, `…` |
| `ACTING_SEQUENCE` | Imperative phrase that does something — the verb-grade unit of execution. The "sequence of elements that act" in the user's vocabulary. | Phrase head-word lemma matches `ACTION_VERBS` set (proceed, dispatch, review, rename, expand, ingest, atomize, build, deploy, verify, audit, commit, push, etc.) AND phrase has ≥ 2 tokens. | `dispatch fleet`, `commit all push`, `review recursive`, `atomize this prompt` |
| `ENV_VAR_DECLARATION` | Bash-style `$VAR = "value"` or `$VAR=…` assignment. The selector-grade unit from substrate Layer A. | Matches `\$[A-Z_][A-Z0-9_]*\s*[=:]` (declaration) or `\$[A-Z_][A-Z0-9_]+\b` (free reference). Sentence-level when the assignment pattern is present; token-level for free references. | `$NEXT = "PITCH_DECK"`, `$MODE`, `$DEPTH=OPERATOR_GRADE` |
| `INTERROGATIVE` | Question seeking confirmation, closure, or audit. Special role in session governance — these often invoke composite predicates. | Sentence ends with `?+` (one or more question marks). Sentence-level only — never token-level (avoids polluting child-atom kind counts). Emitted as a sentence-level atom only when the parent text contains multiple sentences; single-sentence questions ride on the parent atom's kind. | `are we certain, Sisyphus?`, `is this session safe to close?` |
| `META_DIRECTIVE` | Governance language — universal rules, axioms, hard constraints. The constitutional layer. | Matches a curated regex set drawn from feedback memory: `never overwrite`, `rules are additive`, `N/A is a vacuum`, `local:remote = 1:1`, `if lost recover immediately`, `commit all push`, `triple-check`, etc. | `rules are additive`, `never overwrite plans`, `triple-check before closing` |

### Cardinality

- An utterance produces ONE parent atom (kind = whole-utterance classification) and N child token atoms.
- Children are tokens or short phrases. Each carries exactly one `linguisticKind`.
- Sentence-level kinds (INTERROGATIVE, ENV_VAR_DECLARATION) can appear AS WELL AS token-level decomposition for the same span — they are not mutually exclusive.

### Classification cascade (descending precedence)

```
1. ENV_VAR_DECLARATION   (regex match wins — $VAR = … is unambiguous)
2. META_DIRECTIVE        (axiom-pattern lexicon)
3. INTERROGATIVE         (terminal '?+' on whole sentence)
4. NON_WORD              (single token, in stop-list)
5. SPACE_FILLER          (single token in filler-list, OR a run of ?!.…)
6. ACTING_SEQUENCE       (phrase head ∈ action-verb set, ≥ 2 tokens)
7. ELEMENT               (default fall-through)
```

Order matters: `$NEXT = "value"` is ENV_VAR_DECLARATION even though `$NEXT` could also match SPACE_FILLER's regex. ELEMENT is the residual everything-else bucket.

---

## Schema record (extended UAKS atom)

Every record in `utterance-atoms.jsonl` shares all UAKS fields plus:

```json
{
  "unified_id": "utterance-369612a965fc",
  "original_id": "369612a965fc",
  "source_type": "utterance",
  "title": "Each suggested energy phase exchange has been codified…",
  "body": "Each suggested energy phase exchange has been codified as a rule that could be enforced ?????????",
  "date": "2026-04-26",
  "status": "captured",
  "domain": "linguistic",
  "priority": "P3",
  "tags": ["ELEMENT", "NON_WORD", "SPACE_FILLER", "INTERROGATIVE"],
  "actionable": false,
  "agent": "substrate-check",
  "linked_ids": ["utterance-b3531d161f9c", "utterance-9ff4460087e9", "..."],
  "parent_id": null,
  "linguisticKind": "INTERROGATIVE"
}
```

Children carry `parent_id` pointing to the parent's `unified_id`, and `tags = [linguisticKind]`. The parent's `tags` summarize the *set* of child kinds.

### ID format
`utterance-<12 hex chars>` where hex is the first 12 chars of `sha1(text)` for parents and `sha1(parent_hash + ":" + token)` for children. Stable, content-addressed, dedup-friendly.

---

## Backward compatibility

- Existing UAKS atoms get `linguisticKind: null` implicitly — readers MUST treat this as "not yet classified".
- A future batch job may back-classify the 47,299 unified atoms; this taxonomy was designed so that batch can run without schema migration.
- The `tags` field is unchanged in semantics — `linguisticKind` is a NEW dedicated field, not a tag overload.

---

## Detection-rule artifacts (curated lexicons)

Maintained inside `substrate-check`. Update process: edit the constant set, then re-run `substrate-check atomize` against the corpus to re-populate.

| Lexicon | Source | Maintenance |
|---|---|---|
| `NON_WORDS` | Standard English stop-words (closed class). | Frozen. Add only on observed mis-classification. |
| `SPACE_FILLERS` | Hesitation/filler tokens. | Frozen. Add on observed mis-classification. |
| `ACTION_VERBS` | Drawn from substrate Layer C verbs + ORGANVM operational vocabulary (proceed, dispatch, atomize, etc.). | Living. Append-only. |
| `META_PATTERNS` | Drawn from feedback-memory axioms (universal rules 1–60). | Living. Append-only. |
| `ENV_VAR_RE` | Regex: `\$[A-Z_][A-Z0-9_]*\s*[=:]` | Frozen. |

---

## Limits and known gaps (deliberate, for v2)

- No part-of-speech tagging — naive token classification. Words like `each`, `could`, `would` may mis-classify as ELEMENT when they should be NON_WORD/modal-auxiliary.
- No dependency parsing — passive constructions like "has been codified" don't trigger ACTING_SEQUENCE because the head is `has` (auxiliary), not the verb lemma.
- No semantic similarity — `ATOMIZE` and `BREAK_DOWN` are not equated.
- No multi-language support — English-only stop/filler lists.

These are accepted gaps for v1. v2 candidate: optional spaCy backend, pluggable via `--nlp=spacy` flag, falls back silently to naive when unavailable (rule-of-three resilience).

---

## Provenance

- **Trigger session:** 2026-04-26 mid-session-close exchange.
- **Trigger question:** *"Each suggested energy phase exchange has been codified as a rule that could be enforced ?????????"*
- **Plan file:** `~/.claude/plans/i-do-want-you-tidy-sparrow.md`
- **Substrate distillation:** `~/.claude/plans/2026-04-26-prompt-sequence-distillation-env-fn-iso-substrate.md` Layer A (selectors), Layer B (invariants), Layer C (verbs)
- **Implementation:** `dot_local/bin/executable_substrate-check` in chezmoi source
- **First atom written:** `utterance-369612a965fc` (the trigger question itself)

---

*This schema is sculpture. Versioned, never overwritten. v2 will be `linguistic_taxonomy_v2.md`.*
