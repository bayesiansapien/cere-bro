---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37969
url: https://huggingface.co/papers/2609.37969
arxiv_url: https://arxiv.org/abs/2609.37969
date: 2026-09-30
---

# SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video

High-resolution video generation is expensive, as its cost grows rapidly with the number of spatiotemporal tokens. A practical alternative first generates a lower-resolution video and then applies a refiner, but conventional multi-step refinement introduces a second sampling bottleneck. We present SoL-Refiner, a one-step video refiner that transforms low-resolution model outputs into 4K videos with a single denoising step. Our three-stage recipe combines high-resolution continual training, reinforcement learning (RL) post-training, and a final one-step distillation. We introduce Refiner-Bench, a video refinement benchmark constructed from the outputs of different video generators, and use a shared-input protocol to compare refiners at approximately 2K output resolution. At 2K, the one-step SoL-Refiner outperforms all external refiners on the VBench and UniPercept averages, while at 3840!times!2176 it improves both metrics over the three-step LTX-2.3 Refiner. With the complete acceleration stack, SoL-Refiner achieves an 8.91times speedup in refinement latency over the same baseline in our 2K latency setting.
