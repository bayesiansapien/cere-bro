---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994927+05:30
arxiv_id: 2610.36269
url: https://huggingface.co/papers/2610.36269
arxiv_url: https://arxiv.org/abs/2610.36269
date: 2026-10-28
---

# Cross-modal Steering Vectors Exist Across Both Image and Text Generation

Are concepts and mechanisms unified across modalities in current AI models, or instead implemented separately for each one? We operationalize this broad question of modality unification by studying cross-modal steering: 1) finding vectors that successfully steer generation on tokens of one modality, which then 2) transfer zero-shot to steer generation when added to tokens of another modality. Our study goes beyond simple correlational alignment (e.g. representational similarity) because steering is fundamentally causal. We study cross-modal steering in several unified multimodal models (UMMs), since they possess shared parameters for language and image generation, focusing on these two modalities. Across diverse steered concepts such as emotion and object size, we show that steering vectors transfer zero-shot in both directions (text-to-image & image-to-text). Even for concepts that are highly unique to one modality (e.g. formal vs. colloquial language), steering vectors often induce a consistent, interpretable effect in the other modality, such as formal clothing and design. This transfer has a geometric signature too: despite a clear modality gap separating text and image representations, steering vectors with strong cross-modal transferability tend to point in similar directions for the same concept. Our findings shed light on how vision and language interact inside unified multimodal models and point towards more general, modality-agnostic approaches for controlling their behavior.
