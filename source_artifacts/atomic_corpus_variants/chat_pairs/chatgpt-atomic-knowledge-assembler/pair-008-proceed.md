---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 8
prompt_title: "Proceed"
response_title: "Schema Pack v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "f2b0c68ed4393c05576ace4ca282912740c1b929579f46654225fbeb248256ee"
---

# Pair 008

## Prompt

Proceed

## Response

Schema Pack v1


Unified Atomic Knowledge Substrate


Machine-Oriented Core Type System


Document ID: uaks_v1_schema_pack_20260311
Version: 1.0-draft
Status: Draft implementation schema pack


This schema pack converts the ontology charter and API contract into an implementation-facing object model. It is written as a technology-neutral specification, with JSON-like field definitions and constraints. The intent is to provide a stable substrate that can later be rendered as JSON Schema, TypeScript types, GraphQL-backed resolvers, relational migrations, graph node/edge models, and validation contracts.



1. Schema Pack Scope


This pack defines the canonical structures for:

Schema Group
Included
Base substrate
Atom, Entity, RelationEdge, SourceObject, ProvenanceRecord
Primary atomic domain
TextAtom, CodeAtom, EvidenceAtom, PolicyAtom, RecipeAtom, RelationAtom
Analytical derivative domain
AnalysisAtom, ObservationAtom, InterpretationAtom, MetricAtom, TaxonomyProposalAtom, SignatureAtom, DriftAtom, AnalysisRunAtom
Governance domain
ValidationEvent, TrustPolicyBinding
Assembly domain
Recipe, TemplateRef, AssemblyRequest, AssemblyResult
CAS domain
CASObject
Import domain
AnalysisImportEnvelope, AnalysisImportFinding
Utility domain
Span, TimeWindow, ScopeDescriptor, ConfidenceDescriptor


2. Canonical Enumerations


2.1 AtomType


[
  "TEXT",
  "CODE",
  "EVIDENCE",
  "POLICY",
  "RELATION",
  "RECIPE",
  "ANALYSIS",
  "OBSERVATION",
  "INTERPRETATION",
  "METRIC",
  "TAXONOMY_PROPOSAL",
  "SIGNATURE",
  "DRIFT",
  "ANALYSIS_RUN"
]


2.2 AtomClass


[
  "AXIOM",
  "FACT",
  "RULE",
  "PROCEDURE",
  "EVIDENCE",
  "INTERPRETATION",
  "INTERFACE",
  "DEPENDENCY",
  "TEST",
  "RECIPE",
  "ANALYSIS",
  "METRIC",
  "SIGNATURE",
  "DRIFT",
  "TAXONOMY"
]


2.3 ValidationState


[
  "DRAFT",
  "DISTILLED",
  "REVIEWED",
  "VERIFIED",
  "DEPRECATED",
  "DISPUTED",
  "IMPORTED",
  "MACHINE_DERIVED",
  "ACCEPTED",
  "EXPERIMENTAL"
]


2.4 TextKind


[
  "NOTE",
  "REQUIREMENT",
  "POLICY",
  "TRANSCRIPT_CLAIM",
  "DOCUMENTATION_CLAUSE",
  "EVIDENCE_FRAGMENT",
  "SUMMARY_STATEMENT"
]


2.5 CodeKind


[
  "FUNCTION",
  "METHOD",
  "CLASS",
  "MODULE",
  "CONFIG",
  "QUERY",
  "SCRIPT_STEP",
  "TEST_CASE",
  "SCHEMA_UNIT",
  "UI_COMPONENT",
  "INFRA_UNIT"
]


2.6 SideEffectProfile


[
  "PURE",
  "READ_ONLY",
  "WRITE",
  "NETWORK",
  "FILESYSTEM",
  "EXTERNAL"
]


2.7 RelationType


[
  "DERIVED_FROM",
  "SUPPORTED_BY",
  "CONTRADICTS",
  "SUPERSEDES",
  "USES_ENTITY",
  "ASSEMBLED_IN",
  "REFINES",
  "IMPLEMENTS",
  "DOCUMENTS",
  "TESTS",
  "AFFECTS",
  "EXPOSES_INTERFACE",
  "ANALYZES",
  "MAPS_TO",
  "CHARACTERIZES",
  "DETECTS_DRIFT_IN",
  "PROPOSES_TAXONOMY_FOR",
  "REQUIRES_REVIEW_OF",
  "IS_SUPERSEDED_BY",
  "DEPENDS_ON"
]


