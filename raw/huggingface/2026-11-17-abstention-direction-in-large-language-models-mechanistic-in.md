---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.111632+00:00
arxiv_id: 2611.20441
url: https://huggingface.co/papers/2611.20441
arxiv_url: https://arxiv.org/abs/2611.20441
date: 2026-11-17
---

# Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment

Abstention, the withholding of a response by a large language model (LLM) under uncertainty or safety risks, is essential for trustworthy models. The causes of abstention fall into three perspectives: ambiguity in the Query (Q), limits of Model Knowledge (MK), and misalignment with Human Values (HV). However, prior analyses of internal representations have focused on HV, using a refusal direction computed from harmful and harmless queries. No study has analyzed the three perspectives jointly. We therefore extend the refusal direction framework to all three perspectives. Specifically, for each perspective, we construct counterfactual pairs that share a template and differ only in the abstention-inducing factor, and compute an abstention direction by normalizing the difference in mean activations between the two polarities. Activation steering experiments show that intervening in middle layers increases or decreases abstention across all three perspectives. Moreover, steering yields cross-perspective effects, indicating that the abstention directions share a common directional component.
