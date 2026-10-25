# Token arbitrage and the neocloud squeeze

**Sources:** [@deedydas on inference-provider economics](https://x.com/deedydas/status/2114195317860266432); The Information, [A Neocloud's Gathering Storm](https://www.theinformation.com/articles/neoclouds-gathering-storm) and [Anthropic's Margin is OpenAI's Opportunity](https://www.theinformation.com/articles/anthropics-margin-openais-opportunity); [Arena Agent leaderboard](https://x.com/arena/status/2114008313054527901) · raw: `raw/twitter/feed/2026-10-25-morning-ranked.json`, `raw/rss/2026-10-24-the-information-*.md`
**Topic:** compute infrastructure, inference pricing

## TL;DR

Three views of the same market on one day. **Token resellers** make money: renting B300s on demand at about $8/GPU-hour, open models (GLM 5.3, Kimi K3, DeepSeek 4.1) can earn $10-20/GPU-hour at ~100 tok/s, and DeepInfer reports $38/GPU-hour off-peak. Margin depends on utilization and stack quality; gateways (OpenRouter, Vercel) aggregate demand, Chinese labs now ask large providers for revenue share for day-0 access, and dozens of providers launch weekly. Deedy's prediction: commodity service pushes compute prices up and token prices down. **Compute owners with debt** suffer: CoreWeave stock nearly halved in 12 days on rate fears and debt load; Meta's new share class to raise AI capital pulled the Nasdaq down 2.6% and CoreWeave 10%, Nebius 7.2%, IREN 8.3%. SpaceX now sells excess compute, a well-funded competitor. **Model vendors** compete on price: Rippling moved from 57% Anthropic / 16% OpenAI of coding work in May to 52% OpenAI / 18% Anthropic, citing cost.

## Relation to prior wiki pages

- **Extends** the 10-24 "memory sets the rent" item (H200 rent +160% vs H100 +40%): token prices fall while scarce-memory compute gets dearer, so the margin sits with whoever has cheap, memory-rich capacity and a good serving stack.
- **Ties to research:** every efficiency paper that raises tokens per GPU-hour (MOSAIC's 4x cache cut, LIRQuant's 3.5x memory saving, speculative decoding) moves a provider along deedy's throughput curve. The arbitrage is a stack-quality business.
- **Kimi K3.1 Pro** enters Arena's agent leaderboard at #11, top open model, $1.03 median cost per task (13% below K3), just off the Pareto frontier.
