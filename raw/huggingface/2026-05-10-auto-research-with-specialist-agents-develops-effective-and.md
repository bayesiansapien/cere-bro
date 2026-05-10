---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.05724
url: https://huggingface.co/papers/2605.05724
arxiv_url: https://arxiv.org/abs/2605.05724
date: 2026-05-10
---

# Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes

We study auto research as a closed empirical loop driven by external measurement. Each submitted trial carries a hypothesis, an executable code edit, an evaluator-owned outcome, and feedback that shapes the next proposal. We instantiate this loop with specialist agents that partition recipe surfaces and share measured lineage across trials. The central empirical finding is that lineage feedback lets agents turn evaluator outcomes -- including crashes, budget overruns, size failures, and accuracy-gate misses -- into later program-level recipe edits rather than one-shot suggestions. Across 1,197 headline-run trials plus 600 Parameter Golf control trials, humans did not choose proposals, edit recipes, override scores, or repair failed trials during the search.