2.8 EntityType


[
  "PERSON",
  "ORGANIZATION",
  "PROJECT",
  "REPOSITORY",
  "MODULE",
  "SERVICE",
  "INTERFACE",
  "POLICY_DOMAIN",
  "CONCEPT",
  "TERM",
  "TOPIC",
  "DATASET",
  "ARTIFACT",
  "ENVIRONMENT",
  "TIME_WINDOW"
]


2.9 ResolutionLevel


[
  "MICRO",
  "COMPACT",
  "STANDARD",
  "EXTENDED",
  "DEEP"
]



3. Utility Schemas


3.1 Span


A span identifies a precise location within a source or code artifact.


{
  "type": "object",
  "name": "Span",
  "required": ["locatorType", "start", "end"],
  "properties": {
    "locatorType": {
      "type": "string",
      "enum": ["LINE_COLUMN", "BYTE_OFFSET", "TOKEN_RANGE", "AST_PATH", "TIME_OFFSET"]
    },
    "start": {
      "type": "object",
      "required": ["value"],
      "properties": {
        "line": { "type": "integer" },
        "column": { "type": "integer" },
        "byte": { "type": "integer" },
        "token": { "type": "integer" },
        "value": { "type": "string" }
      }
    },
    "end": {
      "type": "object",
      "required": ["value"],
      "properties": {
        "line": { "type": "integer" },
        "column": { "type": "integer" },
        "byte": { "type": "integer" },
        "token": { "type": "integer" },
        "value": { "type": "string" }
      }
    },
    "displayText": { "type": "string" }
  }
}


3.2 TimeWindow


{
  "type": "object",
  "name": "TimeWindow",
  "required": ["start", "end"],
  "properties": {
    "start": { "type": "string", "format": "date-time" },
    "end": { "type": "string", "format": "date-time" },
    "label": { "type": "string" }
  }
}


3.3 ConfidenceDescriptor


{
  "type": "object",
  "name": "ConfidenceDescriptor",
  "required": ["score"],
  "properties": {
    "score": { "type": "number", "minimum": 0, "maximum": 1 },
    "method": { "type": "string" },
    "label": { "type": "string" }
  }
}


3.4 ScopeDescriptor


{
  "type": "object",
  "name": "ScopeDescriptor",
  "required": [],
  "properties": {
    "projectIds": { "type": "array", "items": { "type": "string" } },
    "repositoryIds": { "type": "array", "items": { "type": "string" } },
    "sourceIds": { "type": "array", "items": { "type": "string" } },
    "entityIds": { "type": "array", "items": { "type": "string" } },
    "authorIds": { "type": "array", "items": { "type": "string" } },
    "timeWindow": { "$ref": "TimeWindow" },
    "labels": { "type": "array", "items": { "type": "string" } }
  }
}



4. Base Schemas


4.1 SourceObject


{
  "type": "object",
  "name": "SourceObject",
  "required": [
    "sourceId",
    "sourceType",
    "origin",
    "ingestedAt",
    "checksum",
    "mimeType",
    "rawArchiveRef"
  ],
  "properties": {
    "sourceId": { "type": "string" },
    "sourceType": { "type": "string" },
    "origin": { "type": "string" },
    "ingestedAt": { "type": "string", "format": "date-time" },
    "checksum": { "type": "string" },
    "mimeType": { "type": "string" },
    "authorRef": { "type": "string" },
    "rightsClass": { "type": "string" },
    "rawArchiveRef": { "type": "string" },
    "metadata": { "type": "object" }
  }
}


4.2 CASObject


{
  "type": "object",
  "name": "CASObject",
  "required": [
    "casRef",
    "contentHash",
    "contentType",
    "canonicalizationVersion",
    "byteSize",
    "createdAt",
    "storageLocation"
  ],
  "properties": {
    "casRef": { "type": "string" },
    "contentHash": { "type": "string" },
    "contentType": { "type": "string" },
    "canonicalizationVersion": { "type": "string" },
    "byteSize": { "type": "integer", "minimum": 0 },
    "createdAt": { "type": "string", "format": "date-time" },
    "storageLocation": { "type": "string" },
    "compression": { "type": "string" },
    "metadata": { "type": "object" }
  }
}


