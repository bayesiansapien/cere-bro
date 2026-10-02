---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352391+05:30
arxiv_id: 2609.36931
url: https://huggingface.co/papers/2609.36931
arxiv_url: https://arxiv.org/abs/2609.36931
date: 2026-10-01
---

# Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation

Reproducibility is essential for scientific research, yet prior work shows that LLM outputs vary with hardware and batching. We identify an overlooked factor: the hidden injection of the current date into system prompts, which users cannot control and which changes every day. Across 9 recent LLMs and 6 datasets spanning multiple-choice QA (MCQA), math reasoning, code generation, and machine translation, performance varies solely with the current date, with deltas of up to 6% on MCQA, 14% on math reasoning, 7% on code generation, and 2.84 BLEU on machine translation. Model rankings also shift, affecting leaderboards. This date effect exceeds other sources of non-determinism, such as batch size and numerical precision. Standard prompting techniques -- chain-of-thought and few-shot prompting -- do not reduce the sensitivity; chain-of-thought even amplifies it. Our findings underscore the need for careful evaluation protocols to ensure reproducibility and fair comparisons in LLM research.
