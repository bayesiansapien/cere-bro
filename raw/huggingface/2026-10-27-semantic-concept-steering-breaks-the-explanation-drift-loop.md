---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33877
url: https://huggingface.co/papers/2610.33877
arxiv_url: https://arxiv.org/abs/2610.33877
date: 2026-10-27
---

# Semantic Concept Steering Breaks the Explanation Drift Loop in Continual Learning

Catastrophic forgetting in continual learning (CL) manifests not only as accuracy degradation but also as explanation drift: models maintain predictive accuracy while silently shifting attention from diagnostic features to spurious correlations. This work identifies and resolves a previously overlooked structural flaw in explanation-aware CL: pixel-level saliency regularization derives supervision targets from the model's own frozen saliency maps, creating a self-referential drift loop that actively reinforces spurious attention across tasks. We introduce C^3L (Concept-Consistent Continual Learning), which breaks this loop by anchoring regularization to class-consistent semantic concepts (e.g., ``curved beak'', ``striped pattern'') discovered offline, independent of model state, providing (i) target independence from model drift, and (ii) cross-instance semantic consistency across every instance of a class. We identify that our concept-based objective, combined with approximate LRP relevance conservation, induces a crowding-out effect: since concept and background regions compete for the relevance of the same prediction, enforcing high relevance within concept regions implicitly suppresses spurious background correlations without explicit penalization. \method does not require human-annotated concept sets, as it employs a fully automated concept discovery and spatial grounding. Extensive evaluation across five benchmarks and over 20 baselines demonstrates state-of-the-art performance in accuracy, forgetting, explanation quality, spurious correlation mitigation, and out-of-distribution robustness.
