---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.37267
url: https://huggingface.co/papers/2609.37267
arxiv_url: https://arxiv.org/abs/2609.37267
date: 2026-10-06
---

# Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym

Proactive LLM agents can turn idle compute into useful support before users ask. Yet even correct work can misread user context, impose review costs, or undermine trust. This work proposes foundations for designing, realizing, and evaluating proactive LLM agents around three joint principles (3T): Task Capability, anticipating relevant needs and correctly performing useful work; Temporal Allocation, allocating compute according to resource availability and when results are needed; and Trust, sustaining users' confidence and appropriate reliance on the agent. We connect these objectives to a design space organized around five dimensions: task scope, anticipation horizon, activation trigger, processing timing, and intervention depth, and specify the situation and system modeling needed to support its choices, including user and environment representations, backbone LLMs, and agent harnesses. Lastly, we propose PROACTIVITY-GYM, a simulation-based evaluation testbed including multi-day scenarios, stateful environments, and persona-conditioned simulated users that can evaluate the consequences of proactive assistance across interactions. Evaluations across 23 model-harness configurations uncover substantial performance gaps across 3T and reveal that LLM judges often conflate task capability and trust. A human study with 30 participants demonstrates the importance of the joint 3T optimization: participants show sharp trust declines after intervention misalignment despite correct outcomes, and prefer sleep-time assistance, even when imperfect, to preserve ongoing focus. Together, these findings support designing and evaluating proactive agents through the joint consideration of useful work, compute allocation, and evolving user trust.
