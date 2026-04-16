---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13788
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13788
published: 2026-04-16
authors: Quentin Rolland, Fabrice Mayran de Chamisso, Jean-Baptiste Mouret
---

# Failure Identification in Imitation Learning Via Statistical and Semantic Filtering

**arXiv:** https://arxiv.org/abs/2604.13788
**Authors:** Quentin Rolland, Fabrice Mayran de Chamisso, Jean-Baptiste Mouret

## Abstract

arXiv:2604.13788v1 Announce Type: cross  Abstract: Imitation learning (IL) policies in robotics deliver strong performance in controlled settings but remain brittle in real-world deployments: rare events such as hardware faults, defective parts, unexpected human actions, or any state that lies outside the training distribution can lead to failed executions. Vision-based Anomaly Detection (AD) methods emerged as an appropriate solution to detect these anomalous failure states but do not distinguish failures from benign deviations. We introduce FIDeL (Failure Identification in Demonstration Learning), a policy-independent failure detection module. Leveraging recent AD methods, FIDeL builds a compact representation of nominal demonstrations and aligns incoming observations via optimal transport matching to produce anomaly scores and heatmaps. Spatio-temporal thresholds are derived with an extension of conformal prediction, and a Vision-Language Model (VLM) performs semantic filtering to discriminate benign anomalies from genuine failures. We also introduce BotFails, a multimodal dataset of real-world tasks for failure detection in robotics. FIDeL consistently outperforms state-of-the-art baselines, yielding +5.30% percent AUROC in anomaly detection and +17.38% percent failure-detection accuracy on BotFails compared to existing methods.
