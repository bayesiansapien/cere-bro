---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.594207+00:00
arxiv_id: 2611.07298
url: https://huggingface.co/papers/2611.07298
arxiv_url: https://arxiv.org/abs/2611.07298
date: 2026-11-07
---

# Reducing Representational Interference in Retrieval Embeddings with Trainable Prefix Tokens

Embedding models compress variable-length text into fixed-size vector representations, but this compression can entangle semantic content with residual token-level information, such as artifacts arising from attention sink behavior. We propose a simple method that prepends trainable [DUMP] tokens to the input during embedding model training. The method keeps the model architecture, pooling strategy, and training loss unchanged, while optimizing the added tokens through the standard contrastive retrieval objective. By introducing trainable prefix positions that interact with regular tokens during encoding, [DUMP] tokens help reduce the influence of residual or uninformative token-level signals on the final retrieval representation. Experiments on standard retrieval and long-context benchmarks show that our method consistently improves over finetuned baselines across encoder and decoder embedding models. Further analysis shows that [DUMP] tokens alter token-level activation and attention patterns associated with low-information tokens. These results suggest that trainable prefix tokens provide a lightweight way to improve retrieval representations.
