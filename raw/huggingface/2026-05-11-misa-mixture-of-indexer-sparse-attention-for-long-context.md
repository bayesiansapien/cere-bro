---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.07363
url: https://huggingface.co/papers/2605.07363
arxiv_url: https://arxiv.org/abs/2605.07363
date: 2026-05-11
---

# MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference

DeepSeek Sparse Attention (DSA) sets the state of the art for fine-grained inference-time sparse attention by introducing a learned token-wise indexer that scores every prefix token and selects the top-k for the main attention. To remain expressive, the indexer uses H^I query heads (e.g. 64 on DeepSeek-V3.2) that share the same selected token set; this multi-head design is precisely what makes the indexer the dominant cost on long contexts. We propose MISA (Mixture of Indexer Sparse Attention), a drop-in replacement for the DSA indexer that treats its H^I heads as a pool of mixture-of-experts: a lightweight router uses cheap block-level statistics to pick a query-dependent subset of h << H^I active heads, and only those heads run the heavy token-level scoring. This preserves the diversity of the original indexer pool while reducing the per-query cost from O(H^I*L) to O(h*L+H^I*M) with M=ceil(L/B) << L pooled keys. Following HISA, we further introduce a hierarchical variant, MISA†, that uses the MoE-routed pass to keep an enlarged candidate set and then re-ranks it with the original DSA indexer to recover the final top-k almost exactly. With h=8 active heads and no additional training, MISA matches the dense DSA indexer on LongBench across DeepSeek-V3.2 and GLM-5 while running with 8x and 4x fewer indexer heads, respectively, and outperforms HISA on average; it preserves fully green Needle-in-a-Haystack heatmaps up to 128K context and recovers more than 92% of the tokens selected by the DSA indexer per layer. Our TileLang kernel delivers roughly a 3.82x speedup over DSA's original indexer kernel on a single NVIDIA H200 GPU. These results show that indexer-head-axis routing is a practical and complementary axis of efficiency for fine-grained sparse attention, on top of the existing token-axis hierarchies.
