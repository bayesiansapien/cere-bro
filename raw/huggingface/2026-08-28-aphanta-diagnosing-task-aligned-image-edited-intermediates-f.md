---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.26993
url: https://huggingface.co/papers/2608.26993
arxiv_url: https://arxiv.org/abs/2608.26993
date: 2026-08-28
---

# Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning

Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce Aphanta, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline. Aphanta evaluates three conditions---direct reasoning, reasoning with an editor-generated intermediate, and reasoning with an idealized reference intermediate---to separate potential visual headroom from the practical utility of current editors. Across 20 candidate tasks and multiple editor--MLLM combinations, we find that utility is strongly task-conditioned. Gains concentrate in visual cue injection, grounding, and counterfactual state realization, whereas intermediates requiring symbol-sensitive construction or structural extrapolation are substantially less reliable. On the selected positive-task subset, our consolidated Qwen pipeline improves the mean task score from 0.343 to 0.445 (+10.2 points; +29.7% relative), while the full study also retains filtered and unsuccessful tasks to expose the boundary. These results position image editing as a specialized visual workspace rather than a universal reasoning mechanism, and establish Aphanta as a reusable protocol for measuring task--representation alignment, editor realization, and downstream pipeline utility.
