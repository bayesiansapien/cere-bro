---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38087
url: https://huggingface.co/papers/2609.38087
arxiv_url: https://arxiv.org/abs/2609.38087
date: 2026-09-30
---

# CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments

Behavior Foundation Models (BFMs) give humanoids a promptable policy over a latent behavior space, enabling one single vector to represent a motion to imitate, a pose to reach, or a reward to maximize. Forward-Backward representations successfully produce such spaces, but at the cost of hundreds of GPU-hours for a single robot. Moreover, when the training process is repeated for a second robot, it produces a second space unrelated to the first, resulting in embodiment-specific latents that do not unify or transfer. We address these problems with CrossBFM, treating the latent space as the transferable asset for various embodiments. As retargeting provides frame-level cross-embodiment correspondence, we propose a unified encoder architecture with no robot-specific parameters for distilling the behavior space to address all training embodiments simultaneously in less than a GPU-hour. Following this encoder, latent-conditioned trackers turn the distilled latent into whole-body control in a conventional PPO training manner in just 10 more GPU-hours. On three distilled humanoids, all three prompting modes transfer: motion tracking with latent-conditioned policy losing only 0.025 rad to its joint-conditioned counterpart, smooth goal reaching between poses with no falls, and reward optimization for all 41 reward prompts. Our experiments further reveal that 1) regressing the encoder on a quarter of the motion corpus costs only 5% of tracking performance and 2) training the encoder on a subset of robots and evaluating on an unseen one recovers up to 89% of the tracking performance of seen robots, demonstrating cross-embodiment generalization to morphologically similar robots. We also verify the pipeline on real robots across all three prompting modes and with flow-based generated latents. Project website: https://dotandung.github.io/crossbfm/
