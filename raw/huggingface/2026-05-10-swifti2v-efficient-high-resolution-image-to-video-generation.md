---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06356
url: https://huggingface.co/papers/2605.06356
arxiv_url: https://arxiv.org/abs/2605.06356
date: 2026-05-10
---

# SwiftI2V: Efficient High-Resolution Image-to-Video Generation via Conditional Segment-wise Generation

High-resolution image-to-video (I2V) generation aims to synthesize realistic temporal dynamics while preserving fine-grained appearance details of the input image. At 2K resolution, it becomes extremely challenging, and existing solutions suffer from various weaknesses: 1) end-to-end models are often prohibitively expensive in memory and latency; 2) cascading low-resolution generation with a generic video super-resolution tends to hallucinate details and drift from input-specific local structures, since the super-resolution stage is not explicitly conditioned on the input image. To this end, we propose SwiftI2V, an efficient framework tailored for high-resolution I2V. Following the widely used two-stage design, it addresses the efficiency-fidelity dilemma by first generating a low-resolution motion reference to reduce token costs and ease the modeling burden, then performing a strongly image-conditioned 2K synthesis guided by the motion to recover input-faithful details with controlled overhead. Specifically, to make generation more scalable, SwiftI2V introduces Conditional Segment-wise Generation (CSG) to synthesize videos segment-by-segment with a bounded per-step token budget, and adopts bidirectional contextual interaction within each segment to improve cross-segment coherence and input fidelity. On VBench-I2V at 2K resolution, SwiftI2V achieves performance comparable to end-to-end baselines while reducing total GPU-time by 202x.
