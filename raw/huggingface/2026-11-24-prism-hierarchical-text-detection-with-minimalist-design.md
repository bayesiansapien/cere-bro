---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.930919+00:00
arxiv_id: 2611.26254
url: https://huggingface.co/papers/2611.26254
arxiv_url: https://arxiv.org/abs/2611.26254
date: 2026-11-24
---

# Prism: Hierarchical Text Detection with Minimalist Design

Hierarchical text detection aims to localize words, text lines, and paragraphs while parsing their structural relationships. It provides essential structural cues for visual text understanding. To maximize accuracy, existing methods typically rely on complex multi-scale feature fusion necks and heavy-weight heads, resulting in bloated architectures and low inference efficiency. In this paper, we argue that a sufficiently pre-trained backbone can effectively replace these sophisticated external modules, while simple geometric inclusion suffices for hierarchical text structural parsing. Thus, we propose Prism, a minimalist framework for hierarchical text detection. Prism performs multi-granularity detection by attaching parallel lightweight heads to a single-scale backbone feature map, covering words, text lines, and paragraphs, and reconstructs the structural hierarchy via an efficient geometric inclusion algorithm. In addition, we systematically compare representative lightweight head archetypes and show that pixel-level regression offers the best accuracy-efficiency trade-off in this setting. Experiments on multiple public benchmarks show that our significantly simplified architecture achieves state-of-the-art (SOTA) performance with remarkable efficiency. Specifically, it runs 1.7times faster than LRANet on CTW1500 while achieving higher accuracy, and surpasses the current SOTA method, OmniParser V2, by over 6 PQ points on the hierarchical HierText dataset. Code will be released soon.
