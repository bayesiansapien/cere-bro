---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13924
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13924
published: 2026-04-16
authors: Romain Hermary, Samet Hicsonmez, Dan Pineau
---

# ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection

**arXiv:** https://arxiv.org/abs/2604.13924
**Authors:** Romain Hermary, Samet Hicsonmez, Dan Pineau

## Abstract

arXiv:2604.13924v1 Announce Type: cross  Abstract: Time-series anomaly detection (TSAD) is critical in domains such as industrial monitoring, healthcare, and cybersecurity, but it remains challenging due to rare and heterogeneous anomalies and the scarcity of labelled data. This scarcity makes unsupervised approaches predominant, yet existing methods often rely on reconstruction or forecasting, which struggle with complex data, or on embedding-based approaches that require domain-specific anomaly synthesis and fixed distance metrics. We propose ASTER, a framework that generates pseudo-anomalies directly in the latent space, avoiding handcrafted anomaly injections and the need for domain expertise. A latent-space decoder produces tailored pseudo-anomalies to train a Transformer-based anomaly classifier, while a pre-trained LLM enriches the temporal and contextual representations of this space. Experiments on three benchmark datasets show that ASTER achieves state-of-the-art performance and sets a new standard for LLM-based TSAD.
