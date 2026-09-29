---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.601530+00:00
arxiv_id: 2604.02103
url: https://huggingface.co/papers/2604.02103
arxiv_url: https://arxiv.org/abs/2604.02103
date: 2026-09-28
---

# BoundInk: Boundary-Aware Online Handwriting Generation

Realistic online handwriting depends not only on individual character shapes, but also on how a writer connects, spaces, and aligns adjacent characters. Existing methods rely primarily on long-range sequence modeling and capture these inter-character behaviors only implicitly. This often produces plausible glyphs accompanied by broken cursive joins, inconsistent spacing, or writer-inconsistent transitions. We introduce BoundInk, a writer-conditioned framework that treats inter-character boundaries as explicit generation units. By jointly modeling local transitions and surrounding text context, BoundInk preserves writer-specific glyph appearance while improving connectivity and spacing across complete text lines. We further introduce a boundary-aware evaluation framework that directly assesses cursive continuity and spatial relationships between characters beyond conventional trajectory similarity. Across three benchmark-matched settings, BoundInk improves all applicable boundary-quality measures and reduces normalized dynamic time warping by 17.6--47.8%. In blind human evaluations, BoundInk outputs are preferred in 78.0--82.6% of valid criterion-wise judgments.
