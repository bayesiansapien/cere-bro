---
source: farmer/huggingface
farmed: 2026-08-09T07:10:01.249497+00:00
arxiv_id: 2608.05798
url: https://huggingface.co/papers/2608.05798
arxiv_url: https://arxiv.org/abs/2608.05798
date: 2026-08-09
---

# KVAE: Family of Tokenizers for Multimodal Generative Models

Latent diffusion modeling (LDM), a prominent paradigm, utilizes tokenizers to map input signal to compressed representation. This dependency positions tokenizer as an integral part of generation process itself, since it affects learning speed, quality of synthesized samples and lay foundation for later applications. This report presents series of KVAE tokenizers for audio, image and video, all designed for subsequent text-conditioned generation: KVAE-Audio, a continuous full-band 48 kHz tokenizer with a 50 Hz latent of 64 channels; KVAE-3D -- two causal video tokenizers for 4x16x16 and 4x8x8 compression; KVAE-2D, an image model, compressing input by factor of 8 with 32 channels. We demonstrate that reconstruction (PSNR, LPIPS, PESQ, etc.) and generation results on objective (Frechet Distance, CLIP score, CLAP score, etc.) and subjective (side-by-side evaluation) metrics matches or surpasses frontier opensource tokenizers, such as VAEs from Wan-2.2, HunyuanVideo-1.5, FLUX.2, MovieGen, StableAudio and MMAudio. Considering difficulty of development, we share with community training details, model selection method and ablation on design choices. The code is publicly available at https://github.com/kandinskylab/kvae and https://github.com/kandinskylab/kvae-audio.
