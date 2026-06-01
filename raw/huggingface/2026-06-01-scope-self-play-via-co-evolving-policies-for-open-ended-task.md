---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.31433
url: https://huggingface.co/papers/2605.31433
arxiv_url: https://arxiv.org/abs/2605.31433
date: 2026-06-01
---

# SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

Self-play can train language models without external supervision. However, existing methods require rule-checkable answers, leaving open-ended tasks dependent on curated prompts or frontier-model judges. We introduce SCOPE, a data-free self-play framework for open-ended tasks that co-evolves two policies: a Challenger that generates document-grounded tasks, and a Solver that answers them through multi-turn retrieval. A frozen copy of the initial model serves as the self-judge, which writes task-specific rubrics from the source document and grades Solver responses against them. Across three 7-8B instruction-tuned models (Qwen2.5, Qwen3, OLMo-3), SCOPE improves open-ended performance by up to +10.4 points on eight benchmarks and matches or exceeds GRPO_data trained on ~9K curated prompts. Although trained only on open-ended tasks, SCOPE also improves held-out short-form QA by up to +13.8 points on seven held-out benchmarks, surpassing GRPO_data on all three models.
