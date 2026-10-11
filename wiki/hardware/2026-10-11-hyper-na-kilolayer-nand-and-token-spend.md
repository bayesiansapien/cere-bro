---
title: "Hyper-NA EUV, kilolayer NAND, and where inference dollars actually go"
date: 2026-10-11
sources:
  - https://thesemiconductornewsletter.substack.com/p/weekly-monitor-on-semiconductor-process-9f8
  - https://x.com/deedydas/status/2109118089438896576
  - https://x.com/rohanpaul_ai/status/2109092433065906357
  - https://x.com/rohanpaul_ai/status/2109025847835529580
  - https://the-decoder.com/few-people-pay-for-ai-but-those-who-do-spend-bigonly-a-few-users-pay-for-ai-but-those-who-do-pay-a-lot/
tags: [semiconductor, lithography, nand, compute-economics, token-pricing]
---

# Hyper-NA EUV, kilolayer NAND, and where inference dollars actually go

**Sources:** [The Semiconductor Newsletter weekly process monitor](https://thesemiconductornewsletter.substack.com/p/weekly-monitor-on-semiconductor-process-9f8) (Gmail) · X Following feed (@deedydas, @rohanpaul_ai citing SemiAnalysis and the FT, @StockSavvyShay) · [The Decoder on a16z's Top 100](https://the-decoder.com/few-people-pay-for-ai-but-those-who-do-spend-bigonly-a-few-users-pay-for-ai-but-those-who-do-pay-a-lot/) · AI Weekly Espresso (Nikkei on iPhone orders)
**Raw:** `raw/gmail/2026-10-11-newsletters.md` (private), `raw/twitter/feed/2026-10-11-morning-ranked.json`

## TL;DR

**Supply side (process research).**
- **Hyper-NA EUV (ZEISS + ASML, JMM).** A concept for a scanner with numerical aperture of at least 0.75, past today's 0.55 High-NA. Target resolution is about 5 nm half-pitch vs about 8 nm. It keeps the 13.5 nm source and today's mask platform. Cost: even shallower depth of focus, so resist thickness, stochastic defects, mask 3D effects and overlay all tighten. A concept, not a roadmap.
- **Kilolayer 3D NAND (arXiv perspective).** Roadmaps now contemplate about 1,000 layers. The argument: scaling stops being a lithography/etch problem and becomes a coupled charge-storage problem, where lateral charge migration, cell coupling, read disturb and poly-channel resistance squeeze the operating window together. Relevant to the HBM/NAND supply story this wiki tracks, since NAND tiers increasingly hold offloaded KV cache.
- **Others.** Deterministic MoS2 nucleation (>99% single-crystal yield, 430°C growth, Nature); vacuum HF/H2O oxide etch controlled by a liquid-like layer; 6 nm conformal ferroelectric HZO in 3D vias (needs ~500°C); Samsung Foundry + Synopsys closed-loop failure analysis cut turnaround over 80% (about 4 hours to 30 minutes per die).
- **Demand pressure, downstream.** Apple reportedly cut October iPhone 18 Pro component orders 15-20%, blaming AI-driven memory price surges.

**Demand side (where the tokens are paid for).**
- **OpenRouter in dollars.** Converting OpenRouter's public token stats to spend gives about $1.5B annualized, roughly 1% of all inference by dollars. This week Anthropic took 36% of spend, OpenAI 18%, open-weight models 26%.
- **Subsidy gap.** SemiAnalysis estimates Anthropic's inference business at about 88% blended post-compute margin, with subscriptions served at about 50%. Implication: subscribers get roughly 4x more compute per dollar than API buyers.
- **Price mix shift.** A circulating claim (unsourced) says average token prices fell over 50% since May, mostly because ~60% of top traffic moved to open models at ~$0.83/M vs ~$6.03/M.
- **Consumers.** a16z: 4.5% of US consumers pay for ChatGPT, Gemini or Claude; the top 1% of payers average about $900/month (up 79% since early 2025) and account for nearly a fifth of observed spend, mostly building tools.
- **Open models meet the chip vendor.** The FT reports Nvidia is in early talks to acquire or further invest in Reflection AI ($25B valuation; Nvidia already invested $800M), possibly as a Groq-style acqui-hire ($20B, last December) that avoids full antitrust review. Reflection's Beam is a 501B/23B-active MoE claiming GLM 5.2-level coding at 3-4x less inference compute.

## Relation to prior wiki pages

- **Extends** [compute economics](compute-economics.md): Lambert's 10-10 claim that the effective cost of intelligence falls fast now has a mechanism on the demand side. Most of the price drop is mix shift to open weights and routing, not list-price cuts.
- **Confirms** [inference memory tiers (10-04)](2026-10-04-inference-memory-tiers-and-cycles.md): memory, not logic, is where AI demand hits consumer electronics first.
- **Industry vs research gap.** The kilolayer NAND paper says each extra layer makes reads noisier, while KV-offload systems ([SparseEngine, 10-10](../inference-efficiency/2026-10-10-sparseengine-sparse-first-inference.md)) assume NAND as a cheap, reliable tier. No serving paper yet models read-disturb or retry latency at that tier.
