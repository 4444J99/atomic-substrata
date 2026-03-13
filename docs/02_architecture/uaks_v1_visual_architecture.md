---
title: "UAKS v1 Visual Architecture"
artifact_id: docs::02_architecture::uaks_v1_visual_architecture.md
pair_id: CHATPAIR-007
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1. Visual Architecture Diagram


UAKS-v1 with Source, Code, and External Analysis Lanes


┌──────────────────────────────────────────────────────────────────────────────┐
│                             UNIFIED ATOMIC SYSTEM                           │
│                     Unified Atomic Knowledge Substrate v1                   │
└──────────────────────────────────────────────────────────────────────────────┘

  SOURCE DOMAIN                                    ANALYSIS DOMAIN
  ─────────────                                    ───────────────

  Raw Conversations                                External Linguistic / Analytical System
  Documents                                        ┌──────────────────────────────────────┐
  Notes                                            │ discourse analysis                   │
  Code Repositories                               │ semantic drift                       │
  Config / Schemas                                │ rhetoric / syntax                    │
  Browser Captures                                │ ontology extraction                  │
  Media-Derived Text                              │ signature / motif detection          │
       │                                          └──────────────────────────────────────┘
       │                                                         │
       ▼                                                         ▼
┌──────────────────────┐                               ┌──────────────────────┐
│  Source Intake Layer │                               │ Analytical Export    │
│  register            │                               │ Bundle Publisher     │
│  fingerprint         │                               │ structured findings  │
│  classify            │                               │ run metadata         │
│  archive reference   │                               │ source scope         │
└──────────────────────┘                               └──────────────────────┘
       │                                                         │
       ├──────────────────────────────┐                          │
       │                              │                          ▼
       ▼                              ▼               ┌────────────────────────┐
┌──────────────────────┐   ┌──────────────────────┐   │ Normalization Membrane │
│   Text Refinery      │   │    Code Refinery     │   │ map external schema    │
│ segment              │   │ parse AST            │   │ assign atom classes    │
│ extract entities     │   │ extract symbols      │   │ resolve source refs    │
│ distill propositions │   │ build dep graph      │   │ create provenance      │
│ type text atoms      │   │ type code atoms      │   │ set trust state        │
└──────────────────────┘   └──────────────────────┘   └────────────────────────┘
       │                              │                          │
       ▼                              ▼                          ▼
┌──────────────────────┐   ┌──────────────────────┐   ┌────────────────────────┐
│     TextAtoms        │   │      CodeAtoms       │   │     AnalysisAtoms      │
│ requirements         │   │ functions            │   │ observations           │
│ policies             │   │ methods              │   │ interpretations        │
│ evidence             │   │ modules              │   │ metrics                │
│ documentation        │   │ tests/config/schema  │   │ drift/signatures       │
└──────────────────────┘   └──────────────────────┘   └────────────────────────┘
       └──────────────────────────────┬──────────────────────────┘
                                      ▼
                         ┌────────────────────────────┐
                         │   Atomic Graph Substrate   │
                         │ atoms                      │
                         │ entities                   │
                         │ typed relations            │
                         │ provenance edges           │
                         │ supersession chains        │
                         │ contradiction edges        │
                         └────────────────────────────┘
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────────┐
│    Vector Substrate  │  │       CAS Store      │  │    Raw Source Archive    │
│ semantic embeddings  │  │ immutable payloads   │  │ untouched originals      │
│ hybrid retrieval     │  │ content hashes       │  │ re-refinement anchor     │
└──────────────────────┘  └──────────────────────┘  └──────────────────────────┘
             │                        │                        │
             └────────────────────────┴────────────────────────┘
                                      ▼
                         ┌────────────────────────────┐
                         │     Governance Layer       │
                         │ validation states          │
                         │ trust weighting            │
                         │ review workflows           │
                         │ policy enforcement         │
                         └────────────────────────────┘
                                      │
                                      ▼
                         ┌────────────────────────────┐
                         │      Assembly Engine       │
                         │ scope resolution           │
                         │ atom selection             │
                         │ template application       │
                         │ connective synthesis       │
                         │ recipe persistence         │
                         └────────────────────────────┘
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────────┐
│  Summaries           │  │ Technical Specs      │  │ Trace / Impact Reports   │
│  Briefings           │  │ Documentation        │  │ Policy-Code Drift        │
│  Memos               │  │ Walkthroughs         │  │ Research Assemblies      │
└──────────────────────┘  └──────────────────────┘  └──────────────────────────┘
                                      │
                                      ▼
                         ┌────────────────────────────┐
                         │      GraphQL API Layer     │
                         │ typed query surface        │
                         │ portal projections         │
                         │ clients / CLI / web        │
                         └────────────────────────────┘