4.3 ProvenanceRecord


{
  "type": "object",
  "name": "ProvenanceRecord",
  "required": [
    "provenanceId",
    "operationType",
    "inputRefs",
    "outputRefs",
    "timestamp"
  ],
  "properties": {
    "provenanceId": { "type": "string" },
    "operationType": { "type": "string" },
    "sourceRef": { "type": "string" },
    "inputRefs": { "type": "array", "items": { "type": "string" } },
    "outputRefs": { "type": "array", "items": { "type": "string" } },
    "operatorRef": { "type": "string" },
    "toolVersion": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "notes": { "type": "string" },
    "analysisRunRef": { "type": "string" },
    "normalizationSchemaVersion": { "type": "string" }
  }
}


4.4 Entity


{
  "type": "object",
  "name": "Entity",
  "required": [
    "entityId",
    "entityType",
    "canonicalName",
    "status",
    "createdAt"
  ],
  "properties": {
    "entityId": { "type": "string" },
    "entityType": {
      "type": "string",
      "enum": [
        "PERSON",
        "ORGANIZATION",
        "PROJECT",
        "REPOSITORY",
        "MODULE",
        "SERVICE",
        "INTERFACE",
        "POLICY_DOMAIN",
        "CONCEPT",
        "TERM",
        "TOPIC",
        "DATASET",
        "ARTIFACT",
        "ENVIRONMENT",
        "TIME_WINDOW"
      ]
    },
    "canonicalName": { "type": "string" },
    "aliases": { "type": "array", "items": { "type": "string" } },
    "description": { "type": "string" },
    "status": { "type": "string" },
    "createdAt": { "type": "string", "format": "date-time" },
    "metadata": { "type": "object" }
  }
}


4.5 RelationEdge


{
  "type": "object",
  "name": "RelationEdge",
  "required": [
    "relationId",
    "relationType",
    "sourceId",
    "targetId",
    "createdAt"
  ],
  "properties": {
    "relationId": { "type": "string" },
    "relationType": {
      "type": "string",
      "enum": [
        "DERIVED_FROM",
        "SUPPORTED_BY",
        "CONTRADICTS",
        "SUPERSEDES",
        "USES_ENTITY",
        "ASSEMBLED_IN",
        "REFINES",
        "IMPLEMENTS",
        "DOCUMENTS",
        "TESTS",
        "AFFECTS",
        "EXPOSES_INTERFACE",
        "ANALYZES",
        "MAPS_TO",
        "CHARACTERIZES",
        "DETECTS_DRIFT_IN",
        "PROPOSES_TAXONOMY_FOR",
        "REQUIRES_REVIEW_OF",
        "IS_SUPERSEDED_BY",
        "DEPENDS_ON"
      ]
    },
    "sourceId": { "type": "string" },
    "targetId": { "type": "string" },
    "confidence": { "$ref": "ConfidenceDescriptor" },
    "createdAt": { "type": "string", "format": "date-time" },
    "provenanceRef": { "type": "string" },
    "metadata": { "type": "object" }
  }
}



5. Abstract Atom Schema


5.1 AtomBase


Every atomic subtype MUST embed this structure.


