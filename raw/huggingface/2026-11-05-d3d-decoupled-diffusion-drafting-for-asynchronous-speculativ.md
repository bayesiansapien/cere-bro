---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.303011+00:00
arxiv_id: 2611.06425
url: https://huggingface.co/papers/2611.06425
arxiv_url: https://arxiv.org/abs/2611.06425
date: 2026-11-05
---

# D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with auxiliary autoregressive supervision to achieve long accepted prefixes without target hidden states. This independence lets D3D draft successor blocks during verification in one packed pass, enabling asynchronous speculative decoding. We progressively prune layers according to their effect on acceptance length to reduce the cost of packed drafting. Removing five of 36 layers retains over 99\% of mean acceptance length across three benchmarks with Qwen3-8B as the target. Across seven benchmarks, D3D averages 5.00times and 5.71times decoding speedup with Qwen3-8B and Qwen3-32B targets, compared with 4.03times and 3.67times for DFlash. On GSM8K with Qwen3-32B, speedup reaches 7.48times. Code is publicly available at https://github.com/fudan-generative-vision/D3D.
