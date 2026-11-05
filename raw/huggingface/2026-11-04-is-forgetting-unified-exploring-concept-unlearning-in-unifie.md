---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.366371+05:30
arxiv_id: 2611.04467
url: https://huggingface.co/papers/2611.04467
arxiv_url: https://arxiv.org/abs/2611.04467
date: 2026-11-04
---

# Is Forgetting Unified? Exploring Concept Unlearning in Unified Multimodal Models

Unified multimodal models (UMMs) integrate image generation and visual understanding, but are existing single-pathway unlearning methods sufficient to suppress target concepts across both? In this work, we study cross-pathway concept unlearning. Our goal is to prevent a model from both generating images of a target concept and identifying it in input images, while preserving other capabilities. To this end, we introduce UUBench, a diagnostic benchmark covering 30 target concepts and 60 semantically related neighboring concepts. Experiments on representative UMMs show that the evaluated single-pathway methods achieve limited joint forgetting: generation-side editors strongly suppress target generation but yield limited forgetting in visual understanding, while understanding-side baselines struggle to achieve substantial forgetting even in their own pathway. Their direct composition also yields limited joint forgetting. We therefore propose UniForget, achieving joint forgetting rates of 80.0% on BAGEL-7B-MoT and 92.7% on Janus-Pro-7B, outperforming representative baselines. Further analysis reveals trade-offs between joint forgetting and capability preservation.
