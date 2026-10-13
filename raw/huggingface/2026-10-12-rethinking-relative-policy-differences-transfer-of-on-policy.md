---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222815+05:30
arxiv_id: 2610.13205
url: https://huggingface.co/papers/2610.13205
arxiv_url: https://arxiv.org/abs/2610.13205
date: 2026-10-12
---

# Rethinking Relative Policy Differences Transfer of On-Policy Distillation

On-policy distillation (OPD) trains a target policy on its own rollouts using token-level supervision from a stronger teacher, but typically relies on the teacher being substantially more capable than the target. Recent work relaxes this requirement by transferring the relative policy difference between an expert and a reference policy rather than the expert's absolute distribution. Yet it remains unclear which differences provide useful supervision and which targets can benefit from them. We develop a unified view in which the log-probability ratio between a proxy expert and a proxy reference defines an implicit reward for KL-regularized policy optimization. This formulation induces an on-policy update for the target, recovers conventional OPD as a special case, and enables any-to-any transfer across models that differ in scale, training stage or generation. Our systematic experiments yield three findings. First, a stronger expert is not necessarily a better source of supervision: differences induced by task-specific training, including reinforcement learning and supervised fine-tuning, transfer consistently, whereas those arising from model scale alone transfer weakly or not at all. Second, the expert and reference serve complementary roles: the expert provides the capability to be transferred, while the reference filters out shared behavior and isolates the relevant residual. Third, even a useful difference does not transfer to every target: success requires the induced update to move the target toward the expert and generalize beyond sampled rollouts. Raw policy distance does not predict transferability, whereas an appropriate reference can rescue otherwise unsuccessful transfer. These results characterize when relative policy differences provide effective supervision for OPD.
