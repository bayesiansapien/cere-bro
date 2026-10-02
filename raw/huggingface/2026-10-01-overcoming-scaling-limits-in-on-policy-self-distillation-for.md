---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350579+05:30
arxiv_id: 2609.37915
url: https://huggingface.co/papers/2609.37915
arxiv_url: https://arxiv.org/abs/2609.37915
date: 2026-10-01
---

# Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning

On-policy self-distillation (OPSD) trains a student to match a privileged teacher distribution along its own sampled trajectory. Standard OPSD applies this supervision to unverified student rollouts while conditioning the teacher on privileged context, typically a reference solution. We separate these roles in a factorial analysis and find that scaffold correctness has a stronger effect on downstream accuracy than context correctness. Unverified scaffolds create an imitation gap because the teacher can use information unavailable to the student. This gap shrinks with model scale, yet OPSD continues to supervise mostly unverified trajectories. In contrast, verified scaffolds remain effective even when the teacher is conditioned on the student's own unsuccessful rollout. Based on this finding, we introduce OASIS, which retains the OPSD objective but supervises mostly verified by label on-policy trajectories and replaces written solutions with unverified model-generated attempts as the teacher context. OASIS therefore requires only final-answer labels. Across Qwen3-1.7B, 4B, and 8B on AIME 2024, AIME 2025, and HMMT 2025, OASIS improves over the base model by 3.2--3.8 points on average, while OPSD's gain falls from 3.05 points at 1.7B to 0.14 at 8B. At 8B, OASIS improves over OPSD by 3.05 points, showing that verified on-policy scaffolds preserve the effectiveness of self-distillation as models scale.
