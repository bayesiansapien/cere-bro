---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.506154+00:00
arxiv_id: 2610.18010
url: https://huggingface.co/papers/2610.18010
arxiv_url: https://arxiv.org/abs/2610.18010
date: 2026-10-14
---

# Fish Audio Drama 3 Technical Report

We introduce Fish Audio Drama 3, an open-source speech generation model that turns text into directed performances, built on a 35B-parameter mixture-of-experts backbone that activates 3B parameters per token. It clones voices from multiple references, follows natural-language direction, revises a take when the next turn gives a note, voices multi-character scenes, edits existing speech by infilling, and synthesizes long-form and streaming audio. Multi-turn revision, scene dubbing, editing by infilling, and streaming text input are new in Drama 3, all in one model. Drama 3 pairs the hybrid linear-attention backbone with a new codebook multi-token-prediction audio decoder that predicts the acoustic codebooks of each frame in dedicated layers that attend over the entire sequence. The model is trained with a three-stage pre-training recipe, instruction fine-tuning, and large-batch reinforcement learning whose only reward is a single learned model of human preference. Its inference engine decodes a single stream at 271 frames per second on one H200, against 177 for Fish Audio S2, although Drama 3 has more than seven times as many parameters. The model weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face (https://huggingface.co/fishaudio/drama-3), and inference is available through SGLang-Omni (https://github.com/sgl-project/sglang-omni). We highly encourage readers to visit https://fish.audio to direct their own performances.
