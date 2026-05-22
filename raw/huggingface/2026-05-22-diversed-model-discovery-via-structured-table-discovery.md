---
source: farmer/huggingface
farmed: 2026-05-22T00:00:00+00:00
arxiv_id: 2605.22766
url: https://huggingface.co/papers/2605.22766
arxiv_url: https://arxiv.org/abs/2605.22766
date: 2026-05-22
---

# Diversed Model Discovery via Structured Table Discovery

Model cards describe the behavior of models through a mixture of textual descriptions and structured artifacts, including performance, configuration, and dataset tables. Existing model search systems rely predominantly on semantic similarity over text, which can produce homogeneous result sets and limit users' ability to explore alternatives and reason about trade-offs. We argue that model search is inherently comparative: users want models that are aligned at the task level yet differentiated in measurable ways. We hypothesize that this balance requires retrieval over condensed, high-quality evidence rather than verbose descriptions, and much of that evidence is concentrated in structured tables. We present Structured Semantic Search, a table-driven model search framework built on the curated ModelTables benchmark. Given a query, Structured Semantic Search combines a semantic baseline for task alignment with a structure-aware pipeline that discovers query-related model-card tables using table discovery operators such as unionability, joinability, and keyword search. Retrieved tables are mapped back to model cards under a controlled top-k budget, enabling fair comparison between text-based and table-based retrieval. Beyond retrieval, Structured Semantic Search adapts table integration to the model-table domain through orientation-aware integration, producing compact integrated views of tables from partially overlapping and sometimes transposed evidence tables.
