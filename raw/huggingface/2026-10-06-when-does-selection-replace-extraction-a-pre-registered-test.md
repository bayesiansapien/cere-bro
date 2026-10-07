---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.34227
url: https://huggingface.co/papers/2609.34227
arxiv_url: https://arxiv.org/abs/2609.34227
date: 2026-10-06
---

# When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model

Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough? Published results disagree. Extraction-based systems report gains from distilled facts. Recent studies find raw history with good ranking does as well, but disagree about whether ranking matters. We ran a pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns selected by a single call to Jev, a typed decision model, are non-inferior to an LLM-extraction memory (one-sided 95% bound -3.0 points against a -5-point margin). Blind human grading narrows the margin but does not change the result. Raw turns cost 3,061 times less to write, and the result holds with a second answer model. Within this study, reranking's gain shrinks as the budget grows. It adds 17.4 points on LoCoMo and 9.1 on LongMemEval when three of 30 candidates are kept. At generous budgets it adds 1.5 and 1.1, and extraction systems are more accurate. This suggests why published results disagree. At matched context, Jev selects as accurately as an LLM reranker (non-inferiority bound -2.0) at a third of the latency, and more accurately than a multi-call graph traversal. Reranking lowers correct abstention. Plans, code and graded answers are released.
