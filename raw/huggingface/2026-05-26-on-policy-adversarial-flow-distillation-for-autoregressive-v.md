---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26105
url: https://huggingface.co/papers/2605.26105
arxiv_url: https://arxiv.org/abs/2605.26105
date: 2026-05-26
---

# On-Policy Adversarial Flow Distillation for Autoregressive Video Generation

Autoregressive video generators are attractive for streaming, long-horizon, and interactive applications, but distilling strong black-box teachers into causal students remains difficult. The student must learn under its own rollout distribution, whereas practical teachers may expose only prompt-conditioned completed videos and may differ in architecture, capacity, temporal design, and sampling schedule. This interface makes supervised fine-tuning off-policy, score-based distillation inapplicable, and direct adversarial imitation too sparse for denoising-time credit assignment. We propose Adversarial Flow Distillation (AFD), an on-policy framework for heterogeneous black-box video distillation. AFD queries the teacher and rolls out the current student on the same prompts, trains a prompt-paired Bradley-Terry discriminator to estimate clean-sample teacher-student discrepancy, and converts the resulting on-policy advantage into forward-process flow-matching updates on the student's own noised states. Thus, AFD provides dense velocity-field supervision while requiring no teacher scores, latents, denoising trajectories, step alignment, or reverse-chain reinforcement learning. Experiments across two causal AR student families show that AFD consistently improves motion- and physics-sensitive generation while preserving general video quality, and ablations validate the importance of adaptive on-policy feedback and forward-process credit assignment. The method requires only clean teacher videos and student rollouts, providing a practical route for distilling proprietary or heterogeneous video generators into efficient autoregressive students.
