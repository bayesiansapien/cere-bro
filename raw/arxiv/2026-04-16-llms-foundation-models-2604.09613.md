---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.09613
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.09613
published: 2026-04-16
authors: Huamin Chen, Xunzhuo Liu, Junchen Jiang
---

# Token-Budget-Aware Pool Routing for Cost-Efficient LLM Inference

**arXiv:** https://arxiv.org/abs/2604.09613
**Authors:** Huamin Chen, Xunzhuo Liu, Junchen Jiang

## Abstract

arXiv:2604.09613v2 Announce Type: replace-cross  Abstract: Production vLLM fleets provision every instance for worst-case context length, wasting 4-8x concurrency on the 80-95% of requests that are short and simultaneously triggering KV-cache failures -- OOM crashes, preemption storms, and request rejections. Both problems share a single root cause: configuration-traffic mismatch.   We propose token-budget-aware pool routing: estimate each request's total token budget using a self-calibrating per-category bytes-per-token ratio, then dispatch it to one of two vLLM pools -- a high-throughput short pool or a high-capacity long pool -- each right-sized for its workload class. The ratio is learned online via exponential moving average from usage.prompt_tokens feedback, requiring no tokenizer. A closed-form cost model, savings = alpha * (1 - 1/rho), predicts fleet-level GPU savings from two observable quantities: the short-traffic fraction alpha and the throughput gain ratio rho.   On traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M serving Llama-3-70B on A100 GPUs, token-budget routing reduces GPU instances by 17-39% (\$1.2-2.0M/yr at 1,000 req/s), with savings verified by a self-contained discrete-event simulator. A case study projecting Qwen3-235B-A22B on AMD MI300X at 10,000 req/s shows \$15.4M/yr in savings. The algorithm adds O(1) dispatch overhead, self-calibrates across content types without a tokenizer, and composes with PagedAttention, continuous batching, and prefill-decode disaggregation.
