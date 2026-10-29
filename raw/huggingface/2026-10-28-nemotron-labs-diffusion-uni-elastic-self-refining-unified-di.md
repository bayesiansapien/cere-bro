---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995487+05:30
arxiv_id: 2610.36466
url: https://huggingface.co/papers/2610.36466
arxiv_url: https://arxiv.org/abs/2610.36466
date: 2026-10-28
---

# Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation

We propose Nemotron-Labs-Diffusion-Uni (NLD-Uni), a unified discrete diffusion large language model (DLLM) for visual understanding and generation tasks. Compared with prior unified diffusion models, NLD-Uni introduces two major innovations. First, we propose a unified cross-paradigm on-policy distillation (OPD) framework that successfully transfers the visual understanding ability of autoregressive VLMs and visual generation ability of continuous flow models, to a unified DLLM. Second, NLD-Uni incorporates a novel progressive self-refining diffusion process that gradually corrupts each token across multiple steps during training, as opposed to adopting the conventional masked diffusion formulation that directly corrupts a clean image token to an uninformative mask token. At inference, this design allows NLD-Uni to make intermediate commit to a token, enabling progressive self-refinement for better visual quality. Through extensive experiments, we show that NLD-Uni achieves state-of-the-art performance among unified DLLMs on diverse tasks including visual question-answering, multi-modal reasoning, object grounding, text-to-image generation, and image editing.
