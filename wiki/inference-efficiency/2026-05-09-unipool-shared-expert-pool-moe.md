---
source: HuggingFace Daily Papers
arxiv_id: 2605.06665
date: 2026-05-09
tier: 1
topics: [moe, compression, parameter-allocation, routing]
---

# UniPool: A Globally Shared Expert Pool for Mixture-of-Experts

## TL;DR

Standard MoE locks each transformer layer to its own expert set. UniPool throws that constraint away. One global pool, K experts, accessed by independent per-layer routers. A pool-level auxiliary loss balances utilization across the entire pool, NormRouter keeps routing stable under sharing. Across five LLaMA-architecture scales (182M to 978M) on 30B Pile tokens, UniPool consistently beats matched vanilla MoE on validation loss and perplexity at the same active-parameter budget.

## Why this matters

MoE has been treating expert capacity as a per-layer commodity. UniPool treats it as a global architectural budget. The framing change is the contribution. If experts are allowed to specialize at the document or domain level instead of the layer level, the same active-parameter budget buys more representational diversity. This is the same architectural intuition behind EMO (also today, 2605.06663), arrived at independently, by a different route.

## Mechanism

```
Vanilla MoE:                       UniPool:
  Layer 1: [E1.1 ... E1.N]           Layer 1 router ──┐
  Layer 2: [E2.1 ... E2.N]           Layer 2 router ──┼──► Shared pool: [E1 ... EM]
  Layer 3: [E3.1 ... E3.N]           Layer 3 router ──┘
  experts are layer-owned            experts are layer-shared
```

Two technical pieces hold this together:

**Pool-level balance loss.** A naïve shared pool collapses, with most layers funneling traffic to a small clique of experts. UniPool's auxiliary loss balances utilization across the global pool (not per-layer), so coverage is enforced at the level where the pool actually lives.

**NormRouter.** Standard top-k routers under sharing produce scale instability, because the same expert receives gradients from multiple layers' routers at once. NormRouter normalizes routing logits so the magnitude of the routing signal stays bounded across layers.

## Connections to prior wiki

This is the third architectural-modularity paper this week, and the second on a single day:

- **EMO (2605.06663, today)** restricts tokens within a document to a shared expert pool, but the pool itself is dynamic per-document, not global. Both papers attack the same failure mode (vanilla MoE underuses experts and breaks under subset deployment) from opposite ends. EMO bets on document-level locality. UniPool bets on global capacity sharing. Both ship empirical wins.
- **Nemotron-3 Super hybrid MoE (04-21)** introduced layer-heterogeneous attention but kept per-layer expert ownership. UniPool goes further on the expert side. The natural composition (hybrid attention plus shared expert pool) has not been published.
- **The MoE concept page (`inference-efficiency/`)** has been tracking the per-layer expert-ownership constraint as an open question. UniPool is the first paper in the wiki to break it directly.

## Research angle

Three open questions worth tracking:

1. **Does the win persist past 1B?** UniPool tops out at 978M on 30B tokens. The interesting regime for MoE deployment is 30B+ active / 200B+ total. Whether NormRouter stays stable at scale, and whether the global-balance loss tracks correctly through 1T+ tokens, is the actual deployment question.
2. **Composition with EMO.** UniPool is layer-sharing, EMO is document-restriction. Both losses can be applied simultaneously. The product (a global pool restricted per-document) is a clean architectural primitive that no one has published.
3. **Inference-time pool slicing.** The whole point of MoE-as-modularity is to deploy expert subsets. UniPool's per-layer routers means you cannot cleanly drop experts without re-routing. EMO's document-level pool is more amenable. UniPool plus EMO might give you both training-time expressivity and deployment-time slicability.

## Source

- Paper: https://arxiv.org/abs/2605.06665
- HuggingFace: https://huggingface.co/papers/2605.06665
- Raw: `raw/huggingface/2026-05-09-unipool-a-globally-shared-expert-pool-for-mixtureofexperts.md`
