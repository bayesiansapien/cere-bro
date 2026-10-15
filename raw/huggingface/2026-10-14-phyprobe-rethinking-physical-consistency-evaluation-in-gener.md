---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.507048+00:00
arxiv_id: 2609.38377
url: https://huggingface.co/papers/2609.38377
arxiv_url: https://arxiv.org/abs/2609.38377
date: 2026-10-14
---

# PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos

Evaluating the physical consistency of generated videos remains a fundamental challenge. Existing approaches rely on off-the-shelf vision-language models, which can often be myopic to physical dynamics, or fine-tuned evaluators trained on human annotations, which overfit to dataset-specific cues and fail to generalize. A key challenge is that existing supervision sources provide either relative ordering or absolute scores, but not both reliably and consistently across varied settings. To this end, we introduce PhyProbe, an evaluator that extracts features from a frozen pretrained spatio-temporal encoder and maps them to a scalar physical consistency violation score via a lightweight scoring head. PhyProbe is trained through a unified objective combining pairwise ranking, regression on noisy scalar annotations, and anchor-based calibration over a curated set of heterogeneous supervision sources. Experiments show that PhyProbe outperforms prior methods on most pairwise benchmarks spanning real-generated and generated-generated pairs under varying correspondence, with the largest gains in no-correspondence and generated-generated settings where existing fine-tuned evaluators degrade sharply. PhyProbe achieves strong correlation with human judgments, with close agreement between rank-based and linear metrics, indicating that scores are both well ordered and anchored to a stable [0, 1] scale. Further, despite being trained on supervision indicative of physical consistency, without explicit general-preference labels, PhyProbe also performs competitively on human preference benchmarks: consistent with the observation that physics violations are entangled with broader quality degradations.
