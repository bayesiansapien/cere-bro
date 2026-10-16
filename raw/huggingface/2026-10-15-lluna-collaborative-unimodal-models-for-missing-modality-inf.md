---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234801+05:30
arxiv_id: 2610.20526
url: https://huggingface.co/papers/2610.20526
arxiv_url: https://arxiv.org/abs/2610.20526
date: 2026-10-15
---

# Lluna: Collaborative Unimodal Models for Missing-Modality Inference

Pretrained unimodal models offer a flexible route to multimodal prediction through collaboration, but this collaboration can become less accurate than a surviving unimodal model when modalities are missing. We study this setting using fixed surviving-model anchors and find that collaborative gains can weaken or reverse as inputs disappear, even when the anchor's own input is unchanged. Our diagnostics further reveal reduced recovery of modality-specific information after aggregation and state-dependent collaborative representations. We propose Lluna, which combines a direct private prediction path from adapted unimodal features with a common graph-based collaboration branch that provides a residual correction. Progressive Collaboration Consistency organizes richer-to-poorer guidance along single-modality removals, aligning normalized common representations while task supervision adapts predictions to the available evidence. Across eight datasets spanning affective computing, scene understanding, and medical prediction, Lluna achieves the best evaluated average performance over non-full input states, improving Mean-Missing by 4.26\% on average relative to the strongest evaluated baseline. The fixed-anchor diagnostic also shows positive gains in mean collaboration under minimal inputs on all eight tasks. Code is available at https://github.com/AIFrontierLab/Lluna.
