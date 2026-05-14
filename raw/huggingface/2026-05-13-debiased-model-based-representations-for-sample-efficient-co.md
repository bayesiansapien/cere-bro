---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.11711
url: https://huggingface.co/papers/2605.11711
arxiv_url: https://arxiv.org/abs/2605.11711
date: 2026-05-13
---

# Debiased Model-based Representations for Sample-efficient Continuous Control

Model-based representations recently stand out as a promising framework that embeds latent dynamics information into the representations for downstream off-policy actor-critic learning. It implicitly combines the advantages of both model-free and model-based approaches while avoiding the training costs associated with model-based methods. Nevertheless, existing model-based representation methods can fail to capture sufficient information about relevant variables and can overfit to early experiences in the replay buffer. These incur biases in representation and actor-critic learning, leading to inferior performance. To address this, we propose Debiased model-based Representations for Q-learning, tagged DR.Q algorithm. DR.Q explicitly maximizes the mutual information between the representations of the current state-action pair and the next state besides minimizing their deviations, and samples transitions with faded prioritized experience replay. We evaluate DR.Q on numerous continuous control benchmarks with a single set of hyperparameters, and the results demonstrate that DR.Q can match or surpass recent strong baselines, sometimes outperforming them by a large margin. Our code is available at https://github.com/dmksjfl/DR.Q.
