---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2608.02583
url: https://huggingface.co/papers/2608.02583
arxiv_url: https://arxiv.org/abs/2608.02583
date: 2026-08-04
---

# UEmbed: Unified Sparse and Dense Multimodal Embeddings

Sparse retrieval underpins modern search systems, from web search to retrieval-augmented generation. Existing work has introduced Learned Sparse Retrieval (LSR) to push beyond exact lexical matching toward richer semantics. Yet LSR has so far remained tied to encoder-style bidirectional architectures, and its extension to multimodal settings still relies heavily on auxiliary cross-modal modules. To address these limitations, we introduce UEmbed (Unified Embedding), a decoder-only multimodal embedding model that produces both sparse lexical and dense representations in one causal forward pass. UEmbed appends N learnable special tokens to the input and partitions the vocabulary into N disjoint subsets. Each token's causal hidden state predicts sparse weights over its assigned subset, and the N subsets are concatenated into the full sparse vector. Trained on public data, we release UEmbed at 2B, 4B, and 9B scales. UEmbed-9B reaches 71.8 (dense) and 71.0 (sparse) on MMEB-v2, outperforming multimodal embedding models trained on publicly available data (e.g., RzenEmbed). On BEIR, UEmbed also remains competitive with strong dense and sparse baselines. Furthermore, we demonstrate the practical utility of UEmbed across three dimensions: effectiveness, efficiency, and agentic applications. Overall, UEmbed offers a new paradigm: it unifies dense and sparse embeddings in one model, while further extending sparse retrieval to unify text and multimodal inputs.
