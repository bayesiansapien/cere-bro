---
title: "MemOnce: store a few final-layer states, decode them back into KV on demand"
date: 2026-11-24
source: https://arxiv.org/abs/2611.27973
raw: ../../raw/huggingface/2026-11-23-memonce-a-scalable-memory-architecture-for-large-language-mo.md
tags: [kv-cache, memory, long-context, sparse-attention, architecture]
signal: HuggingFace 11-23 (21 upvotes)
---

# MemOnce: a scalable memory architecture

## TL;DR

A Transformer stores keys and values for every token at every layer, so memory grows linearly with context and attention cost grows quadratically. Linear-time models (SSMs, linear attention) keep a fixed-size state but lose fine detail. MemOnce takes a third path. It stores only a small subset of **final-layer hidden states** as compact memory. When a new input arrives, a **memory decoder** turns the relevant stored states back into KV caches for every attention layer. **Memory sparse attention** picks which memories to load, and it computes those sparse indices **once** and reuses them across all layers. Adapting Qwen3.5-4B with MemOnce cut the stored memory state by **1313x** and prefill latency by **6.9x** at 1M context, raised throughput **3.5x**, and improved memory benchmarks by 5.77 points.

<div class="dg-title">Keep one small state per chunk, rebuild KV only when needed</div>
<div class="dg-sub">The full per-layer KV cache never sits in GPU memory; it is regenerated from a compact final-layer summary.</div>

```mermaid
flowchart LR
  X["Past context<br/><small>long interaction</small>"] --> M["Memory encoder<br/><small>keeps few final states</small>"]
  M --> B["Memory bank<br/><small>1313x smaller</small>"]
  Q["New input<br/><small>current turn</small>"] --> R{"Sparse selector<br/><small>indices computed once</small>"}
  B --> R
  R --> D["Memory decoder<br/><small>rebuilds layer KV</small>"]
  D --> A["Attention layers<br/><small>read decoded KV</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class X,Q input
  class M,D,A core
  class R loop
  class B exit
```

<div class="dg-legend">Blue is input, purple is the model and codec, amber is the selection step, green is what stays in memory.</div>

## Key points

- The trade is memory for compute: decoding memories back into KV costs FLOPs at load time, but GPU memory stops growing with every layer and token.
- Works both from scratch (pretraining) and as an adaptation of an existing model (post-training on Qwen3.5-4B).
- Computing sparse indices once across layers removes the per-layer indexer cost that DSA-style sparse attention pays.

## Relation to prior wiki pages

- **Extends** [kv-cache.md](kv-cache.md): most of the page's methods compress or evict KV per layer. MemOnce stores no per-layer KV for the past at all; it stores a latent and regenerates the cache.
- **Pairs with** [ERNIE 5.5 Flash (same day)](2026-11-24-ernie-5-5-flash-open-weights.md): ERNIE compresses KV inside 37 of 43 layers; MemOnce compresses across layers. Both target the same 1M-context memory wall.
- **Relates** to [parametric-context-internalization.md](parametric-context-internalization.md): another way to keep long-lived context without holding raw KV.

## Gaps

Abstract-level evidence only (no alphaxiv overview). Results are at 4B; no frontier-scale test. Decode-time cost of the memory decoder per turn is not broken out, and "memory performance +5.77%" needs the benchmark list.
