---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.412409+00:00
arxiv_id: 2610.06801
url: https://huggingface.co/papers/2610.06801
arxiv_url: https://arxiv.org/abs/2610.06801
date: 2026-10-09
---

# MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers

Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided by this analysis, we propose Meta-Cached Sparse Attention (MC-Sparse), a training-free framework that selects individual key-value (KV) tokens while organizing similar queries into tile-aligned groups for efficient GPU execution. MC-Sparse caches metadata comprising query groups, KV indices selected using exact attention probabilities, and residuals between dense and sparse attention outputs, and reuses them across subsequent denoising steps. Across video and 3D generation models, MC-Sparse achieves higher fidelity to dense-attention outputs and larger denoising speedups than existing sparse-attention baselines, without visible quality degradation. Relative to dense attention, it delivers a 1.80times denoising speedup on Minimax-H3-Base and a 2.32times speedup on 3D asset generation, both with negligible quality loss.
