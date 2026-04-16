---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13397
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13397
published: 2026-04-16
authors: Caiwen Jiang, Yuzhen Ding, Mi Jia
---

# A Multimodal Clinically Informed Coarse-to-Fine Framework for Longitudinal CT Registration in Proton Therapy

**arXiv:** https://arxiv.org/abs/2604.13397
**Authors:** Caiwen Jiang, Yuzhen Ding, Mi Jia

## Abstract

arXiv:2604.13397v1 Announce Type: new  Abstract: Proton therapy offers superior organ-at-risk sparing but is highly sensitive to anatomical changes, making accurate deformable image registration (DIR) across longitudinal CT scans essential. Conventional DIR methods are often too slow for emerging online adaptive workflows, while existing deep learning-based approaches are primarily designed for generic benchmarks and underutilize clinically relevant information beyond images. To address this gap, we propose a clinically scalable coarse-to-fine deformable registration framework that integrates multimodal information from the proton radiotherapy workflow to accommodate diverse clinical scenarios. The model employs dual CNN-based encoders for hierarchical feature extraction and a transformer-based decoder to progressively refine deformation fields. Beyond CT intensities, clinically critical priors, including target and organ-at-risk contours, dose distributions, and treatment planning text, are incorporated through anatomy- and risk-guided attention, text-conditioned feature modulation, and foreground-aware optimization, enabling anatomically focused and clinically informed deformation estimation. We evaluate the proposed framework on a large-scale proton therapy DIR dataset comprising 1,222 paired planning and repeat CT scans across multiple anatomical regions and disease types. Extensive experiments demonstrate consistent improvements over state-of-the-art methods, enabling fast and robust clinically meaningful registration.
