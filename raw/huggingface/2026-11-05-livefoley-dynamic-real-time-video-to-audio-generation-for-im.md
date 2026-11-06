---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.306155+00:00
arxiv_id: 2611.05988
url: https://huggingface.co/papers/2611.05988
arxiv_url: https://arxiv.org/abs/2611.05988
date: 2026-11-05
---

# LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds

Streaming video-to-audio (V2A) generation is essential for immersive interactive applications. However, real-time constraints leave existing streaming V2A methods far behind offline models: (1) visual frontends shrink their receptive fields to cut look-ahead latency, severely degrading audio-visual alignment; (2) causal autoregressive diffusion backends denoise each audio patch in isolation, impairing audio quality. To this end, we present LiveFoley, a streaming causal autoregressive diffusion architecture that addresses both bottlenecks with imperceptible latency. For the visual frontend, we introduce a Trailing Sliding Window that converts non-causal segment-level encoders into streaming modules without retraining. By simply realigning the window, it preserves precise audio-visual alignment, while a configurable hop size reduces the frontend look-ahead well below the human perceptual threshold. Building on this tunable hop size, we propose the Unified Varhop Framework to accommodate scenarios with diverse latency and computation budgets. For the audio backend, we explore widening the denoising window of the local diffusion transformer (LocDiT) head in two temporal directions. History LocDiT adds past context to improve quality at no latency cost and serves as our default. Alternatively, Future-Warmup LocDiT breaks the autoregressive deadlock with an approximate future condition, further improving generation quality at the cost of an acceptable backend look-ahead. Extensive experiments demonstrate that LiveFoley matches offline models in temporal alignment and leads streaming systems in generation quality. Project page: https://dalision.github.io/livefoley-page/
