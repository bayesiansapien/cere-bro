---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10572
url: https://huggingface.co/papers/2606.10572
arxiv_url: https://arxiv.org/abs/2606.10572
date: 2026-06-10
---

# One Token per Multimodal Evidence: Latent Memory for Resource-Constrained QA

External memory effectively grounds large language models (LLMs) and vision-language models (VLMs)-based question answering (QA) in relevant multimodal evidence. However, existing memory paradigms represent each memory item in raw text and image forms, so retrieval-based systems must pass the retrieved text or images to the generation LLMs/VLMs, resulting in high token consumption and storage pressure, making it unaffordable for resource-constrained applications. We propose Latent Memory, a latent-space memory paradigm that replaces each raw text or image evidence item with a single high-dimensional latent token produced by a small compressor LLM/VLM. Rather than retrieving raw evidence for generation, Latent Memory operates in a unified latent representation space: the query is embedded into this space to retrieve relevant latent tokens, and the retrieved latent tokens are directly prompted to a pretrained LLM or VLM for answer generation. To make each latent token simultaneously informative for reconstruction, retrieval, and generation, we train the compressor with reconstruction, contrastive, and distillation objectives in a unified end-to-end manner. Latent Memory is evaluated on seven text-only QA benchmarks (e.g., HotpotQA) and multimodal QA benchmarks, where it achieves competitive QA performance compared to advanced RAG baselines while consuming 3x to 10x fewer generator tokens. It can also deliver the strongest image-grounded QA performance on WebQA. Code is available at https://github.com/zz1358m/Latent-Memory-Master.
