---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.115964+00:00
arxiv_id: 2611.09825
url: https://huggingface.co/papers/2611.09825
arxiv_url: https://arxiv.org/abs/2611.09825
date: 2026-11-17
---

# BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design

The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely on vector codebooks whose lookup overhead degrades decoding throughput. We present BitDecoding-FP4, an algorithm--system co-design for accurate and efficient native FP4 KV decoding. We mitigate three error sources: Dual-Residual Query Quantization splits queries into two FP4 tensors, cutting query logit error from 60% to 1%; Underflow-Aware Probability Scaling prevents E4M3 scales from rounding long-context probabilities to zero; and Outlier-Aware Key Quantization combines static smoothing, Hadamard rotation, and scale search to suppress key outliers under token-wise scaling. At the system level, we remove the softmax bottleneck via transposed softmax with fused probability quantization and stacked query MMA on paged KV caches. Across dense and MoE models with GQA and MLA, BitDecoding-FP4 stays within 0.5 points of BF16 KV accuracy with NVFP4 (1 point with MXFP4), and tracks BF16 KV in RL training rollouts. In end-to-end serving on NVIDIA B300 with Qwen3-4B and Qwen3-30B-A3B, it delivers 2.4-3.0times higher peak serving throughput than BF16 KV. The implementation is available at https://github.com/OpenBitSys/BitDecoding-FP4.