{
  "type": "object",
  "name": "AtomBase",
  "required": [
    "atomId",
    "atomType",
    "atomClass",
    "contentHash",
    "canonicalPayloadRef",
    "validationState",
    "taxonomyTags",
    "createdAt",
    "updatedAt",
    "status"
  ],
  "properties": {
    "atomId": { "type": "string" },
    "atomType": {
      "type": "string",
      "enum": [
        "TEXT",
        "CODE",
        "EVIDENCE",
        "POLICY",
        "RELATION",
        "RECIPE",
        "ANALYSIS",
        "OBSERVATION",
        "INTERPRETATION",
        "METRIC",
        "TAXONOMY_PROPOSAL",
        "SIGNATURE",
        "DRIFT",
        "ANALYSIS_RUN"
      ]
    },
    "atomClass": {
      "type": "string",
      "enum": [
        "AXIOM",
        "FACT",
        "RULE",
        "PROCEDURE",
        "EVIDENCE",
        "INTERPRETATION",
        "INTERFACE",
        "DEPENDENCY",
        "TEST",
        "RECIPE",
        "ANALYSIS",
        "METRIC",
        "SIGNATURE",
        "DRIFT",
        "TAXONOMY"
      ]
    },
    "contentHash": { "type": "string" },
    "canonicalPayloadRef": { "type": "string" },
    "title": { "type": "string" },
    "sourceRef": { "type": "string" },
    "provenanceRefs": { "type": "array", "items": { "type": "string" } },
    "validationState": {
      "type": "string",
      "enum": [
        "DRAFT",
        "DISTILLED",
        "REVIEWED",
        "VERIFIED",
        "DEPRECATED",
        "DISPUTED",
        "IMPORTED",
        "MACHINE_DERIVED",
        "ACCEPTED",
        "EXPERIMENTAL"
      ]
    },
    "confidence": { "$ref": "ConfidenceDescriptor" },
    "taxonomyTags": { "type": "array", "items": { "type": "string" } },
    "scopeTags": { "type": "array", "items": { "type": "string" } },
    "effectiveFrom": { "type": "string", "format": "date-time" },
    "effectiveTo": { "type": "string", "format": "date-time" },
    "supersedes": { "type": "string" },
    "supersededBy": { "type": "string" },
    "createdAt": { "type": "string", "format": "date-time" },
    "updatedAt": { "type": "string", "format": "date-time" },
    "status": { "type": "string" },
    "metadata": { "type": "object" }
  }
}



6. Primary Atomic Domain Schemas


6.1 TextAtom


{
  "type": "object",
  "name": "TextAtom",
  "extends": "AtomBase",
  "required": [
    "textKind",
    "canonicalStatement",
    "sourceSpan",
    "entitiesMentioned"
  ],
  "properties": {
    "textKind": {
      "type": "string",
      "enum": [
        "NOTE",
        "REQUIREMENT",
        "POLICY",
        "TRANSCRIPT_CLAIM",
        "DOCUMENTATION_CLAUSE",
        "EVIDENCE_FRAGMENT",
        "SUMMARY_STATEMENT"
      ]
    },
    "canonicalStatement": { "type": "string" },
    "sourceSpan": { "$ref": "Span" },
    "claimPolarity": { "type": "string" },
    "temporalTag": { "type": "string" },
    "entitiesMentioned": { "type": "array", "items": { "type": "string" } },
    "evidenceRefs": { "type": "array", "items": { "type": "string" } },
    "contradictionRefs": { "type": "array", "items": { "type": "string" } },
    "parentTextAtomRefs": { "type": "array", "items": { "type": "string" } },
    "childTextAtomRefs": { "type": "array", "items": { "type": "string" } }
  }
}


6.2 EvidenceAtom


{
  "type": "object",
  "name": "EvidenceAtom",
  "extends": "AtomBase",
  "required": [
    "evidenceText",
    "sourceSpan"
  ],
  "properties": {
    "evidenceText": { "type": "string" },
    "sourceSpan": { "$ref": "Span" },
    "evidenceKind": { "type": "string" },
    "measurementValue": { "type": "number" },
    "measurementUnit": { "type": "string" }
  }
}


6.3 PolicyAtom


{
  "type": "object",
  "name": "PolicyAtom",
  "extends": "AtomBase",
  "required": [
    "policyStatement"
  ],
  "properties": {
    "policyStatement": { "type": "string" },
    "policyDomain": { "type": "string" },
    "severity": { "type": "string" },
    "enforcementMode": { "type": "string" }
  }
}


6.4 CodeAtom


