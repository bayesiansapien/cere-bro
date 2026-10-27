---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800097+00:00
arxiv_id: 2610.32250
url: https://huggingface.co/papers/2610.32250
arxiv_url: https://arxiv.org/abs/2610.32250
date: 2026-10-26
---

# Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction

Single-image 3D scene construction is a fundamental problem in 3D vision. Recent methods such as SAM-3Dfy enable end-to-end reconstruction of 3D assets and their scene layouts, but still struggle with fine-grained scene geometry and asset quality. Meanwhile, specialized 3D object generators provide detailed object geometry, while 3D foundation models offer strong and generalizable spatial understanding. We propose Easy-3Dfy, a compositional workflow that decouples object generation from scene layout estimation, allowing specialized models to fully exploit their respective strengths. An RPF-based aligner then bridges these capabilities by establishing geometric correspondence between object-local meshes and partial scene pointmaps, recovering object layout for scene composition. Without requiring complete scene-level supervision, the proposed workflow consistently outperforms SAM-3Dfy across multiple geometric metrics on Scene-Maker and 3D-FUTURE200. Our results demonstrate that explicit geometric composition can effectively combine high-quality object generation with strong spatial understanding, while enabling the workflow to benefit independently from advances in both 3D object generation and foundation models.
