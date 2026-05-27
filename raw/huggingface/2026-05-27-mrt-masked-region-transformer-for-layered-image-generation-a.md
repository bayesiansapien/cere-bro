---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.27235
url: https://huggingface.co/papers/2605.27235
arxiv_url: https://arxiv.org/abs/2605.27235
date: 2026-05-27
upvotes: 1
---

# MRT: Masked Region Transformer for Layered Image Generation and Editing at Scale

Layered image generation and editing is a fundamental capability that enables layer-wise reuse, editing, and composition of generated visual content, analogous to word-level editing in natural language. Despite its importance, this remains an underexplored area at scale. To address this gap, we present MRT, a 20B-parameter masked region diffusion model tailored for multi-layer transparent image generation and editing, trained on over 10M multilingual design samples spanning diverse aspect ratios and textual prompts. To fully leverage this scale, we make two key technical contributions. First, we unify three complementary tasks including text-to-layers, image-to-layers, and layers-to-layers within a shared masked region diffusion framework, where selective token masking enables flexible layer-wise generation and editing. Second, to enable overflow layer generation, we introduce an overflow-aware canvas layer that handles boundary inconsistencies and supports semi-transparent background synthesis, enabling complete editable layers extending beyond visible canvas boundaries. Additionally, we apply diffusion distillation to achieve 8-step, real-time multi-layer generation with minimal quality degradation. Extensive experiments demonstrate that our framework substantially outperforms prior state-of-the-art approaches, including various commercial systems, across all three tasks, establishing a new benchmark for multi-layer transparent image generation. Notably, our model significantly outperforms the concurrent Qwen-Image-Layered model in image-to-layers quality according to user-study results, while achieving 10-100x faster inference and reducing activation GPU memory consumption by 50-90% during image-to-layer inference.
