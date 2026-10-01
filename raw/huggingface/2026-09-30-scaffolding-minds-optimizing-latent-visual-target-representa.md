---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2608.19669
url: https://huggingface.co/papers/2608.19669
arxiv_url: https://arxiv.org/abs/2608.19669
date: 2026-09-30
---

# Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning

Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning (RL) stage. In this paper, we identify two key limitations of this framework, one in each stage. First, the SFT stage typically relies on an off-the-shelf vision encoder to encode the helper image, yielding suboptimal latent representations that may not be well aligned with the downstream reasoning task. Second, existing RL methods treat the latent component only through deterministic regularization, which constrains policy drift but does not create alternative latent trajectories for exploration. To address these limitations, we propose Scaffolding Minds. Our approach learns a dedicated scaffolding encoder that provides an optimized target in latent space, and learns both the mean and variance of the RL sampler. We further show that these two improvements are complementary, together yielding substantial gains over strong baselines. Empirically, our method improves over the strongest latent reasoning baseline by +9.5 points on FrozenLake spatial planning, with the gain widening to +19 points on the 32x32 grids, and by +5.6 points on average across nine visual-centric reasoning benchmarks.
