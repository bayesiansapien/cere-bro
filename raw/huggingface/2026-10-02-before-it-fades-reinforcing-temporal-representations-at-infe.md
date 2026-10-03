---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823333+00:00
arxiv_id: 2610.01595
url: https://huggingface.co/papers/2610.01595
arxiv_url: https://arxiv.org/abs/2610.01595
date: 2026-10-02
---

# Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs

Video Large Language Models (VideoLLMs) receive frames in sequential order and interpret how visual content evolves along the temporal axis, yet temporal reasoning remains a persistent weakness across architectures. Reversing the frame order of a video, a transformation that should invert temporal answers, often leaves the final prediction unchanged. We investigate where this failure originates by defining the temporal divergence vector τ_l, the layer-wise representational difference induced by reversing temporal order. Tracking its magnitude across layers reveals a consistent temporal divergence profile where the divergence peaks at intermediate layers and progressively diminishes toward the output. We confirm this peak is specific to temporal reasoning and functionally critical for predictions, establishing that VideoLLMs acquire temporal information at intermediate layers but fail to maintain it to the output. This progressive fading motivates our method, Temporal Activation Injection (TAI), which extracts τ_l at the peak of the profile for each input and reinjects it into subsequent layers following the measured decay. TAI requires no training and consistently improves temporal reasoning across three VideoLLMs and four benchmarks with negligible impact on non-temporal tasks. Code is available at https://github.com/Youngwoo-git/Before-It-Fades.
