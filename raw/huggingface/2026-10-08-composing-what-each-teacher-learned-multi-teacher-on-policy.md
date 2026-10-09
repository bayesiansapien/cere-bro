---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.308899+05:30
arxiv_id: 2610.10460
url: https://huggingface.co/papers/2610.10460
arxiv_url: https://arxiv.org/abs/2610.10460
date: 2026-10-08
---

# Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts

Multi-teacher on-policy distillation (MOPD) is used in two settings. In common-domain composition, several teachers score each student rollout from one prompt domain and their signals form a single target; in routed-domain distillation, prompts from different domains are assigned to the corresponding specialist. Both settings usually transfer each teacher's endpoint policy, which mixes what post-training changed with preferences inherited from the teacher's base. We introduce Δ-MOPD, which transfers each teacher's teacher-minus-base logit shift re-anchored at the student's frozen initialization, and compare it with endpoint supervision in both settings while holding teacher selection fixed. We first expose the mechanism that impedes endpoint transfer: inherited base pull can exceed the post-training shift. Removing it reduces the teacher-term norm ratio and target--student KL.
  Across our experiments, the results suggest that shift targets are particularly useful when teacher signals are combined at a state. With three composed teachers, Δ-MOPD exceeds endpoint composition by 4.11 Math and 1.95 five-benchmark points; with two, it matches endpoint accuracy. Under phased routing, it achieves higher mean performance in both phase orders and reduces the observed order gap from 10.50 to 6.42 points. Under interleaved routing, where each update involves one teacher, the two targets perform comparably. The phased results provide supporting evidence that the benefit may extend to signals accumulated across training phases. Target construction is thus an independent design axis in MOPD, complementary to teacher selection.
