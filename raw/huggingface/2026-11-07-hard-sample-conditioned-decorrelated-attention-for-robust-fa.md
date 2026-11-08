---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.596764+00:00
arxiv_id: 2610.41789
url: https://huggingface.co/papers/2610.41789
arxiv_url: https://arxiv.org/abs/2610.41789
date: 2026-11-07
---

# Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition

Multi-head attention in Vision Transformers (ViTs) allows independent attention patterns across heads, but without explicit regularization, heads may learn redundant patterns rather than complementary roles. Correlation-based penalties encourage head disentanglement, yet apply uniform regularization across all training samples. In face recognition (FR), hard samples whose embeddings lie close to competing identities are critical for optimization and generalization. Motivated by this, we propose ViT-HarDis, which conditions attention head disentanglement on sample difficulty: samples with high cosine similarity to negative class centers receive stronger head decorrelation, enforcing specialization where identity ambiguity is highest. Experiments show improvements over both the baseline and uniform disentanglement on most benchmarks. Our analysis shows that ViT-HarDis reduces the similarity of hard samples to competing class centers while decreasing inter-head attention similarity, and that applying disentanglement only to the final transformer layers outperforms regularizing the entire network. Trained on WebFace4M, ViT-HarDis achieves SOTA results among ViT-based methods on IJB-B, IJB-C, and TinyFace Rank-1, while achieving the best IJB-B and TinyFace results when trained on MS1MV3, improving FR without architectural modifications or additional inference cost. Code: https://github.com/TaharChettaoui/Hard-Sample-Conditioned-Attention-for-FR.
