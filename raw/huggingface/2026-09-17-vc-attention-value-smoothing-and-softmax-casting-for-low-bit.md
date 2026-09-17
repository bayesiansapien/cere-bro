---
source: farmer/huggingface
farmed: 2026-09-17T10:54:35.301049
arxiv_id: 2609.15810
url: https://huggingface.co/papers/2609.15810
arxiv_url: https://arxiv.org/abs/2609.15810
date: 2026-09-17
---

# VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention

Diffusion Transformers deliver state-of-the-art video generation, but their long spatiotemporal sequences make attention the dominant deployment cost, and a deployable low-bit kernel must be accurate and fast. Accuracy is limited by outliers: a block's quantization scale is set by its largest entries, leaving typical entries confined to a narrow range of representable values. Prior work smooths queries and keys, but value outliers follow no fixed channel or spatiotemporal structure and remain the dominant source of output error. Speed is limited by softmax: low-bit Tensor Cores accelerate only the two matrix multiplications, so the high-precision exponential between them becomes the longest pipeline stage on datacenter GPUs. We propose VC-Attention, a training-free low-bit attention framework that addresses both by pairing Value smoothing with a fused probability Cast. V-Smooth reorders value tokens by lightweight online clustering, so the tokens in a hardware block quantize well together. It quantizes only the residual after subtracting the block mean, and restores that mean from the row sum the online softmax already maintains. ExpCast-FP8 maps log-domain scores directly to E4M3 probability codes with one fused multiply-add, eliminating the FP32 exponential and the format conversion. We implement VC-Attention for B200, B300, H200, RTX PRO 6000, and RTX 5090. Across Wan2.2, LongCat-Video, HunyuanVideo-1.5, and MiniMax-H3, VC-Attention improves fidelity over low-bit baselines, speeds up the attention kernel over BF16 FlashAttention-4 by 1.46-1.59x on datacenter Blackwell and Hopper and by 2.3-3.6x on workstation cards, and generates a clip 1.13-1.19x and 1.36-1.70x faster end to end.
