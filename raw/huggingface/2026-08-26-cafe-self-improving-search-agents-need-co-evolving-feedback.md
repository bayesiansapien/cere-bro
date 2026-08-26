---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24794
url: https://huggingface.co/papers/2608.24794
arxiv_url: https://arxiv.org/abs/2608.24794
date: 2026-08-26
upvotes: 1
---

# CAFE: Self-Improving Search Agents Need Co-Evolving Feedback

Outcome-supervised search agents learn when and how to retrieve evidence, but terminal rewards neither localize intermediate errors nor redirect an ongoing trajectory before those errors compound. Treating corrective feedback as a learned in-trajectory intervention couples the two roles: the agent must decide when to request and use feedback, while the critic must infer useful corrections from outcome-confounded rollouts whose failure patterns shift as the agent improves. We introduce CAFE (Coupled Agent--Feedback Evolution), a framework in which a shared-parameter model alternates between search-agent and critic roles. CAFE initializes feedback-conditioned recovery from trajectories built around the base agent's own failures, then couples online and offline optimization. During online RL, a comparative feedback estimate uses a prompt-level call--skip success gap to shape request returns, while feedback-aware advantage shaping reweights token advantages before and after feedback. Offline, rollout-derived preference optimization learns feedback from matched successful and unsuccessful trajectories. On seven agentic search benchmarks, CAFE outperforms the evaluated RL-based search agents on average, retains its gains across all six out-of-domain benchmarks, and reduces answer-level hallucinations. One-sided ablations show that improving only the agent or only the critic eventually plateaus, whereas alternating the two updates continues to improve performance. These findings suggest that a self-improving search agent needs feedback that co-evolves with the policy it guides.
