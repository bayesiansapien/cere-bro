---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37372
url: https://huggingface.co/papers/2609.37372
arxiv_url: https://arxiv.org/abs/2609.37372
date: 2026-09-30
---

# Think Before You Score: Thinking Reward Model for Visual Generation

Visual reward models are essential for evaluating and improving visual generation models, yet existing approaches typically map task conditions and candidate outputs directly to scalar rewards, leaving implicit what should be evaluated for each individual case. We introduce Think Before You Score, a paradigm that explicitly determines what matters for each case before judging how well the candidate performs. Following this principle, we propose the Thinking Reward Model (TRM), which formulates case-adaptive rubrics, performs rubric-guided assessment, and produces fine-grained pointwise rewards. We further observe that conventional pairwise preference optimization can induce score polarization, and introduce Pairwise Dual-Group Relative Policy Optimization (PD-GRPO), which leverages pairwise supervision to improve reward discrimination while preserving fine-grained pointwise scoring. Extensive experiments on image generation and editing reward-modeling benchmarks demonstrate that TRM achieves state-of-the-art performance among open-source reward models while remaining highly competitive with proprietary alternatives. Moreover, using TRM as a reward for reinforcement learning consistently improves diverse visual generation models, demonstrating that its fine-grained, case-adaptive rewards translate into effective optimization signals for visual generation.
