---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 11
prompt_title: "Proceed"
response_title: "Template Catalog v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "4dd6feb02c2bf2e4f73ab00b35f18bae8aaeb3dacabbd84e00183d37c0445583"
---

# Pair 011

## Prompt

Proceed

## Response

Template Catalog v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_template_catalog_20260311
Version: 1.0-draft
Status: Draft normative catalog


1. Purpose


This catalog defines the canonical output molds used by the Assembly Engine. A template does not create truth. It governs how eligible atoms are arranged, emphasized, and connected for a given communicative purpose.


2. Template thesis


The same governed substrate MUST support multiple rendered forms without duplicating underlying truth objects. Templates therefore act as structural molds over atoms, relations, provenance, and recipes.


3. Template object model

Field
Meaning
templateId
unique template identifier
templateName
human-readable name
templateClass
summary, spec, trace, impact, memo, synthesis, review
templateVersion
version string
eligibleAtomFamilies
allowed source families
requiredSections
mandatory structural sections
optionalSections
conditional structural sections
resolutionBehavior
how section depth scales
provenanceMode
hidden, summary, inline, appendix
analysisInclusionPolicy
whether analytical lane may appear
orderingRules
section and atom sequencing logic
connectiveStyle
rhetorical connective policy

4. Canonical template classes

Template class
Purpose
Summary
concise understanding
TechnicalSpec
formal architecture or implementation explanation
TraceReport
lineage, support, or rule-to-code mapping
ImpactReport
downstream consequence analysis
DecisionMemo
recommendation with rationale
ResearchSynthesis
evidence-rich multi-perspective exposition
ReviewPacket
adjudication and review workflow support
WorkspaceView
portal-facing structured projection

5. Canonical templates


5.1 Executive Summary Template

Field
Value
templateId
template_exec_summary_v1
templateClass
Summary
eligibleAtomFamilies
TextAtom, PolicyAtom, CodeAtom, accepted AnalysisAtom
requiredSections
topic, core points, implications
resolutionBehavior
micro/compact favored
provenanceMode
summary
analysisInclusionPolicy
accepted only if materially relevant

Section order:

Order
Section
Purpose
1
Topic framing
what is being summarized
2
Core claims
highest-centrality substrate truths
3
Implications
practical meaning or consequence

5.2 Technical Specification Template

Field
Value
templateId
template_technical_spec_v1
templateClass
TechnicalSpec
eligibleAtomFamilies
TextAtom, PolicyAtom, CodeAtom, EvidenceAtom, accepted AnalysisAtom
requiredSections
purpose, scope, model, components, rules
resolutionBehavior
standard/extended/deep favored
provenanceMode
appendix or inline
analysisInclusionPolicy
only if it clarifies architecture or drift

Section order:

Order
Section
Purpose
1
Purpose
state what the subsystem does
2
Scope
define boundaries
3
Model
explain conceptual structure
4
Components
enumerate core parts
5
Rules
normative or operational constraints
6
Examples
optional concrete objects
7
Provenance / notes
optional evidence and lineage

5.3 Trace Report Template

Field
Value
templateId
template_trace_report_v1
templateClass
TraceReport
eligibleAtomFamilies
TextAtom, PolicyAtom, CodeAtom, EvidenceAtom, RelationAtom, accepted AnalysisAtom
requiredSections
origin, path, targets, support
resolutionBehavior
standard/deep favored
provenanceMode
inline or appendix
analysisInclusionPolicy
accepted only unless exploratory

Section order:

Order
Section
Purpose
1
Origin object
starting atom or source
2
Trace path
graph path narrative
3
Target objects
downstream or upstream objects
4
Supporting evidence
support and provenance
5
Exceptions/conflicts
contradictions or ambiguities

5.4 Impact Report Template

Field
Value
templateId
template_impact_report_v1
templateClass
ImpactReport
eligibleAtomFamilies
CodeAtom, PolicyAtom, TextAtom, accepted DriftAtom, accepted AnalysisAtom
requiredSections
change trigger, affected objects, risk, actions
resolutionBehavior
compact/standard/extended
provenanceMode
summary or appendix
analysisInclusionPolicy
accepted analytical triggers allowed

