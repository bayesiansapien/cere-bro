---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.927856+05:30
arxiv_id: 2601.15351
url: https://huggingface.co/papers/2601.15351
arxiv_url: https://arxiv.org/abs/2601.15351
date: 2026-10-29
---

# OmniSpectra: A Unified Foundation Model for Universal Spectra Representation Learning

Standard sequence models encode position by token rank rather than physical coordinate, typically forcing practitioners to destructively resample continuous physical signals such as spectra observed across heterogeneous instruments. We identify this coordinate mismatch as a structural limitation in cross-instrument representation learning, and propose OmniSpectra, a wavelength-native foundation model for spectral representation learning: a continuous-coordinate masked autoencoder that discards the integer pixel indexing of sequence modeling. Mapping physical coordinates to a logarithmic basis turns the multiplicative scaling induced by cosmological redshift into a uniform additive shift. In continuous rotary position embeddings, this shared shift cancels from relative token distances rather than producing grid-dependent positional distortion. We further counter the spectral bias inherent to implicit neural decoders with a physics-grounded, resolution-gated Fourier decoder that provides anti-aliasing. Pretrained on eight surveys and benchmarked against seven baselines, our model reaches state-of-the-art performance with only 12.2M parameters while outperforming substantially larger models, indicating that encoding physical structure can substitute for parameter scale.
