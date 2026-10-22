---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.21810
url: https://huggingface.co/papers/2610.21810
arxiv_url: https://arxiv.org/abs/2610.21810
date: 2026-10-20
---

# N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models

Conditional memory expands language-model capacity through selective lookup, but the full embedding table must remain available for every possible input. We introduce Conditional Program (CP), a compressed representation that reconstructs only the rows an input requests. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table. We instantiate this representation with a Gaussian trellis, norm restoration and independently decodable row records. CP's two-bit code lowers output KL by 41--63\% relative to 2-bit round-to-nearest. Analysis across three trained n-gram memory families shows that Gaussian-like coordinate statistics coexist with learned relationships among rows; at matched storage budgets, the shared trellis outperforms the fitted codebooks and low-rank residual variants we test. For DeepSeek, it reduces table storage from 203GB to 51GB, leaving room for larger workloads when the table is kept on GPU.
