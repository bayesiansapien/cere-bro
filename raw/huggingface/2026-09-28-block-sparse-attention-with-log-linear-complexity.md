---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.594360+00:00
arxiv_id: 2609.31093
url: https://huggingface.co/papers/2609.31093
arxiv_url: https://arxiv.org/abs/2609.31093
date: 2026-09-28
---

# Block Sparse Attention with Log-Linear Complexity

Scaling language models to long contexts is limited by the quadratic cost of self-attention. Block sparse attention offers an efficient alternative, but selecting the retained blocks remains a bottleneck. Conventional block selection requires scoring all query-block pairs and therefore remains quadratic in sequence length. To address this issue, we propose PISA, a block-sparse attention mechanism that employs a pyramid Top-K selection strategy. The main idea is to gradually narrow down the candidates across different levels, making it more efficient to find the most relevant keys. Specifically, we construct a coarse-to-fine hierarchy of keys and perform selection from the coarsest level. At each level, LogSumExp scoring is applied to a bounded candidate set to select candidates for the next finer level, continuing until the finest level is reached. Through pooling, we construct O(log N) levels of keys, yielding an overall complexity of O(Nlog N), where N denotes the sequence length. We develop hardware-aware Triton kernels for both training and inference, fusing hierarchical routing and LogSumExp scoring without materializing the query-key score matrix. We further evaluate our method on language modeling tasks. Compared with the baseline, our method achieves comparable performance on benchmarks such as commonsense reasoning while delivering better results on retrieval tasks.
