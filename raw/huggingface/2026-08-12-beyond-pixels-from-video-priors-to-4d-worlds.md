---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.10744
url: https://huggingface.co/papers/2608.10744
arxiv_url: https://arxiv.org/abs/2608.10744
date: 2026-08-12
---

# Beyond Pixels: From Video Priors to 4D Worlds

4D generation synthesizes dynamic 3D scenes from conditions such as text or images. Existing methods either reconstruct generated RGB videos with a separate 4D model or adapt a particular video generator to predict geometry directly. The former suffers from distribution mismatch and error propagation, whereas the latter ties 4D prediction to a specific generator and may require retraining when the generator or conditioning regime changes. We ask whether the final denoised latents of video models that share a variational autoencoder (VAE) can instead provide a reusable interface to explicit 4D prediction. Building on this insight, we introduce direct latent-to-4D generation and instantiate it as Latent-to-4D, which bypasses RGB by aligning a video latent with the token grid of a pretrained 4D decoder and refining it through frame-wise and global spatiotemporal attention. Trained on roughly 1K existing reconstruction clips, a single checkpoint transfers unchanged across multiple video diffusion transformers within the same VAE family. On Text4D-200 and I4D-200, Latent-to-4D surpasses matched same-latent Wan+4RC cascades in projection-based DINO-F1 by 2.88--3.45 and 5.81 points, respectively, while also being preferred by human raters for geometry, temporal stability, and overall quality.
