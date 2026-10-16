---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.226710+05:30
arxiv_id: 2610.16302
url: https://huggingface.co/papers/2610.16302
arxiv_url: https://arxiv.org/abs/2610.16302
date: 2026-10-15
---

# RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models

Video-based interactive world models aim to enable real-time, user-controllable environments. Yet most existing systems are trained and rolled out at a fixed temporal rate, limiting both runtime-rate adaptation and physical-horizon coverage -- a limitation we term temporal-rate coupling. Specifically, when runtime generation throughput differs from the learned temporal rate, the generated world evolves unintentionally more slowly or quickly. Moreover, using a single temporal rate imposes an inherent trade-off between temporal granularity and physical horizon: higher rates capture finer motion but cover a shorter duration under a fixed context window. To address both limitations, we introduce Rate-Adaptive Rollout (RAR), a framework that enables interactive world models to roll out at controllable temporal rates. At its core, Stride-RoPE aligns latent frames sampled at different rates on a shared physical-time coordinate, enabling consistent multi-rate rollout, unseen-rate generalization, and online rate switching without discarding history. Meanwhile, RAR uses multi-stride video sampling to enable joint learning of fine-grained dynamics and long-horizon evolution. Across action- and camera-controlled environments, RAR achieves temporally consistent multi-rate rollout and online rate switching while preserving high-rate generation quality and extending physical horizons under matched training budgets. RAR also transfers to pretrained world models while preserving perceptual quality.
