# What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record

**Source:** HuggingFace Daily Papers · [arXiv 2609.05663](https://arxiv.org/abs/2609.05663) · DX Terminal Pro and DXAP fleets
**Raw:** [`raw/huggingface/2026-09-09-what-llm-trading-agents-actually-do-in-production-a-six-mont.md`](../../raw/huggingface/2026-09-09-what-llm-trading-agents-actually-do-in-production-a-six-mont.md)

## TL;DR

The largest field measurement of autonomous LLM agents this wiki holds, and its headline finding is a harness result dressed as a finance result. Six months, two production fleets sharing one design lineage (3,505 user-funded vaults trading real ETH in Base memecoin markets, plus 500 to 599 user-created agents trading Hyperliquid perpetuals), **7.5M single-model invocations, roughly 300K onchain actions, a further 231,638 multi-tool turns producing 14,596 fills.**

**Finding one is the one that belongs on the harness page: the operating layer determines behavior more than anything written in strategy text.** A risk slider explains leverage at **+0.425 per level**. Agent fixed effects absorb **60% of variance**. And a **leaderboard render boundary causally routes selection**, with a regression discontinuity of **1.75x at the top-3 cut**. That last one is the sharpest: where the UI stops drawing the list changes which agents get chosen and therefore what capital does.

## The other three findings

- **Sizing is volatility-blind.** Median leverage is **5.0x in every volatility sextile**. The agents do not scale exposure to risk at all. One posture-slider cell holding 11% of the book accounts for **62% of liquidations**.
- **Agents capture almost none of the upside they reach.** 43.2% of positions saw at least +300 bps of favorable excursion within 24h, yet **49.3% of those closed with a negative trade return**. A mechanical bracket order recovers **+39.0 bps per position**. The agents get there and give it back; a dumb rule fixes it.
- **No directional edge, in either fleet.** DXAP is not profitable and trails a matched Hyperliquid retail benchmark on roundtrip win rate, **41% against 50%**. A paired-replay league of frontier models across 416 captured production scenarios finds **decision quality statistically indistinguishable** at this horizon, though **choice stability differs sharply across model families**.

Every headline survives day-clustered inference, permutation nulls and a common-fee restatement. The paper closes with a 17-rule methodology canon the authors say was bought with their own retractions.

## Why this matters outside trading

**It is the largest independent confirmation of the harness thesis on this wiki, and it comes from a domain that had no stake in the argument.** The [agent harness engineering page](agent-harness-engineering.md) claims the harness, not the model, is the primary object of design and cost. Almost all of its evidence is benchmark work by people who set out to prove it. Here a six-month production record with real money, built by people trying to make trading agents work, finds that **agent fixed effects absorb 60% of variance and a slider position predicts leverage while the strategy prose predicts nothing measurable.** That is the claim tested where it is expensive to be wrong.

**The model-indistinguishability result is the sharper half and it cuts against a lot of procurement behavior.** Frontier models replayed on 416 real production scenarios produce statistically indistinguishable decision quality. What differs is **choice stability across model families**, which is a harness-relevant property (how much does the same input move the output) rather than a capability one. This lines up with [Iris (09-07)](2026-09-07-iris-search-agents.md), which found the inference-time context policy outweighs most reported model differences, and with the routing literature's repeated finding that the expensive part is not picking the model.

**The leaderboard-render-boundary result deserves to be carried on its own.** It is a rare causal identification of a *user interface* changing agent-mediated capital allocation. Any system where agents are selected by a ranked display inherits this, and nobody designing agent marketplaces is measuring it.

**Read against [the loop-is-an-asset essay (09-09)](2026-09-09-loop-as-asset-bounded-self-improvement.md), it is the failure case that essay warns about, at scale.** Lorica's argument is that a self-improvement loop becomes very good at optimizing what it can see. These fleets optimized within slider defaults and leaderboard position, which is what the operating layer could see, while directional edge, the thing anyone cared about, never moved.

## Gaps

- Both fleets share one design lineage, so "the operating layer dominates" may be a property of *this* operating layer. A second, differently designed fleet is the replication.
- Crypto perpetuals and memecoins are an unusually adversarial and high-noise environment; the null on directional edge may not transfer to slower markets.
- The 416-scenario paired replay is a small sample for a claim of model indistinguishability, and the paper says "at this horizon," which is the right hedge.

## Related

- [Agent Harness Engineering](agent-harness-engineering.md) (concept page)
- [Agent Benchmarks](agent-benchmarks.md) (concept page)
- [Iris: search agents and context policy (09-07)](2026-09-07-iris-search-agents.md)
- [Your AI model is a rental, but the loop is an asset (09-09)](2026-09-09-loop-as-asset-bounded-self-improvement.md)
