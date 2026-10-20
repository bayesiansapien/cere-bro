---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.07898
url: https://huggingface.co/papers/2610.07898
arxiv_url: https://arxiv.org/abs/2610.07898
date: 2026-10-19
---

# FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents

Repository-level software engineering (SWE) is a challenging long-horizon setting: agents must reason over extended interactions, use tools, and adapt to stateful environments. Recent work trains SWE agents with reinforcement learning methods such as Group Relative Policy Optimization (GRPO), which independently sample multiple trajectories per issue, test the resulting patches, and compare terminal rewards within a fixed group. However, this training setup does not reuse verifier feedback from failed patches as context for subsequent attempts, even though this feedback contains valuable diagnostic information about what went wrong. Training on recovery trajectories is challenging because the preceding outcome determines whether the next trajectory is generated, while the failed execution determines its conditioning context. We introduce FC-SWE, a failure-conditioned RL framework that incorporates recovery attempts into policy training. After a patch fails verification, FC-SWE restores the repository to its original task state and uses the failed patch and verifier feedback as context for a recovery trajectory. FC-SWE adapts GRPO to these chains of complete, multi-turn tool-use trajectories through two mechanisms. Trajectory-local rewards preserve each attempt's verifier outcome, preventing recovery success from rewarding an earlier failed patch. Active-set advantage estimation forms a comparison group from all initial and recovery trajectories actually executed for the same issue, so failed attempts remain in the group while unexecuted attempts are excluded. On all 500 SWE-bench Verified tasks under a verifier-assisted protocol, FC-SWE with Qwen3.5-4B and SWE-agent achieves 41.7% Resolved@1 and 52.8% Resolved@2, compared with 38.9% and 48.5% for GRPO. Although trained with at most two attempts per chain, FC-SWE reaches 70.7% Resolved@11 under an eleven-attempt test-time budget.
