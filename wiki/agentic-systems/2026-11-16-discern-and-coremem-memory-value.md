---
title: "DISCERN and CoReMem: agent memory that resolves at read time and pays for itself"
date: 2026-11-16
arxiv: [2611.15729, 2611.17316]
source: DAIR Academy (AI Papers of the Week, Nov 11-12 2026) + Kurate cs.AI #18 (DISCERN)
topic: agentic-systems
---

# DISCERN and CoReMem

Two memory papers from DAIR's week. DISCERN is also on this week's Kurate cs.AI top 20 (#18), so it is cross-source confirmed (Kurate + DAIR).

## DISCERN (Amazon, 2611.15729): preserve at write, resolve at read

**TL;DR.** Chirag Ahuja, Vladislav Tanov, Ramcharan Kakarla and Jonathan Taws argue persistent agent memory fails on *resolution*, not retrieval. On ENT-310 (a synthetic enterprise sales-agent benchmark, 310 queries, 100 unanswerable), a plain RAG reader already matches strong memory systems on recall. Retention and currency scores sit at 0.93-0.98 for every competent system. What stays hard: which entity a query means, which time-state is current, and whether to answer at all. DISCERN writes to an append-only bi-temporal provenance graph (each fact carries when it was true and when it was recorded) that never merges look-alike entities and never drops superseded values. Reads run an agent loop over zero-LLM tools that must end in one of four actions: answer, update, clarify or abstain.

- Abstention F1 0.924 vs at most 0.802 across eight baselines.
- Macro answer correctness 0.861 vs 0.806. Entity resolution 0.800, where no baseline passes 0.40.
- On LoCoMo with zero tuning it still leads, 0.663 vs 0.638.

## CoReMem (Yale, 2611.17316): keep only memory that measurably helps the next task

**TL;DR.** Peiwen Li and colleagues study coding agents solving successive issues on the same evolving repository. Memory must be written before the next task is known. CoReMem runs the next task with and without each trajectory segment (prospective valuation) and keeps a compact memory built around *anchors*: repository locations and executable checks. An RL stage then rewards resolution, penalizes steps in successful runs, and credits steps that actually used memory-supplied anchors. On ChainSWE, the 27B agent's resolve rate goes from 21.0% to 25.7% with 17% fewer steps and 11% fewer total cache-aware tokens, memory calls included.

<div class="dg-title">Memory earns its place by changing the outcome</div>
<div class="dg-sub">DISCERN keeps everything and decides at read time. CoReMem keeps only what a counterfactual run proves useful.</div>

```mermaid
flowchart LR
  T["Trajectory<br/><small>past sessions or tasks</small>"] --> W["Write rule<br/><small>append-only or valued</small>"]
  W --> G["Memory store<br/><small>graph or anchors</small>"]
  Q["New query<br/><small>or next task</small>"] --> R["Read loop<br/><small>zero-LLM tools</small>"]
  G --> R
  R -->|enough evidence| A["Answer<br/><small>or act on anchor</small>"]
  R -->|ambiguous| X["Clarify or abstain<br/><small>no guess</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class T,Q input
  class W,R loop
  class G core
  class A exit
  class X err
  linkStyle 5 stroke:#2f9e44,stroke-width:2px
  linkStyle 6 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is input, amber is a write or read decision, purple is the store, green is a committed answer, red is a deliberate refusal to guess.</div>

## How they relate to prior wiki pages

- **N-of-a-kind: counterfactual memory valuation.** [MemCredit](2026-11-15-memcredit-decision-utility-memory.md) (11-15) values each memory by whether removing it changes the next action and cut memory tokens 74.5%. CoReMem values each trajectory segment by running the next task with and without it. [Cleaning an Agent's History](2026-11-16-cleaning-history-world-state.md) (today) freezes the agent and edits one thing. Three papers in two days measure memory by intervention, not similarity.
- **Confirms** the 10-27/10-28 "raw history is a strong baseline" results ([memory tax](2026-10-28-memory-tax-and-cheap-checks.md)). DISCERN shows recall is saturated and moves the problem to disambiguation and abstention.
- **Extends** WikiTrace (11-12, which links each stored lesson to its raw trajectory). DISCERN's never-merge, never-drop rule is the same evidence-first stance applied to entities and time.

## Gaps

- DISCERN's main benchmark is synthetic and built by the authors. Judging uses a four-LLM council, not humans.
- CoReMem's prospective valuation needs extra runs of the next task at training time. Its cost is not reported next to the 11% token saving.

## Links

- DISCERN: https://arxiv.org/abs/2611.15729 · CoReMem: https://arxiv.org/abs/2611.17316
- Raw: `raw/dair/2026-11-16-123502-dair-academy.md` · `raw/kurate/2026-11-16-cs-ai.md`
- Concepts: [agent-memory](agent-memory.md)