{
  "type": "object",
  "name": "CodeAtom",
  "extends": "AtomBase",
  "required": [
    "codeKind",
    "language",
    "astNodeType",
    "modulePath",
    "astSpan",
    "contentAddressRef"
  ],
  "properties": {
    "codeKind": {
      "type": "string",
      "enum": [
        "FUNCTION",
        "METHOD",
        "CLASS",
        "MODULE",
        "CONFIG",
        "QUERY",
        "SCRIPT_STEP",
        "TEST_CASE",
        "SCHEMA_UNIT",
        "UI_COMPONENT",
        "INFRA_UNIT"
      ]
    },
    "language": { "type": "string" },
    "runtime": { "type": "string" },
    "signature": { "type": "object" },
    "astNodeType": { "type": "string" },
    "symbolName": { "type": "string" },
    "modulePath": { "type": "string" },
    "astSpan": { "$ref": "Span" },
    "dependencyRefs": { "type": "array", "items": { "type": "string" } },
    "dependentRefs": { "type": "array", "items": { "type": "string" } },
    "sideEffectProfile": {
      "type": "string",
      "enum": ["PURE", "READ_ONLY", "WRITE", "NETWORK", "FILESYSTEM", "EXTERNAL"]
    },
    "complexityScore": { "type": "number" },
    "testRefs": { "type": "array", "items": { "type": "string" } },
    "buildRefs": { "type": "array", "items": { "type": "string" } },
    "businessRuleRefs": { "type": "array", "items": { "type": "string" } },
    "interfaceContractRef": { "type": "string" },
    "breakingChangeRisk": { "type": "string" },
    "contentAddressRef": { "type": "string" }
  }
}


6.5 RelationAtom


{
  "type": "object",
  "name": "RelationAtom",
  "extends": "AtomBase",
  "required": [
    "relationType",
    "subjectRef",
    "objectRef"
  ],
  "properties": {
    "relationType": { "type": "string" },
    "subjectRef": { "type": "string" },
    "objectRef": { "type": "string" },
    "qualifiers": { "type": "object" },
    "timeScope": { "$ref": "TimeWindow" }
  }
}


6.6 RecipeAtom


{
  "type": "object",
  "name": "RecipeAtom",
  "extends": "AtomBase",
  "required": [
    "recipeType",
    "resolutionLevel",
    "atomSequence",
    "templateRef"
  ],
  "properties": {
    "recipeType": { "type": "string" },
    "resolutionLevel": {
      "type": "string",
      "enum": ["MICRO", "COMPACT", "STANDARD", "EXTENDED", "DEEP"]
    },
    "atomSequence": { "type": "array", "items": { "type": "string" } },
    "templateRef": { "type": "string" },
    "generationRules": { "type": "object" }
  }
}



7. Analytical Derivative Domain Schemas


7.1 AnalysisRunAtom


{
  "type": "object",
  "name": "AnalysisRunAtom",
  "extends": "AtomBase",
  "required": [
    "analysisRunId",
    "analysisType",
    "engineName",
    "sourceScope",
    "timestampProduced"
  ],
  "properties": {
    "analysisRunId": { "type": "string" },
    "analysisType": { "type": "string" },
    "engineName": { "type": "string" },
    "engineVersion": { "type": "string" },
    "method": { "type": "string" },
    "parameters": { "type": "object" },
    "sourceScope": { "$ref": "ScopeDescriptor" },
    "timestampProduced": { "type": "string", "format": "date-time" },
    "ontologyVersion": { "type": "string" },
    "schemaVersion": { "type": "string" }
  }
}


7.2 AnalysisAtom


{
  "type": "object",
  "name": "AnalysisAtom",
  "extends": "AtomBase",
  "required": [
    "findingId",
    "findingKind",
    "findingText"
  ],
  "properties": {
    "findingId": { "type": "string" },
    "findingKind": { "type": "string" },
    "findingText": { "type": "string" },
    "evidenceRefs": { "type": "array", "items": { "type": "string" } },
    "analysisRunRef": { "type": "string" },
    "method": { "type": "string" },
    "externalTags": { "type": "array", "items": { "type": "string" } }
  }
}


7.3 ObservationAtom


{
  "type": "object",
  "name": "ObservationAtom",
  "extends": "AnalysisAtom",
  "required": [
    "observationText"
  ],
  "properties": {
    "observationText": { "type": "string" }
  }
}


7.4 InterpretationAtom


