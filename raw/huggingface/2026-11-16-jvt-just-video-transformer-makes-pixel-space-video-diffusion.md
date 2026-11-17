---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.999382+00:00
arxiv_id: 2611.18549
url: https://huggingface.co/papers/2611.18549
arxiv_url: https://arxiv.org/abs/2611.18549
date: 2026-11-16
---

# JVT: Just Video Transformer makes pixel-space video diffusion simple

Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-space video diffusion, without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections. We systematically examine video patch embeddings, register tokens, and adaptive layer normalization to identify design choices that balance generation quality and computational efficiency. The resulting JVT design achieves generation quality competitive with latent diffusion baselines in both class-conditioned and unconditional settings. The pixel-space formulation of JVT also naturally supports joint generation of pixel-aligned modalities. We demonstrate this capability through camera-conditioned RGB-disparity generation, which improves camera following relative to RGB-only baselines and yields explicit scene geometry without an additional reconstruction model at inference. These results highlight the potential of simple DiT-style Transformers for pixel-space video diffusion, and we hope our findings offer useful insights and practical guidance for future research.
