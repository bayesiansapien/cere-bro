---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.27355
url: https://huggingface.co/papers/2605.27355
arxiv_url: https://arxiv.org/abs/2605.27355
date: 2026-05-30
---

# Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases

Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulnerability where the LLM undergoing alignment influences the preference dataset, causing RLHF to amplify undesired behaviors. This arises from core limitations of RLHF: (1) preference datasets are constructed from the LLM's own outputs, allowing it to influence them, and (2) pairwise comparisons only indicate which response is better, not why. These limitations can be exploited to cause alignment tampering. For example, if an LLM generates biased responses with higher quality, annotators will prefer them based on quality. However, preference labels do not distinguish quality from bias, and the reward model inherits this limitation. Optimizing such rewards through reinforcement learning or best-of-N sampling can amplify misaligned biases. Our experiments demonstrate amplification across diverse biases: from keyword bias to propaganda (e.g., sexism), brand promotion, and instrumental goal-seeking. Mitigation remains challenging, as existing techniques for robust RLHF fail to fully resolve alignment tampering without sacrificing response quality. These findings reveal structural vulnerabilities of current RLHF and emphasize the need to prevent this vulnerability. Project page: https://alignment-tampering.github.io/
