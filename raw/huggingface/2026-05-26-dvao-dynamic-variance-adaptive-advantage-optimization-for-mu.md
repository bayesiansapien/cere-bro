---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.25604
url: https://huggingface.co/papers/2605.25604
arxiv_url: https://arxiv.org/abs/2605.25604
date: 2026-05-26
---

# DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning

Reinforcement Learning has become a standard paradigm for aligning Large Language Models with human intent and task requirements. While Group Relative Policy Optimization offers an efficient, value-model-free alternative to Proximal Policy Optimization, adapting it to real-world multi-reward settings remains challenging. Standard scalarization practices, such as Reward Combination and Advantage Combination, suffer from significant drawbacks: Reward Combination frequently generates advantages with excessively large squared magnitudes that lead to training instability, while Advantage Combination relies on static hyperparameters and ignores cross-objective correlations. To address these limitations, we propose Dynamic Variance-adaptive Advantage Optimization (DVAO), which dynamically adjusts combination weights based on the empirical reward variance of each objective within a rollout group, effectively up-weighting objectives with a stronger learning signal while suppressing noisy ones. We mathematically prove that DVAO maintains bounded advantage magnitudes for stable training and introduces a self-adaptive cross-objective regularization mechanism. Extensive experiments on mathematical reasoning and tool-use benchmarks using Qwen3 and Qwen2.5 models demonstrate that DVAO significantly outperforms baseline methods, achieving a superior multi-objective Pareto frontier and robust training stability.
