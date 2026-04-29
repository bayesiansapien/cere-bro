---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.20796
url: https://huggingface.co/papers/2604.20796
arxiv_url: https://arxiv.org/abs/2604.20796
date: 2026-04-23
upvotes: 235
---

# LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model

LLaDA2.0-Uni is a unified discrete diffusion language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. It discretizes continuous visual inputs via SigLIP-VQ and enables block-level masked diffusion for both text and vision inputs within the backbone. The decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced through parallel decoding and prefix-aware optimizations, plus few-step distillation in the decoder. Matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Establishes a scalable paradigm for next-generation unified foundation models.
