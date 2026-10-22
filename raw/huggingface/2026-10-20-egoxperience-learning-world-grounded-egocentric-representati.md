---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26625
url: https://huggingface.co/papers/2610.26625
arxiv_url: https://arxiv.org/abs/2610.26625
date: 2026-10-20
---

# EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience

Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned supervision, yet existing methods and datasets offer limited support for either. We present EgoXperience, a full-stack paradigm that addresses these needs through data collection, automatic annotation, unified modeling, and benchmarking. Central to EgoXperience is an automatic annotation engine, EgoX-Engine, that couples geometrically verified object tracking with SLAM-based world alignment, yielding consistent supervision for the camera, scene, hands, and objects. This yields EgoX-Data-6M, a 50-hour dataset of task-driven manipulation and locomotion within and across indoor and outdoor environments, with second-level task captions. We carefully select one hour across these activity categories as EgoX-Bench to evaluate joint reconstruction. To translate this supervision into reconstruction, we introduce EgoX, trained with EgoX-Data-6M and complementary annotations from additional public datasets. Given monocular egocentric video and first-frame object masks, our model achieves joint metric reconstruction of the camera, scene, hands, and objects in a shared world coordinate frame with a single forward pass. Extensive experiments demonstrate state-of-the-art performance across scene estimation and world-space hand-object pose recovery. Against the strongest evaluated baselines, EgoX reduces camera, hand, and depth errors by 68.9%, 65.6%, and 42.9%, and improves object pose scores by 28.0%.
