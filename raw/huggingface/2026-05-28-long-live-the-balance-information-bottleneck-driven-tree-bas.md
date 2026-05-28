---
source: farmer/huggingface
farmed: 2026-05-28T03:59:53Z
arxiv_id: 2605.28109
url: https://huggingface.co/papers/2605.28109
arxiv_url: https://arxiv.org/abs/2605.28109
date: 2026-05-28
---

# Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization

Recent advances in online reinforcement learning (RL) for large language models (LLMs) have demonstrated promising performance in complex reasoning tasks. However, they often exhibit an imbalanced exploration-exploitation trade-off, resulting in unstable optimization and sub-optimal performance. We introduce IB-Score, a novel metric grounded in Information Bottleneck theory that evaluates policy's exploration-exploitation balance by quantifying the trade-off between step-level reasoning diversity and mutual information shared with the correct answer. Analysis based on IB-Score shows that popular online RL approaches (e.g., GRPO) with common regularizers fail to consistently maintain balance during training with suboptimal results. To address this, we propose Information Bottleneck-driven Tree-based Policy Optimization (IB-TPO), a principled framework that formulates IB-Score as a fine-grained optimization objective and utilizes a novel IB-guided tree sampling strategy that not only improves the efficiency of online sampling with 50% more trajectories under the same token budget, but also reuses the tree structure for effective IB-Score Monte Carlo estimation. Extensive experiments across standard benchmarks show that our method significantly outperforms GRPO baseline by 2.9% to 3.6% and also outperforms other state-of-the-art online RL approaches. Our code is available at https://github.com/alibaba/EfficientRL.
