---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.301616+05:30
arxiv_id: 2610.08077
url: https://huggingface.co/papers/2610.08077
arxiv_url: https://arxiv.org/abs/2610.08077
date: 2026-10-08
---

# Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can hindsight teach an agent what it could have anticipated before acting? We introduce prospective learning, which uses post-hoc experience to supervise foresight predictions from the pre-interaction view, and instantiate it with Self-Retrospection Distillation (SRD). Intuitively, a completed trajectory reveals knowledge that would have been useful and pitfalls that should be avoided; SRD distills this privileged hindsight into trajectory-blind foresight of the same policy. Foresight serves only as a training target and need not be explicitly generated at inference time. Across 10 tool-integrated reasoning and long-horizon agentic tasks, SRD complements RLVR and self-distillation baselines with gains of up to 24.2 pp. Its advantage is especially pronounced when reward contrast is scarce: when 37--98% of rollout groups are reward-uniform across model scales, yet SRD can still exploit learning signal from sampled trajectories. In the 2B setting, where 98% of groups are all-failure, the RLVR training ends up at 0.0% success, while adding SRD reaches 60.6% under the same rollout budget. Our results suggest that post-hoc agent experience is useful not only for evaluating or improving behavior, but also for shaping predictive representations before available interaction.
