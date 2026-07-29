---
source: farmer/huggingface
farmed: 2026-07-29T00:00:00Z
arxiv_id: 2607.25948
url: https://huggingface.co/papers/2607.25948
arxiv_url: https://arxiv.org/abs/2607.25948
date: 2026-07-29
---

# MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities

Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy. Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior. In this work, we investigate decoder-only any-to-any multimodal modeling, which treats all modalities symmetrically and supports arbitrary modalities as inputs and outputs without modality-specific heads, losses, or task pipelines. Because every modality is both an input and an output of the same model, the resulting model, named Modus, can support a range of applications, such as chained generation through intermediate modalities or cross-modal self-verification by scoring the model's own outputs with another generated modality. Modus demonstrates strong out-of-the-box performance and is competitive with specialist and multitask baselines using a single model across various benchmarks. All materials are open-sourced at https://modus-multimodal.epfl.ch/.
