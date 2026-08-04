---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2607.29613
url: https://huggingface.co/papers/2607.29613
arxiv_url: https://arxiv.org/abs/2607.29613
date: 2026-08-04
---

# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature of robot control. A naive approach to incorporate observation history into the critic incurs exponential complexity with high-dimensional visual space, and still fails because pure scalar-return regression provides insufficient supervision for learning cross-temporal dynamics. We identify the root cause as a state approximation problem: without an explicit world modeling objective, the critic's representation cannot capture the temporal structure needed for accurate value estimation. To address this, we propose the World Critic Model (WCM), built on a lightweight LeJEPA architecture; WCM jointly predicts future latent state and estimates values, such that the critic's representation is explicitly trained to capture temporal dynamics rather than merely regress scalar returns. WCM integrates seamlessly into both on-policy and off-policy training pipelines and is compatible with state-of-the-art VLA backbones including Pi0, Pi0.5, and OpenVLA-OFT. Extensive experiments on 149 tasks across four benchmarks demonstrate that WCM consistently achieves state-of-the-art performance in both in-distribution and out-of-distribution settings, with particularly strong generalization gains. We further validate WCM on seven real-world manipulation tasks using OpenVLA-OFT and Pi0.5 with off-policy RL, confirming stable deployment across diverse settings.
