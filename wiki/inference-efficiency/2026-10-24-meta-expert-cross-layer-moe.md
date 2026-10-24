---
source: HuggingFace Daily Papers (2026-10-23) + Kurate cs.AI top-20 (#11)
arxiv_id: 2610.27598
date: 2026-10-24
tags: [moe, compression, parameter-sharing, expert-redundancy]
raw: raw/huggingface/2026-10-23-meta-expert-cross-layer-expert-sharing-for-storage-and-retrieval-efficien.md, raw/kurate/2026-10-24-cs-ai.md
---

# Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE

**Links:** [arXiv](https://arxiv.org/abs/2610.27598) · [HF](https://huggingface.co/papers/2610.27598) · cross-source confirmed (HF + Kurate)

## TL;DR

In a standard mixture-of-experts (MoE) model, each layer owns its own experts (the small feed-forward sub-networks a router picks per token). The paper measures that experts in different layers store very similar content, so a lot of parameters are duplicates. It replaces per-layer "Local Experts" with "Meta Experts" shared across layers. With activated experts and expert size held fixed, the shared design matches a vanilla MoE using only 70-80% of the experts, with lower parameter redundancy, lower cross-entropy loss and higher downstream accuracy. A theory section argues that a shared expert gives hidden states more flexible residual pathways, which the authors call better "information retrieval efficiency." Abstract-level only: no alphaxiv overview yet, and scale details are not in the abstract.

<div class="dg-title">One expert pool serves many layers</div>
<div class="dg-sub">Layers keep their own routers but draw from a shared bank, so duplicate experts disappear.</div>

```mermaid
flowchart LR
  L1["Layer i router<br/><small>picks top-k</small>"] --> P["Meta Expert pool<br/><small>shared across layers</small>"]
  L2["Layer j router<br/><small>picks top-k</small>"] --> P
  P --> O["Same active FLOPs<br/><small>k experts per token</small>"]
  O --> S["70-80% of experts<br/><small>matches vanilla MoE</small>"]
  D["Per-layer copies<br/><small>redundant content</small>"] -.->|removed| P
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class L1,L2 loop
  class P core
  class O input
  class S exit
  class D err
```

<div class="dg-legend">Amber are per-layer routers, purple is the shared pool, red is the redundancy removed, green is the parameter saving.</div>

## Relation to prior wiki

- **Second paper making this exact move.** UniPool ([05-09](2026-05-09-unipool-shared-expert-pool-moe.md)) replaced per-layer experts with one global pool accessed by per-layer routers and beat vanilla MoE at matched active parameters (182M to 978M scale). Meta Expert reaches the same conclusion from a redundancy measurement, and reports the saving as an expert-count reduction (20-30%). Two independent groups, five months apart, same architecture. One more and it is a pattern.
- **Complements expert pruning** ([SlimWise, 10-08](2026-10-08-slimwise-phase-decoupled-expert-pruning.md); [ACE expert skipping, 09-08](2026-09-08-ace-expert-skipping-moe.md)): those remove experts after training. Meta Expert never trains the duplicates.
- **Serving angle:** fewer unique experts means a smaller checkpoint, which matters for the NVMe expert-streaming regime ([kimi-k3-in-c, 09-12](2026-09-12-kimi-k3-in-c-nvme-expert-streaming.md)), where total bytes, not active FLOPs, set latency.

## Gaps

Scale and token budget are not stated in the abstract. Load balancing across a shared pool (UniPool needed a pool-level auxiliary loss and NormRouter) and expert-parallel placement (a shared expert must live on a device all layers can reach) are the obvious systems questions.

## Research angle

Shared experts break the assumption behind layer-wise expert-parallel sharding. Whether a shared pool helps or hurts all-to-all traffic (the dominant MoE communication cost; 60-70% of MoE comm volume per today's SemiAnalysis Trainium piece) is unmeasured.
