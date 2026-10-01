---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33326
url: https://huggingface.co/papers/2609.33326
arxiv_url: https://arxiv.org/abs/2609.33326
date: 2026-09-30
---

# ANTMAN: Adaptive Need Tracking for Multi-Agent Navigation in Large Information Spaces

Information-seeking agents increasingly operate over information spaces that are too large to process exhaustively. Yet many multi-agent systems organize computation around static partitions of the available space, causing coordination to grow with how information is segmented rather than with what the query still requires. We introduce ANTMAN, an adaptive coordination framework that treats evolving unresolved information needs as the unit of runtime coordination. ANTMAN maintains a revisable Need Graph that tracks unresolved requirements, accumulated evidence, prior attempts, and search progress, and uses this state to control worker selection, routing, and task-local recovery as new evidence is discovered. By separating the coordination policy from substrate-specific search interfaces, the same need-conditioned mechanism can operate across different information spaces. Experiments across multi-document question answering, controlled long-context scaling, and realistic structured navigation show that ANTMAN remains effective across settings, including when execution is delegated to substantially smaller worker models. Under a 16x increase in searchable context, ANTMAN increases active coordination by only 1.23x, compared with more than 15x for partition-driven baselines, while preserving strong answer quality.
