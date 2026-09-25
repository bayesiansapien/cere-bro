---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.29816
url: https://huggingface.co/papers/2609.29816
arxiv_url: https://arxiv.org/abs/2609.29816
date: 2026-09-25
upvotes: 2
---

# AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation

Recent years have witnessed major progress in joint audio-video generation. Existing models still suffer from limited per-modality fidelity, insufficient text-modality alignment and weak cross-modal synchronization. While reinforcement-learning post-training offers a promising remedy, directly adapting it to joint audio-video generation is challenging. Heterogeneous multimodal rewards entangle learning signals and complicate credit assignment. Joint optimization of two modality towers is computationally expensive given their divergent dynamics. Moreover, synchronization evaluation difficulty depends on paired samples, preventing fair reward comparisons. We propose AV-GRPO, a modality-anchored online diffusion RL framework, and 5DAV, a decoupled, difficulty-controllable training dataset. AV-GRPO includes three key modules: (1) modality-anchored rollouts to disentangle learning signals and stabilize difficulty; (2) trajectory-locked frozen-tower optimization to reduce cost and reassign credit; (3) adaptive objectives and perturbation strengths tailored to modality-specific dynamics. This converts coupled multimodal preference learning into unimodal subproblems for precise reward attribution and better synchronization. Our 5DAV dataset decouples samples across five dimensions for systematic training. Experiments on JavisBench and VABench demonstrate AV-GRPO outperforms LTX-2.3 in generation quality, semantic alignment and cross-modal synchronization under LoRA and full fine-tuning. Ablations confirm our designs. Code and data: https://github.com/zhiyuxu03/AV-GRPO
