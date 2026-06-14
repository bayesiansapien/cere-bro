---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.12282
url: https://huggingface.co/papers/2606.12282
arxiv_url: https://arxiv.org/abs/2606.12282
date: 2026-06-14
---

# PianoKontext: Expressive Performance Rendering from Deadpan Context

Expressive performance rendering (EPR) aims to generate realistic performances constrained on sequences of notes. However, flow matching audio editing models manipulate only synchronized music samples of the same duration, limiting their understanding of expressive timing. We introduce PianoKontext, a flow matching rendering model for classical piano music that generates variable-length performances in the latent space of a pretrained Music2Latent model. We synthesize MIDI scores into deadpan audio and employ Dynamic Time Warping (DTW) in the latent space to construct paired data for training. The aligned embeddings are concatenated in DiT blocks, allowing for a simple and effective learning of the dependencies between the score and performances. Audio samples are available at our demo page: https://realfolkcode.github.io/pianokontext_demo/.