Section order:

Order
Section
Purpose
1
Trigger
what changed
2
Affected scope
impacted objects and areas
3
Risk profile
severity and uncertainty
4
Recommended actions
review, update, test, reclassify
5
Trace appendix
optional detailed path

5.5 Decision Memo Template

Field
Value
templateId
template_decision_memo_v1
templateClass
DecisionMemo
eligibleAtomFamilies
TextAtom, PolicyAtom, CodeAtom, EvidenceAtom, accepted AnalysisAtom
requiredSections
question, options, evaluation, recommendation
resolutionBehavior
standard/extended
provenanceMode
summary or appendix
analysisInclusionPolicy
accepted analytical support allowed

Section order:

Order
Section
Purpose
1
Decision question
define the issue
2
Options
alternatives under consideration
3
Evaluation
compare by evidence and constraints
4
Recommendation
selected path
5
Rationale
why this path follows
6
Risks
known costs or uncertainties

5.6 Research Synthesis Template

Field
Value
templateId
template_research_synthesis_v1
templateClass
ResearchSynthesis
eligibleAtomFamilies
all primary atoms plus reviewed/accepted analytical atoms
requiredSections
framing, evidence lattice, interpretations, tensions, synthesis
resolutionBehavior
extended/deep favored
provenanceMode
inline and appendix
analysisInclusionPolicy
reviewed and accepted, experimental only if explicitly requested

Section order:

Order
Section
Purpose
1
Research framing
topic and scope
2
Core evidence
source-grounded objects
3
Interpretive layer
governed interpretations
4
Tensions and contradictions
unresolved or competing states
5
Synthesis
integrated conclusion
6
Further questions
optional next research lanes

5.7 Review Packet Template

Field
Value
templateId
template_review_packet_v1
templateClass
ReviewPacket
eligibleAtomFamilies
any disputable or promotable family
requiredSections
object summary, provenance, issues, proposed disposition
resolutionBehavior
standard
provenanceMode
inline
analysisInclusionPolicy
include as relevant to adjudication

5.8 Workspace Projection Template

Field
Value
templateId
template_workspace_projection_v1
templateClass
WorkspaceView
eligibleAtomFamilies
TextAtom, CodeAtom, RecipeAtom, Entity
requiredSections
root, groupings, nodes, links
resolutionBehavior
compact/standard
provenanceMode
hidden by default
analysisInclusionPolicy
excluded by default

6. Resolution behavior rules

Resolution
Template behavior
MICRO
core sections only, highest-density atoms
COMPACT
essential sections, minimal support
STANDARD
balanced section set
EXTENDED
full section set with explanatory connective tissue
DEEP
full sections plus evidence, contradictions, lineage

7. Template selection policy

Query or task type
Preferred template
concise overview
Executive Summary
architecture/system design
Technical Specification
what leads to what
Trace Report
what changes if X changes
Impact Report
choose among options
Decision Memo
deep literature / evidence integration
Research Synthesis
adjudicate trust/state
Review Packet
project-style browsing
Workspace Projection

8. Final normative judgment


A valid template implementation MUST separate template structure from underlying truth objects, MUST be resolution-aware, MUST honor trust policy, and SHOULD preserve provenance rendering options.



Provenance Rendering Rules v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_provenance_rendering_rules_20260311
Version: 1.0-draft
Status: Draft normative rules


1. Purpose


These rules define how provenance is surfaced in rendered outputs, trace reports, review packets, portal projections, and inspection interfaces.


2. Provenance rendering thesis


Provenance must remain available without overwhelming every output. The system therefore supports graded provenance visibility based on output mode, template class, and trust context.


3. Provenance modes

Mode
Behavior
Hidden
provenance stored but not shown
Summary
high-level source summary shown
Inline
provenance attached near statements
Appendix
detailed lineage attached after main content
Forensic
full lineage, spans, operations, and states shown

4. Output-mode defaults

Output mode
Default provenance mode
Standard operational
Summary
Research
Inline or Appendix
Exploratory
Appendix
High-trust / compliance
Inline and Appendix
Review / adjudication
Forensic

5. Minimum provenance disclosure rules

