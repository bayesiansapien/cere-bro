---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06638
url: https://huggingface.co/papers/2605.06638
arxiv_url: https://arxiv.org/abs/2605.06638
date: 2026-05-09
---

# Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key

We introduce ScaleLogic, a synthetic logical reasoning framework that offers independent control over two axes of difficulty: the depth of the required proof planning (i.e., the horizon) and the expressiveness of the underlying logic. Using this framework, we show that the RL training compute T follows a power law with respect to reasoning depth D (T proportional to D^gamma, R^2 > 0.99) and that the scaling exponent gamma increases monotonically with logical expressiveness, from 1.04 to 2.60. On downstream mathematics and general reasoning benchmarks, more expressive training settings yield both larger performance gains (up to +10.66 points) and more compute-efficient transfer compared to less expressive settings.
