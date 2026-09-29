---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.594727+00:00
arxiv_id: 2609.27277
url: https://huggingface.co/papers/2609.27277
arxiv_url: https://arxiv.org/abs/2609.27277
date: 2026-09-28
---

# TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent

Time series agents answer analytical questions by calling external tools, and which tools they carry is decided by people before the agent runs. However, we identify two failures in this setup. Human-Agent Tool Misalignment: a library of 21 expert-curated tools helps on some tasks and hurts on others, dropping anomaly accuracy under every backbone we test. Silent Harm: one round of generic self-revision changes 147 answers and breaks 56 of them, while the final score moves by less than a point. Both follow from the same gap: whether a tool helps is decided question by question at runtime, while tools are supplied in advance and judged by a single average. To address this, we propose TimeEvo, which clusters an agent's diagnosed failures into capability gaps, plans a measurement for each, synthesizes evidence-only tools that fill them, and admits the candidate library only through a paired admission gate. Experiments on ten time series QA tasks and three backbones show that TimeEvo, starting from an empty library, improves accuracy on every task and every backbone, and that a library grown on a cheap model still gains when it is installed into stronger ones. Code is available at https://github.com/Muyiiiii/TimeEvo.
