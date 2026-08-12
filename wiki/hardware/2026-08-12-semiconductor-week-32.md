# Semiconductor week 32, 2026: a record quarter, and two bets against HBM

**Source:** The Semiconductor Newsletter, week 32 2026, via starred Gmail · [Post](https://thesemiconductornewsletter.substack.com/p/week-32-2026) · [raw](../../raw/gmail/2026-08-12-starred.md)

**TL;DR.** Global semiconductor revenue hit **$403.3 billion in Q2**, a record, and the newsletter attributes the expansion primarily to memory. Underneath the headline are two developments that matter more for inference economics than the revenue number does: **Sandisk and SK hynix published the first open High Bandwidth Flash specification** for AI inference memory, and **OLIX raised $312 million at a $3.3 billion valuation for an HBM-free inference architecture**. Both are capital and standards moving against the assumption that inference must be served out of HBM.

---

## The memory story, which is the whole story

**Global semiconductor revenue reached $403.3 billion in Q2**, described as historic market expansion driven by memory. That framing is the important part: this is not a logic-led cycle.

**Sandisk and SK hynix released the first open HBF specification.** High Bandwidth Flash is a flash-based tier aimed specifically at AI inference memory. An open spec from two of the three memory majors is a coordination signal, not a product launch, and it is aimed at the capacity problem rather than the bandwidth problem.

**Samsung unveiled a vertical HBM architecture** and a **400-plus-layer V10 NAND** for future AI systems. **Kioxia and Sandisk pushed QLC NAND beyond 37 Gb per mm²** with a 332-layer BiCS10 architecture.

**CXMT is considering a second Beijing DRAM fab** as Chinese memory capacity moves above **600,000 wafers per month**, which is the number to track for whether the memory shortage is structural or a capacity-timing artifact.

## Compute, packaging and power

- **AMD acquired Taalas** to add specialized inference silicon to the Instinct AI architecture. An accelerator vendor buying dedicated inference silicon is the same directional bet as OLIX, from the incumbent side.
- **SpaceX and Tesla committed $16.8 billion to a Terafab semiconductor complex in Texas**, which is vertical integration into fabrication by two companies that were until recently pure customers.
- **NXP entered talks to acquire Ambarella** in a potential **$3.3 billion** edge-AI semiconductor deal.
- **Silicon Box shipped 500 million advanced packaging units** and is targeting a tenfold capacity expansion in 2026. Advanced packaging remains the constraint nobody can buy their way past quickly.
- **Wolfspeed and LITEON qualified 200 mm SiC** for 800 VDC AI data center power, and **Aehr expanded silicon photonics burn-in capacity** as AI optical manufacturing scales. **GlobalFoundries is targeting more than 100% silicon photonics revenue growth.** Three separate items on optical and power, which is where datacenter build-out actually binds.
- **China synthetic diamond exports rose 65.3%** on AI thermal management demand, which is an unusually direct read on how hard cooling has become.

## Policy and geography

- **The United States introduced a 15% tariff and minimum import prices across the polysilicon supply chain.**
- **South Korea activated its Semiconductor Special Act** and added a **₩10 trillion** financing package for supply-chain expansion.
- **Europe expanded its semiconductor strategy beyond fab capacity** toward design, IP and specialized silicon, which is a tacit admission that the fab-subsidy-only approach did not work.
- **China semiconductor exports nearly doubled**, with 23.9% July export growth.
- **Moore Threads revenue jumped 147%** as the Chinese GPU vendor prepares a Hong Kong listing.

## How this relates to what the wiki already knows

**The two HBM-skeptical items are the ones this wiki should carry forward, because they line up with a research result on the same day.** [ICBQ (08-12)](../inference-efficiency/2026-08-12-icbq-interleaved-cross-block-quantization.md) makes 1.58-bit ternary post-training quantization reliable by revisiting block interfaces instead of sweeping past them once, and sub-two-bit weights only stop being academic in a regime where fast memory is genuinely scarce. An HBM-free architecture and a flash-backed inference tier are exactly that regime. **Research making extreme weight compression trustworthy and capital funding memory tiers that require it are aimed at the same deployment, and neither cites the other.**

**It also sharpens yesterday's KV-cache result in a way the paper could not.** [OasisKV (08-11)](../inference-efficiency/2026-08-11-oasiskv-lookahead-sparse-prefetching.md) keeps the whole KV cache outside HBM in host or remote memory and stages only what the next decode step attends to, reporting 1.69x throughput on reasoning workloads. That paper's premise is that a cheaper, larger memory tier exists to spill into. HBF is that tier being standardized. OasisKV was validated against host DRAM; the open question it leaves is what its lookahead prefetch accuracy needs to be when the backing tier is flash rather than DRAM, because flash latency is worse by orders of magnitude and a prefetch miss becomes a much more expensive stall.

**The structural constraint TileRT named is untouched by any of this.** [SemiAnalysis on TileRT (08-11)](2026-08-11-tilert-persistent-kernel-interactivity.md) reported that HBM bandwidth improves 2 to 3x per GPU generation while **memory latency has not improved at all**, so the interactivity gap is structural and widening. Nothing in week 32 addresses latency. Vertical HBM, 400-layer NAND and HBF are all capacity-and-bandwidth plays. That means the latency-premium tier this wiki identified on 08-11 stays a software problem, and the memory industry is competing entirely on the axis that software can already work around by tiering.

**And it is the counterweight to the financialization story.** [NVIDIA turning AI compute into an asset class (08-11)](../ai-industry/2026-08-11-nvidia-compute-asset-class.md) mobilizes over $500 billion of third-party capital on the assumption that efficiency gains get absorbed by demand growth. A record $403.3 billion memory-led quarter is consistent with that. **OLIX's $312 million against HBM and AMD buying Taalas are the hedge inside the same cycle**, and both are small relative to the buildout, which is the honest measure of how contrarian they currently are.

## Gaps and cautions

- **Every item here is a newsletter summary of a primary announcement**, so figures are as-reported and mostly company-sourced.
- **HBF has a specification and no shipping product**, and inference memory specs have failed before on latency and endurance rather than on capacity.
- **OLIX's architecture is undisclosed in this source**, so "HBM-free inference" is a positioning claim, not a verified design. The $3.3 billion valuation is the only hard number.
- **The $403.3 billion figure is revenue, not units**, and in a memory-led cycle with acknowledged shortage pricing those diverge sharply. Treat it as a price signal at least as much as a volume signal.

## Related

- [memory-hierarchy.md](memory-hierarchy.md) · [gpu-kernels.md](gpu-kernels.md)
- [ICBQ: interleaved cross-block quantization (08-12)](../inference-efficiency/2026-08-12-icbq-interleaved-cross-block-quantization.md)
- [OasisKV (08-11)](../inference-efficiency/2026-08-11-oasiskv-lookahead-sparse-prefetching.md) · [TileRT (08-11)](2026-08-11-tilert-persistent-kernel-interactivity.md)
- [NVIDIA compute as an asset class (08-11)](../ai-industry/2026-08-11-nvidia-compute-asset-class.md)
- [Daily digest 2026-08-12](../daily-digest/2026-08/2026-08-12.md)
