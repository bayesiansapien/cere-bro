---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819787+00:00
arxiv_id: 2609.36820
url: https://huggingface.co/papers/2609.36820
arxiv_url: https://arxiv.org/abs/2609.36820
date: 2026-10-02
---

# CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning

Group Relative Policy Optimization (GRPO) is widely used to train reasoning language models, where it computes advantages by centering and normalizing rewards across rollouts of the same prompt. For multiple rewards, GRPO sums the reward components and normalizes the total reward by its within-group standard deviation. The corresponding variance equals the sum of all pairwise reward covariances. For a fixed centered reward, larger aggregate covariance produces smaller advantages, and vice versa, allowing update magnitudes to adapt to reward dependence. However, correlated rewards with large scales can dominate this normalization and suppress signals from smaller-scale rewards. We propose Correlation-Normalized GRPO (CorrGRPO), which normalizes pairwise covariances into Pearson correlation coefficients. CorrGRPO keeps the centered total reward unchanged while balancing the influence of differently scaled rewards on the correlation-based normalization. This allows advantage magnitudes to adapt to reward correlations without the normalization being dominated by large-scale reward components. We compare CorrGRPO with GRPO and other variants on code generation, tool calling, and agent security, using models ranging from 0.5B to 8B parameters. These tasks all involve multiple rewards that can improve together or present tradeoffs. Results show improvements across three domains, including code generation, tool calling, and agent security. Our code is available at https://github.com/HKUST-KnowComp/CorrGRPO.
