---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.23855
url: https://huggingface.co/papers/2607.23855
arxiv_url: https://arxiv.org/abs/2607.23855
date: 2026-07-28
---

# OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation

Recent generative models are moving beyond silent video or standalone audio synthesis toward the joint generation of synchronized audio and video. Despite this progress, jointly generating audio and video with fine-grained cross-modal correspondence remains challenging due to their fundamental structural differences. Most existing methods use audio and video VAEs trained separately. As a result, the two latent spaces lack cross-modal alignment, leaving the downstream generative model to learn cross-modal synchronization from scratch. We present OmniVAE, a jointly trained audio-video VAE that learns fine-grained semantic alignment between audio and video latent representations. Beyond reconstruction, OmniVAE uses a segment-level audio-video contrastive objective to capture temporal-semantic correspondence and align the two latent spaces. In parallel, it distills features from pretrained modality-specific semantic encoders into each modality, improving the downstream learnability of both latent spaces. Extensive experiments show that both objectives consistently improve the learnability of the latent spaces, translating into higher generation quality and more accurate cross-modal synchronization in downstream text-to-audio-video generation. These findings underscore the importance of learning unified representations as a foundation for omnimodal modeling.
