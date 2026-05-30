---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.28424
url: https://huggingface.co/papers/2605.28424
arxiv_url: https://arxiv.org/abs/2605.28424
date: 2026-05-30
---

# Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

Equipping large language models with explicit skills has emerged as a promising paradigm for enabling autonomous agents to solve complex tasks. Agent skills can be inherently divided into general skills for broad cognitive transfer and task-specific skills for dynamic execution. However, existing skill-based reinforcement learning (RL) methods typically force a rigid choice between full externalization, which incurs prohibitive context overhead, and full internalization, which risks overfitting and knowledge conflicts. To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization. Driven by a dynamic, difficulty-aware router, Skill0.5 streams tasks into distinct mastery tiers to apply tailored optimization strategies: it internalizes general skills via privileged distillation to build a cognitive foundation for hard tasks, while using diagnostic probing on easy tasks to penalize shortcuts and enforce specific skill utilization. Experiments on ALFWorld and WebShop demonstrate that Skill0.5 outperforms both memory-based and skill-based RL baselines, yielding performance improvements across both in-distribution and out-of-distribution scenarios.
