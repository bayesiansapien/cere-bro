---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02076
url: https://huggingface.co/papers/2610.02076
arxiv_url: https://arxiv.org/abs/2610.02076
date: 2026-10-06
---

# LLM-as-Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune Them

Jev-style decision models return categorical probability distributions over predefined options without generating free-form text, enabling software systems to act on their outputs directly. In this work, we investigate the extent to which general-purpose LLMs already possess this capability out of the box, and when fine-tuning is actually necessary. We present LLM-as-Jev, an architecture-preserving framework that extracts calibrated decisions directly from next-token probabilities over bracketed numeric identifiers. LLM-as-Jev provides both a training-free inference recipe and a fine-tuning objective that optimizes candidate selection via a tree-factorized listwise loss while anchoring auxiliary predictions to the base model using KL divergence penalties. Evaluating on Qwen3.5-4B and Qwen3-0.6B, we find that modern LLMs are inherently effective decision models: without training, the 4B model matches community Jev-style models built on the same backbone, outperforms letter-logit readouts, supports arbitrary option counts, and natively handles multimodal decisions over images. Fine-tuning provides targeted rather than universal benefits -- substantially improving weaker models and specific tasks (such as many-option intent routing), but offering diminishing returns for strong backbones. Crucially, our KL anchors prevent behavioral degradation in conversational text generation, with LoRA delivering the strongest performance on capable models.
