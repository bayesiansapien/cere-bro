---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13688
category: cs.AI
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13688
published: 2026-04-16
authors: Yizhao Xu, Hongyuan Zhu, Caiyun Liu
---

# Beyond Voxel 3D Editing: Learning from 3D Masks and Self-Constructed Data

**arXiv:** https://arxiv.org/abs/2604.13688
**Authors:** Yizhao Xu, Hongyuan Zhu, Caiyun Liu

## Abstract

arXiv:2604.13688v1 Announce Type: cross  Abstract: 3D editing refers to the ability to apply local or global modifications to 3D assets. Effective 3D editing requires maintaining semantic consistency by performing localized changes according to prompts, while also preserving local invariance so that unchanged regions remain consistent with the original. However, existing approaches have significant limitations: multi-view editing methods incur losses when projecting back to 3D, while voxel-based editing is constrained in both the regions that can be modified and the scale of modifications. Moreover, the lack of sufficiently large editing datasets for training and evaluation remains a challenge. To address these challenges, we propose a Beyond Voxel 3D Editing (BVE) framework with a self-constructed large-scale dataset specifically tailored for 3D editing. Building upon this dataset, our model enhances a foundational image-to-3D generative architecture with lightweight, trainable modules, enabling efficient injection of textual semantics without the need for expensive full-model retraining. Furthermore, we introduce an annotation-free 3D masking strategy to preserve local invariance, maintaining the integrity of unchanged regions during editing. Extensive experiments demonstrate that BVE achieves superior performance in generating high-quality, text-aligned 3D assets, while faithfully retaining the visual characteristics of the original input.
