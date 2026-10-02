---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349898+05:30
arxiv_id: 2609.38597
url: https://huggingface.co/papers/2609.38597
arxiv_url: https://arxiv.org/abs/2609.38597
date: 2026-10-01
---

# PixelUMM: Encoder-Free Unified Image and Video Understanding and Generation

Unified Multimodal Models (UMMs) often rely on separate visual representations for understanding and generation, increasing visual context length and complicating integration with established vision-language pretraining pipelines. Recent advances in pixel-space modeling offer an encoder-free alternative, but extending this paradigm from images to videos is non-trivial: video understanding and generation adopt different temporal representations, leaving the design of a unified visual interface an open question. We present PixelUMM, an encoder-free model for unified image and video understanding and generation directly in pixel space. PixelUMM represents images as spatial patches and videos as spatiotemporal tubelets, connecting raw pixels to a shared multimodal backbone through single-layer linear projections. Its Mixture-of-Transformers architecture combines shared attention with task-specific parameters and extends clean-pixel prediction to video generation, jointly supporting autoregressive text prediction and pixel-space flow matching. Experiments show that PixelUMM achieves competitive performance across image and video understanding and generation tasks. We further conduct empirical studies of key design choices, including decoder design and spatial-temporal patch size, providing insights for future pixel-space unified multimodal models.
