# Meta's Infrastructure Team Needs a Culture Reset (SemiAnalysis)

**Source:** SemiAnalysis, Wayne Ma (2026-07-22) · [post](https://newsletter.semianalysis.com/p/metas-infrastructure-team-needs-a) · [raw](../../raw/rss/2026-07-22-semianalysis-meta-s-infrastructure-team-needs-a-culture-reset.md)

## TL;DR

SemiAnalysis follows its optimistic Meta-Superintelligence piece with a blunt counterpoint: Meta's *infrastructure* organization is the weak link, and a string of expensive silicon and server missteps traces back to culture, a bloated, politically managed org with a six-month stack-rank review cycle that rewards short-term "window washing" over hardware/software co-design. The concrete casualties: a $2.5B+ Rivos acquisition that has been effectively dismantled, two custom server designs (Grand Teton, Ariel) that cost more for worse TCO, and an upcoming decision to take a cut-down "half" MI450 that would blunt AMD's best chip for GenAI.

## Key points

- **Rivos ($2.5B+).** Bought for GPU/accelerator IP closer to NVIDIA-style programmability (SIMT vs Meta's SIMD MTIA). After close, Meta cancelled the "Olympus" chip meant to use Rivos GPU IP (too aggressive, software not ready), stuck with MTIA through MTIA 600, and treated Rivos staff as free headcount. ~30% of acquired Rivos engineers were laid off; co-founder Mark Hayter left; others departed for Nuvacore. A COT (customer-owned-tooling) team could be built for ~$100M/year, making the $2.5B hard to justify.
- **Grand Teton (Hopper gen).** Added a switch tray with four Broadcom PCIe switches to cram in eight extra SSDs per server, at the cost of higher BOM, more power, more complexity. NVIDIA had already designed out standalone PCIe switches via the ConnectX-7 NIC. The extra storage (for training checkpoints) went underused in production; design cancelled. Meta didn't reduce NVIDIA-networking reliance and increased Broadcom reliance.
- **Ariel (Blackwell gen).** A custom GB200 with one B200 per Grace CPU (vs the standard two) in an NVL36x2 layout, chosen for Meta's RecSys embedding workloads (CPU/DRAM-heavy). Result: **14% higher TCO than standard GB200 NVL72**, worse $/FLOP and $/HBM, plus a two-hop cross-rack scale-up that added latency and reliability problems. Meta was the only Ariel customer; the entire Meta GB200 fleet was this inferior SKU. Dropped for GB300.
- **The MI450 warning.** AMD's MI450 is the most advanced GPU coming (2nm, hybrid bonding, 12 HBM stacks, largest CoWoS reticle). Meta's custom version halves the compute silicon and HBM stacks and downgrades HBM4 from 12-Hi to 8-Hi, again to raise the CPU:GPU ratio for RecSys. SemiAnalysis argues this "nukes AMD's volume at Meta" because Meta's own TBD Lab (the GenAI team) will prefer NVIDIA Rubin over a gimped MI450, and publicly urges AMD to push Meta toward the standard MI450.

## How this relates to prior wiki knowledge

Read against the **same-day** NVIDIA Vera Rubin ramp ([2026-07-22-nvidia-vera-rubin-gigascale-ramp](2026-07-22-nvidia-vera-rubin-gigascale-ramp.md)), the two pieces frame the hardware divide of the moment: rack-level hardware/software co-design (NVIDIA's 10x tokens/MW) versus co-design failure (Meta's worse-TCO custom SKUs). It extends the SemiAnalysis thread the [hardware](memory-hierarchy.md) pages track (Cerebras IPO 05-13, 800VDC revolution 05-26, EDA market primer 05-21) and connects to the recent industry note that Meta is renting Anthropic/external compute and now plans to *sell* compute externally, a move that makes its infra dysfunction a market problem, not just an internal one.

It also grounds the "Meta Superintelligence has the right ingredients" optimism the digests carried (07-15 Meta's physics-olympiad result) with the caveat that the researchers at MSL are being served by an infra org that ships them inferior systems.

## Gaps

This is reported analysis sourced from former Meta employees and SemiAnalysis's Accelerator Model, not disclosed by Meta; the specific TCO figure (14%) and the MI450 configuration are SemiAnalysis estimates. Meta could still take the standard MI450, which the piece explicitly lobbies for. The article is part 1 of a series (DSF networking and "how to fix it" promised next), so the prescription is incomplete.

## Research/industry angle

The falsifiable question is whether Meta takes the standard MI450 or the gimped custom version. If it takes standard, AMD gets real GenAI-competitive volume at Meta and the MI450 becomes the first credible Rubin alternative; if it takes the half-chip, AMD's Meta volume collapses and NVIDIA's Rubin lock at Meta's GenAI team tightens. Either way, the deeper signal for compute-supply watchers is that custom silicon economics punish organizations without disciplined hardware/software co-design, the exact discipline NVIDIA's seven-chip Rubin co-design showcases the same day.
