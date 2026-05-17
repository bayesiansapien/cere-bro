---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14269"
url: "https://huggingface.co/papers/2605.14269"
arxiv_url: "https://arxiv.org/abs/2605.14269"
date: 2026-05-17
---

# PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation

Generating realistic human motion is a central yet unsolved challenge in video generation. While reinforcement learning (RL)-based post-training has driven recent gains in general video quality, extending it to human motion remains bottlenecked by a reward signal that cannot reliably score motion realism. Existing video rewards primarily rely on 2D perceptual signals, without explicitly modeling the 3D body state, contact, and dynamics underlying articulated human motion, and often assign high scores to videos with floating bodies or physically implausible movements. To address this, we propose PhyMotion, a structured, fine-grained motion reward that grounds recovered 3D human trajectories in a physics simulator and evaluates motion quality along multiple dimensions of physical feasibility. Concretely, we recover SMPL body meshes from generated videos, retarget them onto a humanoid in the MuJoCo physics simulator, and evaluate the resulting motion along three axes: kinematic plausibility, contact and balance consistency, and dynamic feasibility. Experiments show that PhyMotion achieves stronger correlation with human judgments than existing reward formulations and leads to larger and more consistent improvements (+68 Elo gain).
