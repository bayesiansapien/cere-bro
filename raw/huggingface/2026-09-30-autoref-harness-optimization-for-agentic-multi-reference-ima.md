---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35530
url: https://huggingface.co/papers/2609.35530
arxiv_url: https://arxiv.org/abs/2609.35530
date: 2026-09-30
---

# AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation

Recent image generation models can take multiple reference images as input and combine them into a new image. However, multi-reference image generation remains challenging: models may omit or duplicate subjects from the references, or produce images in which multiple subjects appear unnaturally pasted. Recent work has proposed image generation agents that combine image generation models, reasoning models, and a harness, which is an executable program that specifies how reference images are interpreted, how generation is performed, how outputs are diagnosed, and how the final image is selected. In multi-reference generation, however, references play different roles and outputs must satisfy many criteria at once, such as fidelity to each reference and the naturalness of the whole image, so many parts of the harness could be improved, from how references are processed to how outputs are diagnosed. This makes it hard to predict which changes will improve performance and by how much, and good harnesses difficult to design by hand; indeed, human-written harnesses vary widely in performance. We therefore propose AutoRef, which optimizes the harness automatically while keeping both models frozen: a coding agent iteratively rewrites the harness code. AutoRef separates the tasks whose feedback informs proposals from the tasks used to select candidates, and continues the search from a beam of the top-ranked harnesses on the selection tasks. Using this procedure, we discover AutoRef-Harness, which improves the open-weight FLUX.2 [klein] 4B from 5.72 to 7.37 on held-out four-reference tasks of the MultiBanana benchmark, matching or exceeding proprietary models including Nano Banana Pro and GPT-Image-1.5. Without re-optimization, the same harness also improves results when the generator, number of references, benchmark, evaluator, or reasoning model differs from those used in the search.
