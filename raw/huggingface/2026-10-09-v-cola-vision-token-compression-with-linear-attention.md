---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.415504+00:00
arxiv_id: 2610.11251
url: https://huggingface.co/papers/2610.11251
arxiv_url: https://arxiv.org/abs/2610.11251
date: 2026-10-09
---

# V-CoLA: Vision Token Compression with Linear Attention

Vision-language models (VLMs) have demonstrated impressive capabilities but suffer from substantial computational overhead, as vision tokens dominate the input sequence. This motivates vision token compression as a key direction to alleviate the burden. However, with the emergence of hybrid architectures incorporating linear attention (\eg, Qwen3.5), prior methods designed for softmax attention struggle to generalize. Our analysis reveals that both attention- and similarity-based approaches suffer notable performance degradation, underscoring the urgent need for compression methods tailored to this regime. To this end, we propose V-CoLA, an efficient training-free token compression framework specifically designed for linear attention. V-CoLA introduces a novel uniqueness-aware importance criterion for identifying critical vision tokens, coupled with an adaptive token merging strategy that performs compression. All components are optimized at the implementation level to remain compatible with the chunk-wise parallelism of linear attention, ensuring strong practical value. Extensive experiments across multiple benchmarks demonstrate the superiority of V-CoLA: it achieves 99.5\% of the original performance with only 50.0\% of vision tokens, and over 88.0\% with as few as 12.5\%, while delivering a 1.86times to 6.15times prefill speedup.
