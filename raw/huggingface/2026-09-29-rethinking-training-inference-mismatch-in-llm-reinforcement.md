---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930852+00:00
arxiv_id: 2609.32444
url: https://huggingface.co/papers/2609.32444
arxiv_url: https://arxiv.org/abs/2609.32444
date: 2026-09-29
---

# Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It

We study training-inference mismatch in reinforcement learning with verifiable rewards (RLVR) for large language models, where rollouts are sampled by an inference engine while gradients are computed by a training engine, and the two engines assign different probabilities to the same tokens. To account for this discrepancy in policy updates, we introduce calibrated importance sampling (CIS). CIS is motivated by an empirically supported logit-displacement characterization that expresses the mismatch as an additive displacement varepsilon_t in log-odds, determined by the per-logit perturbation before the softmax, whose distribution is approximately invariant to token confidence. This characterization motivates a confidence-aware truncation: large positive displacements are truncated at a single constant threshold, which maps back to an importance-ratio cap that tightens as token confidence increases. Theoretically, we show that CIS replaces the unbounded second moment that governs the error of exact importance sampling with a term bounded by a constant, at the cost of a bias controlled by the truncated excess. In evaluation across three mixture-of-experts models and five mathematical reasoning benchmarks, CIS achieves the highest five-benchmark average on all three models among the evaluated baselines. Diagnostic analyses show that CIS places less truncation bias on low-confidence tokens than truncated importance sampling, while upward clipping of small importance weights reduces held-out accuracy.
