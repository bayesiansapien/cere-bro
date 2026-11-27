---
title: "Video efficiency shorts: LiveVAE, Lembas token allocation, SPARC attention pruning"
date: 2026-11-27
source: https://arxiv.org/abs/2611.34912
source2: https://arxiv.org/abs/2611.32938
source3: https://arxiv.org/abs/2611.34064
raw: ../../raw/huggingface/2026-11-26-livevae-causal-window-attention-makes-efficient-streaming-vi.md
tags: [video, vae, kv-cache, token-budget, attention-pruning, efficiency]
signal: HuggingFace 11-26
---

# Video efficiency shorts

**TL;DR.** Three video papers that are really efficiency papers. LiveVAE finds a video VAE's patches depend almost only on near neighbours, so causal window attention with a bounded temporal KV cache gives 5.2-6.2x faster encoding and 3.0-3.3x faster decoding (13.4x with its serving stack). Lembas treats video RAG as a token-budget problem solved by water-filling, with 1.7-17.3x fewer TFLOPs in multi-turn use. SPARC prunes a video diffusion model's attention to geometric correspondences, using sparsity as both camera control and memory.

- **LiveVAE (2611.34912).** Effective-receptive-field analysis of pretrained video VAEs shows encoding and decoding a patch rely almost entirely on spatial and temporal neighbours. Causal window attention cuts per-frame compute and keeps the temporal KV cache bounded for streaming. Decoupled encoder/decoder distillation then joint fine-tuning preserves the latent space, so it is a drop-in replacement. On MiniMax-H3: 5.2-6.2x encode, 3.0-3.3x decode, higher PSNR.
- **Lembas (2611.32938).** Each extra token on a frame or subtitle is worth less than the last, and worth even less when similar evidence already has tokens. One objective captures both and is solved by iterative water-filling with a convergence guarantee. Multi-turn: reuses earlier turns' tokens and refines relevance with the VLM's own attention at no extra cost. Up to +7.2 points at comparable compute.
- **SPARC (2611.34064).** For observed regions, attention is restricted to geometrically corresponding history tokens plus local context; unobserved regions keep dense attention. No new modules; better camera adherence and revisit consistency with an inference speedup.

**Relation to prior pages.** LiveVAE is the video analogue of the [kv-cache](../inference-efficiency/kv-cache.md) page's bounded-window eviction results: locality, once measured, licenses a fixed cache. Lembas is diminishing-returns token allocation, the same frame as CLEAR's shadow-price compute rationing on [test-time-compute-allocation](../inference-efficiency/test-time-compute-allocation.md). Both extend 11-26's CodecOPSD (codec-style pruning of video conditioning tokens).
