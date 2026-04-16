---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14048
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14048
published: 2026-04-16
authors: Yuhang Dai, Xingyi Yang
---

# Free Geometry: Refining 3D Reconstruction from Longer Versions of Itself

**arXiv:** https://arxiv.org/abs/2604.14048
**Authors:** Yuhang Dai, Xingyi Yang

## Abstract

arXiv:2604.14048v1 Announce Type: new  Abstract: Feed-forward 3D reconstruction models are efficient but rigid: once trained, they perform inference in a zero-shot manner and cannot adapt to the test scene. As a result, visually plausible reconstructions often contain errors, particularly under occlusions, specularities, and ambiguous cues. To address this, we introduce Free Geometry, a framework that enables feed-forward 3D reconstruction models to self-evolve at test time without any 3D ground truth. Our key insight is that, when the model receives more views, it produces more reliable and view-consistent reconstructions. Leveraging this property, given a testing sequence, we mask a subset of frames to construct a self-supervised task. Free Geometry enforces cross-view feature consistency between representations from full and partial observations, while maintaining the pairwise relations implied by the held-out frames. This self-supervision allows for fast recalibration via lightweight LoRA updates, taking less than 2 minutes per dataset on a single GPU. Our approach consistently improves state-of-the-art foundation models, including Depth Anything 3 and VGGT, across 4 benchmark datasets, yielding an average improvement of 3.73% in camera pose accuracy and 2.88% in point map prediction. Code is available at https://github.com/hiteacherIamhumble/Free-Geometry .
