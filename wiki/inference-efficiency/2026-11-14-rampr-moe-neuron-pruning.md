---
title: "Understanding MoE beyond expert boundaries: RAMP profiling and RAMPr neuron pruning (Tencent)"
date: 2026-11-14
source: https://arxiv.org/abs/2611.13975
raw: ../../raw/twitter/feed/2026-11-13-evening-210002-ranked.json
tags: [pruning, moe, expert-specialization, neuron-importance, memory, prefill-throughput]
signal: X Following feed (@rohanpaul_ai summary + paper link); arXiv abstract
---

# RAMP and RAMPr: MoE skills live in neurons, not experts (2611.13975)

## TL;DR

Whether MoE experts specialize by domain (math, code) or just by token type has been contested. Tencent looks one level below the expert. **RAMP** (Routing-Aware Magnitude Profiling) scores each neuron by its contribution weighted by how often tokens are routed through it. Neuron sets picked for one domain overlap **58-74%** across different samples of that domain but only **15-24%** across domains, and they are scattered across many experts rather than concentrated in one. Tracing three fully open MoE families through training, neuron importance keeps reorganizing between pre-training checkpoints even while expert-level rankings look stable, and post-training mostly preserves the neuron ranking. **RAMPr** prunes neurons across all experts using RAMP scores with mixed-domain calibration data. At 75% neuron retention it keeps an average **91-98%** of full performance across six models. At 50% retention it cuts resident GPU memory **36-43%** and raises batched prefill throughput **17-39%**.

<div class="dg-title">Prune inside every expert, not whole experts</div>
<div class="dg-sub">Domain skill is spread thin across experts, so the cut has to be neuron-level and balanced across domains.</div>

```mermaid
flowchart LR
  C["Mixed-domain data<br/><small>calibration set</small>"] --> R["RAMP score<br/><small>routed contribution</small>"]
  M["MoE model<br/><small>all experts</small>"] --> R
  R --> D["Domain neuron sets<br/><small>58-74% stable</small>"]
  D --> P["RAMPr selection<br/><small>balanced across domains</small>"]
  P -->|75% kept| Q["91-98% quality<br/><small>six models</small>"]
  P -->|50% kept| G["36-43% less memory<br/><small>17-39% faster prefill</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class C,M input
  class R,D core
  class P loop
  class Q,G exit
```

<div class="dg-legend">Blue is input, purple is the profiling step, amber is the pruning decision, green is the result.</div>

## Relation to prior wiki pages

- **Refines the expert-pruning line on [model-pruning-sparsity](model-pruning-sparsity.md).** Prior MoE compression entries mostly dropped or merged whole experts. RAMPr says that throws away domain neurons scattered through the dropped expert, which explains why expert-level pruning degrades unevenly across domains.
- **Settles part of a debate the wiki has tracked.** Reports of domain-specialized experts and analyses showing routing tracks token identity can both be true: routing is token-shaped at the expert level, while domain skill is organized at the neuron level.
- **Pairs with Inkling's 4-bit expert layers (same day).** Both treat MoE expert layers as the cheapest place to remove cost: one by bits, one by neurons. They should stack, but nobody has measured pruning plus NVFP4 together.

## Open questions

- Throughput gains are for batched prefill. Decode, which is memory-bandwidth-bound, should benefit from the memory cut, but it is not reported in the abstract.
- Pruning is calibrated on a fixed domain mix. A deployment with a different mix may lose the skills it needs most.
