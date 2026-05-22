---
source: farmer/huggingface
farmed: 2026-05-22T00:00:00+00:00
arxiv_id: 2605.16928
url: https://huggingface.co/papers/2605.16928
arxiv_url: https://arxiv.org/abs/2605.16928
date: 2026-05-22
---

# Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

Long-context inference in large language models is bottlenecked by the quadratic cost of full attention. Existing efficient alternatives often rely either on native sparse training or on heuristic token eviction, creating an undesirable trade-off among efficiency, training cost, and accuracy. In this work, we show that full-attention LLMs are already intrinsically sparse and can be transformed into highly sparse models with only minimal adaptation. Our approach is built on three observations: (1) only a small subset of attention heads truly requires full long-context processing; (2) long-range retrieval is governed primarily by a low-dimensional subspace, allowing relevant tokens to be retrieved efficiently with a 16-dimensional indexer; and (3) the useful token budget is strongly query-dependent, making dynamic top-p selection more suitable than fixed top-k sparsification. Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. By exploiting the model's intrinsic sparsity, RTPurbo achieves sparsification with only a few hundred training steps. Experiments on long-context benchmarks and reasoning tasks show that RTPurbo preserves near-lossless accuracy while delivering substantial efficiency gains, including up to a 9.36x prefill speedup at 1M context and about a 2.01x decode speedup. These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.
