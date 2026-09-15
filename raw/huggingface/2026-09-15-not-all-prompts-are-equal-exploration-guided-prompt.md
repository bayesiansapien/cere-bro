---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.15051
url: https://huggingface.co/papers/2609.15051
arxiv_url: https://arxiv.org/abs/2609.15051
date: 2026-09-15
---

# Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal Reinforcement Post-Training

Training prompts in online reinforcement learning (RL) differ substantially in how informative they are for the current policy: some are already saturated while others are too difficult to yield reliable learning signals, yet both receive equal rollout budget under standard training. We propose an exploration-guided prompt scaffolding framework that adapts the training prompt distribution dynamically throughout RL post-training of multimodal large language models (MLLMs). Central to our approach is the Exploration Potential Score (EPS), a lightweight rollout-based proxy for prompt utility derived from KL-regularized policy improvement theory, computable directly from on-policy rollout statistics without additional overhead. Rather than discarding low-utility prompts, we use a teacher model to generate scaffolded rewrites that preserve the original task intent while making subsequent training more informative, reframing teacher supervision as training-data refinement rather than output imitation. Integrated with GRPO on Geo3K and MMK12, our method consistently outperforms the baseline on both in-domain and out-of-distribution benchmarks, achieving up to 9.7\% relative improvement in-domain and gains of 11.5\% on MathVision and 11.1\% on MMMU-Pro.
