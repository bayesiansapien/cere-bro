---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.19567
url: https://huggingface.co/papers/2608.19567
arxiv_url: https://arxiv.org/abs/2608.19567
date: 2026-08-25
upvotes: 19
authors: ["Bowen Cui", "Weijie Wang", "Zeyu Zhang", "Yefei He", "Mingda Lin", "Haoyu Zhao", "Yuanyu He", "Donny Y. Chen", "Feng Chen", "Bohan Zhuang"]
---

# Block3D: Efficient Text-to-3D Generation via Block-Wise Diffusion

**Upvotes:** 19
**Authors:** Bowen Cui, Weijie Wang, Zeyu Zhang, Yefei He, Mingda Lin, Haoyu Zhao, Yuanyu He, Donny Y. Chen, Feng Chen, Bohan Zhuang

While text-to-3D generation has advanced rapidly, achieving high geometric fidelity at low inference cost remains challenging. Existing text-to-3D methods either decode discrete shape tokens autoregressively or iteratively refine global 3D representations with diffusion or flow models. However, autoregressive decoding is sequential and cannot revise errors, whereas diffusion and flow-matching models repeatedly process the full representation, making high-quality generation increasingly expensive. In this paper, we propose Block3D, a block-wise diffusion framework that partitions the discrete shape-token sequence into contiguous blocks, generates the blocks autoregressively, and jointly denoises all tokens within the current block. To alleviate error accumulation, we introduce confidence-guided intra-block correction, which revises low-confidence tokens before each block is finalized. On a held-out set from TRELLIS-500K, Block3D reduces mean end-to-end generation time from 25.71 seconds to 4.99 seconds, achieving a 5.15times speedup over the fine-tuned autoregressive baseline without sacrificing geometric fidelity.
