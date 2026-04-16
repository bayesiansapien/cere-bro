---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13386
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13386
published: 2026-04-16
authors: Erik Nordby, Tasha Pais, Aviel Parrack
---

# Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling

**arXiv:** https://arxiv.org/abs/2604.13386
**Authors:** Erik Nordby, Tasha Pais, Aviel Parrack

## Abstract

arXiv:2604.13386v1 Announce Type: new  Abstract: Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types. We show that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge. Across 12 models (0.5B--176B parameters), we find probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81). Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.
