---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.816676+00:00
arxiv_id: 2609.37200
url: https://huggingface.co/papers/2609.37200
arxiv_url: https://arxiv.org/abs/2609.37200
date: 2026-10-02
---

# Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL

Multi-reward guided reinforcement learning (i.e., RL) offers a promising way to improve joint audio-video diffusion models along several complementary objectives, including modality-specific quality, cross-modal semantic alignment, and temporal synchronization. Its effectiveness, however, depends on two quantities that change during training: where reward-driven updates should act, and how competing rewards should be combined. Existing methods tend to rely on fixed routing and reward weights, failing to track evolving model functions. To address these limitations, we propose Adaptive Reward Routing to jointly adapt update locations and reward coordination during forward-process RL (i.e., DiffusionNFT) of joint audio-video diffusion models. Our method consists of two components. (i) Cross-Modal Influence-Guided Routing (Localizing Updates): We use bidirectional cross-attention responses as an efficient proxy for evolving cross-modal influence, dynamically reweighting token-aware losses and scaling gradients across cross-modal layers without additional model interventions. (ii) Preference-Preserving Modality-Aware Reweighting (Coordinating Rewards): We preserve predefined weights as preference priors and use branch-specific reward-gradient interactions as residual corrections after warm-up. This resolves evolving conflicts without letting dominant rewards suppress weak but essential objectives. Extensive experiments demonstrate consistent improvements in modality quality, semantic consistency, and audio-video synchronization over strong RL baselines. Ablations and mechanism analyses further validate the complementary benefits of adaptive update routing and reward coordination.
