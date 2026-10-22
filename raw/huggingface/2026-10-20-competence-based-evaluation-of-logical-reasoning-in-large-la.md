---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.22894
url: https://huggingface.co/papers/2610.22894
arxiv_url: https://arxiv.org/abs/2610.22894
date: 2026-10-20
---

# Competence-Based Evaluation of Logical Reasoning in Large Language Models

Recent advances in large language models (LLMs) have brought impressive performance across diverse tasks; however, shortcomings remain in logical reasoning, including inconsistencies under linguistic variation. To improve the reasoning capacity of LLMs, we must be able to accurately measure their reasoning capacity. Current benchmarks primarily report single accuracy numbers on selected reasoning tasks. Such a performance-based evaluation methodology says little about a model's generalization capacity in reasoning. To address this limitation, we argue for a different evaluation paradigm, called competence-based evaluation (CBE), which tests whether models reliably apply the same competence across a family of problems. A parameterized generator scales complexity while keeping the required competence fixed, and matched answer-preserving presentations test correctness beyond one formulation. We instantiate CBE on elementary ordering tasks, scaling input size while varying presentations of the same ordering rule. Across six GPT and Qwen models, performance is reasonably good over bounded complexity ranges, but even strong models fail the competence condition across the tested family. Chain-of-thought and GRPO extend strong performance without resolving all tested failures; supervised LoRA shows little held-out transfer. CBE provides diagnostic profiles and an evaluation protocol that can grow with future models.
