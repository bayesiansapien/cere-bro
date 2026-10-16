---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.231252+05:30
arxiv_id: 2610.14096
url: https://huggingface.co/papers/2610.14096
arxiv_url: https://arxiv.org/abs/2610.14096
date: 2026-10-15
---

# SWEeper-Bench: Can Agents Discover Bugs in Interactive Software?

Coding agents increasingly interact with users by generating interactive software on the fly rather than replying in text, yet many bugs in such software reveal themselves only after multi-step interactions. Today, users must discover these bugs and wait for fixes, making the development loop slow and expensive. Existing benchmarks typically assume the bugs have already been identified, leaving agents' ability to find interaction-dependent failures largely unevaluated. We introduce SWEeper-Bench, 200 tasks built from real bug fixes in 200 widely used open-source web applications. Each task gives the agent only the codebase and an open-ended request such as "Find and fix issues in Focalboard's board sharing and membership." Because these bugs are hard to detect from code alone, agents must design interactive tests to uncover them. An agentic verifier then judges each repair by what a user would observe in the browser. The best of 15 frontier agents passes only 59.0% of tasks. Through stage-by-stage analysis of agent trajectories, we show that the biggest bottleneck is identifying the buggy behavior: agents often reach the relevant feature but never trigger the failure or fail to recognize it. SWEeper-Bench measures progress toward agents that close this loop themselves, delivering software that works without waiting for user feedback.
