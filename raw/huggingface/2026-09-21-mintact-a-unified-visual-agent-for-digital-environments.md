---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.22083
url: https://huggingface.co/papers/2609.22083
arxiv_url: https://arxiv.org/abs/2609.22083
date: 2026-09-21
---

# MintAct: A Unified Visual Agent for Digital Environments

We present MintAct, a family of vision-language models that unifies UI grounding, multi-step navigation across mobile, desktop, and web, and visual tool use, trained at 2B, 4B, and 8B scales. Through careful design of our environments, data, and training recipes, MintAct models match the performance of per-domain specialists across all of these capabilities. To enable this, we develop a scalable environment and reinforcement learning (RL) infrastructure. On the environment side, we host hundreds of concurrent instances across heterogeneous per-domain backends, serving both trajectory data collection and online RL. To enable efficient and scalable RL training, an asynchronous framework keeps explicit control over the cross-domain training distribution and remains stable under noisy environment feedback and off-policy drift. Experimental results show that MintAct achieves state-of-the-art performance (48.9 on OSWorld-Verified) across a wide range of benchmarks at comparable model sizes.