Rule ID
Requirement
PRR-01
every rendered output SHOULD be able to resolve back to atom IDs used
PRR-02
high-trust outputs MUST expose source and validation lineage
PRR-03
analytical findings MUST be distinguishable from source-grounded claims
PRR-04
superseded or disputed objects MUST be visibly marked when shown
PRR-05
provenance summaries MUST not imply stronger certainty than underlying states justify

6. Statement-level rendering rules

Case
Rendering requirement
source-grounded primary claim
show source summary or inline reference when needed
accepted analysis finding
mark as analytical/derived
reviewed interpretation
mark inferential status where relevant
disputed object
visibly flag dispute
historical object
visibly flag non-current status

7. Provenance packet structure


A provenance packet SHOULD include:

Field
Meaning
atomId
governing atom reference
validationState
trust state
sourceRefs
raw source anchors
sourceSpans
exact locations where available
provenanceRefs
transformation lineage
supersessionStatus
current/historical
analysisRunRef
if analytical derivative
warnings
ambiguity, stale state, low trust

8. Rendering examples


8.1 Summary mode


Main statement followed by concise source note.


8.2 Inline mode


Main statement followed by compact provenance markers or structured parenthetical metadata.


8.3 Appendix mode


Main body remains readable; detailed atom and source table appears after body.


8.4 Forensic mode


Each claim is paired with atom identity, source span, transformation history, and trust state.


9. Final normative judgment


A valid provenance rendering implementation MUST preserve the distinction between source evidence and derivative analysis, MUST support stronger disclosure in higher-trust contexts, and SHOULD avoid clutter in low-friction summaries.



Traceability Report Format v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_traceability_report_format_20260311
Version: 1.0-draft
Status: Draft normative format


1. Purpose


This format standardizes reports that explain how one object or claim is connected to others across the substrate. It is used for rule-to-code trace, source-to-claim trace, claim-to-evidence trace, and analysis-to-review trace.


2. Report thesis


A trace report is not merely a list of links. It is a structured explanation of path, support, state, and consequence.


3. Core report schema

Field
Meaning
reportId
unique report identifier
reportType
rule_to_code, source_to_claim, claim_to_evidence, analysis_to_review, historical_trace
originRef
starting object
targetRefs
reached objects
pathRefs
relation edges and intermediate nodes
stateSummary
current trust/supersession status
provenanceMode
hidden/summary/inline/appendix/forensic
generatedAt
timestamp
recipeRef
if persisted

4. Canonical sections

Order
Section
Required
1
Trace objective
Yes
2
Origin object summary
Yes
3
Path narrative
Yes
4
Target object summaries
Yes
5
Support and provenance
Yes
6
Exceptions, ambiguity, or conflict
Conditional
7
Historical notes
Conditional

5. Trace types


5.1 Rule-to-code trace

Element
Required content
Origin
PolicyAtom or TextAtom
Path
AFFECTS / IMPLEMENTS / DOCUMENTS / TESTS edges
Targets
CodeAtom(s), test atoms, supporting docs
Notes
missing implementations, disputed links, stale code states

5.2 Source-to-claim trace

Element
Required content
Origin
SourceObject or EvidenceAtom
Path
DERIVED_FROM / SUPPORTED_BY / REFINES
Targets
TextAtom, PolicyAtom, InterpretationAtom
Notes
scope and transformation history

5.3 Claim-to-evidence trace

Element
Required content
Origin
TextAtom or PolicyAtom
Path
SUPPORTED_BY
Targets
EvidenceAtom(s), source spans
Notes
evidence sufficiency and gaps

5.4 Analysis-to-review trace

Element
Required content
Origin
DriftAtom, InterpretationAtom, AnalysisAtom
Path
REQUIRES_REVIEW_OF / MAPS_TO / ANALYZES
Targets
objects flagged for review
Notes
trust status, run provenance, scope

6. Trace quality rules

Rule ID
Requirement
TRF-01
a trace report MUST distinguish direct edges from inferred narrative explanation
TRF-02
a trace report MUST surface missing links if the chain is incomplete
TRF-03
a trace report SHOULD mark whether targets are current, superseded, disputed, or accepted
TRF-04
a trace report MUST not collapse contradictory branches without flagging them

