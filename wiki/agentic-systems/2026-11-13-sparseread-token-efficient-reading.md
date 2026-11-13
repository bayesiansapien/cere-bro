---
title: "SparseRead: a reading control layer that cuts agent tokens up to 92.9%"
date: 2026-11-13
source: https://arxiv.org/abs/2608.22237
raw: ../../raw/huggingface/2026-11-12-read-less-solve-more-token-efficient-sparse-reading-of-exter.md
tags: [agents, context-engineering, token-efficiency, harness, tool-output]
signal: HuggingFace daily papers (18 upvotes) + HF daily-papers email
---

# SparseRead: read less, solve more

## TL;DR

Agents read whole web pages, files, repos and tool outputs when they need a few lines. That over-reading costs tokens and latency, and it dilutes the evidence the model needs. SparseRead is a layer that sits between the agent and its sources and decides what text is admitted, without touching the model. It has three parts: a Read Intent Protocol that tracks what the agent currently needs and what each source has already covered; Adaptive Reader Backends that pick how to locate and expose evidence (search, outline, slice); and a Budgeted Read Gate that caps the raw text exposed per episode, with a full-view fallback when the sparse view is not enough. Across six models (including Claude Opus 5) and five scenarios it cuts total tokens up to 92.9% and wall time up to 89.0%, preserving or improving quality in 97% of settings. On web deep-search it saves 31 to 43% of tokens and 23 to 37% of time.

<div class="dg-title">The cheapest token is the one the agent never reads</div>
<div class="dg-sub">A gate between the agent and its sources; the model is untouched.</div>

```mermaid
flowchart LR
  A["Agent<br/><small>any model</small>"] --> I["Read intent<br/><small>need and coverage</small>"]
  I --> B["Reader backends<br/><small>search, outline, slice</small>"]
  B --> G{"Budget gate<br/><small>cap per episode</small>"}
  G -->|sparse view| A
  G -->|not enough| F["Full view<br/><small>faithful fallback</small>"]
  F --> A
  X["Sources<br/><small>web, docs, repos, tools</small>"] --> B
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class X input
  class A core
  class I,B,G loop
  class F exit
  linkStyle 3 stroke:#2f9e44,stroke-width:2px
```

<div class="dg-legend">Blue is the raw sources, purple is the agent, amber is the read-control layer, green is the fallback path.</div>

## Key findings

- Token savings come from admission control, not compression: the agent sees less raw text, not a summary of it.
- The fallback keeps it faithful: when the sparse view fails, the full object is still reachable.
- Portable across three agent frameworks; no model changes.

## Gaps

- Savings are largest on scenarios with big objects; on deep search they fall to 31 to 43%.
- No breakdown of how much comes from prompt-cache interplay: a sparse view may break prefix caching that a stable full view would hit.

## How it relates to prior wiki pages

- **Extends** [agent harness engineering](agent-harness-engineering.md): the harness, not the model, controls context cost. It is the read-side cousin of context compaction (Microsoft's CompactionBench, mentioned the same day) and of AWS's Bedrock cost-per-task guidance naming agent-loop turns and verbosity as hidden cost drivers.
- **Connects** to the token-spend data in [agent memory](agent-memory.md) and the 11-12 WikiTrace page: CMU/JetBrains found doubling token spend buys about 10% more commits. Read control is one of the few levers that cuts spend without cutting output.
