---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.20492
url: https://huggingface.co/papers/2608.20492
arxiv_url: https://arxiv.org/abs/2608.20492
date: 2026-08-26
upvotes: 65
---

# Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs

Multimodal large language models (MLLMs) have become a prevailing paradigm for unified video perception. However, post-training on large multi-task datasets remains challenging, as existing reinforcement learning methods sample on-policy groups with few high-quality rollouts even with costly chain-of-thought (CoT) generation. In this paper, we study the sample efficiency and scalability of RL post-training for video MLLMs and introduce OraRL. We identify an overlooked role for annotations: Beyond scoring rollouts, each can enter its on-policy group as an oracle rollout, a direct positive optimization target. Direct oracle integration, however, is nontrivial: a high-reward oracle raises the group baseline and inverts otherwise positive policy advantages, a failure we term advantage inversion. At the core of OraRL is a decoupled advantage estimator: policy rollouts determine an oracle-free baseline, while the oracle-policy gap modulates both a directional gain and a separate detached oracle advantage. Sign-balanced pruning improves efficiency: by retaining only the oracle and the strongest rollouts of each sign, OraRL requires just 2.2x the step time of SFT, less than half the 4.9x required by GRPO with CoT. OraRL scales with model size and data, surpassing its backbone from 0.8B to 9B and GRPO up to 100k prompts. Without chain-of-thought, Video-ORA-9B decodes in 130 ms instead of 4,780 ms. Compared with the respective prior best models, it raises temporal mIoU from 62.5 to 66.0, tracking AO from 73.0 to 78.2, segmentation from 64.3 to 70.4, and the three-benchmark spatial-intelligence macro average from 51.0 to 56.1; on VSI-Bench, it scores 73.1 against 55.0 for GPT-5 and 55.1 for Gemini-3-Pro.
