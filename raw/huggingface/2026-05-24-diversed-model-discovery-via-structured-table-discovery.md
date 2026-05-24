---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.22766
url: https://huggingface.co/papers/2605.22766
arxiv_url: https://arxiv.org/abs/2605.22766
date: 2026-05-24
---

# Diversed Model Discovery via Structured Table Discovery

Model cards describe model behavior through a mixture of textual descriptions and structured artifacts, including performance, configuration, and dataset tables. Existing model search systems rely predominantly on semantic similarity over text, which can produce homogeneous result sets and limit exploration of alternatives. We argue that model search is inherently comparative: users want models that are task-aligned yet differentiated in measurable ways. We hypothesize that this balance requires retrieval over condensed, high-quality evidence rather than verbose descriptions, and much of that evidence is concentrated in structured tables. We present StructuredSemanticSearch, a table-driven model search framework built on the ModelTables benchmark. Given a query, StructuredSemanticSearch combines a semantic baseline for task alignment with a structure-aware pipeline that discovers query-related model-card tables using table discovery operators such as unionability, joinability, and keyword search. Retrieved tables are mapped back to model cards under a controlled top-k budget, enabling fair comparison between text-based and table-based retrieval. Beyond retrieval, StructuredSemanticSearch adapts table integration to the model-table domain through orientation-aware integration, producing compact integrated views of tables from partially overlapping and sometimes transposed evidence tables. For evaluation, we introduce a nugget-based, auditable protocol that extracts compact evidence items from model cards, matches queries to condition- or intent-specific nuggets, and measures evidence coverage and diversity over retrieved model-card candidate sets. This protocol also provides a scalable path toward approximate, evidence-based labeling in dynamic model lakes. Experiments on 597 model-recommendation queries show improved nugget coverage for the structure-aware pipeline than semantic baseline
