---
title: "Text Refinery Specification v1"
artifact_id: uaks_v1_text_refinery_spec_20260311
pair_id: CHATPAIR-009
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Text Refinery Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_text_refinery_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The Text Refinery converts raw language-bearing sources into governed atomic objects suitable for storage, retrieval, traceability, and assembly. It is the canonical upstream producer for TextAtom, EvidenceAtom, and PolicyAtom, and may also emit supporting entities, relations, and provenance records.


2. Inputs

Input family
Examples
Conversational text
chats, transcripts, interviews, meetings
Documentary text
notes, specs, memos, policies, essays
Structured text
markdown, HTML, JSON-derived text fields
OCR-derived or imported text
PDF extraction, image-derived text, legacy corpus text

3. Outputs

Output type
Purpose
TextAtom
self-contained textual meaning
EvidenceAtom
source-backed supporting fragment
PolicyAtom
normative rule or governance statement
Entity
canonical referenced objects
RelationEdge
support, contradiction, refinement, derivation, use
ProvenanceRecord
refinery lineage

4. Core refinery stages

Stage
Name
Purpose
TR-01
Source normalization
convert input to normalized textual substrate
TR-02
Structural segmentation
divide source into candidate units
TR-03
Entity and cue extraction
detect actors, concepts, times, constraints, signals
TR-04
Proposition decomposition
separate multi-claim units into simpler statements
TR-05
Atomic distillation
rewrite into smallest independent units
TR-06
Atom typing
classify as text, evidence, policy, and assign classes
TR-07
Linking
create entity links, evidence links, parent-child links
TR-08
Deduplication
merge near-equivalent atoms while preserving provenance
TR-09
Validation
enforce atomicity, scope, provenance, and trust rules
TR-10
Publication
persist atoms, relations, and provenance

5. Stage requirements


5.1 TR-01 Source normalization


The refinery MUST normalize encodings, line endings, markup artifacts, and obvious extraction noise. It SHOULD preserve paragraph, heading, speaker-turn, and list structure where available.


5.2 TR-02 Structural segmentation


Segmentation SHOULD honor the native structure of the source.

Source type
Preferred boundary signals
Transcript
speaker turn, timestamp, pause marker
Spec / memo
heading, paragraph, numbered clause
Notes
list item, paragraph, heading
Policy
clause, sentence, subclause
Documentation
heading, paragraph, example block

5.3 TR-03 Entity and cue extraction


The refinery SHOULD extract:

Cue family
Examples
Entities
people, organizations, projects, systems, concepts
Temporal cues
dates, ranges, sequence words
Normative cues
must, should, may, prohibited, required
Evidentiary cues
measured, observed, cited, quoted
Contrast cues
however, except, unless, unlike
Scope cues
for project X, in testing, under policy Y

5.4 TR-04 Proposition decomposition


A segment containing multiple claims MUST be decomposed when those claims can stand independently.


Example:

Input segment
Decomposed outputs
“The system stores recipes, and recipes update when atoms change.”
“The system stores recipes.” / “Recipes update when atoms change.”

5.5 TR-05 Atomic distillation


A candidate atom passes atomic distillation only if it is independently comprehensible without hidden local context. Pronouns, omitted referents, and elliptical fragments SHOULD be resolved during distillation where possible.


5.6 TR-06 Atom typing

Condition
Output
Normative or governance statement
PolicyAtom
Source-backed support fragment or measurement
EvidenceAtom
General self-contained textual meaning
TextAtom

5.7 TR-07 Linking


The refinery SHOULD emit relations for:

Relation
Trigger
DERIVED_FROM
every produced atom
USES_ENTITY
entity mention or resolution
SUPPORTED_BY
claim backed by evidence
REFINES
child atom is more precise than parent
CONTRADICTS
detected scoped conflict
SUPERSEDES
explicit replacement semantics in source

5.8 TR-08 Deduplication


Near-equivalent atoms MAY be merged if meaning is materially the same and provenance is preserved as multiplicity. Contradictory or scope-divergent statements MUST NOT be collapsed.


5.9 TR-09 Validation


An atom MUST be rejected or downgraded if:

Failure mode
Result
no source span
reject publication
unresolved opaque referents
re-distill or downgrade
mixed incompatible claims
decompose further
unclear scope on normative statement
hold for review
unsupported interpretive compression
mark as interpretation or downgrade

5.10 TR-10 Publication


Published atoms MUST receive logical ID, content hash, CAS payload reference, provenance record, validation state, and created timestamps.


6. Atomicity tests

Test ID
Test
Pass condition
TAT-01
Independence
statement stands alone
TAT-02
Referential clarity
main referents explicit or linked
TAT-03
Provenance trace
exact source span present
TAT-04
Scope clarity
scope/temporal qualifiers present when needed
TAT-05
Type fit
chosen atom type matches function
TAT-06
Non-fusion
not improperly bundling multiple separable claims

7. Text refinery decision heuristics

Pattern
Preferred action
rule-like modal verbs
emit PolicyAtom
quotations and measurements
emit EvidenceAtom plus optional linked TextAtom
long descriptive paragraph
split into multiple TextAtoms
summary sentence derived from multiple spans
emit interpretive or summary atom only if marked and linked

8. Minimal publication example


{
  "atomId": "atom_text_014",
  "atomType": "TEXT",
  "atomClass": "FACT",
  "contentHash": "sha256:abcd",
  "canonicalPayloadRef": "cas_014",
  "sourceRef": "src_memo_003",
  "provenanceRefs": ["prov_014"],
  "validationState": "DISTILLED",
  "taxonomyTags": ["architecture", "assembly"],
  "createdAt": "2026-03-11T16:00:00Z",
  "updatedAt": "2026-03-11T16:00:00Z",
  "status": "ACTIVE",
  "textKind": "DOCUMENTATION_CLAUSE",
  "canonicalStatement": "Documents are assembled projections rather than primary storage objects.",
  "sourceSpan": {
    "locatorType": "LINE_COLUMN",
    "start": {"line": 12, "column": 1, "value": "12:1"},
    "end": {"line": 12, "column": 73, "value": "12:73"}
  },
  "entitiesMentioned": []
}
