---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.04596
url: https://huggingface.co/papers/2610.04596
arxiv_url: https://arxiv.org/abs/2610.04596
date: 2026-10-07
---

# DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic, optimizing teacher--student agreement at each prefix despite reasoning quality being determined at the trajectory level. Reinforcement learning with verifiable rewards (RLVR), particularly Group Relative Policy Optimization (GRPO), provides complementary outcome-level supervision but suffers from sparse rewards and coarse credit assignment. We show that OPD and RLVR exhibit complementary blind spots: teacher signals provide dense local guidance but are weakly aligned with rollout correctness, whereas group-relative rewards capture task success but provide coarse token-level credit and vanish on all-failure groups. We introduce DiffGate, an outcome-gated objective that combines GRPO with selective, bounded teacher guidance. Teacher supervision is applied only to failed trajectories, scaled by group difficulty, and smoothly bounded to prevent extreme teacher--student discrepancies from dominating optimization. The verifier therefore determines which trajectories receive teacher guidance, while the teacher provides dense token-level update directions within those trajectories. Across Qwen3-0.6B and Qwen3-1.7B students, DiffGate improves code avg@8 over matched GRPO by +1.7 and +1.8 points and pass@8 by +1.6 and +5.7 points, respectively. On mathematics, avg@8 remains within 0.5 points of GRPO while pass@8 improves by +1.1 and +3.9 points. Overall, DiffGate improves pass@8 across all four model--domain settings, demonstrating improved solution coverage under our evaluation protocol.
