---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994706+05:30
arxiv_id: 2610.35439
url: https://huggingface.co/papers/2610.35439
arxiv_url: https://arxiv.org/abs/2610.35439
date: 2026-10-28
---

# Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams

Omnimodal large language models (Omni-LLMs) are increasingly expected to assist users while observing continuous audiovisual streams. However, existing evaluations provide limited insight into how reliably these models connect stream evidence and user needs to timely, sustained interventions. We introduce Omni-InteractScope, a benchmark of 1,479 human-annotated, cross-reviewed interactions with 1,790 temporal targets across eight task groups. It links input modalities, event triggers, intervention types, and user needs, covering event-timed tool invocation and query-free assistance alongside notifications, warnings, state tracking, and continuous responses. Our experimental results on the proposed benchmark reveal three critical limitations of current Omni-LLMs: (1) Timely tool invocation remains unreliable: all 12 evaluated models produce an on-time first response for at most 40\% of tool-invocation targets, and joint timing-and-tool accuracy reaches at most 32.0\%. (2) Query-free reminders remain poorly covered: all evaluated models achieve lower timely reference-target recall on query-free reminders than on explicit questions, measured on their respective target sets. Reminder recall never exceeds 23.0\%. (3) End-to-end guidance coverage remains limited: nine models cover none of the 26 guidance sequences in full, and the remaining three cover only one to three sequences each. Targeted controls further show that tool-invocation scores alone do not establish event grounding and that reminder coverage depends on response history and frequency. These findings motivate developing and evaluating streaming assistants for timely action, initiative under general user needs, and coverage of entire response sequences.
