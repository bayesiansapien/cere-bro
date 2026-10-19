---
date: 2026-10-19
type: source-summary
topic: inference-efficiency
sources:
  - raw/twitter/feed/2026-10-18-evening-233002-ranked.json
  - raw/twitter/feed/2026-10-19-afternoon-ranked.json
  - https://arxiv.org/abs/2610.21375
  - https://academy.dair.ai/papers/memorilla-latent-semantic-memory-for-llms-2610.21375
---

# Memorilla: a whole document collection in 16 memory tokens

**TL;DR.** Long context is expensive because every retrieved document is paid for again in prefill and stored again in the KV cache (the saved attention keys and values for every token in context). Memorilla (Stanford and Toronto) encodes each document once into reusable embeddings. For each query, a learned module reads across the whole collection and writes what matters into just 16 "memory tokens" placed in a frozen LLM's input embedding space. On FactKG it scores 84.33% against 80.43% with the full documents in context, while using 108x fewer tokens for the source material. It beats Mem0, MemoRAG and other baselines on five of eight benchmarks. Used as agent memory over the agent's own history in TextWorld, success rises from 18.6% to 24.2% and the agent revisits fewer rooms. Surfaced by DAIR Academy and Elvis Saravia on X.

<div class="dg-title">Encode once, read 16 tokens per query</div>
<div class="dg-sub">The frozen LLM never sees the documents, only a query-specific 16-token summary in its own embedding space.</div>

```mermaid
flowchart LR
  D["Documents<br/><small>encoded once, reused</small>"] --> E["Memory bank<br/><small>stored embeddings</small>"]
  Q["Query<br/><small>user or agent step</small>"] --> W["Writer module<br/><small>gathers across bank</small>"]
  E --> W
  W --> M["16 memory tokens<br/><small>108x fewer than docs</small>"]
  M --> L["Frozen LLM<br/><small>weights untouched</small>"]
  L --> A["Answer<br/><small>84.3% vs 80.4% full</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class D,Q,E input
  class W loop
  class M,A exit
  class L core
  linkStyle 3 stroke:#2f9e44,stroke-width:2px
```

<div class="dg-legend">Blue is stored and incoming data, amber is the learned writer, purple is the frozen model, green is the compressed memory and the answer.</div>

## Key findings

- **16 tokens beat full context on FactKG** (84.33% vs 80.43%) with 108x fewer source tokens.
- **Five of eight benchmarks** won against Mem0, MemoRAG and other memory baselines.
- **Agent memory works too:** TextWorld success 18.6% to 24.2% when the collection is the agent's own trajectory.
- The base LLM stays **frozen**. Only the writer is trained, so the method plugs into an existing model.

## Relation to prior wiki pages

- **A third route** next to the two the [parametric-context-internalization](parametric-context-internalization.md) page tracks. That page separates compressing tokens and caching smarter from putting context into weights through a predicted adapter. Memorilla compresses into soft input tokens per query: no weight change, no KV eviction.
- **Extends** the [kv-cache](kv-cache.md) thread "never build the long cache" (10-07): the cheapest cache is the one that is never built. Here the whole collection costs 16 positions of KV.
- **Pairs with** Amazon's FEB-30 (same window, [agent shorts](../agentic-systems/2026-10-19-agent-shorts-memory-audit-data-world.md)), which shows QA scores hide whether a memory store holds the right facts. Memorilla is evaluated on QA, so the same caution applies.

## Gaps

No exact-recall or needle tests reported in the material seen, which is where soft-prompt compression usually breaks. No latency or writer cost per query. FactKG favors fact verification, where a summary may beat noisy full text.
