---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.03344
url: https://huggingface.co/papers/2611.03344
arxiv_url: https://arxiv.org/abs/2611.03344
date: 2026-11-03
---

# FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell

Attention remains a substantial computational cost in Transformer training, particularly at long context lengths. NVIDIA Blackwell GPUs provide high-throughput low-precision matrix multiplication, but exploiting it in attention requires addressing quantization overhead, causal information leakage through shared scales, and numerical inconsistencies between the forward and backward passes. We present FLAMIA, a family of attention kernels for Blackwell with MXFP8 and mixed NVFP4/FP8 training paths. Our design combines token-block scaling that reuses quantized operands across matrix orientations, targeted safeguards against scale-induced leakage, and consistent forward and backward computations. Fused quantization and architecture-specific kernel optimizations reduce overhead, while document-local scaling and workload-aware scheduling support variable-length documents directly in packed layouts without repacking. Across various causal packed-document workloads, the MXFP8 path accelerates the combined forward and backward attention call, including quantization, by factors of 1.10--1.40times on B200 and 1.06--1.42times on B300 relative to the fastest evaluated baseline for each workload. We validate training stability and quality preservation on pretraining Llama-style models. These results show how jointly designing quantization, training numerics, and document scheduling translates low-bit hardware throughput into practical attention acceleration.
