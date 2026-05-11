# Conductor: Learning to Orchestrate Agents in Natural Language

**arXiv:** [2512.04388](https://arxiv.org/abs/2512.04388) · **Venue:** ICLR 2026 · **Date:** Surfaced 2026-05-11
**Authors:** Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang (Sakana AI)
**Tier:** 1 — Routing (model-level orchestration as a learned policy)
**Cross-source confirmed:** DAIR.AI Top Papers of the Week (Gmail) + @burkov retweet via @bayesiansapien (Twitter morning slot)

## TL;DR

A 7B language model trained with reinforcement learning learns to orchestrate larger frontier models (GPT-5, Claude Sonnet 4, Gemini 2.5 Pro) by writing natural-language subtasks, assigning each to one of the workers, and specifying which previous outputs that worker sees in context. The resulting system outperforms every individual frontier model on GPQA Diamond, LiveCodeBench, and AIME25, while averaging about three model calls per question. The Conductor is trained against randomized agent pools, which means it generalizes to agent mixes it never saw during training. When allowed to pick itself as a worker, it forms recursive topologies, producing a new form of dynamic test-time scaling through online iterative adaptation. The 3 percent average gain over the best individual worker is the size of a generational improvement between frontier model versions.

## What makes this a routing paper, not a multi-agent paper

The framing matters. Multi-agent LLM systems have been around for two years. The typical setup hardcodes the topology (e.g. Plan-Execute-Reflect) and the prompts, then evaluates whether the ensemble beats a single agent. The Conductor inverts that. The topology is the policy. The orchestrator decides, per query, who talks to whom and what each one is told. The 7B model is not a worker, it is a router with a learned RL policy. The output of the router is a natural-language plan that the workers execute.

The single RL policy decides two things at once: communication topology and per-worker prompt content. That dual objective is what makes it a learnable orchestrator rather than a wrapper. Topology design produces the workflow graph; prompt content steers each worker toward what it is individually good at.

## Why three model calls per question is the load-bearing number

The Conductor uses approximately three model calls per question on average, which is fewer than the multi-agent pipelines (typically 5 to 12) and self-reflection loops it beats. This is the production-relevant axis. A multi-agent ensemble that beats single-model performance by 3 percent but costs 4x is not a deployment win. A 7B-orchestrated ensemble that beats single-model performance by 3 percent and costs roughly 3x (where the orchestrator itself is cheap) is.

The pricing math is the production interpretation. Routing 3 calls across GPT-5, Claude Sonnet 4, and Gemini 2.5 Pro with a 7B orchestrator on top is cheaper than 3 calls to the most expensive single model when the orchestrator picks the cheaper worker for the subtask that does not need the frontier model. The economics of this paper are routing economics, not multi-agent economics.

## Recursive topologies as a test-time scaling axis

When the Conductor is allowed to pick itself as a worker, recursive topologies emerge. This is the architecturally interesting result. Test-time scaling so far has been about reasoning longer (more tokens) or sampling wider (more rollouts). Recursive orchestration is a third axis: the same model running its own routing decisions at multiple levels of recursion.

The composition with the wiki's existing trajectory-routing thread is clean. Step-level Optimization for Computer-Use Agents (05-02) routes the model axis per agent step. The Conductor routes both the model axis and the subtask axis per query. Stacking them is the next natural research move: a Conductor that itself produces a trajectory of step-level routing decisions.

## Relation to prior wiki coverage

The wiki has been tracking three routing axes (query-level, provider/tier-level, trajectory-level) on the [LLM Routing concept page](llm-routing.md). The Conductor is the cleanest example so far of the model-level routing axis: the orchestrator is the model, and the routing policy is learned end-to-end.

This is the third paper this week converging on "the orchestrator should be the model, not the wrapper":
- **HeavySkill (DAIR.AI weekly)** internalizes parallel reasoning plus deliberation as a learnable inner skill via RLVR, so harness wins look like model wins.
- **Conductor (this paper)** learns the topology itself as an RL policy.
- **CaRE (HF 05-11)** moves routing inside the network as a bi-level MoE primitive.

Three independent papers in one week claiming that the right place for routing is inside the policy, not around it. The wiki's [LLM Routing](llm-routing.md) page now needs a fourth axis: model-internal routing as a primary architectural surface.

## Research angle

**Cache-aware orchestration.** SemiAnalysis (05-01) noted that Anthropic's effective pricing on agentic workloads is driven by 90 percent prompt cache hits. The Conductor distributes calls across providers, which breaks cache locality at the provider boundary. A cache-aware Conductor that prefers to stay within a single provider when the cache hit value exceeds the routing benefit is the obvious extension.

**Adversarial Conductors.** The Conductor is trained against randomized agent pools, which gives it robustness to agents it never saw. The natural follow-up is to introduce adversarial agents into the pool (agents that respond unreliably or with adversarially crafted outputs) and see whether the policy learns to detect and route around them. This is the routing-as-safety axis the wiki has flagged but no paper has measured.

**Pricing comparison at frontier cost.** The 3 percent quality gain is meaningful, but the production number is the cost-quality Pareto front. A direct comparison between (Conductor over 3 frontier models) and (single frontier model at extended thinking budget matched to the same dollar cost) is the comparison that would settle the production deployment question.

## Links

- [arXiv 2512.04388 (PDF)](https://arxiv.org/pdf/2512.04388)
- [DAIR.AI Top AI Papers of the Week (LinkedIn)](https://www.linkedin.com/pulse/top-ai-papers-week-dair-ai-z7dke)
- [@burkov retweet via @bayesiansapien](https://nitter.net/burkov/status/2053636186082521136#m)
- [ChapterPal AI summary](https://www.chapterpal.com/s/3c66a829/learning-to-orchestrate-agents-in-natural-language-with-the-conductor)
- [LLM Routing concept page](llm-routing.md)
- [CaRE (same-day bi-level routing MoE)](2026-05-11-care-bi-level-routing-moe-continual-learning.md)
