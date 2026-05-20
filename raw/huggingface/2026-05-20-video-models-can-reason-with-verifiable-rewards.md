---
source: farmer/huggingface
farmed: 2026-05-20T09:54:45.126133+00:00
arxiv_id: 2605.15458
url: https://huggingface.co/papers/2605.15458
arxiv_url: https://arxiv.org/abs/2605.15458
date: 2026-05-20
---

# Video Models Can Reason with Verifiable Rewards

Video diffusion models have made rapid progress in perceptual realism and temporal coherence, but they remain primarily optimized for plausible generation rather than verifiable reasoning. This limitation is especially pronounced in tasks where generated videos must satisfy explicit spatial, temporal, or logical constraints. Inspired by the role of reinforcement learning with verifiable rewards (RLVR) in reasoning-oriented language models, we introduce VideoRLVR, a practical recipe for optimizing video diffusion models with rule-based feedback. VideoRLVR formulates video reasoning as the generation of verifiable visual trajectories and consists of an SDE-GRPO optimization backbone, dense decomposed rewards, and an Early-Step Focus strategy for efficient training. The Early-Step Focus strategy restricts policy optimization to the early denoising phase, reducing training latency by about 40% while preserving performance. We evaluate VideoRLVR on Maze, FlowFree, and Sokoban, three procedurally generated domains with objective success criteria. Across these tasks, VideoRLVR consistently improves over supervised fine-tuning baselines, with dense decomposed rewards proving especially important in low-success-rate settings. Our RL-optimized model also outperforms the evaluated proprietary and open-source video generation models on these verifiable reasoning benchmarks and out-of-domain benchmarks. These results suggest that verifiable RL can move video models beyond perceptual imitation toward more reliable rule-consistent visual reasoning.
