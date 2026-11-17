---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.999167+00:00
arxiv_id: 2611.18338
url: https://huggingface.co/papers/2611.18338
arxiv_url: https://arxiv.org/abs/2611.18338
date: 2026-11-16
---

# MEM-SQL: Memory-Empowered Text-to-SQL

Text-to-SQL systems translate natural language questions into SQL queries over increasingly complex databases. However, widely used benchmarks evaluate questions independently, overlooking settings where earlier queries over the same database can supply joins or calculations for a new question. We introduce HARE (History-AwaRe Text-to-SQL BEnchmark) to measure the accuracy and cost of adapting historical SQL. HARE comprises 1,600 requests derived from a fixed pool of 823 verified queries across four datasets. Annotations record which components each request preserves and which edits it requires, distinguishing whole-query adaptation from partial reuse. Our method, MEM-SQL (Memory-EMpowered Text-to-SQL), stores whole-query templates, reusable SQL blocks, and mappings from domain concepts to schema elements. MEM-SQL uses a layer only if every requirement assigned to it has a match above that layer's threshold. With On-demand Schema Linking (OSL), MEM-SQL consults the schema only when no layer qualifies or the generator judges retrieved evidence insufficient. Across six language models on HARE, mean execution accuracy rises from 37.1% for Direct Generation without history to 50.0% for MEM-SQL, with 76.6% fewer input tokens and 68.8% lower latency on average. Further analysis shows that requests reusing several verified queries remain a bottleneck, with accuracy falling from 56.7% to 29.7%, most sharply when reused components must be placed in a new query structure or combined with a shared join. Applying OSL to three other memory designs consistently reduces generation cost, while its accuracy benefit depends on the memory design. Verified history can thus make generation both more accurate and cheaper, but its value depends on the evidence retained and when the system consults the schema.
