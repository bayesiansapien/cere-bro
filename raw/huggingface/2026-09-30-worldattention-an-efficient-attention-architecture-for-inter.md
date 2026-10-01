---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34606
url: https://huggingface.co/papers/2609.34606
arxiv_url: https://arxiv.org/abs/2609.34606
date: 2026-09-30
---

# WorldAttention: An Efficient Attention Architecture for Interactive Video World Models

Leveraging the paradigm of autoregressive diffusion, text-conditioned interactive video world models aim to simulate temporally coherent environments guided by textual instructions. While enabling low-latency, long-duration generation is pivotal for embodied AI and simulation-based planning, current frameworks primarily rely on sliding-window mechanisms to bound computational complexity. However, this approach inherently sacrifices historical context, undermining the long-range interactive capabilities. Conversely, maintaining a full-history cache remains computationally prohibitive and memory-intensive: the quadratic complexity of attention leads to excessive computational overhead, while the linear growth of the KV cache inevitably leads to GPU memory saturation. To overcome these limitations, we propose WorldAttention, a system-oriented attention architecture that achieves high efficiency through the co-design of specialized attention kernels and hierarchical KV cache management. First, we introduce Hybrid Sparse Attention (HSA), which integrates linear global attention supplemented with head-adaptive sparse attention. Additionally, we design a Hierarchical KV Cache (HKV) that organizes historical KV pairs into semantically indexed pages across multi-tier memory, enabling fine-grained retrieval and controlled GPU residency. These two designs are supported by tailored kernels to effectively translate their theoretical efficiency into real-world performance. Extensive experiments on VBench-Long and InterVBench demonstrate that WorldAttention consistently surpasses prior state-of-the-art methods, achieving subject consistency scores of 0.9472 on VBench-Long and 0.9668 on InterVBench, respectively.
