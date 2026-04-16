---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.07019
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.07019
published: 2026-04-16
authors: Jusen Du, Jiaxi Hu, Tao Zhang
---

# Native Hybrid Attention for Efficient Sequence Modeling

**arXiv:** https://arxiv.org/abs/2510.07019
**Authors:** Jusen Du, Jiaxi Hu, Tao Zhang

## Abstract

arXiv:2510.07019v3 Announce Type: replace-cross  Abstract: Transformers excel at sequence modeling but face quadratic complexity, while linear attention offers improved efficiency but often compromises recall accuracy over long contexts. In this work, we introduce Native Hybrid Attention (NHA), a novel hybrid architecture of linear and full attention that integrates both intra & inter-layer hybridization into a unified layer design. NHA maintains long-term context in key-value slots updated by a linear RNN, and augments them with short-term tokens from a sliding window. A single softmax attention operation is then applied over all keys and values, enabling per-token and per-head context-dependent weighting without requiring additional fusion parameters. The inter-layer behavior is controlled through a single hyperparameter, the sliding window size, which allows smooth adjustment between purely linear and full attention while keeping all layers structurally uniform. Experimental results show that NHA surpasses Transformers and other hybrid baselines on recall-intensive and commonsense reasoning tasks. Furthermore, pretrained LLMs can be structurally hybridized with NHA, achieving competitive accuracy while delivering significant efficiency gains. Code is available at https://github.com/JusenD/NHA.
