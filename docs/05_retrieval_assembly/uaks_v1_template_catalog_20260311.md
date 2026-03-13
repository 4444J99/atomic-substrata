---
title: "Template Catalog v1"
artifact_id: uaks_v1_template_catalog_20260311
pair_id: CHATPAIR-011
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
