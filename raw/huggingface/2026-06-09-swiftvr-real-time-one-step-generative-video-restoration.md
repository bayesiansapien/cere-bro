---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.09516
url: https://huggingface.co/papers/2606.09516
arxiv_url: https://arxiv.org/abs/2606.09516
date: 2026-06-09
---

# SwiftVR: Real-Time One-Step Generative Video Restoration

Real-time video restoration (VR) for live streams requires high-resolution outputs under strict per-frame latency constraints. Existing one-step diffusion-based VR models remain difficult to deploy on consumer-grade GPUs due to two main bottlenecks: quadratic spatial attention at high resolutions and the latency-memory overhead of large video autoencoders. We present SwiftVR, a streaming one-step generative VR framework that reduces both bottlenecks under a causal chunk-wise protocol. For attention, mask-free shifted-window self-attention gathers each spatial window into a dense tensor via deterministic indexing, keeping all attention calls on the dense scaled dot-product attention path without masks, cyclic shifts, padding, or hardware-specific sparse kernels. Because SwiftVR uses only standard dense SDPA calls, the trained model transfers to consumer GPUs without retraining or custom kernels. For autoencoding, a lightweight Restoration-aware Autoencoder enables fast chunk-wise decoding while preserving reconstruction quality. On a single H100, SwiftVR sustains 31~FPS at 2560x1440 and 14~FPS at 3840x2160, whereas all compared diffusion-based VR baselines exceed the memory limit at 4K. On a consumer RTX~5090, SwiftVR reaches 26~FPS at 1920x1080. To our knowledge, SwiftVR is the first generative VR model to achieve real-time 1080p streaming on a consumer-grade GPU, while attaining strong no-reference perceptual quality with lower inference cost. Project is available at https://h-oliday.github.io/SwiftVR.
