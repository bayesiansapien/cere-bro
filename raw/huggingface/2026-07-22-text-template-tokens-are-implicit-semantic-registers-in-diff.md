---
source: farmer/huggingface
farmed: 2026-07-22T05:46:30Z
arxiv_id: 2607.19139
url: https://huggingface.co/papers/2607.19139
arxiv_url: https://arxiv.org/abs/2607.19139
date: 2026-07-22
---

# Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers

Text-to-image diffusion transformers (DiTs) jointly process text and image tokens, yet their internal computation during denoising remains poorly understood. We introduce a causal interpretability framework for modern large-scale DiTs that combines attention decomposition with targeted interventions across token spans, heads, and layers. Using it to separate prompt-content tokens from structural template tokens, we find that the structural tokens carry little prompt-specific information at the encoder output. Yet surprisingly, they emerge as dominant image-to-text attention sinks and causally maintain object identity inside the DiT, acting as implicit semantic registers. We show that they acquire this identity indirectly, with prompt semantics first injected into the image latents and then read back into the template tokens rather than transferred directly from the prompt tokens. Inspired by the above findings, we design a training-free pruning rule for DiTs. Heads that attend most strongly to prompt tokens are dispensable, and pruning them removes 20% of attention FLOPs with only a 1.4-point drop on GenEval. We further reveal how generative computation in DiTs is organized across heads and depth, separating semantic routing from visual synthesis and progressing from identity formation to propagation and refinement. Our work not only reveals that the tokens encoding semantics at input need not be those that maintain it during generation, but also provides a causal view of internal mechanisms in DiTs.
