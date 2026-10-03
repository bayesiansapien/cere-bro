---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821104+00:00
arxiv_id: 2610.02202
url: https://huggingface.co/papers/2610.02202
arxiv_url: https://arxiv.org/abs/2610.02202
date: 2026-10-02
---

# ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research

What makes great scientists great? Even as AI systems start to make progress on open problems, scientists remain far ahead of them at sensing which prior idea, buried in an ever-growing archive of research, a new problem needs. To study this skill, we draw on researchers who know firsthand which earlier work advanced their completed projects, with papers serving as pointers to the ideas within. Using our automated pipeline that makes author annotation scalable, we build ScholarCatalyst by having 184 lead authors of 207 recent computer science papers label which candidates did or could have advanced their project, each with a detailed rationale. We introduce a retrieval task with author-provided judgments: given an initial research question, retrieve these papers from only the literature available when the project began. Agentic search does no better than embedding retrieval (0.42 vs. 0.48 Recall@20) despite calling that same retriever as a tool. Even an agent built on Claude Fable 5.1, which may have seen the completed papers during training, reaches only 0.51 R@20. These results highlight the need for new training recipes that equip models with expert intuition for searching broad corpora. We envision ScholarCatalyst as a step toward scientific agents that can take a half-formed idea and point to the prior research it needs.
