---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.311266+05:30
arxiv_id: 2610.08902
url: https://huggingface.co/papers/2610.08902
arxiv_url: https://arxiv.org/abs/2610.08902
date: 2026-10-08
---

# Agent Plasticity: Measuring Self-Improvement Through Experience

AI agents increasingly operate in environments where they can diagnose failures and improve through experience, yet existing evaluations largely measure what an agent can do at a fixed point in time rather than how effectively it learns. Evaluating self-improvement requires answering three questions: does future performance improve and generalize beyond the interactions that enabled learning; how efficiently are new capabilities acquired; and where does the self-improvement process break down? To answer these questions, we study self-improvement in a controlled setting where agents amortize past experience into reusable artifacts that are inherited by future instances. At each checkpoint, we measure performance on training and held-out environment interactions while accounting for learning cost. We introduce agent plasticity, the efficiency with which an agent converts experience into gains in future held-out performance. Across multiple environments, frontier models exhibit sharply different improvement trajectories despite comparable opportunities to learn. Some achieve substantial and persistent gains, while others remain near or below their initial performance, and gains within the training regime often transfer only partially to out-of-distribution conditions. Endpoint capability and acquisition efficiency also diverge: the agent that ultimately performs best need not be the one that improves most efficiently. Tracing failures through the improvement loop further reveals different candidate bottlenecks. Agents with low plasticity often fail to reuse relevant artifacts, whereas more plastic agents may still fail despite reusing relevant artifacts, pointing to limitations in artifact quality, generalization, or application. Evaluating self-improving agents requires measuring not only what they can do, but how effectively they become better through experience.
