---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2609.04094
url: https://huggingface.co/papers/2609.04094
arxiv_url: https://arxiv.org/abs/2609.04094
date: 2026-09-05
---

# DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training

Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-truth success signals are not available. Multi-criteria rubrics are a popular way to supply such a reward; they are scored once per trajectory, but a single scalar is a poor signal across tens of steps. We propose DRACO: Distributing Rubric-based Advantage for Credit Optimization. It generates rubrics dynamically during training to track the policy's evolving capability, scores those rubrics once per completed trajectory, and redistributes that judgment over the steps responsible for annotated rubrics to produce differentiated per-step advantages in GRPO. The redistribution is closed-form and does not introduce any trained attribution module. On AppWorld, DRACO gains 15.9 points over the base model and 5.3 points over GRPO trained with a sparse ground-truth reward, despite not using any verifiers itself. On out-of-domain Tau-Bench, it gains 5.3 points over the base model even without a frontier judge, beating both ground-truth-reward training and other rubric-based training settings. The code for DRACO is available at https://github.com/IBM/draco.
