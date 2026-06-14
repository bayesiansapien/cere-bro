---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.09304
url: https://huggingface.co/papers/2606.09304
arxiv_url: https://arxiv.org/abs/2606.09304
date: 2026-06-14
---

# SG-OPD: Sign-Gated On-Policy Distillation via Sign-Consistency Gating and Phased Teacher Sampling

On-policy distillation (OPD) trains a student on its own trajectories with dense per-token supervision from a stronger teacher, and often outperforms off-policy distillation and standard reinforcement learning. However, we find that its effectiveness implicitly relies on two assumptions that frequently break in practice: trajectory-level alignment between the student and the teacher, and uniform token-level reliability of the teacher's preferences. We therefore propose Sign-Gated On-Policy Distillation (SG-OPD), which uses a binary verifier as a trust signal for the teacher at two complementary granularities: phased teacher sampling mixes in verifier-endorsed teacher rollouts at cold-start, and a sign-consistency gate extrapolates the distillation update on tokens where the teacher agrees with the verifier-correct direction and interpolates it where it disagrees. Experiments on competition-level mathematical reasoning benchmarks show that SG-OPD consistently outperforms standard OPD, with average gains of 1.98 and 7.50 at the per-sample and per-question levels, respectively.
