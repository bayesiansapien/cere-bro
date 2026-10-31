---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.158331+00:00
arxiv_id: 2610.38425
url: https://huggingface.co/papers/2610.38425
arxiv_url: https://arxiv.org/abs/2610.38425
date: 2026-10-30
---

# IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation

Humans routinely consume multimodal content, where textual and visual information is naturally interleaved. Although Unified Multimodal Models (UMMs) can jointly generate text and images, multimodal interleaved generation remains largely underexplored. Progress in this area is hindered by two key limitations: (1) the lack of well-defined interleaved generation tasks and corresponding training data, and (2) the absence of fine-grained evaluation protocols that can reliably diagnose model performance across different capability dimensions. To this end, we present IntReal, comprising two complementary components: IntReal-100K, a real-world dataset of multimodal interleaved samples spanning four major categories, and the IntReal Evaluation Suite, which evaluates model performance across seven complementary dimensions using specialized expert models, enabling coarse-to-fine diagnosis. Extensive experiments validate our evaluation suite through low inter-metric redundancy (max pairwise absolute Spearman's ρleq 0.42 ), high agreement with human judgments (83.3% accuracy), and strong consistency across different expert evaluators (Spearman's ρ> 0.9 ), supporting the complementarity and reliability of our metrics. By benchmarking four families of UMMs, we show that IntReal Evaluation Suite reveals distinct strengths and weaknesses across models. Post-training experiments demonstrate the utility of IntReal-100K for improving interleaved generation and further show that training unimodal generation can also benefit interleaved generation. These findings suggest that interleaved generation can benefit from modality-specific optimization, rather than requiring joint text-image training at every stage.
