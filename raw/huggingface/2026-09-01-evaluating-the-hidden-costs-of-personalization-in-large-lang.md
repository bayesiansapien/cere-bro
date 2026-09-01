---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.28833
url: https://huggingface.co/papers/2608.28833
arxiv_url: https://arxiv.org/abs/2608.28833
date: 2026-09-01
---

# Evaluating the Hidden Costs of Personalization in Large Language Models

While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user satisfaction when conditioned on personal context such as conversation history, inferred preferences, and user profiles. Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo chambers; and (3) sycophantic bias, where models agree excessively with user opinions. As a result, models may reference personal information in contexts where it is unnecessary, inadvertently collapse response diversity, or agree excessively with user opinions. Despite the growing use of personalization in AI assistants, there has been limited systematic evaluation of its potential side effects. To bridge this gap, we propose PRISK, a dynamic evaluation framework with automated data generation and tailored metrics that uncovers systematic limitations in current LLM personalization and how personalized information shapes its responses. Our empirical analysis across 13 LLMs demonstrates the presence of user profiles and retrieved memories consistently exacerbates biases, resulting in an average drop of 45.9% in irrelevant personalization, 41.7% in preference narrowing and 61.7% in sycophantic bias.
