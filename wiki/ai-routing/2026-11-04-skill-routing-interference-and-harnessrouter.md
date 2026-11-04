# Lifelong skill routing (Skill++) and HarnessRouter / UHP

**Sources:** [Skill++, arXiv 2611.00544](https://arxiv.org/abs/2611.00544) (surfaced by [@dair_ai](https://x.com/dair_ai/status/2117612013258228030) with a DAIR Academy page) · [HarnessRouter repo](https://github.com/HarnessRouter/harnessrouter) (via [@akshay_pachaar](https://x.com/akshay_pachaar/status/2117605592999313843)) · raw: `raw/twitter/feed/2026-11-03-evening-210222-ranked.json`

**TL;DR.** Agents now carry skill libraries. Each skill has a name, a description and a body. Under progressive disclosure, a router (usually the LLM itself) picks skills by name and description alone, then loads only the bodies it picked. As the library grows, a new skill with similar metadata can *displace* an older one. Routing that used to work breaks, even though neither the old skill nor the router changed. Skill++ frames this as lifelong skill routing, a class-incremental continual-learning problem. Its fix touches only metadata. Each incoming skill's name and description are rewritten to say what it supports, how it differs from its closest existing neighbour, and what it excludes. There is no router training and no labelled data. With 731 skills accumulated over ten sessions, the router selects every required skill for 76.3% of queries, against 36.4% with the original metadata. Substitution errors nearly disappear and crowding errors halve. The gains hold across three benchmarks, five routers and the Codex CLI harness.

<div class="dg-title">A new skill can silently steal an old skill's traffic</div>
<div class="dg-sub">The fix is a contrastive description written when the skill is added, not a better router.</div>

```mermaid
flowchart LR
  N["New skill<br/><small>name + description</small>"] --> K["Nearest skill<br/><small>closest existing metadata</small>"]
  K --> W["Rewrite<br/><small>supports, differs, excludes</small>"]
  W --> Lib["Library<br/><small>731 skills, 10 sessions</small>"]
  Q["Query"] --> R{"Router<br/><small>reads metadata only</small>"}
  Lib --> R
  R -->|76.3% full recall| OK["Right skills<br/><small>vs 36.4% before</small>"]
  N -.->|no rewrite| X["Interference<br/><small>substitution, crowding</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class N,Q input
  class K,W core
  class R loop
  class Lib,OK exit
  class X err
  linkStyle 6 stroke:#2f9e44,stroke-width:2px
  linkStyle 7 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is input, purple is the metadata rewrite, amber is the router, green is correct routing, red is the interference failure.</div>

## HarnessRouter / UHP (same evening, practitioner side)

- **What it is.** UHP (Unified Harness Protocol) is an open interface for running a task on *any* agent harness: Codex, Claude Code, Gemini CLI, Hermes, Pi and others. HarnessRouter is the Apache-2.0 server that implements it. The backend sends a task with a `harness_id`. The router starts that harness in its own session, streams progress, and returns files, artifacts and failures through one interface. It supports 30 harness bases.
- **Routing claim.** Its benchmarks say that changing only the harness, with the model fixed, cut cost 25-64% on healthcare-compliance tasks. Changing both harness and model widened the cost spread to 99.8%. This is vendor-reported, but it fits the wiki's growing evidence that the harness is a routing dimension in its own right.

## Relation to prior wiki

- **Extends** [LLM routing](llm-routing.md) from "which model" to "which skill" and "which harness". Routed Continual Learning (FAIR, 11-01) routed each run to a cluster of past trajectories with its own memory. Skill++ adds the failure that every growing routed library must face: additions interfere with old routes. This is the same stability-plasticity tradeoff the 10-27 "Are Self-Evolving Agents Continual Learners?" study measured (r = -0.72 between plasticity and stability).
- **Pairs with** today's continual harness evolution study ([summary](../agentic-systems/2026-11-04-continual-harness-evolution-forgetting.md)), where Meta-Harness went from 94.0% to 32.0% on SWE-Bench after five rounds of evolving on another dataset. Skill++ is a local, metadata-scoped edit, which is exactly the kind of edit that study and EMMA (10-29, one owner per self-edit) suggest is safe.
- **Open:** Skill++ assumes the description matches the body. Public skills often do not, as the paper itself notes. A rewrite made from the body, not the stated description, is the obvious next step.
