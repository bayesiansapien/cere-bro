---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.306850+00:00
arxiv_id: 2611.03394
url: https://huggingface.co/papers/2611.03394
arxiv_url: https://arxiv.org/abs/2611.03394
date: 2026-11-05
---

# TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation

Streaming digital humans produce detailed video while continuing speech as new text arrives. High-resolution denoising is costly, and text updates can cause repeated or interrupted speech. We present TaoMate-HD, an autoregressive model for high-resolution audio-video streaming. For each short segment, or chunk, two denoising steps establish coarse video structure at low resolution. A final step refines the video to high resolution, with audio generated throughout the same trajectory. Each stage passes its audiovisual predictions to the same stage of the next chunk as history. Across text updates, the model retains this history to infer what has already been spoken. Continuation training utilizes asymmetric text conditioning, with separate text windows for generation and distillation. Experiments show a 1.6x speedup over direct high-resolution generation with the same model and hardware. Optimized stage-parallel deployment provides a further 1.9x overall speedup over serial progressive generation. Our continuation training reduces character error rate by 11.18 percentage points relative to the baseline. The model also supports hour-long audiovisual generation. Our project page is https://taoliveaigc.github.io/TaoMate-HD.
