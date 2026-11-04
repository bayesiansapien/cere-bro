---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.00859
url: https://huggingface.co/papers/2611.00859
arxiv_url: https://arxiv.org/abs/2611.00859
date: 2026-11-03
---

# Wave Forcing: Towards Speed-of-Light Streaming Video Generation

Real-time long-video generation requires continuous output with consistent appearance and natural motion. Existing chunk-wise autoregressive methods face challenges in both generation efficiency and long-video quality: serialized denoising and history-cache refresh require two forward passes even with one-step denoising, and longer rollouts can degrade quality and cause camera drift. We propose Wave Forcing (WF), which co-designs generation, training, and execution for continuous video output with multi-step denoising. WF uses chunk-wise causal attention to access earlier, cleaner chunks before their denoising is complete, and distributes staggered denoising and cache-refresh stages across full-model replicas to achieve 1F1C: one output chunk per concurrent forward round after pipeline fill. To adapt the model to this continuous generation process, we develop a three-stage training procedure that successively introduces mixed-noise denoising, motion supervision, and causal adaptation using self-generated history. To execute this process efficiently, Wave Runtime (WaveRT) uses Wave Parallelism (WP) for early K/V delivery and communication-computation overlap, together with optimized kernels and pipelined VAE decoding. Experiments on Wan2.1-T2V-1.3B show that 5-step WF maintains overall quality comparable to Rolling Forcing while achieving higher Dynamic Degree on both short and long videos. Our system efficiency experiments show that 4-step WF achieves 147.6 DiT FPS and 134.8 end-to-end FPS on eight H200 GPUs, yielding 7.07x the single-GPU end-to-end throughput. In DiT-only tests with matched SageAttention+W8A8 backends, denoising steps, and GPU counts, WP delivers up to 2.53x the throughput of the faster of the Ulysses and Ring context-parallel baselines across six model scales (1.3B-14B).
