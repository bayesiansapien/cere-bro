---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.231525+05:30
arxiv_id: 2610.15425
url: https://huggingface.co/papers/2610.15425
arxiv_url: https://arxiv.org/abs/2610.15425
date: 2026-10-15
---

# Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination. The full instruction route treats skill chaining as long-horizon imitation. In a controlled study, full instruction training on limited skill combination sequences reaches 40.0% ordered success on covered combinations but only 7.7% on recombination, suggesting memorization of sequence templates rather than robust skill recombination. We introduce Hierarchical Subtask Execution (HSE), a diagnostic framework that exposes skill recombination through a shared modular interface over the planner, trigger, and policy, decomposing long-horizon failures into separable modes. We introduce RoboCombine, a benchmark for skill recombination without combined skill training trajectories, with metrics for ordered success and transition conversion across subtask boundaries. RoboCombine reveals that atomic competence alone does not ensure ordered execution. Failures concentrate at transitions where downstream subtasks launch from handoff states from preceding subtasks rather than canonical atomic starts. We identify this mismatch as the start state gap. To address it, we introduce Pose Robust Task Initialization (PRTI), a lightweight atomic task post-training strategy that broadens start state coverage beyond canonical starts. Under oracle timed HSE on RoboCombine, PRTI reaches 18.16% ordered success, compared with 4.21% under random perturbation and 9.47% under a robot-reset oracle, without combined skill training trajectories. These results show that combinatorial generalization requires handoff robust atomic skills that convert first stage progress into reliable downstream execution, not merely decomposition into known subtasks. Code: https://github.com/AutoLab-SAI-SJTU/RoboCombine.
