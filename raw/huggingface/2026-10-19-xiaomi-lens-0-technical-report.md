---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23279
url: https://huggingface.co/papers/2610.23279
arxiv_url: https://arxiv.org/abs/2610.23279
date: 2026-10-19
---

# Xiaomi-Lens-0 Technical Report

Multimodal large language models (MLLMs) answer questions about whole images well, yet they still struggle with fine-grained region understanding. A key reason is that text-only supervision never specifies which regions support an answer. To close this gap, we present Xiaomi-Lens-0, a 4B MLLM built on Qwen3.5 that predicts masks from its own visual representations. Specifically, a lightweight decoder combines vision-encoder patch features with visual latents, the language model's mask-token states, so mask supervision reaches the shared backbone without an additional segmentation encoder. Because each latent decodes to a mask, the model can interleave reasoning with region-specific latents and thus think with visual latents, while grounded reasoning traces supervise the regions it visits during chain-of-thought. As a result, across all eight RefCOCO, RefCOCO+, and RefCOCOg splits, Xiaomi-Lens-0 gains 5.6 points on average over Qwen3.5 in referring comprehension and achieves the highest segmentation cIoU among compared models. Moreover, it surpasses Qwen3.5 across all perception benchmarks. Homepage: https://seerray-lab.github.io/Xiaomi-Lens-0{this https URL}
