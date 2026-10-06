---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.28339
url: https://huggingface.co/papers/2609.28339
arxiv_url: https://arxiv.org/abs/2609.28339
date: 2026-10-05
---

# Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control

Pretrained generative Diffusion Transformers (DiTs) capture rich pixel-level visual and language-conditioned structure through large-scale image and video generation training. A growing line of robot policies builds on this generative prior, but how it should be transferred to control remains unclear, and existing approaches commonly instantiate this transfer through future visual prediction. We ask a more basic question: what a pretrained generative DiT actually contributes to action learning, and how this prior should be adapted for control. We introduce NowWAM, a future-target-free co-training formulation that denoises the current observation and predicts robot actions from the same visual stream, directly coupling the native generative objective to the action-facing representation across the denoising trajectory. Under matched controlled settings, past and future visual targets perform comparably, while restricting training to the clean endpoint substantially reduces robustness, suggesting that a separate future target is not essential for generative adaptation, while the denoising trajectory remains an effective interface for control. On LIBERO-Plus, NowWAM reaches 87.7% with FLUX2-Klein, improving over the future-target co-training baseline by 6.1 points while halving training visual tokens (784 to 392) and reducing step time from 2.85 s to 1.63 s, a 1.8x speedup. With the pure text-to-image Z-Image backbone, NowWAM further reaches 87.8%, showing that strong control adaptation is not tied to video generation or image-editing backbones.
