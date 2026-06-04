---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2605.29489
url: https://huggingface.co/papers/2605.29489
arxiv_url: https://arxiv.org/abs/2605.29489
date: 2026-06-04
---

# Access Sets Matter: Budgeting Expert Reads for Scalable Weight-Space Model Merging

Weight-space model merging is usually formulated as an algebraic operation on checkpoints, yet at LLM scale the limiting resource is often the set of expert weights that must be read. We introduce MergePipe, a budget-aware execution layer that casts LLM merging as an expert access-set problem: given a merge operator and a checkpoint family in a shared weight coordinate system, choose which expert delta blocks to access under an explicit I/O budget. MergePipe indexes parameter blocks, builds deterministic access plans, and executes the induced budgeted merge with replayable manifests. The plan is budget-sound by construction and recovers the full-read merge at full budget; for fixed-coefficient additive operators, the omitted-update error is bounded by the norm of omitted deltas. Across Qwen and Llama merging workloads, MergePipe reduces expert-read I/O by up to an order of magnitude and achieves up to 11times speedups. Representative budget sweeps show O(10^{-3}) parameter deviation from full-read merges and no monotonic degradation on downstream benchmarks.
