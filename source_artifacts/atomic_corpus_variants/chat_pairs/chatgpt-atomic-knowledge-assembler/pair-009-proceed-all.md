---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 9
prompt_title: "Proceed all"
response_title: "Text Refinery Specification v1"
prompt_sha256: "fdd3a0990909d012eed70a1a19eab5698e7e146b1d0d6f3ece957395ef1c775b"
response_sha256: "b80c90db11de89357ab4535e42efb0b0b3912537ed238d5af7e2cda9bae6c6f4"
---

# Pair 009

## Prompt

Proceed all

## Response

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



Code Refinery Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_code_refinery_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The Code Refinery converts technical sources into governed CodeAtoms, dependency edges, technical entities, provenance records, and traceability links to text and policy atoms. It MUST be structurally grounded and MUST NOT rely on naive text chunking as its primary method.


2. Inputs

Input family
Examples
Source code
Python, JavaScript, TypeScript, Rust, etc.
Configuration
YAML, TOML, JSON, env templates
Schema definitions
SQL migrations, ORM models, interface schemas
Test code
unit tests, integration tests, assertions
Infrastructure
Dockerfiles, workflow files, IaC manifests
Shell and scripts
bash, zsh, PowerShell, CLI orchestration

3. Outputs

Output type
Purpose
CodeAtom
executable or technical logic unit
Entity
repos, modules, services, interfaces, schemas
RelationEdge
dependencies, tests, implementation links
ProvenanceRecord
parse and transformation lineage

4. Core refinery stages

Stage
Name
Purpose
CR-01
Source normalization
canonicalize file encoding and parser input
CR-02
AST or structural parse
generate syntax/structure model
CR-03
Symbol extraction
identify functions, methods, classes, modules, configs
CR-04
Boundary determination
set atom spans
CR-05
Signature and metadata extraction
inputs, outputs, language, runtime
CR-06
Dependency analysis
build call/import/interface graph
CR-07
Semantic tagging
side effects, complexity, role, domain
CR-08
Cross-domain linking
map code to policy, docs, tests
CR-09
Validation
ensure parse integrity and code atom validity
CR-10
Publication
persist atoms, edges, provenance

5. Stage requirements


5.1 CR-01 Source normalization


The refinery MUST preserve source-exact spans while normalizing encoding and line endings.


5.2 CR-02 AST or structural parse


Supported languages SHOULD use AST-aware parsers. Unsupported languages MAY use fallback structural parsing, but outputs SHOULD remain lower-trust until parser-grade support exists.


5.3 CR-03 Symbol extraction


The refinery MUST support at least these atom categories:

Category
Examples
FUNCTION
standalone callable
METHOD
class-bound callable
CLASS
type definition
MODULE
file/package logical unit
CONFIG
config block
QUERY
SQL or query object
SCRIPT_STEP
shell/invocation step
TEST_CASE
test unit
SCHEMA_UNIT
schema or migration
UI_COMPONENT
component unit
INFRA_UNIT
deployment/infrastructure unit

5.4 CR-04 Boundary determination


Atom boundaries SHOULD correspond to operationally meaningful spans, not arbitrary token windows. One file MAY produce many code atoms.


5.5 CR-05 Signature and metadata extraction


Where possible the refinery SHOULD extract:

Field
Meaning
symbolName
canonical symbol
signature
arguments, returns, modifiers
language
source language
runtime
interpreter/compiler/runtime
astNodeType
parser classification
modulePath
logical workspace path

5.6 CR-06 Dependency analysis


The refinery SHOULD emit DEPENDS_ON and reverse dependency maps where robustly resolvable.


Dependency sources include:

Dependency family
Examples
import/module
imports, requires, use statements
call graph
function or method calls
contract
interface or schema dependency
configuration
env or config requirement
data access
table/model/query dependency

5.7 CR-07 Semantic tagging


The refinery SHOULD estimate:

Tag
Meaning
side effect profile
pure, read-only, write, network, filesystem, external
complexity score
static estimate
breaking-change risk
low/medium/high
technical role
parser, transport, validation, UI, persistence

5.8 CR-08 Cross-domain linking


Where evidence exists, the refinery SHOULD permit links such as:

Relation
Meaning
IMPLEMENTS
code realizes text/policy rule
DOCUMENTS
text describes code
TESTS
code/test validates code
AFFECTS
rule change impacts code

5.9 CR-09 Validation


A CodeAtom MUST NOT be published as verified without:

Requirement
Meaning
parse integrity
span is structurally valid
source trace
exact file and span recorded
hash integrity
payload corresponds to CAS object
type integrity
atom category is valid

5.10 CR-10 Publication


Published CodeAtoms MUST include content hash, CAS reference, source span, language, code kind, and timestamps.


6. Code refinery invariants

