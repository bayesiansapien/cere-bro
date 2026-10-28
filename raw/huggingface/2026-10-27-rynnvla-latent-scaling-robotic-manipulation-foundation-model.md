---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34356
url: https://huggingface.co/papers/2610.34356
arxiv_url: https://arxiv.org/abs/2610.34356
date: 2026-10-27
---

# RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

Scaling vision-language-action (VLA) models is constrained by scarce action-labeled demonstrations and incompatible control spaces across robot embodiments. We present RynnVLA-Latent, a framework that turns heterogeneous interaction videos into scalable supervision for robot policy pretraining. At its core, RynnLAM learns continuous, 3D-grounded latent actions from visual transitions without requiring native robot controls. By combining residual future-feature prediction, camera-compensated 3D-flow supervision, and camera-motion decoupling, RynnLAM encourages representations that capture control-relevant motion rather than appearance changes alone. We apply RynnLAM to 30.1K hours of human, robot, and simulation videos, producing 745.52M latent-action descriptors. RynnVLA-Latent then learns to predict latent-action chunks from visual observations and language through flow matching, before adapting its pretrained backbone and action expert to embodiment-specific robot actions. The resulting 4B policy achieves 98.8% success on LIBERO, 84.7% on LIBERO-Plus without benchmark-specific adaptation, 51.9% average success across five VLABench tracks, and 88.6% average success on the RoboTwin 2.0 bimanual benchmark. It also achieves the highest observed success rates among the compared methods on six real-world manipulation tasks across dexterous-hand and mobile-gripper platforms. Together with representation ablations and data-scaling results, these findings demonstrate the potential of latent-action supervision for scaling robot policy learning beyond native action-labeled data.
