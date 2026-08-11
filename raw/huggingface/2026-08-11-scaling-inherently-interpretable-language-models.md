---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.07594
url: https://huggingface.co/papers/2608.07594
arxiv_url: https://arxiv.org/abs/2608.07594
date: 2026-08-11
---

# Scaling Inherently Interpretable Language Models

Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
  We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.
