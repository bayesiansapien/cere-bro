---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.02148
url: https://huggingface.co/papers/2608.02148
arxiv_url: https://arxiv.org/abs/2608.02148
date: 2026-08-10
---

# Douyin Multimodal Embedding Model Technical Report

Multimodal representation learning is a cornerstone of modern AI. By encoding multimodal queries and targets into vectors, it powers industrial search and recommendation and underpins modern agents. Real-world platforms with complex modalities and massive-scale content, such as Douyin, Xiaohongshu, and YouTube, demand both efficiency under billion-scale indexing and fine-grained discrimination for hard matching. Existing MLLM embedding models rarely satisfy both. Contrastive models are efficient but rely on pair-level supervision too coarse for fine-grained distinctions, while CoT-based models improve discrimination through explicit generation impractical to serve online. We present Douyin Multimodal Embedding (DME), a model trained in two stages to combine both strengths. Stage 1 performs large-scale contrastive pre-training that establishes a unified multimodal embedding space with broad modality and task coverage. Stage 2 supplements semantic sufficiency, the property that an embedding is grounded in retrieval-relevant evidence and preserves fine-grained counterpart-side semantics, via two mechanisms. Evidence-Grounded Typed Latent Reasoning organizes retrieval evidence through hidden-space latent reasoning, and Cross-Conditional Reconstruction enforces counterpart-side semantics through cross-directional autoregressive reconstruction. Both act only during training and add only marginal query-side overhead, so DME serves as efficiently as a standard contrastive encoder. On MMEB-v2, DME reaches state-of-the-art results at comparable scales for its 2B and 9B variants (74.8 and 78.4), with especially strong video and visual-document tasks. In production, DME delivers a 2.92% relative gain on Douyin's in-house offline evaluation set, is deployed across Douyin scenarios such as generative, image, and AI search, and yields a 0.1% Lifetime (LT) gain in online A/B testing on Douyin search.
