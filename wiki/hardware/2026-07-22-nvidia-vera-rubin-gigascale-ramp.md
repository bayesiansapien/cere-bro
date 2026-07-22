# NVIDIA Vera Rubin Ramps to Gigascale: 10x Tokens per Megawatt

**Source:** NVIDIA blogs via Twitter/@nvidia (2026-07-22, SIGGRAPH week) · [Vera Rubin blog](https://nvda.ws/4ywCiQn) · [Spectrum-6 blog](https://nvda.ws/44AO2nn) · [Wistron Fort Worth](https://nvda.ws/4pusD8Q) · [raw](../../raw/twitter/2026-07-22-morning.md)

## TL;DR

NVIDIA used SIGGRAPH 2026 week to declare the Vera Rubin platform in gigascale production. The headline metric is power efficiency, not raw FLOPs: CoreWeave's first measured silicon numbers on Vera Rubin NVL72 show **10x more tokens per megawatt than Grace Blackwell NVL72** on DeepSeek-R1 (real hardware, not projections), landing directly on the metric that matters in a power-constrained buildout. Alongside it, NVIDIA announced Spectrum-6 (a 102.4 Tb/s Ethernet switch, 2x the previous generation) now arriving in AI factories, and opened Wistron's first US plant in Fort Worth producing Grace Blackwell Ultra boards with Vera Rubin next.

## Key points

- **10x tokens/MW vs Blackwell** on CoreWeave's DeepSeek-R1 benchmark, framed explicitly as "performance per watt" and "lowest token cost for the agentic era." The efficiency story has fully displaced the raw-throughput story in NVIDIA's own messaging.
- **Vera CPU**: DeepInfra benchmarks put it >2x faster than comparison CPUs and able to support more concurrent AI agents.
- **Extreme co-design across seven chips and five rack trays**: Vera Rubin NVL72, Vera CPU rack, Groq 3 LPX, Spectrum-6 SPX, and Vera BlueField-4 STX, engineered as one system rather than assembled from parts.
- **Spectrum-6**: 102.4 Tb/s Ethernet, 2x prior capacity, first adopters CoreWeave, Microsoft, Nebius, SpaceXAI, Tesla.
- **Supply chain**: 350+ factory sites across 30 countries; Wistron's 324,000-sq-ft Fort Worth plant ($700M combined investment) frames the ramp as US reindustrialization.

## How this relates to prior wiki knowledge

This is the deployed-hardware payoff of the [memory-hierarchy](memory-hierarchy.md) and energy-efficiency threads the hardware pages track. The [energy-to-token position paper](2026-05-14-energy-to-token-position-paper.md) argued tokens-per-joule is the metric the industry should optimize; NVIDIA's own launch messaging now leads with exactly that number, a rare case of a research framing becoming the vendor's headline within a quarter. It also extends the Blackwell-generation deep dives (DoubleAI Blackwell Sol ExecBench, 05-28) one node forward.

The sharp contrast to draw is with the **same-day** SemiAnalysis piece on Meta's infrastructure ([2026-07-22-semianalysis-meta-infra-culture-reset](2026-07-22-semianalysis-meta-infra-culture-reset.md)): NVIDIA ships a co-designed rack hitting 10x tokens/MW while Meta is documented cutting the MI450 in half and shipping a worse-TCO custom GB200 (Ariel) than the standard SKU. The lesson both tell is that hardware/software co-design at the rack level is now the dividing line, and going off-menu against NVIDIA's reference design is expensive.

## Gaps

The 10x-tokens/MW figure is one workload (DeepSeek-R1) on one partner (CoreWeave), a first measured point, not a swept curve; the comparison baseline (Grace Blackwell NVL72) and the exact inference configuration are not fully specified in the launch material. Vendor benchmarks self-select favorable workloads. Independent MLPerf-style numbers will be the real test.

## Research angle

For Amit's Tier 1 GPU-optimization interest, the question is where the 10x actually comes from: how much is the Rubin GPU itself, how much is the Vera CPU offload, how much is Spectrum-6 networking removing communication stalls, and how much is co-design (kernel/scheduler tuning) that a non-NVIDIA stack could also capture. If most of the gain is networking and co-design rather than silicon, it strengthens the case that the frontier efficiency lever is the rack-and-fabric system, not the accelerator die, which is precisely the co-design discipline Meta is shown lacking.
