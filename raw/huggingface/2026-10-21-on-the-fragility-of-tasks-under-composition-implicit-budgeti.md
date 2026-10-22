---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.644949
arxiv_id: 2610.27190
url: https://huggingface.co/papers/2610.27190
arxiv_url: https://arxiv.org/abs/2610.27190
date: 2026-10-21
---

# On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models

Modern language models are increasingly asked to handle several tasks within a single prompt. Doing so requires solving each task correctly while integrating the resulting answers into a coherent response. In this paper, we identify a fundamental limitation in this process, where models make substantially more errors when tasks are composed, even when they can solve every constituent task reliably in isolation. This degradation cannot be fully explained by the accumulation of independent errors. Across both open-weight models and the frontier model Claude Opus 5, our findings instead point to an implicit thinking budget underlying this effect. In particular, under composition, models use substantially fewer tokens per task than in isolation, even when the full sequence remains well within the context window. Tasks that require longer solution traces in isolation are consequently more fragile under composition, i.e., models make more errors on prompts containing these tasks. In isolation, non-fragile tasks receive more reasoning than they need and waste compute. However, by grouping tasks according to their fragility, the implicit budgeting can be manipulated to reduce token usage by 43\% across a range of math and linguistic tasks while also preserving accuracy.
