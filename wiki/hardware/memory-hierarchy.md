# Memory Hierarchy for AI (concept)

The tiered memory system that modern AI — and especially agentic AI — runs on. The 2026 thesis: the binding constraint on AI infrastructure has shifted from compute (FLOPS) to memory (where state lives and how fast it moves). This page synthesizes what the wiki knows about each tier and how the research it tracks maps onto the hardware.

## Current State (as of 2026-07-25)

**Memory stops being a component and becomes the axis of competition, on the same day, in three forms.** The 07-22 section below set a falsifiable watch on whether Meta would take the standard MI450 or the half-strength variant. [Today's SemiAnalysis Advancing AI 2026 analysis](2026-07-25-semianalysis-amd-cuda-moat.md) **resolves it: most of Meta's MI455 orders are the cut-down part** (compute halved 8 XCDs → 4, HBM halved 12 stacks → 6, and downgraded 12-Hi → 8-Hi). The decision was made by RecSys infrastructure teams before Meta's TBD Lab existed, TBD has no interest in the resulting part, and SemiAnalysis says external customers will not want it either. AMD's Meta GenAI volume is the casualty exactly as the 07-22 prediction framed it, with one hedge: Zuckerberg has begun rapidly reworking Meta's infra org culture since that article.

Three concrete memory facts arrived with it. **(1) The standard MI455X is a memory part first**: 12 HBM4 stacks for **432GB at 23.3 TB/s**, against Rubin's 8 stacks for 288GB. Fitting 3 cubes per base-die edge required growing the HBM-facing edge to 32mm (the MI300X AID's 29mm could not fit three). **(2) NVIDIA answered with pin speed, not capacity, and moved a JEDEC spec to do it.** It raised its HBM4 target to 10.7 Gbps, 40% above AMD's 7.6 Gbps and well past the original JEDEC HBM4 specification, purely to erase AMD's bandwidth lead. That lands Rubin at 22 TB/s from a 33% narrower bus, forces NVIDIA onto a much higher-quality bin, made suppliers rework HBM4, and delayed Rubin's own ramp. Competitive pressure between two accelerator vendors propagated backwards into a memory standard. **(3) The shortage is now deleting product features.** The up-to-1TB of direct-attached LPDDR per MI455X EAM module, present on earlier roadmaps as a second memory tier, has quietly disappeared, which SemiAnalysis reads as a consequence of tight supply. The second tier of accelerator-attached memory is a casualty of allocation.

The commercial counterpart landed the same 24 hours: [NVIDIA announced a $500B partnership with SK Group](2026-07-25-nvidia-sk-korea-500b.md), owner of SK hynix, explicitly to access more HBM and fill more datacenters, including **joint HBM co-development** plus a 2GW Vera Rubin DSX factory in Korea. One vendor signs a half-trillion-dollar supply arrangement with a memory maker; the other deletes a memory tier. That is what this page's structural-shortage thesis (Micron's ~3:1 HBM-to-DDR5 wafer trade ratio rising per generation, packaging bottleneck, top-end HBM allocation-driven into 2030) looks like when it reaches the balance sheet. Markets are pricing it accordingly: Micron is up 213% year to date and AMD 142%, against NVIDIA's 10% despite 83% expected revenue growth.

**Rack-level memory movement is now a named cost line too.** Helios connects 72 MI455X through 12 merchant Broadcom Tomahawk 6 switches (only 432 of each switch's 512 lanes usable, because 102.4T does not divide evenly into 72 GPUs, where NVIDIA sized the 28.8T NVSwitch for exactly 72 with zero waste). AMD's 200G SerDes cannot hold the copper backplane, so ~85% of Meta's scale-up links need Broadcom retimers, 550+ per rack. Backplane plus compute-tray content: $68,928 per rack, 10,368 differential copper pairs. The lesson the page has been accumulating since Vera Rubin: at rack scale, moving bytes is the cost, and co-design is the only lever on it.

## Current State (as of 2026-07-22)

**Two same-day hardware signals frame the co-design divide: NVIDIA ships a rack-co-designed Vera Rubin at 10x tokens/MW while Meta is documented wasting billions going off-menu.** NVIDIA declared Vera Rubin in gigascale production at SIGGRAPH week ([summary](2026-07-22-nvidia-vera-rubin-gigascale-ramp.md)): CoreWeave's first measured silicon shows **10x more tokens per megawatt than Grace Blackwell NVL72** on DeepSeek-R1, framed explicitly as performance-per-watt and lowest token cost, plus Spectrum-6 (102.4 Tb/s Ethernet, 2x prior) and the Vera CPU (>2x faster, more concurrent agents). The headline is now efficiency, exactly the tokens-per-joule metric the [energy-to-token position paper](2026-05-14-energy-to-token-position-paper.md) argued for, and it comes from extreme co-design across seven chips and five rack trays. The counterpoint, from SemiAnalysis the same day ([summary](2026-07-22-semianalysis-meta-infra-culture-reset.md)), is Meta's infra org shipping the opposite: a $2.5B+ Rivos acquisition effectively dismantled, a custom GB200 (Ariel, one B200 per Grace in NVL36x2) with **14% higher TCO** than the standard SKU that Meta's whole GB200 fleet ran on, and an upcoming plan to take a *half* MI450 (halved compute silicon and HBM stacks, HBM4 downgraded 12-Hi → 8-Hi) to chase a higher CPU:GPU ratio for RecSys embeddings. The MI450 matters for this page's memory thesis: the standard part has 12 HBM stacks and the largest CoWoS reticle on the market; gimping it to 8-Hi trades exactly the HBM capacity/bandwidth that GenAI training and inference are bottlenecked on. Falsifiable watch: whether Meta takes the standard MI450 (AMD gets its first Rubin-competitive GenAI volume) or the half-chip (AMD's Meta volume collapses, NVIDIA Rubin lock tightens). The meta-lesson both pieces teach: at the rack level, hardware/software co-design is the dividing line, and custom silicon without that discipline is a money furnace.

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
