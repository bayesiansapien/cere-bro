---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.16893
url: https://huggingface.co/papers/2605.16893
arxiv_url: https://arxiv.org/abs/2605.16893
date: 2026-05-19
---

# NGM: A Plug-and-Play Training-Free Memory Module for LLMs

Recent studies introduce conditional memory modules that decouple knowledge storage from neural computation, enabling more direct knowledge access. Compared to MoE, which relies on dynamic computation paths, explicit lookup provides a more efficient knowledge retrieval mechanism. However, these approaches still depend on learned memory embeddings, requiring additional training and limiting flexibility. To address this, we propose N-gram Memory (NGM), a training-free, plug-and-play module composed of a Causal N-Gram Encoder and a Cosine-Gated Memory Injector. The Causal N-Gram Encoder directly averages the pretrained token embeddings of the backbone model to construct N-gram representations, thereby eliminating the need to train separate N-gram embeddings from scratch. This design requires neither an additional memory table nor a retrieval pipeline. The Cosine-Gated Memory Injector then uses a non-parametric cosine gate with ReLU to modulate the retrieved embeddings into the contextual representations. We evaluate NGM on the Qwen3 series from 0.6B to 14B across eight benchmarks. NGM improves average performance by 0.5 to 1.2 points, with particularly clear gains on code generation and knowledge-intensive tasks (e.g., +3.0 on LiveCodeBench and +3.03 on GPQA for Qwen3-14B). Moreover, NGM also improves performance in multimodal benchmarks (e.g., MMStar +1.53 on Qwen3-VL-2B).