{
  "type": "object",
  "name": "InterpretationAtom",
  "extends": "AnalysisAtom",
  "required": [
    "interpretationText"
  ],
  "properties": {
    "interpretationText": { "type": "string" },
    "dependsOnFindingRefs": { "type": "array", "items": { "type": "string" } }
  }
}


7.5 MetricAtom


{
  "type": "object",
  "name": "MetricAtom",
  "extends": "AnalysisAtom",
  "required": [
    "metricName",
    "metricValue"
  ],
  "properties": {
    "metricName": { "type": "string" },
    "metricValue": { "type": "number" },
    "metricUnit": { "type": "string" },
    "metricContext": { "type": "object" }
  }
}


7.6 TaxonomyProposalAtom


{
  "type": "object",
  "name": "TaxonomyProposalAtom",
  "extends": "AnalysisAtom",
  "required": [
    "proposalText",
    "proposedClasses"
  ],
  "properties": {
    "proposalText": { "type": "string" },
    "proposedClasses": { "type": "array", "items": { "type": "string" } },
    "clusterRefs": { "type": "array", "items": { "type": "string" } }
  }
}


7.7 SignatureAtom


{
  "type": "object",
  "name": "SignatureAtom",
  "extends": "AnalysisAtom",
  "required": [
    "signatureText"
  ],
  "properties": {
    "signatureText": { "type": "string" },
    "patternFamily": { "type": "string" },
    "frequencyScore": { "type": "number" }
  }
}


7.8 DriftAtom


{
  "type": "object",
  "name": "DriftAtom",
  "extends": "AnalysisAtom",
  "required": [
    "driftText",
    "timeWindowA",
    "timeWindowB"
  ],
  "properties": {
    "driftText": { "type": "string" },
    "timeWindowA": { "$ref": "TimeWindow" },
    "timeWindowB": { "$ref": "TimeWindow" },
    "driftDimension": { "type": "string" }
  }
}



8. Governance Schemas


8.1 ValidationEvent


{
  "type": "object",
  "name": "ValidationEvent",
  "required": [
    "validationEventId",
    "targetRef",
    "previousState",
    "newState",
    "timestamp"
  ],
  "properties": {
    "validationEventId": { "type": "string" },
    "targetRef": { "type": "string" },
    "previousState": { "type": "string" },
    "newState": { "type": "string" },
    "actorRef": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "reason": { "type": "string" },
    "notes": { "type": "string" }
  }
}


8.2 TrustPolicyBinding


{
  "type": "object",
  "name": "TrustPolicyBinding",
  "required": [
    "bindingId",
    "targetRef",
    "policyName",
    "appliesFrom"
  ],
  "properties": {
    "bindingId": { "type": "string" },
    "targetRef": { "type": "string" },
    "policyName": { "type": "string" },
    "policyVersion": { "type": "string" },
    "appliesFrom": { "type": "string", "format": "date-time" },
    "appliesTo": { "type": "string", "format": "date-time" },
    "policyPayload": { "type": "object" }
  }
}



9. Assembly Schemas


9.1 Recipe


{
  "type": "object",
  "name": "Recipe",
  "required": [
    "recipeId",
    "recipeType",
    "resolutionLevel",
    "atomSequence",
    "templateRef",
    "createdAt"
  ],
  "properties": {
    "recipeId": { "type": "string" },
    "recipeType": { "type": "string" },
    "resolutionLevel": {
      "type": "string",
      "enum": ["MICRO", "COMPACT", "STANDARD", "EXTENDED", "DEEP"]
    },
    "atomSequence": { "type": "array", "items": { "type": "string" } },
    "templateRef": { "type": "string" },
    "generationRules": { "type": "object" },
    "createdAt": { "type": "string", "format": "date-time" },
    "createdBy": { "type": "string" }
  }
}


9.2 TemplateRef


{
  "type": "object",
  "name": "TemplateRef",
  "required": [
    "templateId",
    "templateName",
    "templateType"
  ],
  "properties": {
    "templateId": { "type": "string" },
    "templateName": { "type": "string" },
    "templateType": { "type": "string" },
    "version": { "type": "string" },
    "rules": { "type": "object" }
  }
}


9.3 AssemblyRequest


