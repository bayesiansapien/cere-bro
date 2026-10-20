---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.14746
url: https://huggingface.co/papers/2610.14746
arxiv_url: https://arxiv.org/abs/2610.14746
date: 2026-10-19
---

# BridgeWAM: Bridging Video and Action Experts via Latent Bridge Queries

World Action Models (WAMs) commonly couple video and action experts through dense, layer-wise Mixture-of-Transformers (MoT) attention, exposing action prediction to irrelevant visual features while enforcing matched expert depths. This coupling hinders selective visual-feature use and introduces redundant computation. We introduce Bridge-of-Experts (BoE), instantiated as BridgeWAM, which aggregates visual, language, and proprioceptive priors through 32 Latent Bridge Queries (LBQs) into a shared, limited latent space. Joint video-action supervision lets action gradients guide the Video Expert toward representations better suited for action prediction, while the Action Expert learns to selectively retrieve task-relevant information through cross-attention. Decoupling expert depths and reusing LBQs during action denoising yield a 5.06B model with a 30-layer Video Expert and a two-layer Action Expert, achieving 98.25% success on LIBERO and 72.24% pooled success on LIBERO-Plus, demonstrating effective task execution and strong generalization with an ultralight action head. Ablations support joint representation adaptation and unified LBQ conditioning. Relative to Fast-WAM, BridgeWAM reduces single-sample inference FLOPs by 28.72% in simulation profiling and real-robot latency to 77.1 ms (a 2.47-fold speedup). Qualitative experimental results further indicate preferential attention to target objects and task destinations across perturbations.
