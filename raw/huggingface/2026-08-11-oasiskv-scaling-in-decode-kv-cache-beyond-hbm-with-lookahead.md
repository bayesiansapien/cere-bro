---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.08097
url: https://huggingface.co/papers/2608.08097
arxiv_url: https://arxiv.org/abs/2608.08097
date: 2026-08-11
---

# OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic during LLM token generation, i.e., decode. In particular, HBM capacity has become a scarce and costly resource that heavily limits inference batch size and system throughput. This paper presents OasisKV, a memory-centric LLM inference system design that alleviates HBM capacity pressure by decoupling full KV-cache storage from HBM during LLM decoding. Because decode-time attention is naturally sparse, OasisKV keeps only the KV entries of the most relevant tokens in HBMs for attention computation. We observe that future important tokens can be predicted accurately in advance using lookahead tokens drafted by speculative decoding (SD). OasisKV employs an efficient attention background pipeline to identify important KV blocks. They are then prefetched from higher-capacity memory tiers (e.g., host or remote memory) and staged in HBMs before being used in the next decode step.
  We implement OasisKV based on vLLM. The lookahead prediction is accurate enough to keep accuracy within 0.7 points of full attention under a 2,048-token KV budget. This lets OasisKV turn sparsity into throughput gain: 1.69times over dense vLLM on the reasoning workload at 0.1 points of accuracy loss, and up to 2.1times on multi-GPU long-context serving. Under prefill--decode disaggregation, OasisKV reaches about 2times dense throughput while admitting each request with 6.5--9.7times less KV and holding 2.2-2.6 less decode-node host memory than full KV transfer.
