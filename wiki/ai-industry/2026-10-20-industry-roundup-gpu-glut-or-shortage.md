# Industry roundup 2026-10-20: GPU glut or GPU shortage?

**Sources:** The Decoder RSS (2026-10-19), AI lab feeds, X home feed (Business Insider, Gartner, Morgan Stanley, Goldman, company posts surfaced by @rohanpaul_ai, @StockSavvyShay, @edzitron and others). Raw: `raw/rss/2026-10-19-the-decoder-*.md`, [`raw/labs/2026-10-20-100728-labs.md`](../../raw/labs/2026-10-20-100728-labs.md); X captures gitignored.

## The split signal

- **Glut evidence.** Business Insider reports Amazon has warehouses of GPUs it cannot install and an "early rack receipt" program taking about **$3B a month** in GPUs with no clear path to installation. Critics read it as Nvidia channel stuffing.
- **Shortage evidence.** Nebius spot pricing for B200s reportedly **more than tripled in a week**. IREN's CEO says 2026 capacity is sold out, new contracts are priced at more than double last year's, and "bringing GPUs online" is the bottleneck. Anthropic is reportedly in talks for another 460 MW at Nscale's Monarch campus after a **$45B, 6-year** deal for the first 460 MW.
- **Reconciliation:** both are true if the constraint is powered, cooled floor space, not chips. GPUs pile up where buildings are late; rentable, powered GPUs get scarce. This matches SemiAnalysis (10-19): leases are signed, construction and power set the pace.

## Forecasts

- **Morgan Stanley:** 2027 hyperscaler + neocloud AI spend of **$1.58T** once leases are counted as capex; Nvidia takes about **$690B (44%)**; ~$550B flows to Korean memory makers, Taiwanese ODMs and private firms. 2027 is the projected peak cash shortfall.
- **Gartner:** ~$1T AI infrastructure spend in 2026 and **$6T in 2027-2030**; more than **$3.5T may need write-downs by 2030** because revenue will not cover cost before chips are replaced. Neoclouds most exposed.
- **Goldman on CoreWeave:** ~15% unlevered IRR even if GPUs are worth zero after five years; new contracts at ~$13M/MW vs ~$10M/MW blended; ~3-year payback vs ~2 for IREN and Nebius.
- **The Decoder:** executives expect only **7-10 of hundreds of neoclouds** to survive; customers outside hyperscalers are **45% of Nvidia's datacenter revenue**.

## Products, models, policy

- Meta Prometheus details and Muse Glimmer 30B open-weight report ([summary](../hardware/2026-10-20-meta-prometheus-supercluster.md)).
- MiniMax M3.1 Flash: 42 on the Artificial Analysis index (+13), 73.7% DeepSWE v1.1 under $0.30/task, $0.60 per million output tokens, 1M context.
- DeepSeek-V4.1-Flash-1017 (Max) is #1 open model in Arena's Agent Arena, #11 overall.
- Inception Mercury 3, a diffusion LLM: 4-8x faster than comparable small models at the same price; OpenRouter shows 2-4x effective.
- Kling 4.0 video (30 s clips, 10 keyframes) holds level with Wan 3.0 and Seedance 2.5, does not pull ahead.
- Exa 3.0 search; OpenAI low-resource language coding (COBOL, Fortran, Visual Basic evals); Together Post-Training (RL/SFT service, Tinker-compatible, launches with Muse Spark Open, GLM 5.3, Kimi K3, Qwen 3.8-27B); TwelveLabs Pegasus 1.5 on Bedrock; Salesforce Launa-Omni voice model; AWS TorchNeuron.
- Nvidia Vera CPU deal with Modal (reported 2x capacity for agent workloads); Nvidia targets ~$20B CPU revenue this fiscal year.
- Marvell shows photonic memory modules that place HBM and DDR up to 50 m from the GPU at hundreds of ns latency.
- DHS orders civilian agencies to remove DeepSeek and products built on it, including US-hosted weights.
- Two German courts (Munich, Aachen) now treat Google AI Overviews as Google's own content for liability.
- Anthropic's leaked AI safety bill draws criticism for a "50 deaths" harm threshold. Anthropic Public Benefit Fund (5% of shares) draws Musk's counter-proposal.
- Stripe says agent purchases through Link are growing; no numbers.
- Germany signs a Joint Declaration of Intent with Nvidia on industrial AI.

## Funding and valuations

- **Greptile** $50M Series B led by Menlo Ventures at **$750M**; reviews over 1% of GitHub PRs daily.
- An agent web-access startup raised **$9M** led by General Catalyst (via YC).
- **Polsia**: $20M run rate in 340 days, $30M raised at $250M; its AI bill peaked at $1.2M a month before moving to open models on rented GPUs.
- **Anduril** employee share sale near **$90B**, up from ~$30B 16 months ago.
- **Anthropic IPO chatter**: Eric Schmidt's ~1% stake would be worth ~$20B at a $2T listing (unconfirmed).
- A $10M European compute-grant program backed by Nvidia and Accel for open models, coding agents and inference.
