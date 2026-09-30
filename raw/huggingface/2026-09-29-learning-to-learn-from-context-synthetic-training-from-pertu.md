---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929914+00:00
arxiv_id: 2609.33642
url: https://huggingface.co/papers/2609.33642
arxiv_url: https://arxiv.org/abs/2609.33642
date: 2026-09-29
---

# Learning to Learn from Context: Synthetic Training from Perturbed Public Documents

Real-world tasks often require large language models (LLMs) to learn from complex task-specific context rather than pretrained parametric knowledge. This capability remains a weakness of LLMs, while human annotation for such task contexts is expensive and difficult to scale. Public high-quality documents are an abundant alternative, but much of the public web has already been consumed during pretraining: training on such documents naively would reward memorization rather than context learning. In this work, we attempt to make use of high-quality public documents with small perturbations and empirically find that LLMs can successfully generate context-dependent reasoning traces and answers, which are then used to train a student model. Specifically, we construct a synthesis pipeline that (i) rewrites source documents to reduce memorization risk, (ii) generates questions and rubrics that require reasoning over the document, (iii) answers the questions with the document as context, and (iv) admits only samples that genuinely depend on the document. Without any human annotators, our pipeline generates about 10k samples from 3.5k documents, and the resulting student model substantially improves the performance on CL-bench. SFT raises a Qwen3.6-35B-A3B student from 13.7% to 22.8%, and a subsequent rubric-reward RL stage reaches 24.6%, on CL-bench comparable with a frontier model of over a trillion parameters, Qwen3.8-2.4T (23.9%). We also observe a broad transfer of improvements to long-context understanding, instruction following, and reasoning, while code generation and knowledge remain mostly flat. We hope this work provides a reproducible and scalable way to improve the ability of LLMs to learn from context, and to facilitate further research on context-grounded reasoning.
