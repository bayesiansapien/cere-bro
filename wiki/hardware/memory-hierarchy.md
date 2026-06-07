# Memory Hierarchy for AI (concept)

The tiered memory system that modern AI — and especially agentic AI — runs on. The 2026 thesis: the binding constraint on AI infrastructure has shifted from compute (FLOPS) to memory (where state lives and how fast it moves). This page synthesizes what the wiki knows about each tier and how the research it tracks maps onto the hardware.

## The tiers (fast/scarce → slow/abundant)

| Tier | Bandwidth (order) | Role in agentic AI |
|------|-------------------|--------------------|
| **On-chip SRAM** | 80–150 TB/s | Groq-style LPU primary weight/state store; low-latency decode, low jitter. Capacity-poor, must shard across chips. |
| **HBM3E / HBM4** | ~8 TB/s/GPU (HBM4 stack >2.8 TB/s) | Training, prefill, large-batch inference, hot weights. The scarce, allocation-driven tier. |
| **GDDR7** | board-level | Cost-efficient inference / context-phase accelerators (e.g. Rubin CPX, 128GB GDDR7). HBM pressure-release valve. |
| **DDR5 RDIMM / MRDIMM** | MRDIMM ~8.8K MT/s, +39% BW | CPU-attached bulk: orchestration, RAG working sets, tool runtime, KV staging. |
| **LPDDR5X / SOCAMM2 / LPDDR6** | Vera CPU ~1.2 TB/s | Low-power server memory; SOCAMM2 claims >2.3x TTFT for KV-cache offload at 1/3 power and footprint of RDIMM. |
| **CXL memory** | PCIe-coherent | Capacity expansion + pooling; de-strands DRAM, holds vector indexes and KV overflow. |
| **NVMe SSD + AI-native context (NVIDIA CMX)** | storage-class | Active KV tier — ephemeral KV cache and long-context state that cannot stay in HBM. |
| **PIM / CIM** | near-memory | Longer-term escape from the data-movement wall (Samsung HBM-PIM, ReRAM/PCM/analog MAC). |

## Core facts the wiki keeps returning to

- **KV cache, not weights, is the dominant memory traffic at long context.** Generation is memory-bandwidth-bound; as context grows the traffic shifts from model weights to KV cache. This is the hardware fact underneath every KV-cache software paper the wiki tracks. (Ken Huang memory survey, 06-07; UC Berkeley 2026 report.)
- **Agentic workloads consume ~15x more tokens** than traditional AI apps (NVIDIA), so they stress every tier at once, not just HBM.
- **The memory shortage is structural.** Micron's ~3:1 HBM-to-DDR5 wafer trade ratio (rising per HBM generation) + advanced-packaging bottleneck → tight/allocation-driven through 2026, selective relief 2027, broader 2028-2029, top-end HBM allocation-driven into 2030.
- **Latency over throughput for agents.** Interactive agents are judged on time-to-first-token and tail latency, which favors SRAM-first designs, disaggregated prefill/decode, and KV-aware tiering over raw batch throughput.

## How the research maps onto the hardware

- **KV-cache eviction / quantization / low-rank latent caches** (VASE 06-03, VideoMLA/StateKV 06-01, LongAttnComp 06-02) are the software answer to "KV cache is the bottleneck tier" — they shrink what must live in HBM so cheaper tiers (LPDDR SOCAMM2, CXL, SSD) suffice. See [kv-cache](../inference-efficiency/kv-cache.md).
- **Parametric context internalization** (Code2LoRA, Video2LoRA 06-06) is the most aggressive move: bake context into weights so it never enters the KV cache at all. See [parametric-context-internalization](../inference-efficiency/parametric-context-internalization.md).
- **Input-side compression** (AdaCodec 06-06, SEAOTTER 06-07) cuts bytes/tokens before they reach the model — relief upstream of every memory tier.
- **Compute rationing** ([CLEAR](../inference-efficiency/2026-06-05-clear-shadow-price-reasoning-budget.md) 06-05) is the demand-side dual: when HBM is scarce for five years, the serving stack must ration per-query compute by marginal utility, and (the open direction) ration KV-cache placement across tiers per-request.

## Open problems / what to watch

- **KV-aware tiering policies** — deciding per-request which KV blocks live in HBM vs LPDDR/CXL/SSD. The hardware counterpart to CLEAR's per-query compute rationing; not yet a shipped serving-stack feature.
- **Will PIM/CIM cross from research to product** for attention/embedding/search, or stay niche behind analog-precision and compiler-maturity barriers?
- **Does the SRAM-first bet (Groq) capture agentic inference** as the market tilts toward low-latency, high-value tokens, or does ecosystem/software depth keep HBM-GPU dominant?

## Sources

- [Memory Technology for Agentic AI Workloads (Ken Huang, 06-07)](2026-06-07-agentic-ai-memory-hierarchy.md)
- Related hardware pages: [gpu-kernels](gpu-kernels.md), SemiAnalysis 800VDC / cluster-goodput primers.
- Related efficiency: [kv-cache](../inference-efficiency/kv-cache.md), [parametric-context-internalization](../inference-efficiency/parametric-context-internalization.md)
