---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819436+00:00
arxiv_id: 2609.40097
url: https://huggingface.co/papers/2609.40097
arxiv_url: https://arxiv.org/abs/2609.40097
date: 2026-10-02
---

# AutoDataBench: A Data-centric Testbed for Accelerating Auto Research

Existing auto-research benchmarks often entangle multiple sources of improvement, including training frameworks, hyperparameters, compute budgets, and data, making it difficult to attribute why one frontier agent outperforms another to specific research capabilities. In this work, we isolate and systematically evaluate Data Intelligence: an agent's ability to understand, manipulate, and improve the data that shapes model capabilities. We introduce AutoDataBench, a controlled testbed built on a conceptual framework of data intelligence spanning data diagnosis, data organization, and data construction, instantiated through three highly curated optimization tasks while holding non-data factors fixed. Across tool use, retrieval, and knowledge injection, we evaluate frontier LLMs' ability to improve training data through iterative experimentation under task-specific resource budgets. Beyond optimization performance, we ask: do LLMs understand what their data interventions do? We compare predictions made before training with observed outcomes to seek evidence of data-effect reasoning beyond trial and error, and explore whether iterative feedback helps LLMs better understand how changes to training data affect model performance. Finally, we show that reusing AutoDataBench trajectories for mid-training improves downstream coding performance, highlighting its value in both evaluating data intelligence and generating high-quality training data. Code and resources are available at https://github.com/AutoDataBench/AutoDataBench.
