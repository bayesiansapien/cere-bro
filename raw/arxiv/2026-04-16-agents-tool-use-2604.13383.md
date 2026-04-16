---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13383
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13383
published: 2026-04-16
authors: Jiatao Dai, Wei Dong, Han Zhou
---

# UniBlendNet: Unified Global, Multi-Scale, and Region-Adaptive Modeling for Ambient Lighting Normalization

**arXiv:** https://arxiv.org/abs/2604.13383
**Authors:** Jiatao Dai, Wei Dong, Han Zhou

## Abstract

arXiv:2604.13383v1 Announce Type: new  Abstract: Ambient Lighting Normalization (ALN) aims to restore images degraded by complex, spatially varying illumination conditions. Existing methods, such as IFBlend, leverage frequency-domain priors to model illumination variations, but still suffer from limited global context modeling and insufficient spatial adaptivity, leading to suboptimal restoration in challenging regions. In this paper, we propose UniBlendNet, a unified framework for ambient lighting normalization that jointly models global illumination, multi-scale structures, and region-adaptive refinement. Specifically, we enhance global illumination understanding by integrating a UniConvNet-based module to capture long-range dependencies. To better handle complex lighting variations, we introduce a Scale-Aware Aggregation Module (SAAM) that performs pyramid-based multi-scale feature aggregation with dynamic reweighting. Furthermore, we design a mask-guided residual refinement mechanism to enable region-adaptive correction, allowing the model to selectively enhance degraded regions while preserving well-exposed areas. This design effectively improves illumination consistency and structural fidelity under complex lighting conditions. Extensive experiments on the NTIRE Ambient Lighting Normalization benchmark demonstrate that UniBlendNet consistently outperforms the baseline IFBlend and achieves improved restoration quality, while producing visually more natural and stable restoration results.
