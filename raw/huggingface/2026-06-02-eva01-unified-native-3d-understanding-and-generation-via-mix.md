---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.16745
url: https://huggingface.co/papers/2605.16745
arxiv_url: https://arxiv.org/abs/2605.16745
date: 2026-06-02
---

# EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers

This paper addresses the challenge of integrating 3D meshes as a native modality within Multimodal Large Language Models (MLLMs). Diffusion-based large reconstruction models decouple semantic understanding from geometric reasoning, operating as stateless reconstructors conditioned on dense 2D pixel priors. Recent MLLM-based methods treat the 3D modality as an external output rather than a native component of the multimodal sequence, making incremental adaptations without a systematic analysis of how geometric manifolds align with MLLM feature spaces. We introduce EVA01, a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing. Built upon a Mixture-of-Transformers (MoT) architecture, EVA01 decouples the model into a pre-trained Understanding Expert (E_{und}) and a structurally mirrored Generation Expert (E_{gen}), coupled through shared global self-attention with hard modality routing. This design aligns the semantic latent space of the MLLM backbone with the geometric manifold, enabling direct transfer of multimodal priors without intermediate 2D representations. Results show that EVA01 achieves state-of-the-art native text-to-3D generation fidelity and unlocks robust long-context multi-turn geometric editing with identity preservation, a capability fundamentally inaccessible to stateless reconstruction pipelines. Our findings further offer architectural insights for integrating 2D foundation models with 3D tasks, informing the design of 3D-native multimodal systems. Project Page: https://www.seeles.ai/research/pages/EVA01
