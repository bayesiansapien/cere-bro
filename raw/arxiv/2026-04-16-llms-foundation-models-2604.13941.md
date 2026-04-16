---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13941
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13941
published: 2026-04-16
authors: Songlin Du, Xiaoyong Lu, Yaping Yan
---

# SceneGlue: Scene-Aware Transformer for Feature Matching without Scene-Level Annotation

**arXiv:** https://arxiv.org/abs/2604.13941
**Authors:** Songlin Du, Xiaoyong Lu, Yaping Yan

## Abstract

arXiv:2604.13941v1 Announce Type: new  Abstract: Local feature matching plays a critical role in understanding the correspondence between cross-view images. However, traditional methods are constrained by the inherent local nature of feature descriptors, limiting their ability to capture non-local scene information that is essential for accurate cross-view correspondence. In this paper, we introduce SceneGlue, a scene-aware feature matching framework designed to overcome these limitations. SceneGlue leverages a hybridizable matching paradigm that integrates implicit parallel attention and explicit cross-view visibility estimation. The parallel attention mechanism simultaneously exchanges information among local descriptors within and across images, enhancing the scene's global context. To further enrich the scene awareness, we propose the Visibility Transformer, which explicitly categorizes features into visible and invisible regions, providing an understanding of cross-view scene visibility. By combining explicit and implicit scene-level awareness, SceneGlue effectively compensates for the local descriptor constraints. Notably, SceneGlue is trained using only local feature matches, without requiring scene-level groundtruth annotations. This scene-aware approach not only improves accuracy and robustness but also enhances interpretability compared to traditional methods. Extensive experiments on applications such as homography estimation, pose estimation, image matching, and visual localization validate SceneGlue's superior performance. The source code is available at https://github.com/songlin-du/SceneGlue.
