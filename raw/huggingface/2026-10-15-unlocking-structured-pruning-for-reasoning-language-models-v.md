---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234426+05:30
arxiv_id: 2610.19121
url: https://huggingface.co/papers/2610.19121
arxiv_url: https://arxiv.org/abs/2610.19121
date: 2026-10-15
---

# Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming

Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models. However, existing methods can cause reasoning performance to collapse on long-form reasoning tasks such as AIME. We propose LayerTrim, a training-free structured pruning method that identifies redundant decoder layers and selectively trims their MLP features while preserving attention and decoder depth. LayerTrim is the first training-free structured pruning method designed to preserve long-form reasoning without gradients or recovery training. Across three reasoning language models and five benchmarks, LayerTrim outperforms existing structured pruning methods in most evaluated settings, improving average accuracy by up to 21.4 percentage points over RESP. On Qwen3-14B, LayerTrim achieves 1.24times faster prefill and 19.7\% lower peak GPU memory than the dense model, while better preserving reasoning ability. It also achieves the shortest average generation length among evaluated pruned models, while retaining the highest average accuracy. These results demonstrate that LayerTrim improves reasoning efficiency through both structural compression and reduced token generation.
