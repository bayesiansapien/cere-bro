---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33608
url: https://huggingface.co/papers/2610.33608
arxiv_url: https://arxiv.org/abs/2610.33608
date: 2026-10-27
---

# Mycelium: A Meta-Study of Hallucination Detection Across Provenance, Typology, and Granularities

Hallucination detection is increasingly important for evaluating and deploying large language models. However, existing methods are often compared across benchmarks that define and measure hallucination in substantially different ways, making reported scores difficult to interpret across settings. We study hallucination detection as a benchmark-conditioned measurement problem and organize existing benchmarks along three axes: provenance, which describes how model outputs and evidence conditions are obtained; typology, which captures the factuality and faithfulness failures represented by benchmark labels; and granularity, which specifies the unit at which hallucinations are annotated, predicted, and evaluated. Using this framework, we analyze how benchmark construction, annotation, and evaluation choices shape the underlying prediction task, and relate detector mechanisms and assumptions to the settings in which their performance is measured. We also examine span-level evaluation, where variation in annotation boundaries can substantially affect reported results, and propose Span Coverage F1 as a complementary containment-based metric. Our analysis clarifies what detector scores capture, highlights limitations of cross-benchmark comparisons, and motivates more explicit evaluation of generalization across benchmark conditions.
