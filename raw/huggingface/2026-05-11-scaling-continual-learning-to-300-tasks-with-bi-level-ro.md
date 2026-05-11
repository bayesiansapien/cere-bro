---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2602.03473
url: https://huggingface.co/papers/2602.03473
arxiv_url: https://arxiv.org/abs/2602.03473
date: 2026-05-11
---

# Scaling Continual Learning to 300+ Tasks with Bi-Level Routing Mixture-of-Experts

Continual learning, especially class-incremental learning (CIL), on the basis of a pre-trained model (PTM) has garnered substantial research interest in recent years. However, how to effectively learn both discriminative and comprehensive feature representations while maintaining stability and plasticity over very long task sequences remains an open problem. We propose CaRE, a scalable Continual Learner with efficient Bi-Level Routing Mixture-of-Experts (BR-MoE). The core idea of BR-MoE is a bi-level routing mechanism: a router selection stage that dynamically activates relevant task-specific routers, followed by an expert routing phase that dynamically activates and aggregates experts, aiming to inject discriminative and comprehensive representations into every intermediate network layer. On the other hand, we introduce a challenging dataset, OmniBenchmark-1K, for CIL performance evaluation on very long task sequences with hundreds of tasks. Extensive experiments show that CaRE demonstrates leading performance across a variety of datasets and task settings, including commonly used CIL datasets with classical CIL settings (e.g., 5-20 tasks). To the best of our knowledge, CaRE is the first continual learner that scales to very long task sequences (ranging from 100 to over 300 non-overlapping tasks), while outperforming all baselines by a large margin on such task sequences.
