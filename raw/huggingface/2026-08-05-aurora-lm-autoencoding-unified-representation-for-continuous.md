---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.02602
url: https://huggingface.co/papers/2608.02602
arxiv_url: https://arxiv.org/abs/2608.02602
date: 2026-08-05
---

# AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling

Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity, decodable text latent and design the diffusion model to learn its distribution directly.
  We introduce AURORA-LM, a continuous-latent diffusion language model that separates the construction of a decodable text representation from the modeling of its distribution. A Query-based Encoder-Decoder organizes text into a high-capacity, prefix-aligned latent sequence, and a Block-causal Diffusion Transformer learns its distribution through flow matching, generating blocks left to right while denoising positions within each block in parallel. Because such a latent is harder for diffusion to model, AURORA-LM restricts only the noisy-input pathway while retaining the full clean-latent prediction target, accommodating full-width latents without reducing decoder-facing capacity. We further calibrate the noise-level distribution to the latent width, and introduce self-trajectory consistency to bridge independently sampled training noise and iterative denoising at inference.
  AURORA-LM achieves the strongest performance among evaluated continuous and diffusion-based language models on OpenWebText free generation and XSum summarization. Scaling to 1B parameters with about 1500 EFLOPs of total compute yields further gains, surpassing a larger publicly released latent-diffusion language model under a matched evaluation protocol. All experiments are conducted on Ascend NPUs.
