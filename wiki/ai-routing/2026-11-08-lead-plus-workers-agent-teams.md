---
title: "Lead plus cheap workers: routing inside a coding-agent team (Cohere, AI Engineer)"
date: 2026-11-08
source: https://youtube.com/watch?v=maitMe9HCvw
raw: ../../raw/youtube/2026-11-07.json
tags: [routing, multi-agent, coding-agents, cost, harness]
---

# Frontier lead, cheaper workers: ~70% lower cost for close to all-frontier results

**TL;DR.** Nouha Dziri (Cohere) presented hundreds of experiments on teams of coding agents on ProgramBench and Commit0. A lead agent splits the work and workers explore, build and check in parallel. Teams can beat one agent on long software tasks but cost several times more. Three rules decide where extra workers pay off: delegate only the stage where the task is stuck; use a lead that waits for its workers instead of running ahead; and pair a strong lead with cheaper planning workers. That last pairing gets close to an all-frontier team at about 70% lower cost. Source is the talk description; no paper was captured.

<div class="dg-title">Only the lead needs to be expensive</div>
<div class="dg-sub">The routing decision happens inside the harness, per role, not per query at an API gateway.</div>

```mermaid
flowchart LR
  T["Task<br/><small>long software job</small>"] --> L["Frontier lead<br/><small>splits work, waits</small>"]
  L --> G{"Stuck stage?<br/><small>delegate only here</small>"}
  G -->|yes| W["Cheap workers<br/><small>plan, explore, check</small>"]
  G -->|no| L
  W --> L
  L --> O["Result<br/><small>about 70% lower cost</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class T input
  class L,W core
  class G loop
  class O exit
  linkStyle 1 stroke:#f08c00,stroke-width:2px
  linkStyle 5 stroke:#2f9e44,stroke-width:2px
```

<div class="dg-legend">Blue is the task, purple are models, amber is the delegation gate, green is the outcome.</div>

## Relation to prior wiki pages

- **Routing by role is now a pattern.** Claude Code moved background status updates to Haiku 5.5 for ~99% lower cost per update (11-07). Drex (11-07, [summary](2026-11-07-drex-open-decision-model-family.md)) answers bounded choices with a 27B model at ~1/170 the cost. HKU's AgentPilot (11-07) lets a 9B model steer a frontier coder. Cohere's result is the fourth instance in a week of routing by *role inside the loop* rather than by *query difficulty at the gateway*.
- **Same week, same message from harness work.** Hugging Face found "same open model, different harness, very different results" and shipped "harness adapters" ([@Thom_Wolf](https://x.com/Thom_Wolf/status/2118863053001531676)). Garry Tan removed a skill because Opus 5.5 does it better unaided. The harness, not the model string, sets cost.
- **Open question.** The 70% figure has no published per-benchmark breakdown. Whether "delegate the stuck stage" can be detected automatically (a learned gate) is the routing research question.

Concept page: [llm-routing](llm-routing.md).
