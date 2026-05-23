# Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.22177](https://arxiv.org/abs/2605.22177)
**Authors:** Jinyang Wu, Guocheng Zhai, Ruihan Jin, Zhengqi Wen, Jianhua Tao (Tsinghua University), Yuhao Shen, Zhengxi Lu (Zhejiang University), Fan Zhang (CUHK), Haoran Luo (NTU), Zheng Lian (Tongji University).
**Code:** [github.com/jinyangwu/Maestro](https://github.com/jinyangwu/Maestro)

## TL;DR

Maestro is a routing system that learns, via reinforcement learning, when to call which model and which skill across a hierarchical registry of frozen experts. A 4B-parameter orchestrator outperforms GPT-5 and Gemini-2.5-Pro on ten multimodal benchmarks (70.1% vs 69.3% vs 68.7%) by composing ensembles of frozen expert models with a two-tier skill library. The policy is trained with outcome-only RL, no step-level supervision. Crucially, the policy generalizes to unseen models and skills without retraining: adding out-of-domain experts to the registry pushes accuracy to 59.5% on four challenging benchmarks, beating all closed-source baselines.

## Why this matters for routing

LLM routing has been mostly hand-engineered to date. Existing frameworks pick one model per call (mix-of-models with classifier-style routers) or one tool per call (function-calling style). Maestro reframes the problem: at each step the policy decides (a) whether to call an external expert at all, (b) which model-skill pair to invoke, and (c) when to terminate. The output is a learned coordination policy rather than a fixed dispatch table.

Three load-bearing claims:

1. **Outcome-only RL is enough.** No step-level reward shaping. The 4B orchestrator learns the routing policy from final-task success alone. This is the same setup as GRPO-style RLVR but applied to model-skill selection rather than token-level generation.

2. **A 4B router beats a frontier monolithic model.** With access to the right expert pool, a small router outperforms GPT-5 and Gemini-2.5-Pro on multimodal benchmarks. This is the strongest evidence to date that routing-with-experts is competitive with scale-up.

3. **The policy generalizes to unseen experts.** Adding out-of-domain experts to the registry without retraining yields 59.5% accuracy on four held-out benchmarks. This means Maestro is not memorizing which expert solves which problem: it is learning a meta-policy that recognizes when expert authority is needed.

## Architecture sketch

```
                ┌──────────────────────────────────────┐
                │      Maestro Policy (4B)             │
                │   trained with outcome-based RL      │
                └──────────────┬───────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       [call expert?]   [which model?]   [which skill?]
              │                │                │
              └────────────────┼────────────────┘
                               ▼
              ┌────────────────────────────────────┐
              │  Frozen expert pool                │
              │  + two-tier skill library          │
              │  (high-level skills,               │
              │   low-level tool primitives)       │
              └────────────────────────────────────┘
```

## Connections to prior wiki state

This is the third paper this month after [MiSA (mixture-of-indexer sparse attention, 05-11)](../inference-efficiency/2026-05-11-misa-mixture-of-indexer-sparse-attention.md) and the [GRAM "generative recursive reasoning" paper (HF 05-21)](../llms-foundation-models/) to argue that a learned coordinator with frozen experts beats a single large model. Maestro is the most direct test of the orchestration thesis on heterogeneous multimodal benchmarks.

It also extends the pattern flagged on 2026-05-13 around model routing: that small orchestrators with access to large frozen experts are becoming a viable architecture for frontier-equivalent performance at a fraction of inference cost.

## Gaps

The paper doesn't report inference latency or token-budget comparisons against monolithic frontier models. The 70.1% vs 69.3% comparison against GPT-5 is accuracy-only. The whole point of the orchestration thesis is unit-economics improvement; without latency and cost numbers, that part of the argument is implicit, not demonstrated.

The "registry expansion without retraining" claim is the most interesting result, but the four held-out benchmarks are not named in the abstract. Whether this is genuine cross-domain transfer or selection-favorable benchmark choice will matter.

## Research angle

The closest open problem this paper opens is whether the meta-policy for routing transfers across **task families**, not just across new experts within the same family. If a Maestro trained on math + chart reasoning can route effectively to a chemistry expert at test time, that is the foundation of an open-ended routing system. If it cannot, the policy is closer to a per-family dispatcher than a general orchestrator.

A second open angle: the policy is trained with outcome-only RL on final tasks. The hierarchy of skills (two-tier) is hand-designed. Whether the hierarchy itself can be learned: that is, whether the policy can discover its own skill abstractions: is the natural follow-up.

## Raw source

[raw/huggingface/2026-05-23-maestro-reinforcement-learning-to-orchestrate-hierarchical-m.md](../../raw/huggingface/2026-05-23-maestro-reinforcement-learning-to-orchestrate-hierarchical-m.md)
