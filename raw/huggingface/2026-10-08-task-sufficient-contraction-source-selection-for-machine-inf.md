---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.313082+05:30
arxiv_id: 2610.08884
url: https://huggingface.co/papers/2610.08884
arxiv_url: https://arxiv.org/abs/2610.08884
date: 2026-10-08
---

# Task-Sufficient Contraction: Source Selection for Machine Information Interfaces

A declared task can sometimes certify a reduced source before a downstream encoder, codebook, rate, distortion target, or optimizer is chosen. This paper studies when one such reduction preserves the complete downstream problem family, a property termed Task-Sufficient Contraction. The reduced source is fixed by the task before the later operating point is selected. An exact contraction allows the later problem to be solved on that source with the same result as if the full source had been retained.
  For a machine with a fixed set of possible actions and a fixed loss, the paper identifies a consumer-specific source by merging states only when every available action has the same regret in both. For finite action sets, replacing the richer source by this reduced source preserves the complete one-step rate-regret curve, even though the reduction is fixed before the distortion target is chosen. A second result gives an exact characterization for quadratic loss on affine feasible-action sets: the canonical reduced source is the projection onto the directions in which feasible actions can differ. Under a fixed energy budget, this becomes centered load, while retaining only the optimal water-filled action is too coarse. Earlier Information Bottleneck, semantic rate-distortion, and goal-oriented quantization results are then used to distinguish exact, architecture-conditioned, approximate, failed, and corrected contractions. The framework suggests a way for heterogeneous machines to exchange what a receiving task needs without first aligning their full internal representations.
