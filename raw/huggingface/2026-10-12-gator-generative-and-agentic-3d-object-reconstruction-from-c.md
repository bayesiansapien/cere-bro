---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.225490+05:30
arxiv_id: 2610.11215
url: https://huggingface.co/papers/2610.11215
arxiv_url: https://arxiv.org/abs/2610.11215
date: 2026-10-12
---

# GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images

Reconstructing complete, scene-aligned 3D objects from casual images requires integrating sparse, uncertain observations and inferring surfaces hidden by occlusions. We present GATOR, a generative and agentic framework that recovers textured object assets and their scene-relative pose from one or more images. Our local modality mixer couples patch-aligned RGB, target-mask, and pointmap features before cross-view reasoning, preserving scene context while distinguishing the target from its surroundings. Text-guided semantic conditioning complements these spatial cues with category names and object captions through stage-specific adapters for structure, geometry, and appearance generation. The generated asset initializes a multimodal agent, providing instance-specific geometry and pose for targeted structural and texture refinement through an observation-guided edit-render-review loop. Across synthetic objects, cluttered tabletops, and indoor scenes, GATOR achieves strong geometric and appearance fidelity while recovering scene-relative pose from sparse observations. Time-budget comparisons and scene-level simulation further demonstrate the reconstruction efficiency and simulation readiness. Project page: https://research.nvidia.com/labs/lpr/gator/
