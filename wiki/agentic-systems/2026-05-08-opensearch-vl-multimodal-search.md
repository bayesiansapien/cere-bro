# OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

**arXiv:** [2605.05185](https://arxiv.org/abs/2605.05185)
**Authors:** Shawn Chen, Hangting Chen, Tianyu Pang (Tencent Hunyuan); Quanxin Shou (UCLA, HKU); Kaituo Feng, Wenxuan Huang, Dasen Dai, Yunlong Lin, Xiangyu Yue (CUHK); Shenghua Gao (HKU)
**Tier:** 2 — agentic-systems / multimodal

## TL;DR

The first fully-open training recipe for multimodal deep-search agents the wiki has tracked. Open data, open environment, open RL algorithm. Targets three concrete bottlenecks: (1) shallow perception-level queries that don't trigger real tool use, (2) lack of robust visual pre-processing for imperfect inputs, (3) cascading tool failures invalidating RL rollouts in long-horizon tool-use.

## The three bottlenecks (and OpenSearch-VL's response)

```
Bottleneck                      OpenSearch-VL response
─────────────────────────       ──────────────────────────────────────
Shallow queries that don't  ──► training data designed for multi-hop
trigger real tool use            agentic interactions, not single-shot
                                 visual QA

Imperfect visual inputs     ──► robust visual pre-processing built into
(blurred, low-res, skewed)       the agent loop, treated as a first-class
                                 capability not an after-thought

Cascading tool failures     ──► RL algorithm designed to extract partial
in long-horizon tool-use         credit from partially-successful
                                 trajectories without amplifying noise
                                 from failed gradients
```

## The data + environment + recipe argument

OpenSearch-VL's structural claim is that the gap between proprietary frontier multimodal agents and open recipes is not algorithmic, it's data-and-infrastructure. The proprietary labs' moat is:
- Proprietary training data
- Lack of transparent trajectory synthesis pipelines
- Insufficiently detailed training recipes

The paper closes the gap by releasing all three. If the structural claim is right, the open ecosystem catches up faster than the closed-vs-open trajectory in pure LLMs would predict.

## How this relates to prior wiki work

- **Open-recipe analog of the build-not-buy mentality** Lambert documents in his [China AI labs piece](../ai-industry/2026-05-08-lambert-china-ai-labs.md) (today). Tencent Hunyuan + CUHK + HKU is exactly the cohort Lambert visited. The "data industry is far less developed in China, so labs build their own" pattern shows up here as "we built the open recipe ourselves."
- **Companion to [today's Rethinking Reasoning-Intensive Retrieval](2026-05-08-rethinking-reasoning-intensive-retrieval.md)** from the Yale NLP Lab. Different geography, similar critique. Existing benchmarks evaluate retrievers in isolation rather than within the agentic loop they actually serve. Both papers argue the retriever-vs-agent distinction is the wrong frame.
- **Connection to [agent-benchmarks](../agentic-systems/agent-benchmarks.md)** concept page. OpenSearch-VL is closer to a recipe than a benchmark, but it includes evaluation and the data is benchmark-shaped.
- **Lateral to [tool-calling concept page](../agentic-systems/tool-calling.md)** for the cascading-tool-failure RL sub-problem.

## What's surprising

The paper's RL-on-long-horizon-tool-use claim is the most interesting unsolved sub-problem. When 4 of 7 tool calls succeed and 3 fail, current RL approaches either (a) treat the whole trajectory as failed and ignore the partial credit, or (b) treat the whole trajectory as successful and pollute the policy with bad signal from the failed sub-steps. OpenSearch-VL's claim is that they extract the partial credit cleanly. The paper does not yet have a head-to-head against [t2po](../agentic-systems/2026-05-05-t2po-uncertainty-multi-turn-rl.md) (05-05), which is the wiki's other 2026-05 paper on uncertainty-aware multi-turn RL.

## Open questions

1. **Head-to-head vs t2po and Step-Level Optimization.** Three papers from the past two weeks are all working on uncertainty + partial-credit + trajectory-level RL for tool-use agents. Comparative evaluation on shared benchmarks is the next step.
2. **Cross-modal generalization.** OpenSearch-VL is multimodal-search-specific. Whether the partial-credit RL recipe transfers to non-search agentic domains (e.g., coding agents, GUI agents) is open.
3. **Reproducibility test.** The "open recipe" claim has to be tested by an independent reproduction. The paper releases code, data, and training scripts, but no third-party reproduction is yet on the record.

## Why it matters

OpenSearch-VL plus today's [ResRL](../llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md) plus the [Rethinking Reasoning-Intensive Retrieval](2026-05-08-rethinking-reasoning-intensive-retrieval.md) all share a structural argument that 2026's open-research moat is data, environments, and recipe completeness, not algorithm. If that's right, the next year of agentic RL is a competition over which open lab releases the cleanest recipe rather than which proprietary lab discovers the cleverest algorithm.
