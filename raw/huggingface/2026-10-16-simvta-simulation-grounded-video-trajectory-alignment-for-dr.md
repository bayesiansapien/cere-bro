---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.13781
url: https://huggingface.co/papers/2610.13781
arxiv_url: https://arxiv.org/abs/2610.13781
date: 2026-10-16
---

# SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models

Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a simulation-grounded post-training framework that combines trajectory optimization with video supervision. First, we sample candidate trajectories for each observation and use a real-world simulator (e.g., World Engine) to render future videos for high-reward candidates in real-world scenes reconstructed with 3D Gaussian Splatting (3DGS). This provides trajectory-matched supervision independent of the model's own predictions. Under a limited rendering budget, we prioritize video supervision for higher-error futures among these rendered candidates. Finally, we optimize trajectory planning with Group Relative Policy Optimization (GRPO) and use a flow-matching loss on the matched videos to update shared representations. At inference time, the model predicts trajectories directly, without simulator calls. On NAVSIM v1, applying SimVTA to a WAM initialization improves PDMS from 86.2 to 91.3 (+5.1). It achieves 88.2 EPDMS on NAVSIM v2 and an average HD-Score of 38.8 in closed-loop evaluation on HUGSIM. Ablations show that updating shared representations with video supervision improves planning, while prioritizing higher-error futures among high-reward trajectories further improves performance.
