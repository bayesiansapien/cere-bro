---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06850
url: https://huggingface.co/papers/2610.06850
arxiv_url: https://arxiv.org/abs/2610.06850
date: 2026-10-06
---

# InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction datasets and retarget them into humanoid robot references while preserving whole-body coordination and dexterous hand-object relationships. This produces a large and diverse humanoid robot reference collection for dexterous whole-body loco-manipulation. Second, we train a physics-based generalist tracker that executes these references in simulation on a humanoid with dexterous hands, covering a scale and diversity beyond prior humanoid tracking systems for loco-manipulation. Third, we close a data flywheel: each round makes small, task-preserving changes to where an interaction takes place and how the body performs it, fine-tunes the tracker on them, and keeps only the variants whose simulated execution completes the task, which seed the next round. With more iterations, these small edits compound into broader coverage around the sparse original demonstrations while preserving task semantics and motion quality. Experiments show contact-preserving retargeting across robot configurations, broad tracking with a single generalist policy, executable motions that keep growing over augmentation rounds, and transfer to real robots. InterMimicGen provides a unified path from heterogeneous human demonstrations to a continually expanding motion resource for humanoid robot learning.
