---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.004478+00:00
arxiv_id: 2610.41354
url: https://huggingface.co/papers/2610.41354
arxiv_url: https://arxiv.org/abs/2610.41354
date: 2026-11-16
---

# OneSteer: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control

Deployment objectives often specify desired outcomes without providing revised trajectories, while parts of the original reference must still be followed. We present OneSteer, a one-step diffusion whole-body controller that combines general motion tracking with selective test-time steering. To accommodate new objectives, differentiable task costs guide optimization of the generator's input noise with frozen weights, while body-group reference masks relax selected tracking requirements. Predicted state-action plans provide a shared interface for task optimization and feedback-conditioned execution. For nominal tracking, the model trained from scratch achieves the lowest local tracking error among the evaluated baselines on successful held-out AMASS and BONES clips. For steering, one frozen distilled controller adapts across diverse deployment objectives in simulation, raising the clean passage rate under a 1.25 m bar from 2% to 90%. On a physical Unitree G1, OneSteer completes all 27 nominal tracking trials across nine diverse whole-body motion sequences without falling. With a steering cost derived from a signed distance field built using only onboard LiDAR, it also passes under a 1.1 m low bar in four of five attempts and steps over a 12 cm hurdle without falling in all three attempts. Beyond control, prediction variation in the model trained from scratch ranks likely tracking failures without physics rollouts. This scoring method is more than 10x faster than simulation-based scoring with five rollouts per clip and guides targeted fine-tuning. Project page: https://onesteer.github.io
