---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.929381+00:00
arxiv_id: 2611.30627
url: https://huggingface.co/papers/2611.30627
arxiv_url: https://arxiv.org/abs/2611.30627
date: 2026-11-24
---

# From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning

Reinforcement learning (RL) has become an important component in large language models (LLMs). However, existing RL approaches focus on final outputs or textual solution trajectories, leading to coarse-grained rewards and unreliable reasoning. Such paradigms focus mainly on what the model outputs while overlooking how the model internally reasons. Therefore, can we reward how a model thinks internally rather than merely what it says? We first reveal the problem of textual reward aliasing in existing reward modeling approaches. Motivated by this, we propose the Attention Process Reward Model (APRM), which assigns internal rewards based on hidden states and attention maps to capture high-quality reasoning patterns. With only approximately 46M parameters, APRM is trained using ranking and counterfactual objectives, and its reward guides RL optimization while being periodically updated to handle distribution shifts. Integrated with representative RL methods, APRM achieved an average pass@8 gain of 2.88\%. Our results demonstrate the promise of incorporating internal reasoning signals into RL for LLMs.
