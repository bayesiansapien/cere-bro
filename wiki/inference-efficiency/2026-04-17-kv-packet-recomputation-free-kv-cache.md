---
source: raw/huggingface/2026-04-17-kv-packet-recomputation-free-context-independent-kv-caching.md
arxiv: https://arxiv.org/abs/2604.13226
date: 2026-04-17
---

# KV Packet: Recomputation-Free Context-Independent KV Caching

## TL;DR

KV caches are context-dependent — reusing a cached document in a new context normally requires recomputing its KV states to account for different attention distributions. KV Packet eliminates that recomputation entirely by wrapping cached documents in lightweight trainable soft-token adapters that bridge context shifts. Near-zero FLOPs, lower TTFT than recomputation baselines, comparable accuracy.

## Key Findings

- **Problem**: standard KV caches store attention keys/values that are specific to the context they were computed in. Reuse in a new context requires recomputation, adding latency (TTFT).
- **KV Packet approach**: treat cached documents as immutable packets. Wrap them with trainable soft-token adapters trained via self-supervised distillation to bridge the context discontinuity — no recomputation needed.
- **Results on Llama-3.1 and Qwen2.5**: near-zero FLOPs overhead, lower Time-to-First-Token than CacheBlend/EPIC/SAM-KV (all recomputation-based), F1 scores comparable to full recomputation.

## How It Works

```
Standard KV reuse (old approach):
  Document KV cache
       │
  New context arrives  →  recompute subset of tokens  →  higher TTFT
                           to adjust attention distribution

KV Packet (new approach):
  Document KV cache (immutable packet)
       │
  Soft-token adapter  ←  trained via self-supervised distillation
  (lightweight, wraps the packet)
       │
  New context arrives  →  adapter bridges the discontinuity
                           NO recomputation, near-zero FLOPs
```

## Why It Matters

Recomputation is the main bottleneck for KV cache reuse in production. Every prior approach (CacheBlend, EPIC, SAM-KV) just reduces how much you recompute — they don't eliminate it. KV Packet is the first to get to zero recomputation. Lower TTFT matters directly for interactive inference latency.

## Related Pages

- [KV Cache](kv-cache.md)
- [Knowledge Distillation](knowledge-distillation.md)
