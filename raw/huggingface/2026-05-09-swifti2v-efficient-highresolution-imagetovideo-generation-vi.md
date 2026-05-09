---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06356
url: https://huggingface.co/papers/2605.06356
arxiv_url: https://arxiv.org/abs/2605.06356
date: 2026-05-09
---

# SwiftI2V: Efficient High-Resolution Image-to-Video Generation via Conditional Segment-wise Generation

High-resolution image-to-video (I2V) generation aims to synthesize realistic temporal dynamics while preserving fine-grained appearance details of the input image. We propose SwiftI2V, an efficient framework tailored for high-resolution I2V. It addresses the efficiency-fidelity dilemma by first generating a low-resolution motion reference to reduce token costs and ease the modeling burden, then performing a strongly image-conditioned 2K synthesis guided by the motion to recover input-faithful details. SwiftI2V introduces Conditional Segment-wise Generation (CSG) to synthesize videos segment-by-segment with a bounded per-step token budget. On VBench-I2V at 2K resolution, SwiftI2V achieves performance comparable to end-to-end baselines while reducing total GPU-time by 202x.
