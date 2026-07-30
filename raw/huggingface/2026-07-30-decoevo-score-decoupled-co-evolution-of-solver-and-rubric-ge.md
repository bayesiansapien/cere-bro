---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.25675
url: https://huggingface.co/papers/2607.25675
arxiv_url: https://arxiv.org/abs/2607.25675
date: 2026-07-30
---

# DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space

Text-space optimization adapts large language models (LLMs) by editing external natural-language artifacts rather than model weights, so the optimized artifacts remain inspectable and the model can be treated as a black box. However, most existing text-space methods keep evaluation fixed. On open-ended tasks, this can become a bottleneck: once the solver improves on the criteria a rubric measures, omitted dimensions remain invisible to the optimization signal. Simply evolving the rubric is also unreliable when updates are selected by the current solver's score, because apparent progress can come from making the rubric easier to satisfy. We introduce DecoEvo (Decoupled Co-Evolution), which co-evolves a solver skill and a rubric-generator skill under decoupled objectives without using gold rubrics during optimization. The solver skill is updated using criterion-level feedback, while the rubric-generator skill is revised through complementary audits of requirement coverage and response discrimination that are independent of aggregate solver score. This separation focuses generator updates on newly exposed solver weaknesses, reducing repeated emphasis on criteria the solver already satisfies. Under each benchmark's official evaluation, DecoEvo outperforms all compared methods across five benchmarks and three LLM backbones, yielding 2.8--5.0\% relative gains over SkillOpt in the five-benchmark average.
