---
source: farmer/huggingface
farmed: 2026-05-07T00:00:00Z
arxiv_id: 2605.04569
url: https://huggingface.co/papers/2605.04569
arxiv_url: https://arxiv.org/abs/2605.04569
date: 2026-05-07
---

# Lightning Unified Video Editing via In-Context Sparse Attention

Video editing has evolved toward In-Context Learning (ICL) paradigms, yet the resulting quadratic attention costs create a critical computational bottleneck. In this work, we propose In-context Sparse Attention (ISA), the first near-lossless empirical sparse framework tailored for ICL video editing. Our design is grounded in two key insights: first, context tokens exhibit significantly lower saliency than source tokens; second, we theoretically prove and empirically validate that Query sharpness correlates with approximation error. Motivated by these findings, ISA implements an efficient pre-selection strategy to prune redundant context, followed by a dynamic query grouping mechanism that routes high-error queries to full attention and low-error ones to a computationally efficient 0-th order Taylor sparse attention. Furthermore, we build LIVEditor, a novel lightning video editing model via ISA and a proposed video-editing data pipeline that curated a 1.7M high-quality dataset. Extensive experiments demonstrate that LIVEditor achieves a ~60% reduction in attention-module latency while surpassing state-of-the-art methods across EditVerseBench, IVE-Bench, and VIE-Bench, delivering near-lossless acceleration without compromising visual fidelity.