{
  "type": "object",
  "name": "AssemblyRequest",
  "required": [
    "templateRef",
    "resolutionLevel"
  ],
  "properties": {
    "requestId": { "type": "string" },
    "query": { "type": "string" },
    "atomIds": { "type": "array", "items": { "type": "string" } },
    "templateRef": { "type": "string" },
    "resolutionLevel": {
      "type": "string",
      "enum": ["MICRO", "COMPACT", "STANDARD", "EXTENDED", "DEEP"]
    },
    "includeAnalysis": { "type": "boolean" },
    "includeExperimental": { "type": "boolean" },
    "scope": { "$ref": "ScopeDescriptor" }
  }
}


9.4 AssemblyResult


{
  "type": "object",
  "name": "AssemblyResult",
  "required": [
    "renderedText",
    "atomIdsUsed",
    "provenanceRefs"
  ],
  "properties": {
    "resultId": { "type": "string" },
    "recipeRef": { "type": "string" },
    "renderedText": { "type": "string" },
    "atomIdsUsed": { "type": "array", "items": { "type": "string" } },
    "provenanceRefs": { "type": "array", "items": { "type": "string" } },
    "warnings": { "type": "array", "items": { "type": "string" } }
  }
}



10. External Analysis Import Schemas


10.1 AnalysisImportFinding


{
  "type": "object",
  "name": "AnalysisImportFinding",
  "required": [
    "findingId",
    "findingKind",
    "findingText"
  ],
  "properties": {
    "findingId": { "type": "string" },
    "findingKind": { "type": "string" },
    "findingText": { "type": "string" },
    "confidence": { "oneOf": [{ "type": "number" }, { "type": "string" }] },
    "evidenceRefs": { "type": "array", "items": { "type": "string" } },
    "tags": { "type": "array", "items": { "type": "string" } },
    "supersedes": { "type": "string" },
    "metrics": { "type": "object" },
    "clusterId": { "type": "string" },
    "timeWindowA": { "$ref": "TimeWindow" },
    "timeWindowB": { "$ref": "TimeWindow" },
    "suggestedRelations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["relationType", "targetId"],
        "properties": {
          "relationType": { "type": "string" },
          "targetId": { "type": "string" },
          "metadata": { "type": "object" }
        }
      }
    }
  }
}


10.2 AnalysisImportEnvelope


{
  "type": "object",
  "name": "AnalysisImportEnvelope",
  "required": [
    "analysisRunId",
    "analysisType",
    "engineName",
    "timestamp",
    "sourceScope",
    "findings",
    "schemaVersion"
  ],
  "properties": {
    "analysisRunId": { "type": "string" },
    "analysisType": { "type": "string" },
    "engineName": { "type": "string" },
    "engineVersion": { "type": "string" },
    "method": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "sourceScope": { "$ref": "ScopeDescriptor" },
    "parameters": { "type": "object" },
    "findings": {
      "type": "array",
      "items": { "$ref": "AnalysisImportFinding" }
    },
    "relations": {
      "type": "array",
      "items": { "$ref": "RelationEdge" }
    },
    "ontologyVersion": { "type": "string" },
    "schemaVersion": { "type": "string" }
  }
}



11. Invariants and Validation Rules


11.1 Global invariants

Invariant ID
Rule
INV-001
Every atom MUST have atomId, atomType, atomClass, contentHash, and canonicalPayloadRef.
INV-002
Every verified or accepted atom MUST have at least one provenance reference.
INV-003
supersedes and supersededBy MUST NOT both point to self.
INV-004
contentHash MUST correspond to an existing CAS object for persisted payloads.
INV-005
Every RelationEdge.sourceId and RelationEdge.targetId MUST resolve to existing IDs.

11.2 Text invariants

Invariant ID
Rule
TXT-001
TextAtom.canonicalStatement MUST be non-empty.
TXT-002
TextAtom.sourceSpan MUST exist.
TXT-003
TextAtom.entitiesMentioned SHOULD resolve where applicable.

11.3 Code invariants

Invariant ID
Rule
CODE-001
CodeAtom.language, CodeAtom.astNodeType, CodeAtom.modulePath, and CodeAtom.astSpan MUST exist.
CODE-002
CodeAtom.contentAddressRef MUST resolve to a CAS object.
CODE-003
CodeAtom.codeKind MUST be one of the defined code categories.

