---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.02840
url: https://huggingface.co/papers/2610.02840
arxiv_url: https://arxiv.org/abs/2610.02840
date: 2026-10-05
---

# PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation

World action models jointly learn to forecast world dynamics and predict robot actions, such that the learned internal world dynamics guide accurate actions. Existing approaches typically represent the world as RGB frames or latent counterparts while predicting actions as end-effector poses or joint angles, but they often struggle to capture the 3D spatial structure and contact geometry central to dexterous manipulation. We introduce Point World Action Model (PointWAM), a 3D world action model that decomposes the world into a scene (i.e., environment) and hands (i.e., actor), and jointly forecasts both as 3D point trajectories within a shared space-time coordinate frame. This explicit, disentangled representation enables effective pre-training on large-scale human demonstration videos without requiring any task-specific object or keypoint selection. Given a colored point cloud and a language instruction, PointWAM predicts how the scene and hands co-evolve in 3D space over time, then retargets the forecast hand motion to robot actions. Pre-training on human videos improves average DexJoCo success by 56.9 percentage points, and scene-trajectory supervision adds 10.9 points over forecasting the hands alone. With both, PointWAM surpasses the prior state of the art on ten DexJoCo tasks by 11.7 points and outperforms strong VLAs on a real robot.
