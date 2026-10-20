---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23841
url: https://huggingface.co/papers/2610.23841
arxiv_url: https://arxiv.org/abs/2610.23841
date: 2026-10-19
---

# StopWatch: Goal Grounding for Object-goal Navigation

Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack. Our diagnosis identifies goal grounding as the dominant failure. These policies explore well, yet often fail to notice that the goal is already in view or to estimate how far away it is. To address this failure, we ground the goal explicitly. Explicit grounding substantially improves success and reaches state-of-the-art results on six benchmarks across three scene collections. We also correct annotation defects in these benchmarks, so that future methods are evaluated more faithfully. Our analysis on the clean benchmarks shows that, with ground-truth grounding, our policy nearly matches the expert that generated its demonstrations, leaving the headroom in perception rather than policy learning. Our work points to goal grounding as a missing piece of object-goal navigation and offers a simple and effective solution to the task.
