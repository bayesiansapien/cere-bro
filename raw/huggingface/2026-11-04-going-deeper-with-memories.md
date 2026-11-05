---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.367682+05:30
arxiv_id: 2611.05255
url: https://huggingface.co/papers/2611.05255
arxiv_url: https://arxiv.org/abs/2611.05255
date: 2026-11-04
---

# Going Deeper With Memories

Byte level language models avoid tokenizer dependence and provide universal coverage, but processing every byte at full resolution is expensive. We introduce DeepMem, a causal multiscale architecture that separates semantic compression from exact byte preservation. A learned invertible subband transform constructs a hierarchy of shorter sequences, while a lossless carrier and explicit detail sidebands preserve byte identity. Fast weight memory blocks operate along the encoder, with iterative shared state computation at the compressed bottleneck, while an attention based super resolution decoder restores byte resolution representations. DeepMem achieves stronger language modeling performance than a matched byte level Transformer on FineWeb-Edu and PG19, and obtains the best macro average performance across the evaluated FLORES languages. It also improves PIQA accuracy while remaining competitive on code modeling, multiple choice reasoning, and byte level corruption robustness. Bottleneck refinement requires approximately 7{,}600times fewer counted FLOPs than equivalent full resolution reasoning, while maintaining competitive evaluation throughput.
