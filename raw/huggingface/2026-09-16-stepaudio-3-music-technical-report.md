---
source: farmer/huggingface
farmed: 2026-09-16T13:11:10.933414
arxiv_id: 2609.16034
url: https://huggingface.co/papers/2609.16034
arxiv_url: https://arxiv.org/abs/2609.16034
date: 2026-09-16
---

# StepAudio 3 Music Technical Report

We introduce StepAudio 3 Music, a large-scale, long-form music generation model that supports explicit musical planning and open-domain text-controlled generation. The StepAudio Music Tokenizer represents audio as a 50-Hz stream from a 65536-entry single codebook, using semantically informed self-supervised and multi-task training to preserve musical structure and reconstruction-relevant information. A flow-matching diffusion Transformer (DiT) predicts continuous StepAudio VAE latents, which our VAE decoder converts into 48-kHz audio. This discrete-continuous design is guided by comparisons of single-codebook VQ, Semantic and Acoustic RVQ, and different DiT configurations. For explicit planning, a Mixture-of-Experts autoregressive model uses ABC notation to produce an intermediate arrangement plan (ABC-CoT) before predicting music tokens, making harmony, rhythm, and melodic structure part of the generation context. A progressive training curriculum and supervised fine-tuning support song and instrumental generation, accompaniment generation from dry vocals, and cover-song synthesis for up to 5 minutes and 30 seconds. With reinforcement learning via direct preference optimization (DPO), the final model achieves the highest AudioBox Content Enjoyment, Content Usefulness, and Production Quality scores and the highest MuQ-MuLan similarity among the evaluated systems, with competitive SongBench results. On the preliminary Artificial Analysis Music Arena Vocals leaderboard, it obtains a Quality Elo of 1105, behind only Suno V5.5 and Mureka and ahead of Suno V5, MiniMax models, and other systems. Audio demonstrations are available at https://stepaudiollm.github.io/step-audio-3-music.
