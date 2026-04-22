# PrfaaS: Prefill-as-a-Service via Cross-Datacenter KV Cache Transfer

**Date:** 2026-04-22  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.15039](https://arxiv.org/abs/2604.15039)  
**Institution:** Moonshot AI and Tsinghua University  
**Raw:** (parallel daily digest 2026-04-22)

---

## TL;DR

PrfaaS (Moonshot AI + Tsinghua) offloads long-context prefill computation to separate compute-dense clusters in different datacenters, then transfers the resulting KV cache over commodity Ethernet. The enabler is hybrid-attention models (Kimi Linear, MiMo-V2-Flash, Qwen3.5-397B, Ring-2.5-1T) that produce 13-36x smaller KV caches than dense-attention models — making cross-WAN transfer economically viable. Results: 54% higher throughput, 50% lower mean TTFT vs homogeneous baselines.

---

## Architecture

```
User request (long prompt)
       │
  [Prefill cluster]           ← compute-dense, separate datacenter
  Hybrid-attention model      ← most layers are linear (O(L) not O(L²))
  Produces compressed KV      ← 4.66 Gbps vs 59.93 Gbps for dense attention
       │
  Transfer over commodity Ethernet
       │
  [Decode cluster]            ← memory-bandwidth-optimized, production DC
  Receives KV cache           ← 13x smaller than dense-attention equivalent
  Runs autoregressive decode
       │
  Output tokens streamed to user
```

**Why hybrid-attention makes this possible:** Dense transformers produce KV caches at full attention dimensionality for every layer. Hybrid-attention models interleave a small number of full-attention layers with a larger number of linear-complexity layers (state-space or linear recurrence). The linear layers produce tiny or no KV state. MiMo-V2-Flash produces cache at 4.66 Gbps versus 59.93 Gbps for dense-attention MiniMax-M2.5 — a 13x reduction. At that volume, cross-datacenter Ethernet is fast enough.

**Why prefill and decode split differently:** Prefill is compute-intensive (process the entire prompt in parallel). Decode is memory-bandwidth-intensive (one token per step, bottlenecked by KV reads). Separating them to hardware optimized for each is the natural split; PrfaaS just moves that split across a WAN link.

---

## Key Numbers

| Model | KV transfer rate | vs Dense |
|-------|-----------------|---------|
| MiMo-V2-Flash | 4.66 Gbps | 13x reduction |
| Dense MiniMax-M2.5 | 59.93 Gbps | baseline |
| System throughput gain | +54% | vs homogeneous |
| TTFT improvement | -50% | vs homogeneous |

---

## Strategic Implication

This paper changes what "serving topology" means for hybrid-attention models. It creates a feedback loop: models with smaller KV caches enable new serving architectures (cross-DC disaggregation), which reduce infrastructure costs, which create economic incentive to prefer hybrid-attention models. Architecture choice is now a serving economics decision, not just a quality decision.

---

## Relation to Prior Wiki Pages

**Directly extends KV cache concept page:** Previous work (KV Packet 04-17) addressed reuse; LongAct (04-18) addressed training efficiency at cache positions; TurboQuant (04-22) addresses compression. PrfaaS addresses serving topology — a level up from per-token cache management.

**Connects to Nemotron 3 Super (04-21):** Nemotron's Mamba blocks produce much smaller state than full attention — same category as hybrid-attention models enabling PrfaaS. The serving economics argument for hybrid attention now has concrete backing.

**Connects to AI routing (Tier 1 intersection):** PrfaaS is essentially routing prefill to specialist compute. If goodput (SemiAnalysis 04-21) varies by provider, a routing framework that selects prefill providers based on cache transfer cost and compute density per dollar would be a natural extension.

---

## Open Questions

1. What is the WAN latency impact on TTFT at tail percentiles? 54% throughput and 50% mean TTFT are strong — but P99 TTFT under network jitter is the production-critical metric.
2. Does the cache-transfer approach work with TurboQuant compression applied at the prefill cluster before transfer? That would compound the volume reduction.
3. How does disaggregation interact with KV Packet-style cross-request cache reuse? If cached document packets live in the decode cluster, prefill that hits a cached segment could skip transfer entirely.

---

## Related Pages

- [KV Cache](kv-cache.md)
- [TurboQuant: Online Vector Quantization](2026-04-22-turbo-quant-kv-cache-quantization.md)
- [KV Packet: Recomputation-Free KV Cache Reuse](2026-04-17-kv-packet-recomputation-free-kv-cache.md)
- [Nemotron 3 Super: Hybrid Mamba-Attention MoE](2026-04-21-nemotron3-super-hybrid-moe.md)
- [SemiAnalysis GPU Cluster Goodput](../hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md)
