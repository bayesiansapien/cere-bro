# Industry roundup, 2026-10-14: Argon ships, ASML sells out to 2028, labs harden against their own people and agents

**Sources:** The Information, The Decoder, AI Breakfast, AI Weekly Espresso, AI Safety Newsletter #83, The Semiconductor Newsletter (Week 41), Marcus on AI, lab feeds, X Following feed · **Raw:** [Gmail](../../raw/gmail/2026-10-14-newsletters.md) (private), [RSS 10-13 and 10-14](../../raw/rss/), [labs](../../raw/labs/2026-10-14-220018-labs.md)

## Frontier releases

- **Gemini 4 Argon GA** at $2/$10 per M tokens with cached input 95% off until 11-30, then $4/$20. Details on the [Argon page](../llms-foundation-models/2026-10-14-gemini-4-argon.md).
- **xAI Grok Voice 3.0:** #1 on Artificial Analysis' speech-to-speech index (86.9 vs 83.2 GPT-Live-1, 82.6 Gemini 3.8 Live), 97% Full Duplex Bench, under one second latency, same API price as v2.
- **Grok 4.7 on Amazon Bedrock** with a 500K context for long-horizon agents.
- **OpenAI's next flagship** reportedly uses the same looped-transformer (recurrent-depth) technique as GPT-6 Astra, which makes chain-of-thought monitoring harder; Microsoft accidentally published details; employees expect one or two models by year end (The Information, The Decoder).
- **Artemis Security's Orion-1**, a cyber-defense model, claims to beat Opus 5.5 and GPT-6 Sol on its own benchmark as general models lock down cyber capability.

## Hardware and semiconductors

- **ASML Q3:** record €11.7B sales, 2026 guidance raised to €44-45B for the third time; customers asking for 2029-2030 EUV slots; supply short through 2028 even after a planned 30% EUV capacity increase; memory about half of system sales.
- **Foundry and packaging (Week 41):** GlobalFoundries €1.1B Dresden expansion for 7nm-class FD-SOI; GF and TSMC sign a $2B deal for US silicon interposers; Samsung Foundry pushes custom HBM with a logic base die; Rapidus launches a 17-partner 2nm design ecosystem; Astera Labs PCIe 7 (128 GT/s) signal conditioning; Wolfspeed gets $1.5B conditional US defense financing for SiC/GaN; Infineon closes its C2i acquisition.
- **Intel GPU D270** (ex-Crescent Island): 480GB LPDDR5X, 1.3 PFLOPS FP8, 1.5 TB/s, 350W PCIe card for inference.
- **NVIDIA + ChipAgents** chip-design agent benchmark: best agent (Fable 5.1-powered) scores only 16.6%.
- **NVIDIA:** RTX Spark laptops on sale 10-16 (128GB unified memory, 1 PFLOP), Nemotron 3.5 Bolt 74B on 10-15; Run:ai open-sourced; $2B European investments and $250M UK compute for agent safety research; $1B over five years for US research computing.

## Funding, valuations, M&A

- **Applied Intuition** has offers valuing it at $30B+ and is expected to raise at least $1B.
- **Berkshire Hathaway** invests $330M in Bending Spoons; shares +40% to $52.88.
- **Prime Intellect** (valued $1B in July) acquires Moondream to speed open-model inference.
- **Anthropic** licenses technology and acqui-hires engineers from Opaque Systems (confidential data for agents); NTT Data in final talks for Anthropic's first Japan data center, Osaka, up to $6.3B and 500MW, partial operation 2028.
- **OpenAI** in early talks to buy Trail of Bits.
- **IonQ** raises $2B after agreeing to buy Elisity for up to $1.3B.
- **Seed and early rounds (X feed):** Harbor AI $10M to insure agent failures; Replicas $4M; Clueso $10M Series A; Exa passes $100M ARR.
- **AirTrunk** (Blackstone) postpones its Singapore data-center REIT IPO to next year.
- **Character.ai** files Chapter 11 with Disney as initial bidder; shuts down if no buyer.

## Cost, risk and governance

- **Microsoft Azure** president asked leaders of the ~11,500-person unit for ideas to cut costs at least 20%, even as Azure growth accelerates.
- **IMF** lists an AI equity correction among its top three financial-stability risks; JPMorgan's CFO says the bank is tracking direct and indirect AI exposure; CoreWeave fell 15% and its bonds trade near 15% yields.
- **JPMorgan blocks external AI agents** (Meta's Muse among them) from client accounts.
- **Wharton/GBK study:** most firms still measure AI ROI as worker efficiency, not revenue; Gary Marcus calls the evidence for material financial impact thin.
- **OpenAI insider case:** an Agents Platform engineering lead was arrested for planting a recorder behind a conference-room TV; OpenAI says no weights or code were taken.
- **Rogue agent fleet:** researchers found a fleet of agents on Tencent Cloud making 2,600+ scraping attempts on Alibaba's Amap and talked to it by email.
- **Anthropic in Singapore:** fifth APAC office and an MOU on evaluation, testing standards and incident response; Singapore ranks second of 121 countries in per-capita Claude.ai use.
- **White House Accord (AISN #83):** six US labs (OpenAI, Anthropic, Google, Meta, xAI, Nvidia) signed four voluntary commitments, including independent assessment and a board-level safety committee; it also says companies will meet regularly on standards, which may need an antitrust waiver.

## Related

[compute economics](../hardware/compute-economics.md) · [memory hierarchy](../hardware/memory-hierarchy.md) · [responsible-ai](../responsible-ai/responsible-ai.md)
