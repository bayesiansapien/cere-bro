---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.908210+00:00
arxiv_id: 2611.33579
url: https://huggingface.co/papers/2611.33579
arxiv_url: https://arxiv.org/abs/2611.33579
date: 2026-11-26
---

# DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data

A growing body of recent work addresses the retargeting of human hand-object demonstrations to robotic hands. To train whole-robot policies, however, the retargeted motions must be kinematically feasible and physically executable, and be produced efficiently at scale. We present DexEngine, a simulation pipeline that turns human manipulation data into train-ready, physically executable arm-hand trajectories. DexEngine first places each clip's hand-object motion where the arms can reach it, finds an arm motion that follows the human hands, and then corrects the motion in physics simulation with residual reinforcement learning. From nine human hand-object datasets, we generate about 5,200 clips for each of four dexterous hands, augmented into 65,000 trajectories (116 h) and 325,000 episodes (578 h) in total. Even with arms attached, DexEngine tracks objects more accurately than prior floating-hand methods and runs over 10x faster than RL-based ones. Policies trained on our data far outperform those trained on the same clips without physics correction or with the arms attached after a floating-hand correction, showing that fine-tuning data need physics correction. Mid-training on our data further improves them at equal fine-tuning budget, in simulation and on a real robot.
