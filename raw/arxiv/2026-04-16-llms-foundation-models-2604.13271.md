---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13271
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13271
published: 2026-04-16
authors: Anton Saenko, Pranshav Gajjar, Abiodun Ganiyu
---

# Enhancing Confidence Estimation in Telco LLMs via Twin-Pass CoT-Ensembling

**arXiv:** https://arxiv.org/abs/2604.13271
**Authors:** Anton Saenko, Pranshav Gajjar, Abiodun Ganiyu

## Abstract

arXiv:2604.13271v1 Announce Type: new  Abstract: Large Language Models (LLMs) are increasingly applied to complex telecommunications tasks, including 3GPP specification analysis and O-RAN network troubleshooting. However, a critical limitation remains: LLM-generated confidence scores are often biased and unreliable, frequently exhibiting systematic overconfidence. This lack of trustworthy self-assessment makes it difficult to verify model outputs and safely rely on them in practice. In this paper, we study confidence calibration in telecom-domain LLMs using the representative Gemma-3 model family (4B, 12B, and 27B parameters), evaluated on TeleQnA, ORANBench, and srsRANBench. We show that standard single-pass, verbalized confidence estimates fail to reflect true correctness, often assigning high confidence to incorrect predictions. To address this, we propose a novel Twin-Pass Chain of Thought (CoT)-Ensembling methodology for improving confidence estimation by leveraging multiple independent reasoning evaluations and aggregating their assessments into a calibrated confidence score. Our approach reduces Expected Calibration Error (ECE) by up to 88% across benchmarks, significantly improving the reliability of model self-assessment. These results highlight the limitations of current confidence estimation practices and demonstrate a practical path toward more trustworthy evaluation of LLM outputs in telecommunications.
