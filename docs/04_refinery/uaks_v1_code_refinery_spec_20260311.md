---
title: "Code Refinery Specification v1"
artifact_id: uaks_v1_code_refinery_spec_20260311
pair_id: CHATPAIR-009
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
