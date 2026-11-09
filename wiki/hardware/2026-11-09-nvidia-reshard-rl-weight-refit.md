---
title: "NVIDIA Reshard: RL weight refit that moves only what changed hands"
date: 2026-11-09
source: https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/
raw: ../../raw/labs/2026-11-08-162141-labs.md
tags: [gpu-optimization, collectives, nccl, rl-training, interconnect]
---

# NVIDIA Reshard collective

**TL;DR.** In RL post-training, every step ends with a *refit*: the trainer's updated weights must reach the inference engine that generates the next rollouts. Today that is an all-gather plus broadcast, moving about 2x the model per step (≈11.2TB for a 2.8T-parameter model in BF16). Reshard treats refit as converting one sharded tensor layout into another (DTensor to DTensor). It sends only the exact shard intersections each receiver needs, and groups replicas by NVLink domain so each byte crosses the slow network once and then fans out over NVLink. In NeMo RL on DGX H100 and GB200 (Qwen3-235B, DeepSeek-V3 671B): 2.7-5.7x faster refit. Hybrid in practice: Reshard for big FFN projections, gather-broadcast for small weights. Open-sourced as NCCL M2N Reshard in NVIDIA/nccl-extensions.

<div class="dg-title">Refit is a layout change, not a broadcast</div>
<div class="dg-sub">Only overlapping shards move, and each crosses the network once.</div>

```mermaid
flowchart LR
  T["Trainer shards<br/><small>FSDP/TP layout</small>"] --> I["Intersect layouts<br/><small>who needs which slice</small>"]
  I --> N["Cross-node send<br/><small>once per NVLink domain</small>"]
  N --> V["NVLink fan-out<br/><small>replicas share locally</small>"]
  V --> G["Inference shards<br/><small>vLLM/TP layout</small>"]
  T -.->|old way| X["All-gather + broadcast<br/><small>~2x model per step</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class T input
  class I loop
  class N,V core
  class G exit
  class X err
```

<div class="dg-legend">Blue is the trainer, amber is the layout planning, purple is communication, green is the inference copy, red is the old cost.</div>

## Relation to prior wiki
- Same move as CHARM+ ([summary](2026-11-09-charm-plus-cross-hardware-ring-attention.md)) the same window: put the slow link off the critical path by separating inter-domain from intra-domain traffic.
- RL post-training at trillion-parameter scale is becoming communication-bound, not FLOP-bound; see [compute economics](compute-economics.md).

Concept page: [GPU kernels](gpu-kernels.md)
