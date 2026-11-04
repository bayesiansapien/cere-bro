---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.02102
url: https://huggingface.co/papers/2611.02102
arxiv_url: https://arxiv.org/abs/2611.02102
date: 2026-11-03
---

# NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale

Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supplies diverse executable tasks to the NorthCUA Harness, which sustains long interactions, records decisions, and checks task outcomes. The Flywheel uses these records to curate verified trajectories. For unsolved tasks, recursive self-improvement evolves reusable skills and preserves verified milestones so later attempts build on earlier progress. Staged Learning combines this experience with grounding data from the Flywheel to develop GUI competence through mid-training and long-horizon supervised fine-tuning. The policy then learns from fresh attempts in the same Harness through joint desktop-web reinforcement learning, closing the loop between experience production and policy improvement. The resulting Nano, Mini, and Pro family achieves state-of-the-art results among open-source models across GUI grounding, desktop execution, and Web interaction under the reported evaluation settings. For more responsive Web workflows, NorthCUA-Ultrafast pairs direct action selection with open-ended generation on pre-RL Nano, offering a measured quality-latency tradeoff. Together, these advances establish NorthCUA as a high-performing model family and a reusable foundation for agents that carry complex software work from intent to completion.
