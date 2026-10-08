---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.38972
url: https://huggingface.co/papers/2609.38972
arxiv_url: https://arxiv.org/abs/2609.38972
date: 2026-10-07
---

# Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment

Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose CoT-Interpretability Alignment (CIA), a metric that measures the agreement between a model's CoT traces and its internal reasoning strategies as detected by interpretability tools. We evaluate CIA on three tasks (two-hop question answering, hint intervention, and integer multiplication) across three LLMs, finding that LLMs exhibit limited alignment across all tasks (44.8-75.9%). We then experiment with improving CIA via post-training, setting both the task accuracy and parametric faithfulness signals as a reward. Experiments show that we can substantially improve CoT parametric faithfulness while maintaining or improving the task accuracy. We provide rich analysis, such as their generalization patterns. Our work provides both a framework for auditing CoT parametric faithfulness and a pathway toward making models' explicit reasoning more trustworthy. Code and data are available at https://github.com/yihuaihong/CIA-minimal-repro.
