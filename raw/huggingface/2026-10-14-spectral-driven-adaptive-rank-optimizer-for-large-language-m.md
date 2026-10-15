---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.508458+00:00
arxiv_id: 2610.16533
url: https://huggingface.co/papers/2610.16533
arxiv_url: https://arxiv.org/abs/2610.16533
date: 2026-10-14
---

# Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards

Reinforcement learning with verifiable rewards (RLVR) is reshaping how large language models (LLMs) acquire reasoning capabilities, yet the optimizers used remain largely inherited from teacher-forcing training. This raises a fundamental question: does RLVR induce a distinct optimization geometry that calls for a different optimizer? We investigate this question through the spectral structure of LLM gradients and find that gradient energy progressively concentrates into a shrinking effective subspace, which is characteristic of RLVR, as it is absent under supervised fine-tuning (SFT) and is largely removed when the verifiable reward is replaced by a random one. Moreover, the rank required to capture a fixed fraction of gradient energy steadily decreases over training, revealing that the effective dimensionality of useful updates itself evolves with training. These findings motivate a new optimization principle: rather than prescribing the update rank externally, an optimizer should adapt its rank to the evolving spectral structure of the gradient. We introduce Ares (Adaptive Rank-Effective Spectral Optimization), which estimates the effective update rank from the gradient's spectral energy distribution, tracks its evolution, and confines the gradient signal driving each update to the resulting low-rank subspace. Across LLMs of different scales, Ares improves accuracy over widely used optimizers and generalizes across RLVR algorithms and tasks. Results suggest that effective optimization may require optimizers to be designed around the geometry and dynamics of the training process. We release the code and data at https://github.com/RUCAIBox/Ares.
