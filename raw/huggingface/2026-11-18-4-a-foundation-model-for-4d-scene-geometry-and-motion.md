---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.23144
url: https://huggingface.co/papers/2611.23144
arxiv_url: https://arxiv.org/abs/2611.23144
date: 2026-11-18
---

# π^4: A Foundation Model for 4D Scene Geometry and Motion

π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for multi-image inputs. It couples a geometry branch with a geometry-conditioned motion branch, which predicts image-space correspondences that are lifted into 3D using reconstructed target-view geometry. Across diverse benchmarks, π^4 achieves the best overall average rank in geometry evaluation, alongside competitive performance in single- and multiview 2D/3D point tracking and moving-object segmentation. With a shared backbone, the full geometry-and-motion system contains approximately 0.5B parameters---less than half the size of most baselines. It produces joint reconstructions and tracks in one forward pass, including large-scale scenes with thousands of input images despite training with contexts of at most 64 views. We further present the data and training recipe underlying these capabilities, together with empirical studies of key design choices. Code and models are available at https://github.com/yyfz/Pi4.
