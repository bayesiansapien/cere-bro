# KV Cache

The KV cache (Key-Value cache) stores the key and value tensors from the attention mechanism for tokens already processed. This means those tokens don't need to be recomputed on every new generation step — critical for making autoregressive decoding fast.

## Current State (as of 2026-05-01)

KV caching is standard in all production LLM serving. Active research is focused on four problems: (1) making caches reusable across contexts without recomputation, (2) compressing the cache to reduce memory footprint, (3) smarter eviction policies when the cache is full, and (4) extending cache-based acceleration patterns (like speculative decoding) to non-text modalities. The parallel daily digest (04-22) introduced two major KV-focused papers — TurboQuant (ultra-low-bit compression) and PrfaaS (cross-datacenter disaggregation via hybrid attention) — signaling that the KV cache is now the primary optimization target in production serving.

**Economic context (SemiAnalysis 05-01):** the unit economics of frontier model labs now depend on >90% prompt-cache hit rates. Anthropic's blended price for Opus 4.7 on agentic workloads is ~$0.99/MTok (vs $5/$25 sticker) because cached input tokens dominate. Cache compression / reuse research is now financial-impact-driven, not just academic.

## Key Papers

**KV Packet (2026-04-17)** — Eliminates recomputation-on-reuse entirely. Wraps cached documents as immutable packets with lightweight soft-token adapters (trained via self-supervised distillation) that bridge context shifts. Near-zero FLOPs, lower TTFT than all recomputation-based baselines (CacheBlend, EPIC, SAM-KV). → [summary](2026-04-17-kv-packet-recomputation-free-kv-cache.md)

**LongAct (2026-04-18)** — Identifies high-magnitude activations in Q/K vectors during long-context processing. These "saliency peaks" (same ones that trouble quantization) are the positions where attention is doing real work. LongAct restricts RL gradient updates to only those weights, yielding ~8% gain on LongBench v2 with universal compatibility across GRPO and DAPO. Bridges the KV saliency insight from quantization research into RL training. → [summary](2026-04-18-longact-saliency-sparse-rl.md)

**TurboQuant (2026-04-22, via parallel digest)** — Google (ICLR 2026). Online vector quantization: randomly rotates input vectors to induce a concentrated Beta distribution, applies optimal scalar quantizers per coordinate, followed by a 1-bit QJL transform on the residual for an unbiased inner product quantizer. Absolute quality neutrality at 3.5 bits/channel; marginal degradation at 2.5 bits/channel; 6x+ KV cache memory reduction. Community integrations with vLLM and llama.cpp appearing despite no official implementation.

**PrfaaS / Prefill-as-a-Service (2026-04-22, via parallel digest)** — Moonshot AI + Tsinghua. Offloads long-context prefill to standalone compute-dense clusters in separate datacenters, transfers resulting KV cache over Ethernet. Enabled by hybrid-attention models (Kimi Linear, MiMo-V2-Flash, Qwen3.5-397B) that mix full-attention + linear-complexity layers. MiMo-V2-Flash produces KV cache at 4.66 Gbps vs 59.93 Gbps for dense-attention baseline (13x reduction). 54% higher throughput, 50% lower mean TTFT vs homogeneous baselines.

**SDVG (2026-04-22)** — Extends speculative decoding to continuous video generation. A 1.3B drafter proposes video blocks in 4 denoising steps; ImageReward scores per block using worst-frame aggregation; accepted blocks enter the 14B target's KV cache directly. 1.59x speedup at 98.1% quality; 2.09x at 95.7%. Training-free. → [summary](2026-04-22-sdvg-speculative-decoding-video.md)

## Key Concepts

- **Context dependency**: KV states computed for a document are specific to the attention context at the time. Reusing them in a new context produces attention distribution mismatch — hence the need to recompute.
- **TTFT (Time-to-First-Token)**: the latency before the model outputs the first token. KV cache reuse directly impacts this.
- **Soft-token adapters**: trainable lightweight token representations that can modify how a cached KV state interacts with a new context, without recomputing the underlying states.
- **Cache eviction**: when the KV cache fills up, old entries must be evicted. Policy choices (LRU, saliency-based, etc.) affect quality and memory efficiency.

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)
- [LLM Routing](../ai-routing/llm-routing.md)
