---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.01336
url: https://huggingface.co/papers/2606.01336
arxiv_url: https://arxiv.org/abs/2606.01336
date: 2026-06-02
---

# LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning

As real-world applications increasingly require processing inputs of 100k+ tokens, the gap between context length and inference efficiency has become a critical bottleneck. Context compression offers a way to reduce prefill costs while preserving task accuracy. However, existing training-free attention-based methods leave substantial gaps in demanding long-context tasks such as code reasoning. We present LongAttnComp, a long-context adaptation of AttnComp that fine-tunes a lightweight cross-attention scoring layer and introduces tokenlevel chunking, a token-budget top-p algorithm, positional reordering, and a formatagnostic query parser. We further design a two-stage fine-tuning recipe for the compressor: Stage 1 builds a general retrieval foundation from NIAH-style data, and Stage 2 extends it with multi-hop and reasoning data for broader long-context task coverage. On InfiniteBench Code-Debug, LongAttnComp matches or exceeds full-context accuracy, substantially outperforms training-free baselines, and transfers across four target models from three families. On LongBench v2, the two-stage recipe largely closes the Stage 1 gap on multi-document reasoning while preserving Code-Debug performance.
