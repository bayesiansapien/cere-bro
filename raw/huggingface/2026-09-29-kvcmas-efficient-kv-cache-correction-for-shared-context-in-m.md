---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933996+00:00
arxiv_id: 2609.34060
url: https://huggingface.co/papers/2609.34060
arxiv_url: https://arxiv.org/abs/2609.34060
date: 2026-09-29
---

# KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems

Prompt-specialized multi-agent systems enable multiple agents to share a model while performing complementary roles to solve complex tasks. However, agent-specific prefixes change the KV cache generated for the same shared context, causing each agent to repeatedly prefill the growing context and construct a separate cache with high computation and memory overhead. Selective recomputation reduces this redundancy but still retains substantial model execution, while existing delta correction methods either support only recurring context relations or maintain memory-intensive online correction states for dynamically changing context. For first seen shared context, these methods also construct a reference cache outside the agent workflow, and an approximate correction at the first agent affects the outputs passed to subsequent agents. We present KVCMAS, an online KV cache correction framework that represents cross-agent cache deviations using compact low-rank states and seamlessly chains corrections along the agent workflow without an additional reference prefill. This design supports dynamically changing shared context while preserving an exact first-agent cache. Across multiple language and vision-language workloads, KVCMAS matches or improves the accuracy of prior KV cache sharing methods while achieving the lowest TTFT under highly concurrent serving. Under controlled serving traces, it provides a 2.0x TTFT speedup over inference without KV cache sharing and reduces peak GPU memory by up to 3.7x relative to a prior KV cache correction method. These results establish KVCMAS as an accurate and scalable KV cache sharing approach for prompt-specialized multi-agent serving.
