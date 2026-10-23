---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.192752+00:00
arxiv_id: 2610.29441
url: https://huggingface.co/papers/2610.29441
arxiv_url: https://arxiv.org/abs/2610.29441
date: 2026-10-22
---

# Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers

Full 3D attention is costly in video Diffusion Transformers. Block-sparse attention reduces this cost by computing only selected attention blocks. However, existing methods either overlook the potential to optimize sparsity allocation or rely on heuristic rules or local metrics to guide it. In this work, we observe that sparsifying attention in different layers and at different denoising steps affects final-video fidelity to substantially different degrees. Yet the identities of the most sensitive layer-step pairs remain nearly unchanged across inputs. Building on these findings, we propose Allocating Layer-step Latency by Output Tests (ALLOT), a training-free sparsity allocation method. Treating each layer-step pair as a cell, ALLOT estimates each cell's contribution to final-video error through (i) cell probing and (ii) trajectory calibration, then jointly optimizes cell densities under a measured-latency budget. It preserves existing selection strategies and kernels, replacing only the allocation component. At equal or shorter wall-clock time, ALLOT outperforms every compared allocation strategy with XAttention, with an 11.8 dB PSNR gain on HunyuanVideo. Extensive experiments across four additional published pipelines on Wan2.1, Wan2.2, and HunyuanVideo show that ALLOT outperforms or ties the default in all nine settings.
