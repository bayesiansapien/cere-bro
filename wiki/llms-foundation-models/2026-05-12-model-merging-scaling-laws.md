# Model Merging Scaling Laws in Large Language Models

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2509.24244](https://arxiv.org/abs/2509.24244)
**Tier:** 2 — Scaling laws / model merging / training economics

## TL;DR

A compact empirical scaling law for language-model merging measured by cross-entropy. The law has two components: a *size-dependent floor* that decreases with model capacity, and a *merging tail* with clear diminishing returns in the number of experts. Practical headline: gains fall roughly as 1/k in the number of merged experts, and variability shrinks as more experts are included. The law holds in-domain and cross-domain across four merging methods (Average, Task Arithmetic, TIES, DARE) and across architectures. A simple theory derives the 1/k tail and links the floor to base-model properties and the diversity across domains. Predictive payoff: estimate how many experts are needed to hit a target loss, decide when to stop adding experts, and trade off scaling the base model versus adding experts under a fixed budget.

## Why it matters

Merging has been used widely and predicted poorly. This paper turns it into a predictable, budget-aware alternative to multitask fine-tuning. Two implications for production: first, the floor-and-tail decomposition makes the "scale base model or add experts" tradeoff quantitative (you can compute the crossover for a given budget). Second, the variability-shrinks-with-k observation says the loss-curve shape gets more reliable as you merge more experts, which is a hedging argument for merging over single-task fine-tunes when downstream behavior must be predictable.

## How it relates to prior wiki state

- **Geometry Conflict (today).** Same phenomenon, different layer. The scaling law is the macroscopic curve, geometry conflict is the microscopic explanation: as k grows, geometry conflict between the merged state and the next expert rises, and the marginal gain drops. The 1/k tail in this paper matches the qualitative prediction of the geometry account.
- **Weight Disentanglement / Task Arithmetic (2026-04-22).** That paper established when task arithmetic works. This paper quantifies how much it gains as you scale k.
- **Prescriptive Scaling Laws for Data-Constrained Training (2026-05-09).** Both papers move scaling-law work from descriptive to prescriptive. The data-constrained paper asks how to allocate a fixed data budget. This paper asks how to allocate a fixed *expert* budget under merging. Same prescriptive turn, two different resource axes.
- **MIT Superposition Scaling Laws (2026-05-03).** The superposition account predicts diminishing returns from adding features along non-orthogonal directions. Merging k experts is a sum of k task vectors in roughly the same parameter space, so the 1/k decay is consistent with the superposition picture: each new expert overlaps increasingly with prior experts.

## Research angle

The size-dependent floor is the most actionable variable. The paper says the floor decreases with model capacity, but the dependence shape is the planning input. If the floor goes as 1/N for model size N and the tail goes as 1/k, the optimal allocation under a fixed (N * k) budget is a closed-form. The paper does not state the closed-form explicitly. A second angle: the law is measured at cross-entropy, not at downstream task accuracy. The mapping from cross-entropy reduction to downstream gain is non-monotonic in many regimes, so the budget calculus the paper enables may need a per-task correction. A third angle: does the 1/k tail change under non-uniform expert quality? Real merging pipelines have heterogeneous experts; the paper appears to treat them uniformly.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2509.24244)
- [HuggingFace page](https://huggingface.co/papers/2509.24244)
- Raw source: [raw/huggingface/2026-05-12-model-merging-scaling-laws-in-large-language-models.md](../../raw/huggingface/2026-05-12-model-merging-scaling-laws-in-large-language-models.md)

## Related wiki pages

- [Geometry Conflict](2026-05-12-geometry-conflict-continual-post-training.md)
- [Weight Disentanglement / Task Arithmetic](2026-04-22-weight-disentanglement-task-arithmetic.md)
- [Prescriptive Scaling Laws for Data-Constrained Training](2026-05-09-prescriptive-scaling-laws-data-constrained.md)
- [MIT Superposition Scaling Laws](2026-05-03-mit-superposition-scaling-laws.md)
