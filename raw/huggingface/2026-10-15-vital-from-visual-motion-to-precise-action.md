---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.230055+05:30
arxiv_id: 2610.20604
url: https://huggingface.co/papers/2610.20604
arxiv_url: https://arxiv.org/abs/2610.20604
date: 2026-10-15
---

# VITAL: From Visual Motion to Precise Action

World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, reconstruction captures the dominant maneuver but leaves centimeter-scale errors. We therefore introduce VITAL (Vision-Induced Tokens for Action Learning), an action tokenizer that couples a visually derived motion scaffold with a compact residual encoding the trajectory error left by that scaffold. This representation makes visual motion the principal prediction target and gives small metric corrections a separate, normalized learning scale. Using flow matching, the action expert jointly predicts both components from the current image, ego state, and navigation command, without generating future images at inference. The same residual coordinates support bounded reinforcement post-training that refines execution while keeping the predicted visual scaffold fixed. With only one action denoising step, VITAL achieves 90.8 PDMS on NAVSIM v1 navtest, within 0.13 points of its ten-step score at 3.29x the end-to-end inference speed. Without retraining, it achieves 91.1 EPDMS on NAVSIM v2 navtest and 38.6 on navhard. Project page: https://worldbench.github.io/vital
