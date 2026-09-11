---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.10355
url: https://huggingface.co/papers/2609.10355
arxiv_url: https://arxiv.org/abs/2609.10355
date: 2026-09-10
---

# Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs

Video understanding has rapidly evolved toward video large language models (VideoLLMs): systems that couple video representations with pretrained large language models and condition generation on a textual prompt. Their strong performance on captioning, question answering, retrieval and temporal grounding comes at a computation and memory cost that grows with frame count and context length, limiting deployment in real-time, mobile and resource-constrained settings. This survey covers inference-efficiency mechanisms for visual and audiovisual VideoLLMs that report concrete reductions in parameter count, FLOPs per input, latency, memory, or visual and audio token count. We analyze bottlenecks across frame sampling, modality encoding, connector-level token reduction, and LLM prefilling and decoding. We organize methods by the pipeline stage at which they act, covering VideoLLMs developed since late 2022 together with earlier frame-sampling and vision-encoder mechanisms that remain components of current pipelines. We assemble literature-reported accuracy--cost comparisons under shared host models and input protocols wherever available, distinguish them from heterogeneous cross-paper evidence, and identify gaps in audiovisual efficiency and standardized evaluation. We maintain a repository at https://github.com/momentslab/awesome-efficient-videollm.
