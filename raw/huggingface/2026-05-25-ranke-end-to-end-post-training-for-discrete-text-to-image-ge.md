---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.21195
url: https://huggingface.co/papers/2605.21195
arxiv_url: https://arxiv.org/abs/2605.21195
date: 2026-05-25
---

# RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution

Discrete autoregressive (AR) text-to-image (T2I) models pair a VQ tokenizer with an AR policy, and current post-training pipelines optimize only the policy while keeping the VQ decoder frozen. Recent diffusion T2I work, exemplified by REPA-E, has shown that the VAE itself constitutes a key alignment bottleneck, yet no analogous investigation exists for discrete AR models. We show that policy-only optimization induces Latent Covariate Shift: as the policy evolves, the resulting token distribution diverges from the ground-truth distribution on which the decoder was trained, such that reward scores improve while decoded image quality degrades. To address this mismatch, we propose RankE, the first end-to-end post-training framework for discrete T2I generation. Rather than optimizing the policy against a fixed decoder, RankE co-evolves both components through alternating optimization: each module maximizes a ranking-based alignment objective while being regularized by a stability-preserving anchor suited to its parameter space. This co-evolution breaks the fidelity--alignment trade-off that plagues frozen-decoder approaches: on LlamaGen-XL (775M), standard RL improves CLIP but degrades FID, whereas RankE improves both simultaneously (FID 15.21, CLIP 33.76 on MS-COCO 30K). Consistent gains on Janus-Pro (1B) confirm that decoder co-evolution reliably converts reward optimization into pixel-space quality improvements.
