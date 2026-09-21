---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.18620
url: https://huggingface.co/papers/2609.18620
arxiv_url: https://arxiv.org/abs/2609.18620
date: 2026-09-21
---

# DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation

Creating deformable assets for robot manipulation requires jointly specifying their geometry, appearance, and physical properties. This is especially challenging for deformable objects, since text and images provide limited evidence about how they deform and respond to contact, yet these responses directly affect their suitability for interaction. Automated generation therefore needs to resolve coupled physical requirements and use interaction evidence to guide construction and refinement. We present DeformSmith, a framework that enables automated generation of interactive, physically credible deformable assets from text or a single image. Through hierarchical agentic construction and a shared physics-grounded harness, it progressively builds, tests, and refines geometry, physical models, material behavior, and robot interaction until the resulting asset is ready for simulation and manipulation. Robot interaction closes the generation loop through manipulation feedback and replayable interaction data. Results show that DeformSmith generates assets with better visual quality and physical plausibility than state-of-the-art baselines, including PhysGen3D, PhysGM, and PhysX-Omni, while supporting the synthesis of data for robotic manipulation of deformable objects. Project page: https://can-lee.github.io/deformsmith-web/
