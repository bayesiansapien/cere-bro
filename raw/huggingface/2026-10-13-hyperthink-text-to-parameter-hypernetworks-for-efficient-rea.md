---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.03039
url: https://huggingface.co/papers/2610.03039
arxiv_url: https://arxiv.org/abs/2610.03039
date: 2026-10-13
---

# HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning

Long-form thinking traces can substantially improve the multi-step reasoning performance of large language models (LLMs), but they introduce high inference-time overhead, with latency dominated by sequential decoding. We propose HyperThink, a text-to-parameter approach that amortizes this reasoning computation into a single query-conditioned parameter update: a lightweight hypernetwork reads the question and predicts updates to a small subset of the base LLM's parameters, while a vector-quantized decoder constrains them to a finite set of reusable patterns to improve robustness and transfer. Trained end-to-end on outputs from the base model itself, HyperThink eliminates long thinking traces at test time: after one hypernetwork forward pass, the adapted model generates a concise step-by-step solution and final answer without an intermediate trace, using far fewer tokens while retaining strong reasoning performance. Empirically, HyperThink improves the low-latency region of the accuracy-latency trade-off on mathematical and general reasoning tasks, with its strongest gains in the near-non-thinking regime.
