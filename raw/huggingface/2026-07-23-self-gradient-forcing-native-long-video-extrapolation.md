---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.20368
url: https://huggingface.co/papers/2607.20368
arxiv_url: https://arxiv.org/abs/2607.20368
date: 2026-07-23
---

# Self Gradient Forcing: Native Long Video Extrapolation

Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state. As a result, future losses cannot supervise how earlier generated latents should be written into more useful keys and values for later video-latent generation. We call this the historical context-gradient gap. We propose Self Gradient Forcing (SGF), a two-pass training strategy that restores this missing supervision signal without backpropagating through the full serial rollout. Pass 1 performs a no-gradient autoregressive rollout matching inference and, at a sampled denoising exit step, records both the self-generated context and the noisy latents fed to the model. Pass 2 performs parallel context-gradient reconstruction for the recorded exit step. The generated context is used as stop-gradient clean-latent input, while the model recomputes the context KV representations and future-to-context causal attention. Thus, SGF provides the missing memory-writing supervision within the native autoregressive training objective, using losses on future video latents to train the model to encode context into more effective causal memory. Across extensive long-horizon frame-wise and chunk-wise experiments under different initializations, SGF achieves stronger native long-video extrapolation than Self Forcing, especially in subject identity, background/layout consistency, and temporal stability. Remarkably, using only a 5-second training window, SGF can extrapolate to videos lasting several minutes. Code and models will be released to advance research on autoregressive video generation.
