---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.23377
url: https://huggingface.co/papers/2609.23377
arxiv_url: https://arxiv.org/abs/2609.23377
date: 2026-09-22
---

# One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents

Repository-level software engineering (SWE) comprises heterogeneous task categories, whose progress under pooled agentic reinforcement learning can be uneven: gains in some categories coincide with regressions in others, while aggregate resolution obscures these changes. Motivated by this category see-saw, we develop a category-aware expert-training and policy-integration framework. Executable task construction and SWE Labeler, an evidence-grounded multi-axis labeling system, organize the training pools. Initial category-specific RL improves average training success while leaving uneven instance-level progress, motivating explicit consolidation of successful behavior and policy-adaptive task selection. Same-origin category experts alternate long-horizon Agentic-miniRL with Refresh-Repair-Expand (RRE): the updated policy refreshes instance mastery, reuses its own verified successful trajectories for Repair SFT, and reselects tasks for further RL. Label-routed multi-teacher on-policy distillation (MOPD) consolidates the experts into one deployable student, with ReLU-gated reward extrapolation keeping only each teacher's improving direction over the reference. Expert training and policy integration require no external model to provide solution trajectories or action targets. We evaluate Pooled RL and Balanced RL, expert development, and single-model integration through aggregate and per-category resolution, the minimum category lift over each joint-RL baseline, and expert-gain recovery. The final MOPD policy achieves mean resolution of 58.04% on Pro-618 and 59.00% on SWE-bench Multilingual, improving over the base model by 5.39 and 2.78 percentage points, respectively.
