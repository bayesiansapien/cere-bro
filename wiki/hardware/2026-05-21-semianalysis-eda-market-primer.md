# SemiAnalysis EDA Market Primer (Part 2): how chip-design software became a $16B/yr AI tailwind

**Source:** SemiAnalysis, "EDA Market Primer", 2026-05-21 (via Gmail starred, paywalled but starred-email summary substantial).
**Link:** [Newsletter post](https://newsletter.semianalysis.com/p/eda-market-primer)

## TL;DR

The Electronic Design Automation (EDA) industry — Synopsys, Cadence, Siemens EDA, plus Ansys (now part of Synopsys) — is the indispensable substrate beneath every advanced chip. Big-3 hold over 85% combined market share. Combined CY2025 revenue is around $16B across tools, IP, emulation hardware, and simulation software. EDA grows at 13% CAGR while semiconductor R&D grows at 7%, a six-point spread that widened after 2018 specifically because of hyperscaler AI silicon programs, emulation hardware economics, and advanced-node verification cost.

## Why an AI wiki should care

Three reasons:

1. **EDA captures part of every dollar spent on AI silicon.** Customer base now includes the systems companies (Google, Amazon, Microsoft, Meta, Apple, Tesla) which account for 45% of EDA demand. Each new hyperscaler custom-silicon program is incremental EDA revenue. SemiAnalysis estimates Broadcom's ASIC group alone spends $200-500M annually on EDA tools, IP, and emulation.

2. **AI is reshaping the EDA stack itself.** Part 3 of the primer (not yet released) will cover this. The teaser is that AI accelerator proliferation has created $15-20B in new chip programs, and the verification surface area of these programs (PCIe Gen6, HBM4, UCIe) compounds existing workloads. So AI-assisted EDA is both a tailwind and a product.

3. **The cost of a chip respin at leading-edge nodes is $50-100M and 6-12 months.** This is a hard ceiling on how aggressively hyperscalers can iterate on custom silicon, and it explains why AI lab compute is supply-constrained at a deeper layer than just "fab capacity." Design verification time is the bottleneck above the foundry.

## Numbers from Part 2

| Item | Value |
|------|-------|
| EDA + IP industry total revenue 2025 | $18B |
| Big-3 combined revenue 2025 | ~$16B |
| Synopsys CY2025 revenue (incl Ansys) | $8B |
| Cadence CY2025 revenue | $5.30B |
| Siemens EDA estimated CY2025 revenue | $2.2-2.5B |
| EDA growth CAGR | 13% |
| Semiconductor R&D growth | 7% |
| Synopsys IP revenue | $1.7B |
| Cadence IP revenue | $0.7B+ |
| EDA as % of semiconductor R&D spend | 9-12% (or 12-15% including IP) |
| Hardware emulation market | $1.5B+ |
| 3nm design rules at foundry | 25,000+ |
| Process-voltage-temperature corners at 3nm | 20-30+ (vs 5-7 at 28nm) |
| Verification % of design time | 60-70%, growing 15%+/yr |
| Chip respin cost at leading-edge | $50-100M, 6-12 month delay |
| Per-engineer EDA spend (fabless) | $80-150K/yr |
| Per-engineer EDA spend (IDMs) | $40-80K/yr |
| Hyperscaler custom-silicon market 2025-2026 (estimated) | $15-20B |
| NVIDIA EDA spend per chip | $100M+ |
| Apple EDA spend per chip | $170-260M |

## Customer breakdown

Seven categories of EDA buyers, each with distinct procurement behavior:
1. Fabless chip designers (NVIDIA, Qualcomm, AMD, Broadcom, MediaTek).
2. Systems companies (hyperscalers, Apple, Tesla, automotive Tier-1s) — 45% of demand, fastest growing.
3. IDMs (Intel, TI, ADI, Infineon, ST) — enterprise-wide agreements, internal IP reduces external licensing.
4. Memory companies (Samsung, SK Hynix, Micron, Kioxia) — HBM verification approaching logic-chip complexity.
5. Foundries (TSMC, Samsung Foundry, Intel Foundry, GF, Rapidus) — co-develop PDKs with EDA vendors 24 months pre-production.
6. Turnkey ASIC houses (Broadcom ASIC, Marvell Custom, Alchip, GUC) — multiple concurrent tape-outs.
7. IP companies (ARM, Rambus, Alphawave) — license once, sell repeatedly.

## Pricing model nuance

Per-engineer pricing varies more than 4x across customer types (NVIDIA spends 150K per engineer; IDMs spend 40-80K). The lever EDA vendors use is the enterprise license agreement (ELA) shape, with seats, tokens, and hardware emulation hours all bundled.

## Industrial implication

For the wiki's hardware section, the EDA primer fills a gap: prior pages have covered the foundry side (Cerebras, NVIDIA Hopper/Blackwell/Rubin), but not the design-tool layer. The May 2026 supply tightness story (HBM long deals with no-waiver clauses, per today's Twitter morning slot) is downstream of EDA throughput on the memory-controller side. The EDA primer explains why:
- Verification corners grew from 5-7 at 28nm to 20-30+ at 3nm. Verification-tools throughput limits how fast HBM controllers can be re-spun.
- New protocols (PCIe Gen6, HBM4, UCIe) add verification surface area faster than EDA throughput improves.

So the bottleneck pile-up is: AI lab compute demand → custom-silicon program supply → foundry capacity → memory supply → EDA verification time. The EDA layer is the second-to-last constraint that breaks before the supply chain becomes elastic, and it grows 13% per year against 7% in the substrate.

## Open questions

- What does AI inside EDA tooling look like in detail? Part 3 will cover this. Likely candidates: ML-driven place-and-route, RL on verification corner exploration, generative HDL.
- China EDA capability gap — the primer notes a section on Chinese EDA vendor financials and the 2019-2025 export-control timeline, but the Gmail summary truncated before that section.
- R-squared lock-in intensity by customer (mentioned in TOC) — the formal measure of customer dependence on tool stack.

## Cross-references

- [semiconductor-week17 (2026-04-27)](2026-04-27-semiconductor-week17.md)
- [Broadcom-OpenAI-Microsoft chip (2026-05-10)](../ai-industry/2026-05-10-broadcom-openai-microsoft-chip.md)
- [Cerebras IPO SemiAnalysis (2026-05-13)](2026-05-13-semianalysis-cerebras-ipo.md)
- [SemiAnalysis GPU cluster goodput (2026-04-21)](2026-04-21-semianalysis-gpu-cluster-goodput.md)

## Source

Raw: `raw/gmail/2026-05-22-starred.md` (item 5) — the original SemiAnalysis post.
