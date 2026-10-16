---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.233241+05:30
arxiv_id: 2606.24472
url: https://huggingface.co/papers/2606.24472
arxiv_url: https://arxiv.org/abs/2606.24472
date: 2026-10-15
---

# G^3VLA: Geometric Inductive Bias for Vision-Language-Action Models

Vision-language-action (VLA) models have rapidly advanced generalist robot manipulation by harnessing the semantic knowledge of pretrained vision-language backbones. However, their visual representations are typically grounded in 2D image coordinates rather than calibrated camera geometry. This limitation is especially pronounced in multi-camera systems, where views are coupled by known intrinsics and extrinsics but processed as independent images. We propose G^3VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or original action-learning objective. G^3VLA combines intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion to establish geometrically consistent representations across camera views. Geometric supervision is provided by ground-truth point maps or confidence-gated π^3X teacher predictions, enabling training without depth sensors or manual geometric annotations. On π_0, G^3VLA consistently improves performance on LIBERO and RoboCasa24 under both supervision regimes, while ground-truth supervision improves five-task RoboTwin2.0 averages with three cameras. Experiments on camera-shifted LIBERO-Goal and real robots demonstrate improved robustness to unseen camera viewpoints. Controlled calibration studies across π_0 and π_{0.5} show that these gains depend on correct camera geometry while remaining stable under mild calibration perturbations. These results demonstrate that grounding VLA visual tokens in calibrated camera geometry provides a simple and general mechanism for improving geometric consistency, multi-view reasoning, and viewpoint robustness in pretrained robot policies.
