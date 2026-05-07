---
source: farmer/huggingface
farmed: 2026-05-07T00:00:00Z
arxiv_id: 2605.04461
url: https://huggingface.co/papers/2605.04461
arxiv_url: https://arxiv.org/abs/2605.04461
date: 2026-05-07
---

# Stream-T1: Test-Time Scaling for Streaming Video Generation

While Test-Time Scaling (TTS) offers a promising direction to enhance video generation without the surging costs of training, current test-time video generation methods based on diffusion models suffer from exorbitant candidate exploration costs and lack temporal guidance. To address these structural bottlenecks, we propose shifting the focus to streaming video generation. We identify that its chunk-level synthesis and few denoising steps are intrinsically suited for TTS, significantly lowering computational overhead while enabling fine-grained temporal control. Driven by this insight, we introduced Stream-T1, a pioneering comprehensive TTS framework exclusively tailored for streaming video generation. Specifically, Stream-T1 is composed of three units: (1) Stream-Scaled Noise Propagation, which actively refines the initial latent noise of the generating chunk using historically proven, high-quality previous chunk noise, effectively establishes temporal dependency and utilizing the historical Gaussian prior to guide the current generation; (2) Stream-Scaled Reward Pruning, which comprehensively evaluates generated candidates to strike an optimal balance between local spatial aesthetics and global temporal coherence by integrating immediate short-term assessments with sliding-window-based long-term evaluations; (3) Stream-Scaled Memory Sinking, which dynamically routes the context evicted from KV-cache into distinct updating pathways guided by the reward feedback, ensuring that previously generated visual information effectively anchors and guides the subsequent video stream. Evaluated on both 5s and 30s comprehensive video benchmarks, Stream-T1 demonstrates profound superiority, significantly improving temporal consistency, motion smoothness, and frame-level visual quality.
