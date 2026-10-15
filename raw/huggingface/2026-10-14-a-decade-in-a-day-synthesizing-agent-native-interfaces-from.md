---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.504751+00:00
arxiv_id: 2610.15765
url: https://huggingface.co/papers/2610.15765
arxiv_url: https://arxiv.org/abs/2610.15765
date: 2026-10-14
---

# A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution

Large language model agents are emerging as an important new class of users of desktop applications. However, existing desktop interfaces were designed for human end users or application developers, leaving agents to interpret visual controls or discover and compose low-level software operations. This mismatch can hinder even capable agents, yet it remains unclear what interface properties make desktop software easier for agents to use. To study this question, we treat software evolution as a natural source of interface variation and introduce DeskIF-Bench, a benchmark of 255 artifact-verified tasks across six desktop applications. By holding the task, agent, and verifier fixed while varying the software release, we measure how interface changes affect agent performance. Across two models and six applications, the newest release consistently outperforms the oldest. Trajectory analysis identifies three relevant interface properties: discoverability, granularity, and observability. Guided by these properties, we develop ANIS, a framework that synthesizes agent-native interfaces from the capabilities of installed applications. On an expanded evaluation of 368 tasks across eight applications, atomic interfaces improve success over native SDK use by 3.8 and 3.5 percentage points with DeepSeek V4 Flash and Claude Haiku 4.5, respectively, while reducing online token usage by approximately 73%. Goal-level commands further raise success to 74.5% and 67.4%, respectively.
