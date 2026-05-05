---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2605.01725
url: https://huggingface.co/papers/2605.01725
arxiv_url: https://arxiv.org/abs/2605.01725
date: 2026-05-05
---

# Motion-Aware Caching for Efficient Autoregressive Video Generation

Autoregressive video generation paradigms offer theoretical promise for long video synthesis, yet their practical deployment is hindered by the computational burden of sequential iterative denoising. The researchers introduce MotionCache, a framework that uses inter-frame differences to identify which pixels require more denoising iterations versus those that can skip steps safely.

The method employs a two-phase approach: an initial warm-up establishes semantic consistency, followed by motion-weighted cache reuse that adjusts update frequencies dynamically. Testing on SkyReels-V2 and MAGI-1 models demonstrates substantial acceleration: 6.28x and 1.64x faster respectively, while maintaining quality with minimal degradation in VBench scores (1% and 0.01% drops). The implementation is publicly available on GitHub.
