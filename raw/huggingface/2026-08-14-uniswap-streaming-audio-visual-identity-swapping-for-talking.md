---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.11752
url: https://huggingface.co/papers/2608.11752
arxiv_url: https://arxiv.org/abs/2608.11752
date: 2026-08-14
---

# UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transfers the reference appearance and vocal timbre within a single audio-visual diffusion transformer while preserving the source content and dynamics. To address the scarcity of aligned cross-identity training pairs, we introduce a swap-and-reconstruct pipeline that removes visual and vocal identity from real clips and uses the original clips as reconstruction targets. Starting from a bidirectional backbone, we progressively adapt the model through In-context Pretraining for joint replacement, Conditional Streaming Adaptation for block-causal KV-cached generation, and Efficient Self-forcing DMD for mitigating exposure bias and reducing sampling from 30 to 3 denoising steps per block. Efficient Multi-LoRA Switching enables the three DMD roles to share a single frozen backbone. Feature-RoPE Decomposition keeps cached positions within the training range, supporting stable long-form inference. Experiments demonstrate strong audio-visual synchronization, competitive identity preservation, efficient streaming, and stable long-form generation.
