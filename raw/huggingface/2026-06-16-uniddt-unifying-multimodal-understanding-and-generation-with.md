---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16255
url: https://huggingface.co/papers/2606.16255
arxiv_url: https://arxiv.org/abs/2606.16255
date: 2026-06-16
---

# UniDDT: Unifying Multimodal Understanding and Generation with Decoupled Diffusion Transformer

Unified Multimodal Models (UMMs) have emerged as a critical direction for general-purpose multimodal intelligence, integrating understanding and generation into a single framework. However, existing UMMs face prominent challenges: (1) the inherent learning conflicts between visual understanding and generation tasks, leading to suboptimal modeling in both tasks; (2) different understanding and generation visual spaces impeding scalability; (3) over-reliance on task-specific data that neglects the duality of text-image understanding and generation. To address these challenges, we propose UniDDT, which leverages a Noisy ViT encoder along with an LLM to unify semantic encoding for visual generation and understanding tasks, while employing a separate diffusion decoder to decouple diffusion decoding from text decoding. With this Noisy ViT encoder, UniDDT is able to leverage the latent space as a unified visual representation, enabling seamless compatibility between understanding and generation tasks. Thus, the scalability within the generation tasks and the semantic expressiveness within understanding tasks can be balanced. Also, we construct dual data structures from the same image-text pairs, fostering interdependence between the generation and understanding data to exploit their inherent duality. Extensive experiments demonstrate that UniDDT achieves effective unification of multimodal understanding and generation with enhanced semantic consistency and scalability. For visual generation tasks, our UniDDT achieves 0.87 GenEval score and 86.9 DPG overall score. For multimodal understanding tasks, our UniDDT achieves 1699.5 score on MME benchmark and 76.5 overall score on SEEDbench.
