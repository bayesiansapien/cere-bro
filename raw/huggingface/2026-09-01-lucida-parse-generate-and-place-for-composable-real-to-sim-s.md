---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30821
url: https://huggingface.co/papers/2608.30821
arxiv_url: https://arxiv.org/abs/2608.30821
date: 2026-09-01
---

# Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling

Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations. We propose Lucida, which keeps this order but redistributes the requirements, so each step consumes only what a real capture reliably provides and precision is reached at the end of the pipeline rather than demanded at its start. Lucida parses the video into a scene graph whose nodes carry per-instance multi-view evidence, generates a complete asset for each instance from its evidence, and places assets with GizmoAct, a VLM policy that casts placement as multi-turn GUI interaction, manipulating the object's gizmo in a closed loop and deciding itself when alignment is reached. Across scene-level 3D object detection, object pose estimation, and scene reconstruction, Lucida improves mAP over Boxer by 69% on R2S-Scene, raises ADD-SB@0.05 from 57.8% to 83.4% on CA-1M, and increases scene F-Score from 0.794 for SAM3D to 0.924.
