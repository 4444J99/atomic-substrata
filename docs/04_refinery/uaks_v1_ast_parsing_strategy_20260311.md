---
title: "AST Parsing Strategy v1"
artifact_id: uaks_v1_ast_parsing_strategy_20260311
pair_id: CHATPAIR-010
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

AST Parsing Strategy v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_ast_parsing_strategy_20260311
Version: 1.0-draft
Status: Draft normative strategy


1. Purpose


This strategy defines how UAKS-v1 structurally parses code and technical artifacts to produce CodeAtoms and dependency relations. The aim is parser-grounded technical atomization with exact spans, stable symbol extraction, and language-aware boundaries.


2. Strategy thesis


The code refinery MUST be structurally grounded. It MUST prefer AST or equivalent parse-tree representations for supported languages and structured grammars for supported non-code artifacts.


Regex-only or arbitrary chunking approaches MAY serve as fallback for unsupported inputs, but outputs from those paths SHOULD remain lower-trust until upgraded by parser-grade support.


3. Parser tiers

Tier
Description
Trust
Tier 1
full AST parser with stable grammar
highest
Tier 2
structured parser or schema-aware parser
high
Tier 3
fallback structural parser
medium-low
Tier 4
text chunk heuristic
low

4. Language support model


The implementation SHOULD maintain a language support registry.


4.1 Example support registry

Family
Preferred parsing mode
Python
full AST
TypeScript / JavaScript
full AST
Rust
full AST
SQL
grammar-aware structured parse
YAML / TOML / JSON
structured parse
shell
structured parse where feasible, fallback otherwise
Dockerfile / workflow YAML
structured parse
Markdown with code fences
mixed-mode parse

5. Parser outputs required for publication


For a supported code object to be published as a normal CodeAtom, the parser path SHOULD emit:

Output
Meaning
symbol identity
name or anonymous stable boundary
node type
AST classification
source span
exact location
container path
file/module/package location
child relationships
contained members if applicable
dependency indicators
imports, calls, references where possible

6. Boundary rules


6.1 Functional boundaries


A function or method SHOULD usually become one CodeAtom.


6.2 Type boundaries


A class, interface, schema, or migration unit MAY become one CodeAtom if operationally meaningful.


6.3 Module boundaries


A module MAY become a CodeAtom when file-level logic or configuration has meaning beyond contained symbols.


6.4 Composite handling


A file MAY produce:

Result
Example
one module atom only
small config file
module atom plus child function atoms
utility source file
class atom plus method atoms
object-oriented source file
schema atom plus migration-step atoms
database migration

7. Dependency extraction priorities


The parser strategy SHOULD prioritize these dependency classes:

Priority
Dependency class
1
imports / requires / use statements
2
function/method calls
3
inheritance / interface implementation
4
query/model/schema usage
5
config/environment dependency
6
workflow step dependency

8. Fallback mode rules


When a language lacks Tier 1 or Tier 2 support:

Rule
Requirement
FP-01
fallback outputs MUST be marked as lower trust
FP-02
spans MUST still be exact where possible
FP-03
semantic merge of fallback code atoms SHOULD be conservative
FP-04
reprocessing SHOULD be possible when parser support improves

9. Mixed artifact parsing


Some source files contain multiple modalities.


Examples:

Artifact
Parsing approach
markdown with code fences
document parse + embedded code parse
notebooks
cell-aware parse
workflow YAML with shell fragments
structured parse + embedded shell segments
template files
container parse + extracted logic blocks

The parsing strategy SHOULD support multimodal boundary extraction where practical.


10. Final normative judgment


A valid UAKS-v1 AST strategy MUST:

Requirement
Status
support parser tiers
mandatory
record parser provenance
mandatory
preserve exact spans
mandatory
distinguish parser-grade from fallback-grade outputs
mandatory
support reprocessing on parser improvement
mandatory
