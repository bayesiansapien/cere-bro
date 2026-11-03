---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.498910+05:30
arxiv_id: 2610.31222
url: https://huggingface.co/papers/2610.31222
arxiv_url: https://arxiv.org/abs/2610.31222
date: 2026-11-02
---

# GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching

Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limiting practical deployment. Despite recent efficiency gains in generative LLIE, high-quality enhancement with a single function evaluation and low overall computation remains challenging, particularly under diverse real-world low-light conditions. We introduce GLOW-FM, a one-step latent flow-matching framework for efficient generative LLIE. GLOW-FM performs conditional transport in the latent space of a frozen Tiny-VAE and leverages Terminal Velocity Matching (TVM) to enable enhancement with a single function evaluation. Matched comparisons with alternative one-step objectives support TVM as an effective design choice, and, to the best of our knowledge, this is its first adaptation to image restoration and specifically to LLIE. Extensive experiments on challenging real-world benchmarks demonstrate that GLOW-FM achieves competitive image quality and state-of-the-art cross-dataset generalization while requiring only a single function evaluation and 34 GFLOPs for the small variant. These findings highlight the potential of GLOW-FM to bring generative LLIE closer to practical deployment through single-step inference and compact latent modeling. Code will be made publicly available upon publication.