11.4 Analysis invariants

Invariant ID
Rule
AN-001
Every imported analysis object MUST trace back to an AnalysisRunAtom.
AN-002
Analytical objects in ACCEPTED state MUST have analysis provenance and transformation provenance.
AN-003
DriftAtom MUST contain both timeWindowA and timeWindowB.


12. Example Minimal Objects


12.1 Minimal TextAtom


{
  "atomId": "atom_text_001",
  "atomType": "TEXT",
  "atomClass": "FACT",
  "contentHash": "sha256:abc123",
  "canonicalPayloadRef": "cas_001",
  "validationState": "DISTILLED",
  "taxonomyTags": ["documentation", "architecture"],
  "scopeTags": ["uaks_v1"],
  "createdAt": "2026-03-11T15:00:00Z",
  "updatedAt": "2026-03-11T15:00:00Z",
  "status": "ACTIVE",
  "textKind": "DOCUMENTATION_CLAUSE",
  "canonicalStatement": "Documents are assembled projections rather than primary truth objects.",
  "sourceSpan": {
    "locatorType": "LINE_COLUMN",
    "start": { "line": 10, "column": 1, "value": "10:1" },
    "end": { "line": 10, "column": 78, "value": "10:78" },
    "displayText": "L10-L10"
  },
  "entitiesMentioned": []
}


12.2 Minimal CodeAtom


{
  "atomId": "atom_code_001",
  "atomType": "CODE",
  "atomClass": "PROCEDURE",
  "contentHash": "sha256:def456",
  "canonicalPayloadRef": "cas_002",
  "validationState": "DISTILLED",
  "taxonomyTags": ["refinery", "parser"],
  "scopeTags": ["uaks_v1"],
  "createdAt": "2026-03-11T15:00:00Z",
  "updatedAt": "2026-03-11T15:00:00Z",
  "status": "ACTIVE",
  "codeKind": "FUNCTION",
  "language": "python",
  "runtime": "python3.12",
  "astNodeType": "FunctionDef",
  "symbolName": "distill_text_atom",
  "modulePath": "refinery/text/distill.py",
  "astSpan": {
    "locatorType": "LINE_COLUMN",
    "start": { "line": 22, "column": 1, "value": "22:1" },
    "end": { "line": 46, "column": 1, "value": "46:1" },
    "displayText": "L22-L46"
  },
  "contentAddressRef": "cas_code_blob_001"
}


12.3 Minimal AnalysisImportEnvelope


{
  "analysisRunId": "run_001",
  "analysisType": "semantic_drift",
  "engineName": "external_linguistic_engine",
  "timestamp": "2026-03-11T15:00:00Z",
  "sourceScope": {
    "projectIds": ["project_uaks"]
  },
  "findings": [
    {
      "findingId": "finding_001",
      "findingKind": "drift",
      "findingText": "The term 'validation' increasingly refers to governance rather than schema conformance.",
      "confidence": 0.91,
      "tags": ["semantic_drift", "validation"]
    }
  ],
  "schemaVersion": "1.0"
}



13. Implementation Mapping Guidance


This schema pack is technology-neutral, but the intended mapping is straightforward.

Target implementation
Mapping guidance
Graph database
Atoms and entities as nodes, RelationEdge as edges, provenance optionally as nodes
Relational database
Base tables per object family, enum tables optional, relation table normalized
CAS store
canonicalPayloadRef and contentAddressRef map to immutable object records
GraphQL
Types map directly to API contract already drafted
TypeScript
AtomBase becomes a base interface with discriminated unions
JSON Schema
Each object block can be converted into a strict schema file


14. Recommended Next Artifact


The highest-value continuation after the schema pack is:


Text Refinery Specification v1


That is the first place where the abstract model becomes operational, because it defines how raw language is segmented, distilled, typed, deduplicated, and validated into TextAtom, EvidenceAtom, and PolicyAtom.


After that, the correct sequence is:

Order
Next artifact
1
Text Refinery Specification v1
2
Code Refinery Specification v1
3
Graph Relation Catalog v1
4
Validation and Trust Policy v1
5
Assembly Engine Specification v1

I can continue directly into Text Refinery Specification v1.