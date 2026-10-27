---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800556+00:00
arxiv_id: 2610.24481
url: https://huggingface.co/papers/2610.24481
arxiv_url: https://arxiv.org/abs/2610.24481
date: 2026-10-26
---

# DuoLM: Fast and Effective Personalized Recommendation with Language Models

Language models can make personalized recommendations from rich item content, user history, and feedback. However, evaluating many candidates with full-text inputs incurs substantial online computation and limits serving throughput. We introduce DuoLM, a framework for fast and effective personalized recommendation that integrates a compact recommendation model with an efficient serving runtime. An encoder LLM learns compact item representations for offline reuse, while a personalized ranker LLM combines them with user history and feedback for recommendation. We train both models end to end with recommendation supervision and teacher distillation. The runtime further accelerates inference through virtual token IDs for embedding access, shared history computation, and CUDA Graph replay. Benchmark results show that our framework achieves recommendation quality comparable to that of the expert teacher model. On a single H100, it delivers approximately 26,400 candidate scores per second, about 60times the throughput of the teacher served with vLLM and automatic prefix caching.