7. Minimal trace result example

Field
Example
Origin
atom_policy_005
Path
AFFECTS -> atom_code_021, TESTS -> atom_code_test_003
Targets
implementation function, linked test
Notes
one dependent code path lacks reviewed test coverage

8. Final normative judgment


A valid traceability report MUST be path-aware, state-aware, and provenance-aware. It SHOULD be readable both as a structured table and as narrative explanation.



Impact Analysis Report Format v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_impact_analysis_report_format_20260311
Version: 1.0-draft
Status: Draft normative format


1. Purpose


This format standardizes reports that explain likely downstream consequences of a change in policy, code, ontology, analysis findings, or other substrate objects.


2. Report thesis


Impact analysis is not simply dependency listing. It is structured consequence analysis combining direct dependency paths, risk, trust state, and recommended action.


3. Core report schema

Field
Meaning
reportId
unique report identifier
triggerRef
changed or proposed-to-change object
affectedRefs
impacted objects
impactPaths
graph paths supporting impact claims
riskSummary
severity and uncertainty
recommendedActions
next steps
generatedAt
timestamp
recipeRef
persisted recipe if any

4. Canonical sections

Order
Section
Required
1
Trigger summary
Yes
2
Affected scope
Yes
3
Path-based impact explanation
Yes
4
Risk classification
Yes
5
Recommended actions
Yes
6
Supporting provenance
Yes
7
Historical / supersession context
Conditional

5. Impact trigger classes

Trigger class
Typical impact targets
PolicyAtom change
CodeAtom, docs, tests, workflows
CodeAtom change
dependents, tests, interfaces, docs
DriftAtom accepted finding
taxonomy, policy, reclassification targets
TaxonomyProposalAtom adoption
entity classes, retrieval behavior, templates
Recipe/template change
portal views, rendered outputs, downstream clients

6. Risk model

Risk level
Meaning
Low
localized, low uncertainty
Medium
multiple dependents or unclear edge effects
High
broad dependency spread, policy/compliance implications, or high-trust outputs affected

Risk SHOULD consider:

Factor
Influence
dependency breadth
upward
trust criticality
upward
missing test/support coverage
upward
accepted historical stability
downward
clear rollback path
downward

7. Recommended action classes

Action
Use
review
human adjudication needed
update_code
implementing logic must change
update_policy
normative rule must change
reclassify
ontology or trust state must change
rerun_analysis
analytical confirmation needed
add_test
insufficient validation coverage
no_action
impact determined minimal

8. Quality rules

Rule ID
Requirement
IAF-01
an impact report MUST distinguish direct from indirect impact
IAF-02
an impact report SHOULD include uncertainty notes where graph paths are incomplete
IAF-03
an impact report MUST surface high-trust affected objects clearly
IAF-04
an impact report SHOULD name missing evidence or missing test coverage where relevant

9. Minimal example

Section
Example content
Trigger
accepted semantic drift finding about “validation”
Affected scope
taxonomy node, policy atom, two implementing code atoms
Risk
medium-high because policy-code semantics may have diverged
Recommended actions
taxonomy review, policy review, code trace audit, add targeted tests

10. Final normative judgment


A valid impact report MUST be consequence-aware, path-aware, and action-oriented. It SHOULD explain not only what is affected, but why and what should happen next.



Resolver Contract Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_resolver_contract_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


This specification defines the behavior of GraphQL resolvers and adjacent query handlers over the UAKS-v1 substrate. It exists to ensure that API behavior remains consistent with ontology, trust policy, provenance rules, and storage boundaries.


2. Resolver thesis


Resolvers are contract surfaces, not truth sources. They orchestrate retrieval, filtering, joining, projection, and rendering over authoritative substrate layers.


3. Resolver responsibilities

Responsibility
Meaning
object resolution
map IDs to canonical objects
policy enforcement
apply validation/access/trust gates
hybrid retrieval orchestration
invoke lexical, semantic, graph channels
projection
shape results into API contract
provenance attachment
expose lineage according to mode
error signaling
distinguish not found, unauthorized, filtered, ambiguous

