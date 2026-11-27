---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.905620+00:00
arxiv_id: 2611.33636
url: https://huggingface.co/papers/2611.33636
arxiv_url: https://arxiv.org/abs/2611.33636
date: 2026-11-26
---

# What Is Redundant at High Resolution? Efficient Attention and Feed-Forward Design for All-in-One Image Restoration

Multi-scale architectures are widely adopted in all-in-one image restoration (AIO-IR) to capture larger-scale context at low-resolution stages and refine details at high-resolution (HR) stages. However, processing spatially large feature maps at HR stages incurs substantial computational costs and memory traffic, making efficient HR processing challenging. To address this challenge, we propose High-resolution Global-Local Restoration (HiGLR), an efficient multi-scale AIO-IR network grounded in an analysis of spatial redundancy in self-attention and convolutional feed-forward networks (ConvFFNs). Specifically, this analysis identifies three key redundancies: per-query readout at the finest-scale stage, key routing across neighboring queries at intermediate stages, and spatial mixing in the expanded feature spaces of ConvFFNs. Accordingly, HiGLR replaces costly self-attention at the finest-scale stage with a learned input-independent kernel. At intermediate stages, we propose a Block-Routed Hybrid Attention, which combines coarse-scale dense attention with fine-scale block-sparse attention over value residuals relative to coarse summaries, and shares routing indices across neighboring queries. We further introduce a Dual-Space FFN that performs spatial mixing in a compact space and pointwise nonlinear transformation in an expanded space, enabling efficient kernel fusion. Combining these designs, HiGLR achieves state-of-the-art performance while delivering up to a 4.24times inference speedup over existing methods.
