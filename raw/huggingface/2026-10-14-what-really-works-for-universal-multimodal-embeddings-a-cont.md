---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.508599+00:00
arxiv_id: 2610.15035
url: https://huggingface.co/papers/2610.15035
arxiv_url: https://arxiv.org/abs/2610.15035
date: 2026-10-14
---

# What Really Works for Universal Multimodal Embeddings? A Controlled Study of Contrastive Training Strategies

Contrastive learning has become the standard paradigm for multimodal representation learning, aligning semantically matched pairs while separating mismatched ones in a shared embedding space. Although various contrastive training strategies have been proposed across negative selection, batch construction, and gradient modulation, their actual effectiveness under controlled, reproducible conditions remains poorly understood. This motivates a fundamental question: Do sophisticated contrastive strategies consistently bring meaningful downstream gains in multimodal embedding learning? To address this, we systematically evaluate representative strategies under a unified benchmarking framework on MMEB. Surprisingly, direct evaluations reveal that most existing strategies offer marginal gains over a standard aligned baseline, with several even degrading overall performance. To uncover the underlying failure modes, we introduce an MLLM-as-a-Judge diagnostic framework that dissects top-1 retrieval behaviors into labeled positives, false negatives (unlabeled valid matches), and hard/easy negative errors. Our systematic analysis yields three key insights: (1) Gradient distortion: Upweighting gradients from high-similarity negatives consistently hurts downstream generalization; (2) Distribution illusion: Wider separation between positive and negative similarity distributions does not necessarily translate to better retrieval performance; and (3) Synergistic training: While false-negative mitigation or hard-batch construction yields limited gains in isolation, integrating hard-negative mining, false-negative mitigation, and hard-batch construction achieves optimal performance, delivering an average improvement of 6.0% on MMEB with Qwen2-VL-2B. Overall, our findings demystify popular contrastive strategies and provide actionable recipes for training universal multimodal embedding models.