Invariant ID
Rule
CRI-01
one exact source span per published code atom
CRI-02
one content-addressed payload reference per code atom
CRI-03
supported-language code atoms SHOULD derive from parser output
CRI-04
dependency edges MUST be directional
CRI-05
code atoms MAY coexist across versions via supersession rather than overwrite

7. Minimal publication example


{
  "atomId": "atom_code_021",
  "atomType": "CODE",
  "atomClass": "PROCEDURE",
  "contentHash": "sha256:efgh",
  "canonicalPayloadRef": "cas_021",
  "validationState": "DISTILLED",
  "taxonomyTags": ["refinery", "text"],
  "createdAt": "2026-03-11T16:10:00Z",
  "updatedAt": "2026-03-11T16:10:00Z",
  "status": "ACTIVE",
  "codeKind": "FUNCTION",
  "language": "python",
  "runtime": "python3.12",
  "astNodeType": "FunctionDef",
  "symbolName": "segment_source_text",
  "modulePath": "refinery/text/segment.py",
  "astSpan": {
    "locatorType": "LINE_COLUMN",
    "start": {"line": 8, "column": 1, "value": "8:1"},
    "end": {"line": 29, "column": 1, "value": "29:1"}
  },
  "sideEffectProfile": "PURE",
  "contentAddressRef": "cas_code_021"
}



Graph Relation Catalog v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_graph_relation_catalog_20260311
Version: 1.0-draft
Status: Draft normative catalog


1. Purpose


This catalog defines the canonical edge vocabulary for the graph substrate. Relations represent typed, directional semantics between atoms, entities, sources, and recipes.


2. General rules

Rule ID
Requirement
GRC-01
every edge MUST have a source and target
GRC-02
every edge MUST have a declared relation type
GRC-03
every verified edge SHOULD have provenance
GRC-04
edge semantics MUST remain directional unless explicitly symmetric
GRC-05
contradictory edges MAY coexist if scope or provenance differs

3. Canonical relation catalog

Relation
Source
Target
Directional
Meaning
DERIVED_FROM
Atom
SourceObject or Atom
Yes
output derives from prior object
SUPPORTED_BY
Atom
EvidenceAtom or Atom
Yes
claim is backed by support
CONTRADICTS
Atom
Atom
Usually symmetric
scoped conflict
SUPERSEDES
Atom
Atom
Yes
later state replaces earlier
USES_ENTITY
Atom
Entity
Yes
references or invokes entity
ASSEMBLED_IN
Atom
RecipeAtom
Yes
recipe membership
REFINES
Atom
Atom
Yes
more specific or more resolved form
IMPLEMENTS
CodeAtom
TextAtom or PolicyAtom
Yes
code realizes rule/statement
DOCUMENTS
TextAtom
CodeAtom
Yes
text describes code
TESTS
CodeAtom
CodeAtom
Yes
test validates target
AFFECTS
PolicyAtom or TextAtom
CodeAtom
Yes
change in rule impacts code
EXPOSES_INTERFACE
CodeAtom
Entity
Yes
code exposes contract/interface
ANALYZES
Analysis family
SourceObject or Atom
Yes
analysis studies target
MAPS_TO
Analysis family
Entity or Atom
Yes
external label aligned to local concept
CHARACTERIZES
Analysis family
Entity or corpus target
Yes
structural description
DETECTS_DRIFT_IN
DriftAtom
Entity or Atom
Yes
temporal change detected
PROPOSES_TAXONOMY_FOR
TaxonomyProposalAtom
corpus/entity/concept set
Yes
taxonomy suggestion
REQUIRES_REVIEW_OF
Analysis family
Atom
Yes
flags re-evaluation
IS_SUPERSEDED_BY
Analysis family
Analysis family
Yes
analytical successor
DEPENDS_ON
CodeAtom
CodeAtom or Entity
Yes
operational dependency

4. Edge qualifiers


An edge MAY carry qualifiers.

Qualifier
Meaning
confidence
strength or trust score
scope
project/time/jurisdiction scope
provenanceRef
lineage record
effectiveFrom / effectiveTo
validity window
rationale
explanatory note

5. Recommended inverses


Some inverses MAY be materialized for convenience.

Primary edge
Optional inverse
SUPERSEDES
IS_SUPERSEDED_BY
DEPENDS_ON
DEPENDENT_OF as derived view only
IMPLEMENTS
IMPLEMENTED_BY as derived view only
TESTS
TESTED_BY as derived view only

The canonical stored edge SHOULD remain the primary direction unless operational needs justify both.


6. High-value relation patterns


6.1 Rule to code trace


PolicyAtom → AFFECTS → CodeAtom
CodeAtom → IMPLEMENTS → PolicyAtom


6.2 Claim support chain


