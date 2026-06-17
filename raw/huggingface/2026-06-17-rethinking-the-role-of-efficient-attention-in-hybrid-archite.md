---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.15378
url: https://huggingface.co/papers/2606.15378
arxiv_url: https://arxiv.org/abs/2606.15378
date: 2026-06-17
---

# Rethinking the Role of Efficient Attention in Hybrid Architectures

Modern language models increasingly adopt hybrid architectures that combine full attention with efficient attention modules, such as sliding-window attention (SWA) and recurrent sequence mixers. However, how these efficient modules shape model capabilities remains poorly understood. To address this gap, we conduct a systematic analysis across hybrid architectures from three perspectives: scaling behavior, mechanism analysis, and architecture design. First, from a scaling perspective, we find that efficient-attention design primarily affects how fast long-context capability emerges, while different hybrids eventually converge to comparable long-context performance under sufficient training. Second, mechanistically, we show that long-range retrieval is mainly carried by full attention, whereas efficient attention shapes its optimization trajectory. This explains a counter-intuitive phenomenon we call Large-Window Laziness: larger SWA windows can delay the formation of retrieval heads in full-attention layers. Third, guided by this mechanism, we show that applying NoPE to only the full-attention layers of a small-window SWA hybrid substantially improves long-context performance with negligible impact on short-context performance.
