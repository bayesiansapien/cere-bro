---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.39820
url: https://huggingface.co/papers/2609.39820
arxiv_url: https://arxiv.org/abs/2609.39820
date: 2026-10-05
---

# Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only teacher, producing counterfactual corrections while the policy remains in control. Outcome-aware admission then converts useful proposals into corrective targets and retains successful uncorrected actions as quiet anchors for guarded LoRA updates. We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones. Compared with the base policies, FailBank improves the joint success-cost operating point. Across the two backbones, FailBank improves task success rate by 8.5 and 6.9 percentage points, while reducing policy-induced cumulative cost by 35.6\% and 23.8\%, respectively. Compared with runtime shielding, FailBank raises task success rate by 25.4 and 9.5 percentage points, while maintaining comparable policy-induced cumulative cost. These results show that runtime feedback can serve as persistent policy supervision rather than only as a temporary action constraint.
