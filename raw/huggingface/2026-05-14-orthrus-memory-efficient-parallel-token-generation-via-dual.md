---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12825
url: https://huggingface.co/papers/2605.12825
arxiv_url: https://arxiv.org/abs/2605.12825
date: 2026-05-14
---

# Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion

We introduce Orthrus, a simple and efficient dual-architecture framework that unifies the exact generation fidelity of autoregressive Large Language Models (LLMs) with the high-speed parallel token generation of diffusion models. The sequential nature of standard autoregressive decoding represents a fundamental bottleneck for high-throughput inference. While diffusion language models attempt to break this barrier via parallel generation, they suffer from significant performance degradation, high training costs, and a lack of rigorous convergence guarantees. Orthrus resolves this dichotomy natively. Designed to seamlessly integrate into existing Transformers, the framework augments a frozen LLM with a lightweight, trainable module to create a parallel diffusion view alongside the standard autoregressive view. In this unified system, both views attend to the exact same high-fidelity Key-Value (KV) cache; the autoregressive head executes context pre-filling to construct accurate KV representations, while the diffusion head executes parallel generation. By employing an exact consensus mechanism between the two views, Orthrus guarantees lossless inference, delivering up to a 7.8x speedup with only an O(1) memory cache overhead and minimal parameter additions.
