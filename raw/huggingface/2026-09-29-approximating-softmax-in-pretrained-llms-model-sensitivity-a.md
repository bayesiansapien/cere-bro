---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934878+00:00
arxiv_id: 2609.33586
url: https://huggingface.co/papers/2609.33586
arxiv_url: https://arxiv.org/abs/2609.33586
date: 2026-09-29
---

# Approximating Softmax in Pretrained LLMs: Model Sensitivity and Kernel Acceleration

On NVIDIA Blackwell B200, tensor-core throughput outpaces special-function exponential throughput by more than two orders of magnitude, exposing exponential evaluation in fused attention kernels. A pretrained Transformer, however, may not need it evaluated accurately at every element. We characterize what a pretrained model does need by approximating softmax at inference in ten frozen decoder-only models (0.5B-72B). The number of positions the softmax map assigns probability to and within-row resolution can be cut substantially, yet uniform weighting of the same positions is damaging. Where a fixed resolution budget is placed matters as much as its size, with resolution near the row maximum consistently favored. Perturbations matched on scalar distortion produce model-dependent responses of opposite sign. These findings motivate Rowmax-PoT, a coarse logarithmic weight representation anchored at each row maximum, and Rowmax-H15, its hardware specialization in FlashAttention-4. On B200, the patched FP8 attention forward is 12.4% faster at causal 8K and 25.8% faster at non-causal 8K in host-side call-latency measurements; board energy per forward falls by 8.4% at causal 16K. Measured separately on the BF16 kernel path at 2K, Rowmax-H15 increases perplexity by 0.091-0.492% across five models from three families.
