---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503742+00:00
arxiv_id: 2610.11850
url: https://huggingface.co/papers/2610.11850
arxiv_url: https://arxiv.org/abs/2610.11850
date: 2026-10-14
---

# VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval

Finding the right video often requires distinguishing similar scenes in which different events occur. Joint matching improves retrieval, but processing rich video representations for each query is costly. VEDJE compresses features within sampled frames while keeping their representations separate in a reusable cache. Feature-change prediction supplies an auxiliary training signal that improves retrieval from the compressed cache without adding work at query time. On MSR-VTT, MSVD, DiDeMo, and ActivityNet, VEDJE improves R@1 over matched first-stage retrievers in both retrieval directions. On MSR-VTT, it reaches 59.8 text-to-video R@1 with a fine-tuned VideoCLIP-XL first stage. In the VideoPrism configuration, shrinking the per-video cache fourfold to 12 KiB preserves text-to-video recall within 0.2 points. These results show that accurate video search can operate on compact evidence, encoded once and reused as new queries arrive.
