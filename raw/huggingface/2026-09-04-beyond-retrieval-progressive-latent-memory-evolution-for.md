---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.04131
url: https://huggingface.co/papers/2609.04131
arxiv_url: https://arxiv.org/abs/2609.04131
date: 2026-09-04
---

# Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding

Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as additional visual context. Though effective, this store-and-retrieve paradigm keeps historical evidence as external visual context, preventing it from being internalized into a compact, evolving latent memory that can continuously guide streaming reasoning. To bridge this gap, we introduce LatentStream, a progressive latent working memory framework that shifts streaming memory from store-and-retrieve to retrieve-and-internalize. Specifically, LatentStream comprises three coordinated components. First, Query-agnostic Hierarchical Streaming Memory organizes visual history into short-, mid-, and long-term levels under a fixed memory budget through Jenks-guided adaptive consolidation. Once a query arrives, Hierarchical Latent Memory Evolution equips groups of latent memory tokens with progressively expanding memory receptive fields, enabling them to iteratively retrieve historical evidence from their corresponding scopes and internalize it into a compact, fixed-length latent memory. Finally, Progressive Confidence-guided Latent Memory Optimization constructs a hierarchical progression reward from group-wise predictive entropy and jointly refines the latent memory tokens and retrieved evidence, encouraging increasingly confident streaming reasoning. Extensive experiments demonstrate that LatentStream achieves new state-of-the-art results on existing online and offline video benchmarks.
