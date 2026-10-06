---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.26425
url: https://huggingface.co/papers/2609.26425
arxiv_url: https://arxiv.org/abs/2609.26425
date: 2026-10-05
---

# QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for Video World Models

Video world models achieve long-range temporal consistency by storing KV cache during generation, but the growing cache makes KV cache memory a major deployment bottleneck, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on VBench, however, when applied to video world models, we find they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to larger output degradation. We trace this discrepancy to attention in video world models: Key perturbations can change the attention logits, and shift the temporal-spatial tokens selected by Queries. These observations motivate us to preserve attention logits and temporal-spatial token selection during KV cache quantization. To address this issue, we present QuantWM, a training-free 2-bit KV cache quantization framework for video world models. QuantWM introduces two complementary techniques to mitigate the attention shifts. Firstly, quantization-sensitivity-aware clustering (QSAC) jointly considers historical Query sensitivity and residual ranges to select INT2-friendly Key centroids, which reduces quantization errors in channels that are more critical to attention. In addition, principal-subspace attention compensation (PSAC) restores the remaining Key errors along the dominant Query subspace using low-rank projections, which provides a direct and efficient correction to stabilize attention logits. Experiments on LingBot-World-v2, HY-World 1.5, Matrix-Game-2, Longcat-Video and Causal-Forcing demonstrate that QuantWM significantly improves visual quality and temporal consistency, while outperforming existing methods across benchmarks with up to 6.20 KV cache memory compression and limited additional overhead.
