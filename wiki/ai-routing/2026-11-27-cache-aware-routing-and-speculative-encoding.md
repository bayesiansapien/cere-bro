---
title: "Cache-aware routing and speculative encoding: the router decides whether you pay prefill again"
date: 2026-11-27
source: https://x.com/akshay_pachaar/status/2125947339739378081
source2: https://x.com/omarsar0/status/2125995984035438717
raw: ../../raw/twitter/feed/2026-11-26-evening-ranked.json
tags: [llm-routing, prefix-cache, kv-cache, load-balancing, cross-model-kv]
signal: X Following feed (practitioner explainers, two independent threads) + Google Antigravity number
---

# Cache-aware routing and speculative encoding

**TL;DR.** Two practitioner threads landed on the same point within hours: in a multi-replica deployment, each replica keeps its own KV cache, so a load balancer that ignores caches sends a follow-up agent turn to the right replica only about 1/N of the time (12.5% with 8 workers). The rest re-prefill the whole system prompt, tools and history. Google's Antigravity team gave the anchor number: 4.5% more cache hits for Neon meant 28% more tasks within quota. Separately, Elvis Saravia pointed to "speculative encoding", which translates one model's cached representation of a context into an approximate cache another model can use, the missing piece for routing between models mid-task.

<div class="dg-title">The busy replica with the cache beats the idle one without it</div>
<div class="dg-sub">Cache-aware routers score remaining prefill plus load, not load alone.</div>

```mermaid
flowchart LR
  Q["Agent turn<br/><small>long shared prefix</small>"] --> R["Router<br/><small>hash prefix blocks</small>"]
  R -->|cache hit| A["Replica A<br/><small>busy, prefix cached</small>"]
  R -->|load only| B["Replica B<br/><small>idle, cold cache</small>"]
  A --> O["Fast first token<br/><small>decode only</small>"]
  B --> P["Full prefill<br/><small>system, tools, history</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class Q input
  class R loop
  class A,B core
  class O exit
  class P err
  linkStyle 1 stroke:#2f9e44,stroke-width:2px
  linkStyle 2 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the request, amber is the routing decision, purple is a replica, green is the cheap path, red is the re-prefill cost.</div>

## Key points

- **Ladder of fixes** (Pachaar): prefix affinity (same client to same worker; one heavy client overloads it), consistent hashing on a session key or prompt start, then full prefix-aware routing that tracks hashed prompt blocks and cache add/evict events from workers and scores both remaining prefill work and current load.
- **Worked example** (Chawla): three replicas, least-busy balancing, high time-to-first-token for agent traffic. The answer is that the balancer ignores which replica holds the prefix.
- **Google's number**: +4.5% cache hit rate for Neon in Antigravity, which Google says means 28% more tasks within quota. Google did not say how.
- **Speculative encoding** (Saravia, paper not linked in capture): one model reads a long context once; its internal state is translated into an approximate cache another model can read. Open questions: end-to-end savings over a workflow, quality drift across repeated handoffs, when translation costs more than prefill.

## How it relates to prior wiki pages

- **Confirms** [11-14 prefix-cache metastability](../inference-efficiency/2026-11-14-prefix-cache-metastability-bursts.md) and [11-17 agent-session cache discipline](../inference-efficiency/2026-11-17-agent-sessions-prefix-cache-discipline.md): agent cost is mostly prefill locality.
- **Gap-filling for routing.** The [llm-routing](llm-routing.md) page has treated model choice and cache placement as separate problems. A router that moves a long task to a cheaper model throws the cache away. Speculative encoding plus Stanford Hazy Research's result reported the same day (one rotation plus a global scale lets one LLM read another's hidden states, across 12 base models) are the first hints that cross-model cache reuse is possible.
- **Tension** with NVIDIA's model-driven compaction ([11-27](../agentic-systems/2026-11-27-model-driven-context-management.md)): edits break prefix hashes at the edit point.

## Gaps

All practitioner explainers; the speculative encoding and Hazy Research papers were not captured with links or numbers.

Related: [llm-routing](llm-routing.md) · [kv-cache](../inference-efficiency/kv-cache.md)
