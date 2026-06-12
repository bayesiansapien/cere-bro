---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.13289
url: https://huggingface.co/papers/2606.13289
arxiv_url: https://arxiv.org/abs/2606.13289
date: 2026-06-12
---

# HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers

Holistic visual tokenizers are fundamental to unified multimodal models (UMMs) as they map diverse visual inputs into a unified representation space. In this paper, we present HYDRA-X, the first UMM that unifies image and video tokenization within a single Vision Transformer (ViT). Our design is driven by two core challenges: efficiently injecting spatiotemporal reconstruction capability into a native ViT, and embedding image- and video-level semantic awareness into the latent space. To address the first, comprehensive ablations reveal two key findings: (1) frame-level causal temporal attention suffices for visual reconstruction, whereas full spatiotemporal attention degrades it; and (2) hierarchical temporal compression substantially outperforms single-step alternatives. To tackle the second, we propose a lightweight decompressor that upsamples temporally compressed features under joint image-video teacher supervision, thereby enforcing complementary semantic structures within the compact latent space. Building on this holistic tokenizer, we further propose a principled improvement of the editing pipeline: source-target interaction should occur at the latent level inside the tokenizer rather than at the semantic level inside the LLM, substantially improving editing consistency and accelerating convergence. Instantiated at the 7B dense model, HYDRA-X achieves strong performance across image and video understanding and generation tasks, paving the way for future unified-tokenizer UMMs.
