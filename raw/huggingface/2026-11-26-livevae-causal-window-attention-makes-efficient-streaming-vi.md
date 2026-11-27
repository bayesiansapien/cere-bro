---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.908508+00:00
arxiv_id: 2611.34912
url: https://huggingface.co/papers/2611.34912
arxiv_url: https://arxiv.org/abs/2611.34912
date: 2026-11-26
---

# LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE

While video diffusion models have grown faster and increasingly streamable, the video VAE remains a primary latency bottleneck across interactive generation and editing pipelines. Existing VAEs and their acceleration methods rely mainly on heavy convolutions or full frame attention, and most focus only on decoding, leaving encoding costly for streaming conditional generation and editing. This raises a natural question: Do video VAE encoding and decoding actually require such global spatiotemporal modeling? By analyzing the effective receptive fields of pretrained video VAEs, we find that both encoding and decoding a patch rely almost entirely on its spatial and temporal neighbors. To exploit this strong locality, we introduce LiveVAE, a streaming encoder and decoder built on causal window attention, which cuts per frame compute while keeping the temporal KV cache bounded for streaming. Decoupled encoder/decoder distillation followed by joint finetuning preserves the pretrained latent space, making LiveVAE a drop-in replacement for the original VAE. On MiniMax-H3, LiveVAE achieves 5.2-6.2x faster encoding and 3.0-3.3x faster decoding than the official VAE with higher PSNR. Paired with our dedicated inference infrastructure, LiveVAE pushes the speedup to 13.4x with almost no quality loss. Code and models will be released.
