# KV Cache

The KV cache (Key-Value cache) stores the key and value tensors from the attention mechanism for tokens already processed. This means those tokens don't need to be recomputed on every new generation step — critical for making autoregressive decoding fast.

## Current State (as of 2026-04-18)

KV caching is standard in all production LLM serving. Active research is focused on three problems: (1) making caches reusable across contexts without recomputation, (2) compressing the cache to reduce memory footprint, and (3) smarter eviction policies when the cache is full.

## Key Papers

**KV Packet (2026-04-17)** — Eliminates recomputation-on-reuse entirely. Wraps cached documents as immutable packets with lightweight soft-token adapters (trained via self-supervised distillation) that bridge context shifts. Near-zero FLOPs, lower TTFT than all recomputation-based baselines (CacheBlend, EPIC, SAM-KV). → [summary](2026-04-17-kv-packet-recomputation-free-kv-cache.md)

**LongAct (2026-04-18)** — Identifies high-magnitude activations in Q/K vectors during long-context processing. These "saliency peaks" (same ones that trouble quantization) are the positions where attention is doing real work. LongAct restricts RL gradient updates to only those weights, yielding ~8% gain on LongBench v2 with universal compatibility across GRPO and DAPO. Bridges the KV saliency insight from quantization research into RL training. → [summary](2026-04-18-longact-saliency-sparse-rl.md)

## Key Concepts

- **Context dependency**: KV states computed for a document are specific to the attention context at the time. Reusing them in a new context produces attention distribution mismatch — hence the need to recompute.
- **TTFT (Time-to-First-Token)**: the latency before the model outputs the first token. KV cache reuse directly impacts this.
- **Soft-token adapters**: trainable lightweight token representations that can modify how a cached KV state interacts with a new context, without recomputing the underlying states.
- **Cache eviction**: when the KV cache fills up, old entries must be evicted. Policy choices (LRU, saliency-based, etc.) affect quality and memory efficiency.

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)
- [LLM Routing](../ai-routing/llm-routing.md)
