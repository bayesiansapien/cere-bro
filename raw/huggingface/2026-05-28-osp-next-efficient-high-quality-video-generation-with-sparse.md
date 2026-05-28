---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28691
url: https://huggingface.co/papers/2605.28691
arxiv_url: https://arxiv.org/abs/2605.28691
date: 2026-05-28
---

# OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning

Diffusion Transformers achieve strong video generation quality, but the quadratic cost of full attention limits efficiency. We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning. OSP-Next uses a hybrid full-sparse attention architecture, where the sparse component is implemented with Skiparse-2D Attention. This fixed-pattern mechanism applies token-wise and group-wise sparse attention along spatial dimensions, leveraging locality while maintaining native compatibility with FlashAttention kernels. Based on the local equivalence of rearrangement in Skiparse-2D Attention, we further propose Sparse Sequence Parallelism (SSP), which partitions subsequences across ranks and switches sparse patterns through a single All-to-All communication. Compared with Ulysses Sequence Parallelism (SP), SSP provides a native parallel strategy for sparse attention and reduces communication volume by 75%. OSP-Next also incorporates HiF8 quantization to enable stable joint training with 8-bit quantization and sparse fine-tuning, and applies Mix-GRPO post-training to improve the performance of the sparse model. Experiments show that OSP-Next achieves a VBench total score of 83.73%, surpassing the Wan2.1 baseline. Under the 5-second 720P and 5-second 768P settings, OSP-Next achieves up to 1.64times single-GPU speedup and over 1.52times eight-GPU speedup on NVIDIA H200 GPUs. In addition, with only a 0.4% drop in VBench total score, OSP-Next-HiF8 achieves 1.69times and 2.27times speedups under the two settings on a single Ascend 950PR, demonstrating the efficiency and performance of OSP-Next across hardware platforms.
