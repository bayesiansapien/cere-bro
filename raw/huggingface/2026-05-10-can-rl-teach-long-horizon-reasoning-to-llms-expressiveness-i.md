---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06638
url: https://huggingface.co/papers/2605.06638
arxiv_url: https://arxiv.org/abs/2605.06638
date: 2026-05-10
---

# Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key

Reinforcement learning (RL) has been applied to improve large language model (LLM) reasoning, yet the systematic study of how training scales with task difficulty has been hampered by the lack of controlled, scalable environments. We introduce ScaleLogic, a synthetic logical reasoning framework that offers independent control over two axes of difficulty: the depth of the required proof planning and the expressiveness of the underlying logic. We show that the RL training compute T follows a power law with respect to reasoning depth D (T proportional to D^gamma, R^2 > 0.99), and that the scaling exponent gamma increases monotonically with logical expressiveness, from 1.04 to 2.60.
