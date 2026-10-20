---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.19378
url: https://huggingface.co/papers/2610.19378
arxiv_url: https://arxiv.org/abs/2610.19378
date: 2026-10-19
---

# Robust Explanatory Analysis for Structured Optimization Networks (REASON) in Learning

We seek a hierarchical resolution of residual error under a composite learning objective as a principled mechanism for identifying and exploiting additional information, particularly under distribution shift and perturbation. Inspired by the System 1/System 2 paradigm, we formulate this principle as a two-loop mechanism serving a common inference goal. A fast, System 1-like loop resolves the residual addressable by the available evidence; the remaining epistemic residual triggers a medium speed, System 2-like loop that actively acquires additional evidence and measures its informational value through residual reduction. Over nested solution spaces, the medium-loop optimum is provably no worse than the fast-loop optimum. Experiments show that the resulting two-loop model consistently improves upon the fast loop at approximately half the computation of the medium loop, including under unseen corruptions, and, when provided a cleaner observation, outperforms staged classifiers and learning-to-defer methods at equal computational cost.
