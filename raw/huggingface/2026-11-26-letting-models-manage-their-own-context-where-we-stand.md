---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.906555+00:00
arxiv_id: 2611.34147
url: https://huggingface.co/papers/2611.34147
arxiv_url: https://arxiv.org/abs/2611.34147
date: 2026-11-26
---

# Letting Models Manage Their Own Context: Where We Stand

Agent harnesses today manage context on the model's behalf: when the window fills, the harness triggers a compaction that summarizes the history. We study the alternative, model-driven context management, in which the model itself decides when and what to compact through a context API. We gave models control over their own context in \nooa, NVIDIA's open source agent harness, and compared the two strategies on document research and machine learning engineering across context budgets from 8K to 512K tokens. Models that use the context API effectively reach higher accuracy, often with fewer input tokens, especially at tight budgets: GPT 6.1 nearly triples its score at a 32K budget on OfficeQA Pro v2 (21\%~rightarrow~56\%), and Kimi gains with up to 41\% fewer input tokens. Models differ widely, however, in how often they use the API, how aggressively they compact, and when they start compacting, and prompt changes shift that timing. Finally, we show that inference engines can make model-driven edits cheaper: by reusing the KV cache of the unchanged suffix after an edit, we cut prefill compute by up to 15\% per request with no measurable change in accuracy. Together, these results point to a new co-design frontier: models trained to manage their own context, served by inference engines that support KV cache editing.
