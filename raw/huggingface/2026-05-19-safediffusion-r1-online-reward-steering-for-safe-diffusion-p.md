---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.18719
url: https://huggingface.co/papers/2605.18719
arxiv_url: https://arxiv.org/abs/2605.18719
date: 2026-05-19
---

# SafeDiffusion-R1: Online Reward Steering for Safe Diffusion Post-Training

Diffusion models have been widely studied for removing unsafe content learned during pre-training. Existing methods require expensive supervised data, either unsafe-text paired with safe-image groundtruth or negative/positive image pairs, making them impractical to scale. Furthermore, offline reinforcement learning and supervised fine-tuning approaches that generate synthetic data offline suffer from catastrophic forgetting, degrading generation quality. We propose a novel online reinforcement learning framework that addresses both data scarcity and model degradation through post-training with Group Relative Policy Optimization (GRPO) on both negative and positive text prompts. To eliminate the need for fine-tuning specialized safe/unsafe reward models, we introduce a steering reward mechanism that exploits an inherent property of CLIP embeddings: steering text representations toward positive safety directions and away from negative ones in the embedding space. Our online-policy approach enables the model to learn from diverse prompts, including explicit unsafe content, without catastrophic forgetting. Extensive experiments demonstrate that our method reduces inappropriate content to 18.07\\% (vs. 48.9\\% for SD v1.4) and nudity detections to 15 (vs. 646 baseline) while improving compositional generation quality from 42.08\\% to 47.83\\% on GenEval. Remarkably, these safety gains generalize to out-of-domain unsafe prompts across seven harm categories, achieving state-of-the-art performance without supervised paired data or reward tuning. Github: https://github.com/MAXNORM8650/SafeDiffusion-R1.
