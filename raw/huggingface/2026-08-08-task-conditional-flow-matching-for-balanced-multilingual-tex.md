---
source: farmer/huggingface
farmed: 2026-08-08T23:44:03.927649
arxiv_id: 2608.05785
url: https://huggingface.co/papers/2608.05785
arxiv_url: https://arxiv.org/abs/2608.05785
date: 2026-08-08
---

# Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation

Multilingual text embedding models are commonly adapted using a single training objective across diverse tasks, despite different tasks requiring fundamentally different optimization strategies. We introduce Task-Conditional Flow Matching (TCFM), a multilingual embedding adaptation framework that selectively applies Flow Matching to translation tasks while optimizing retrieval, classification, and pair-classification tasks with objectives better aligned to their learning dynamics. TCFM further combines teacher-guided representation preservation with a three-stage curriculum to enable stable adaptation. Evaluated on the Indic Massive Text Embedding Benchmark, TCFM establishes a new state-of-the-art, consistently improving embedding quality across a diverse set of multilingual tasks and generalizing across embedding model families. We will publicly release the codebase and datasets upon acceptance of the paper.