TextAtom → SUPPORTED_BY → EvidenceAtom


6.3 Analysis-triggered maintenance


DriftAtom → REQUIRES_REVIEW_OF → TextAtom
TextAtom → AFFECTS → CodeAtom


6.4 Assembly trace


Atom → ASSEMBLED_IN → RecipeAtom



Validation and Trust Policy v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_validation_trust_policy_20260311
Version: 1.0-draft
Status: Draft normative policy


1. Purpose


This policy governs lifecycle states, review thresholds, trust gradients, and assembly eligibility for all atom families.


2. Core validation states

State
Meaning
Standard assembly eligibility
DRAFT
created but not conformance-checked
No
DISTILLED
machine-produced and schema-valid
No
REVIEWED
human or trusted review applied
Conditional
VERIFIED
approved for normal assembly
Yes
DEPRECATED
retained, not active
No
DISPUTED
challenged or conflicting
No

3. Analysis trust states

State
Meaning
Standard assembly eligibility
IMPORTED
raw accepted external import
No
MACHINE_DERIVED
normalized machine analysis
No by default
ACCEPTED
approved for standard use
Yes
EXPERIMENTAL
exploratory research lane only
No by default

4. Promotion rules

From
To
Minimum requirement
DRAFT
DISTILLED
schema-valid and provenance present
DISTILLED
REVIEWED
reviewer check or trusted adjudicator
REVIEWED
VERIFIED
passes domain-specific trust threshold
IMPORTED
MACHINE_DERIVED
normalization membrane completed
MACHINE_DERIVED
REVIEWED
review performed
REVIEWED
ACCEPTED
approved for standard analytical inclusion

5. Mandatory review cases


The following SHOULD require human or high-trust review before standard assembly:

Atom family
Trigger
PolicyAtom
operational, legal, or governance consequence
CodeAtom
external side effects, high breaking-change risk
InterpretationAtom
inferential claims influencing decisions
TaxonomyProposalAtom
ontology-changing suggestion
DriftAtom
triggers taxonomy or policy review
any atom
contradiction or low-confidence ambiguity

6. Assembly inclusion policy

Output mode
Allowed states
Standard operational output
VERIFIED, ACCEPTED
Research output
REVIEWED, VERIFIED, ACCEPTED, optional EXPERIMENTAL
Exploratory output
may include DISTILLED and MACHINE_DERIVED if explicitly requested
High-trust/compliance output
VERIFIED only unless policy exception exists

7. Dispute handling


A disputed atom MUST remain traceable, MUST retain provenance, and SHOULD remain queryable in forensic contexts while excluded from normal assembly.


8. Supersession handling


Superseded atoms MUST NOT be deleted merely because newer atoms exist. They SHOULD remain accessible for history, lineage, and comparison.



Assembly Engine Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_assembly_engine_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The Assembly Engine converts governed atoms into human-facing outputs or saved recipes. It does not originate truth. It selects, sequences, and renders truth-bearing substrate objects subject to trust, scope, and template rules.


2. Inputs

Input
Description
query
user or system request
atom set
explicit list of atoms
recipe
prior assembly plan
template
output mold
resolution level
micro to deep
policy
trust and inclusion constraints

3. Outputs

Output
Description
rendered text
assembled human-readable output
recipe
reusable ordered atom plan
provenance refs
lineage exposure
warnings
ambiguity, missing support, low-trust inclusion

4. Assembly stages

Stage
Name
Purpose
AE-01
scope resolution
determine topic, audience, trust mode, depth
AE-02
candidate retrieval
fetch atoms through hybrid retrieval
AE-03
policy filtering
exclude ineligible states
AE-04
structural grouping
group atoms by role and template needs
AE-05
sequencing
order atoms logically
AE-06
connective synthesis
generate transitions and framing
AE-07
provenance packaging
attach source references if needed
AE-08
recipe persistence
save reusable assembly plan

5. Resolution model

Resolution
Inclusion logic
MICRO
highest-centrality core atoms only
COMPACT
core atoms plus minimal support
STANDARD
balanced claim, support, and context
EXTENDED
detailed support and operational structure
DEEP
evidence lattice, edge cases, contradictions, and lineage

6. Template classes

Template class
Purpose
Summary
concise overview
Technical Spec
formal structured explanation
Trace Report
rule-code or source-claim lineage
Impact Report
downstream effect analysis
Decision Memo
rationale, options, recommendation
Research Synthesis
multi-layer evidence-rich exposition

7. Engine rules

Rule ID
Requirement
AE-R-01
the engine MUST honor validation/trust policy
AE-R-02
the engine MUST NOT present unsupported generated claims as substrate truth
AE-R-03
connective prose MAY be generated
AE-R-04
recipe capture SHOULD store atom order, template, and resolution
AE-R-05
contradiction-aware outputs SHOULD surface scoped conflicts rather than flatten them

