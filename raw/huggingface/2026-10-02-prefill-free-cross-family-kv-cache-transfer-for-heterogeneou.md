---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822239+00:00
arxiv_id: 2609.32259
url: https://huggingface.co/papers/2609.32259
arxiv_url: https://arxiv.org/abs/2609.32259
date: 2026-10-02
---

# Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs

Recent multi-agent LLM systems increasingly combine heterogeneous models for specialized agent roles. However, text-based communication requires each receiver to prefill shared context already processed by the sender. Reusing the sender's key-value (KV) cache avoids this redundancy, but prefill-free transfer across model families must handle differences in tokenization, model depth, and KV representations. To address these issues, we propose HeteroFold, a prefill-free cross-family KV cache transfer method that keeps both the sender and receiver frozen. HeteroFold aligns model structures, maps the sender cache into the receiver space, and calibrates it to preserve receiver behavior. Across six transfer directions, HeteroFold achieves the best cache-transfer performance on all four long-context benchmarks and most short-context settings. It also matches text-based communication on the multi-agent benchmark. At 32K context length, Llama-3.1-8BrightarrowMinistral-3-14B transfer is 10.7times faster than Native Prefill and 1.18--1.47times faster than the state-of-the-art prefill-free baselines, Dense Latent and KV Ridge. These results show that HeteroFold enables efficient cross-family KV reuse without receiver prefill.
