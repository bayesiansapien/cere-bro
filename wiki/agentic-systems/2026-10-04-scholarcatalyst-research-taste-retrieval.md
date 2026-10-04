---
title: "ScholarCatalyst: can agents find the paper that unlocks your project?"
date: 2026-10-04
sources:
  - https://arxiv.org/abs/2610.02202
tags: [agent-benchmarks, research-agents, retrieval, research-taste]
---

# ScholarCatalyst: a benchmark for research taste

**TL;DR.** Stanford, UW, CMU, AI2, MIT and SNU (Kim, Lee, Neubig, Koh, Khattab, Choi, Finn and others; arXiv 2610.02202) asked **184 lead authors of 207 recent CS papers** to label which earlier papers did, or could have, advanced their project, each with a rationale. The task: given the research question as it stood *before* the project, retrieve those "catalyst papers" from the literature available at the time. **Agentic search does no better than plain embedding retrieval (0.42 vs 0.48 Recall@20)**, even though the agent calls that same retriever as a tool. An agent on Claude Fable 5.1, which may have seen the finished papers in training, reaches only **0.51**.

<div class="dg-title">The agent adds steps but not taste</div>
<div class="dg-sub">Wrapping the retriever in an agent loop lowered recall.</div>

```mermaid
flowchart LR
  Q["Early question<br/><small>pre-result framing</small>"] --> E["Embedding search<br/><small>R@20 0.48</small>"]
  Q --> A["Agentic search<br/><small>same retriever as tool</small>"]
  A --> R1["R@20 0.42<br/><small>worse than tool alone</small>"]
  Q --> F["Fable 5.1 agent<br/><small>may have seen answers</small>"]
  F --> R2["R@20 0.51<br/><small>far from saturated</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class Q input
  class E,A,F core
  class R1 err
  class R2 exit
```

<div class="dg-legend">Blue is the query, purple the retrieval systems, red the regression, green the best (still low) score.</div>

## How this relates to prior wiki pages

- **Same finding as Taste-Bench (09-23)**, where the best frontier model chose the better research fork 59.7% of the time and more reasoning budget did not help ([page](2026-09-23-taste-bench-tasteful-agent.md)). Two independent benchmarks now say research judgment is the bottleneck for auto-research agents, not tool access.
- **Cost angle:** the agent loop spent more tokens for lower recall. A harness that adds steps without adding judgment is pure cost, the HarnessTax (09-22) lesson in a new domain. See [agent-benchmarks](agent-benchmarks.md).

**Raw source:** X Following feed, 2026-10-03 ([@yoonholeee](https://x.com/yoonholeee/status/2106036734798725577)).
