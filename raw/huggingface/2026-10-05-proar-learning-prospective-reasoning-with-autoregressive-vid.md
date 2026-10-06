---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.03664
url: https://huggingface.co/papers/2610.03664
arxiv_url: https://arxiv.org/abs/2610.03664
date: 2026-10-05
---

# ProAR: Learning Prospective Reasoning with Autoregressive Video Models

Autoregressive (AR) video models excel at causal generation, but their reliance on next-chunk prediction confines them to a short-sighted, reactive paradigm. This limitation is particularly consequential for reasoning-oriented generation, where achieving a target outcome through valid intermediate states matters more than local visual plausibility. To address this challenge, we propose Learning Prospective Reasoning with Autoregressive Video Models (ProAR), a novel framework that transforms autoregressive video generation into a goal-oriented reasoning process. ProAR introduces two key components: (1) To anchor generation to the long-range outcome, we integrate goal-frame prediction into the autoregressive loop via an asymmetric attention mask, enabling the predicted goal frame to guide the generation of intermediate states without being disrupted by them. (2) To guide short-range transitions, we introduce future representation self-alignment to encourage current hidden states to anticipate upcoming temporal dynamics. By leveraging teacher-forcing in AR training, we extract clean future representations in a single forward pass and align current representations with them using a lightweight, training-only predictor. Together, these two mechanisms seamlessly combine explicit, sparse target supervision with implicit, dense step-wise guidance, promoting coherent, goal-directed reasoning progress with modest computational cost. Experiments show that ProAR's complementary components consistently improve performance across diverse visual reasoning benchmarks. The framework proves highly training-efficient, surpassing fully trained standard AR baselines using only 25% of the training steps. This paradigm also demonstrates promising applicability to embodied reasoning tasks.