8. Minimal recipe object


{
  "recipeId": "recipe_101",
  "recipeType": "technical_spec",
  "resolutionLevel": "STANDARD",
  "atomSequence": ["atom_text_014", "atom_policy_005", "atom_code_021"],
  "templateRef": "template_technical_spec_v1",
  "generationRules": {
    "includeProvenance": true,
    "includeAnalysis": false
  },
  "createdAt": "2026-03-11T16:30:00Z"
}


9. Minimal assembly result


{
  "resultId": "assembly_101",
  "recipeRef": "recipe_101",
  "renderedText": "The system stores knowledge as atoms and renders documents as assemblies. Policy logic is enforced by linked code paths.",
  "atomIdsUsed": ["atom_text_014", "atom_policy_005", "atom_code_021"],
  "provenanceRefs": ["prov_014", "prov_005", "prov_021"],
  "warnings": []
}



Foundational Launch Artifact Set


Consolidated Launch Inventory


Below is the launch-ready foundational set, normalized from the prior architecture work into operational categories.


1. Governance ring

Artifact
Required
Vision and Thesis Document
Yes
Scope and Exclusions Charter
Yes
Ontology Charter v1
Yes
Naming Convention Standard
Yes
Provenance Policy
Yes
Validation and Trust Policy v1
Yes
Supersession Policy
Yes
Contradiction Handling Policy
Yes
Security and Rights Policy
Yes

2. Architecture ring

Artifact
Required
Architecture Specification v1
Yes
Visual Architecture Diagram
Yes
Logical Data Model
Yes
Physical Storage Architecture
Yes
Service Decomposition Spec
Yes
Trust Boundary Map
Yes
Failure Mode and Resilience Analysis
Yes
Nonfunctional Requirements Spec
Yes

3. Schema ring

Artifact
Required
Schema Pack v1
Yes
GraphQL Schema Draft v1
Yes
Graph Relation Catalog v1
Yes
CAS Object Model
Yes
Hashing Standard
Yes

4. Pipeline ring

Artifact
Required
Text Refinery Specification v1
Yes
Code Refinery Specification v1
Yes
External Analysis Integration Spec v1
Yes
Atomicity Test Suite
Yes
AST Parsing Strategy
Yes
Deduplication and Merge Policy
Yes
Re-refinement Protocol
Yes
QA Rubric
Yes

5. Retrieval and assembly ring

Artifact
Required
Retrieval Scoring Specification
Yes
Template Catalog
Yes
Assembly Engine Specification v1
Yes
Recipe Persistence Spec
Yes
Provenance Rendering Rules
Yes
Traceability Report Format
Yes
Impact Analysis Report Format
Yes

6. Interface and operations ring

Artifact
Required
Resolver Contract Specification
Yes
Query Pattern Library
Yes
Portal Projection Specification
Yes
Auth and Access Model
Yes
Pilot Intake SOP
Yes
Review Workflow SOP
Yes
Change Management SOP
Yes
Incident Response SOP
Yes
Release Checklist
Yes
Runbook Set
Yes
Observability Dashboard Spec
Yes

7. Evaluation ring

Artifact
Required
Benchmark Corpus Definition
Yes
Gold-Standard Atom Set
Yes
Retrieval Evaluation Harness
Yes
Assembly Evaluation Harness
Yes
Traceability Coverage Report
Yes
Drift Detection Report
Yes
Cost and Capacity Model
Yes
Launch Readiness Scorecard
Yes

8. Seed ring

Artifact
Required
Canonical Ontology Examples
Yes
Sample TextAtom Corpus
Yes
Sample CodeAtom Corpus
Yes
Rule-to-Code Bridge Examples
Yes
Initial Template Pack
Yes
Initial Recipe Pack
Yes


Recommended Build Order


Execution Sequence

Phase
Deliverables
Phase 1
governance pack, ontology charter, naming, provenance, trust
Phase 2
architecture spec, diagram, trust boundary map, storage decisions
Phase 3
schema pack, relation catalog, GraphQL contract
Phase 4
text refinery, code refinery, analysis integration, parsing strategy
Phase 5
retrieval scoring, templates, assembly engine, provenance rendering
Phase 6
SOPs, runbooks, auth, portal projection, release checklist
Phase 7
benchmarks, evaluation harnesses, readiness scorecard, seed corpora


Practical Recommendation


At this point, the highest-value next drafting cluster is:

Priority
Next artifact
1
Retrieval Scoring Specification
2
Deduplication and Merge Policy
3
AST Parsing Strategy
4
Portal Projection Specification
5
Release Checklist + Launch Readiness Scorecard

If you want the most implementation-useful continuation, the next correct move is the Retrieval Scoring Specification v1 pack.