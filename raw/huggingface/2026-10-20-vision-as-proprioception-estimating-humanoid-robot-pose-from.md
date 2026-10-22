---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25288
url: https://huggingface.co/papers/2610.25288
arxiv_url: https://arxiv.org/abs/2610.25288
date: 2026-10-20
---

# Vision as Proprioception: Estimating Humanoid Robot Pose from Video

Estimating a humanoid robot's internal state from video has a wide range of real-world applications but remains unexplored. During interactions with a robot, its onboard state information may be unavailable due to privacy, ownership, or communication constraints. Meanwhile, online and AI-generated robot videos provide rich sources of data but typically lack corresponding joint configurations, limiting their direct use in robot learning. To address these issues, we present HumanoidPose, a new framework that treats vision as proprioception to recover full-body joint configurations in world space from video alone. Specifically, we combine pretrained human-pose features with robot kinematics in a unified model that predicts each embodiment's joint configurations. We retarget human motions to sixteen different humanoid embodiments, enabling scalable learning entirely from synthetic data. To improve real-world generalization, we further leverage unlabeled online videos through self-training to develop a 2D robot-pose detector. In our evaluation, HumanoidPose improves joint-angle and joint-position accuracy over the evaluated baselines and reduces joint-angle error by 18-32% relative to the best-performing baseline on each of the three real humanoid platforms. We further show improved global localization and generalization to unseen embodiments. HumanoidPose enables visual understanding of other robots during interaction and extraction of robot motion from online and generated videos.
