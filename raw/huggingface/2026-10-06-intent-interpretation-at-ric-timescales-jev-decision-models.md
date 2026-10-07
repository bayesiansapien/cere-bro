---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.23136
url: https://huggingface.co/papers/2609.23136
arxiv_url: https://arxiv.org/abs/2609.23136
date: 2026-10-06
---

# Intent Interpretation at RIC Timescales: Jev Decision Models versus Large Language Models in 6G Open RAN

Intent-based Open RAN needs an interpreter that turns intents into A1 policies within the loop of the RAN intelligent controller (RIC). Decision models such as Jev-1.13.0 return typed policy fields, whereas generative large language models (LLMs) produce the policy token by token. We ask whether the extra delay of LLMs costs control deadlines, RIC capacity, or radio performance. We compare Jev-1.13.0 and two other decision models with LLMs on the RANIntent v1 benchmark, in closed-loop ns-3 simulation and on a real A1 and E2 path. Median interpretation takes 0.286 to 2.35 s, against under 25 ms for A1 and E2 transfer. Jev-1.13.0 meets the 1 s near-real-time budget on 99.8% of calls, while two hosted LLMs meet it on 17.9% and 0%. In the radio network, ideal enforcement moves the affected-class service-level agreement (SLA) violation by 3.96 percentage points in the direction each intent requests, against no update at the base point. No hosted LLM showed a resolved increase over Jev-1.13.0 at that point. At the same point, per-second direct control gave no resolved SLA reduction over a numerical xApp. Slow interpreters miss the 1 s budget, and two interpreters saturate their queues at 2 intents/s, whereas no radio penalty of slow interpreters was resolved at the base point.