4. Resolver classes

Resolver class
Purpose
direct object resolver
fetch one object by ID
collection resolver
search/filter paginated object sets
trace resolver
produce path-aware trace results
impact resolver
produce consequence-aware results
assembly resolver
produce rendered text and recipe-aware outputs
import mutation resolver
ingest external analysis bundles
relation mutation resolver
create governed relations

5. Core contract rules

Rule ID
Requirement
RCS-01
resolvers MUST not bypass validation/trust policy
RCS-02
resolvers MUST not invent substrate objects absent from authoritative storage
RCS-03
resolvers SHOULD return score breakdowns or match reasons where practical for ranked retrieval
RCS-04
resolvers MUST distinguish current from superseded/historical objects when relevant
RCS-05
resolvers MUST preserve ontology distinctions across evidence, primary atoms, and analysis atoms

6. Query resolver behavior


6.1 atom(id)

Requirement
Behavior
direct ID resolution
fetch canonical object by ID
trust handling
enforce access, not assembly eligibility
historical behavior
return object even if superseded, clearly marked

6.2 atoms(filter, limit, offset)

Requirement
Behavior
candidate generation
hybrid retrieval if textQuery present
filter application
type, state, scope, source, entity filters
pagination
deterministic and stable
explanation
SHOULD include match reasons in debug/inspection modes

6.3 traceRuleToCode(ruleAtomId)

Requirement
Behavior
origin validation
confirm origin is rule-like object
path traversal
prioritize AFFECTS, IMPLEMENTS, DOCUMENTS, TESTS
result shape
path-aware and target-aware trace result
missing links
return explicit warnings, not silent omission

6.4 impactAnalysis(codeAtomId)

Requirement
Behavior
dependency traversal
downstream and linked rule/doc/test paths
risk shaping
classify risk and uncertainty
result shape
structured consequence result

6.5 assemble(input)

Requirement
Behavior
retrieval
invoke scoring specification if query-driven
policy filtering
enforce output-mode trust rules
template application
honor requested template
provenance mode
attach according to template and mode
output
return rendered text plus atom/provenance references

7. Mutation resolver behavior


7.1 createRelationEdge

Requirement
Behavior
ontology validation
relation type must be canonical or approved
endpoint validation
source and target must exist
provenance capture
mutation should record actor/time/provenance
policy enforcement
restricted by access and trust rules

7.2 importAnalysisBundle

Requirement
Behavior
schema validation
envelope must satisfy import contract
normalization membrane
MUST be applied
output
return AnalysisRunAtom and imported object references
trust state
imported objects enter with imported/machine-derived states, not accepted automatically

8. Error contract


Resolvers SHOULD classify errors into stable categories.

Error class
Meaning
NOT_FOUND
no such object exists
UNAUTHORIZED
caller lacks access
FILTERED_BY_POLICY
object exists but is not eligible under requested mode
INVALID_INPUT
malformed request
AMBIGUOUS_QUERY
request resolves to multiple incompatible anchors
INCOMPLETE_TRACE
result exists but graph path is incomplete
IMPORT_REJECTED
analysis bundle failed schema or trust checks

9. Performance and batching rules

Rule ID
Requirement
RCS-P-01
resolvers SHOULD batch related object fetches
RCS-P-02
resolvers SHOULD avoid N+1 graph traversals where possible
RCS-P-03
ranked collection queries SHOULD cap candidate pools before expensive deep expansion
RCS-P-04
provenance expansion SHOULD be lazy unless requested or required by mode

10. Final normative judgment


A valid resolver implementation MUST behave as a disciplined orchestration layer over the authoritative substrate. It MUST respect ontology, trust, provenance, and history semantics, and SHOULD expose enough explanation to make ranked retrieval and trace behavior auditable.



Recommended Immediate Next Set


The highest-value next drafting cluster is now:

Priority
Artifact
1
Query Pattern Library v1
2
Auth and Access Model v1
3
Portal Projection Data Model v1
4
Pilot Intake SOP v1
5
Review Workflow SOP v1

At this point, the architecture stack is coherent enough that the next phase is less about ontology invention and more about operationalizing query behavior, access control, and workflow discipline.