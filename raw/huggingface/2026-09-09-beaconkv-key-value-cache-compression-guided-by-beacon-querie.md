---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.04971
url: https://huggingface.co/papers/2609.04971
arxiv_url: https://arxiv.org/abs/2609.04971
date: 2026-09-09
---

# BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference

Large Reasoning Models (LRMs) achieve superior problem-solving through extended Chain-of-Thought (CoT) generation, but the resulting key-value (KV) cache grows linearly with sequence length and creates severe memory bottlenecks, often exceeding GPU capacity for long reasoning traces. Existing KV cache compression methods rely on recent queries to estimate future token importance, implicitly assuming these serve as reliable proxies for future attention patterns. We demonstrate that this assumption fails in long-horizon reasoning: certain decoding steps generate Thought Revisiting Tokens (TRT) that re-attend to distant previous context, such as task-solving plans formulated early in the trace. Through systematic analysis, we discover that queries corresponding to the TRT cluster into a small number of similarity groups in the embedding space. Based on this insight, we propose BeaconKV, a training-free KV cache compression method that maintains beacon queries, compact representatives for each global query cluster, to anticipate which KV pairs will be revisited without storing the entire query history. Across four open-source LRMs and diverse reasoning benchmarks, BeaconKV generally outperforms existing compression methods, achieving up to 5.8times memory reduction while nearly preserving full cache accuracy and improving throughput by over 4.3times.
