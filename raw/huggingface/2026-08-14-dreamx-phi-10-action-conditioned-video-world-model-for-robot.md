---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.13489
url: https://huggingface.co/papers/2608.13489
arxiv_url: https://arxiv.org/abs/2608.13489
date: 2026-08-14
---

# DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

We present DreamX-Phi 1.0, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm SE(3) transformations into attention via PRoPE-style geometric encoding, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight depth branch for scene-level geometry and use SAM3 masks with a frozen V-JEPA teacher to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing,  achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.
