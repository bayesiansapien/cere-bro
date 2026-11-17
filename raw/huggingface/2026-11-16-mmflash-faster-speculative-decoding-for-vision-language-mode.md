---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.997630+00:00
arxiv_id: 2611.18482
url: https://huggingface.co/papers/2611.18482
arxiv_url: https://arxiv.org/abs/2611.18482
date: 2026-11-16
---

# MMFlash: Faster Speculative Decoding for Vision-Language Models

Speculative decoding accelerates generation by letting a lightweight drafter propose tokens for parallel verification by a target model. Diffusion drafters such as DFlash propose an entire token block in a single forward pass, but mainly focus on text-only tasks, leaving multimodal drafting underexplored. To study this setting, we first introduce a metric of token-level visual dependence based on the KL divergence between next-token distributions with and without visual input. We find that acceptance rates decrease from 46% in the lowest visual-dependence quartile to 22% in the highest, with this disparity persisting after multimodal training. Motivated by this observation, we propose MMFlash, a simple and effective framework that adaptively upweights visually dependent tokens that the drafter predicts poorly. For long video inputs, MMFlash further employs sparse attention to reduce redundant attention computation and improve drafting quality. Across various multimodal benchmarks, MMFlash achieves lossless decoding speedups of up to 3.58times, outperforming EAGLE-3 and DFlash by up to 195.4% and 17.1%, respectively.
