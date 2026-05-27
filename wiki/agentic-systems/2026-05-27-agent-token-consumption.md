# How Do AI Agents Spend Your Money? Token Consumption in Agentic Coding

**Source:** Twitter curated retweet (@jiqizhixin / @rohanpaul_ai) · arxiv 2604.22750
**Authors:** Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei (Michigan, Stanford, AllHands AI, Google DeepMind, MIT)
**arxiv:** [2604.22750](https://arxiv.org/pdf/2604.22750) · [project site](https://longjubai.github.io/agent_token_consumption/)
**Date:** 2026-05-27 (surfaced via Twitter; paper April 2026)
**Raw:** [raw/twitter/2026-05-27-morning.md](../../raw/twitter/2026-05-27-morning.md)
**Tier:** 2 (agentic systems, with efficiency/cost intersection)

## TL;DR

The first quantitative study of where coding agents actually spend tokens. The authors analyze trajectories from eight frontier LLMs on SWE-Bench Verified using the open OpenHands framework, and test whether models can predict their own cost before running a task. Three headline results: agentic coding is uniquely expensive (it consumes substantially more tokens than code reasoning or code chat, with input:output ratios as high as 154:1 because history and tool outputs get re-fed every turn); spend is high-variance and only weakly tied to accuracy (the most expensive task can cost ~7M more tokens than the cheapest, the same task re-run varies ~2x, and accuracy peaks at *intermediate* cost rather than rising with spend); and frontier models systematically underestimate their own token usage before execution.

## Key findings

- Agentic coding consumes exponentially more tokens than code reasoning or code-QA chat, driven by multi-turn interaction and large, growing context (every code query and file dump re-enters the history). Observed input:output ratio up to **154:1**.
- Cost is highly stochastic: across 500 SWE-Bench-Verified tasks, the priciest task can run ~7M tokens above the cheapest, and variance grows with cost. Even repeated runs of one task differ ~2x between cheapest and priciest.
- **More spend does not buy more accuracy.** Accuracy peaks at intermediate token cost, then flattens or declines, so naive "let it think longer" budgeting is wasteful.
- Models cannot price their own work: all eight frontier models underestimate token consumption before task execution, so self-budgeting agents misjudge difficulty.

## Relation to prior wiki state

This is the empirical underside of the cost story the wiki tracked all week. [The Efficiency Frontier (05-27)](../inference-efficiency/2026-05-27-efficiency-frontier-context-cost.md), which models context-strategy selection as a deployment-aware optimization and finds accuracy plateaus while cost keeps climbing, predicts exactly the "accuracy peaks at intermediate cost" curve this paper measures in the wild. Together they say: the marginal token in a long agentic run is usually wasted, and nobody, not even the model, knows where the plateau is.

It also gives a concrete number to Gary Marcus's bubble argument (Gmail, 05-26): Uber's COO reporting no proportional productivity gain after blowing through the annual AI token budget in months is the macro version of "the same task varies 2x and accuracy doesn't follow spend." And it sharpens the harness argument in [Scaling the Harness (05-27)](2026-05-27-scaling-the-harness.md): if agent behavior emerges from the orchestration stack, then context-management discipline in the harness is where the 154:1 ratio gets fixed.

## Why it matters

Token cost is now the binding constraint on agentic-coding deployment economics, not capability. A finding that frontier models cannot predict their own spend means cost governance has to live in the harness (budget caps, context pruning, early-stop on plateau), not in the model. Expect "agent cost telemetry" and per-trajectory budget guards to become standard in coding-agent platforms.

## Gaps

Single benchmark (SWE-Bench Verified) and one harness (OpenHands); whether the 154:1 ratio and the intermediate-cost-accuracy peak hold on other agentic domains (browser agents, deep research) is untested. The study measures consumption, not a fix.

## Links

- [Paper PDF](https://arxiv.org/pdf/2604.22750) · [Project](https://longjubai.github.io/agent_token_consumption/)
- Raw: [raw/twitter/2026-05-27-morning.md](../../raw/twitter/2026-05-27-morning.md)
- Related: [The Efficiency Frontier 2026-05-27](../inference-efficiency/2026-05-27-efficiency-frontier-context-cost.md), [Scaling the Harness 2026-05-27](2026-05-27-scaling-the-harness.md)
