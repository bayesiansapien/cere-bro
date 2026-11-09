---
title: "CHARM+: ring attention that respects the slow link"
date: 2026-11-09
source: https://arxiv.org/abs/2611.05906
raw: ../../raw/kurate/2026-11-09-cs-ai.md
tags: [sequence-parallelism, ring-attention, interconnect, gpu]
signal: Kurate cs.AI #2 (ai_rating 6.0), not on HuggingFace
---

# CHARM+

**TL;DR.** Ring Attention splits a long sequence across GPUs and passes KV blocks around a ring, overlapping each hop with compute. Two things break that overlap: hops depend on each other in sequence, and in mixed topologies (two NUMA sockets over PCIe, or two nodes over a slower link than NVLink inside a node) the slowest link sets the pace for every synchronization. CHARM+ ([arXiv 2611.05906](https://arxiv.org/abs/2611.05906)) reorganizes the sequential ring into levels with parallel communication inside each level, and decouples cross-hardware traffic from intra-hardware traffic, re-merging partial attention results afterward. Against Ring Attention: forward/backward 1.3x/1.7x on dual-NUMA PCIe, 2.8x/2.9x on dual-node NVLink.

<div class="dg-title">Keep the slow link off the critical path</div>
<div class="dg-sub">Fast local rings run freely; cross-node traffic runs on its own stream and merges later.</div>

```mermaid
flowchart LR
  Q["Local Q shard<br/><small>sequence slice</small>"] --> L["Intra-node ring<br/><small>NVLink, fast</small>"]
  Q --> X["Cross-node stream<br/><small>slow link, async</small>"]
  L --> P1["Partial attention<br/><small>local KV blocks</small>"]
  X --> P2["Partial attention<br/><small>remote KV blocks</small>"]
  P1 --> M["Re-merge<br/><small>combine softmax stats</small>"]
  P2 --> M
  M --> O["Output<br/><small>2.8x fwd vs Ring</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class Q input
  class L,X loop
  class P1,P2,M core
  class O exit
```

<div class="dg-legend">Blue is the input shard, amber is communication, purple is attention compute, green is the result.</div>

## Relation to prior wiki
- Same theme as TPUv7's DCP (decode context parallelism that shards KV by position) in SemiAnalysis's AgentX post ([11-06](2026-11-06-tpu-ironwood-agentx-semianalysis.md)): long-context performance is now a communication-topology problem.
- Training-side counterpart to FLAMIA ([11-04](2026-11-04-flamia-microscaling-attention-blackwell.md)), which attacked attention cost inside one Blackwell GPU with microscaling formats.

## Gaps
No comparison to newer topology-aware schemes (USP/Ulysses hybrids, DeepSpeed's tiled variants). No inference (decode) numbers; gains are forward/backward training kernels. Tested on two-domain topologies; behavior at 8+ nodes is not shown.

Concept pages: [GPU kernels](gpu-kernels.md) · [memory hierarchy](memory-hierarchy.md)
