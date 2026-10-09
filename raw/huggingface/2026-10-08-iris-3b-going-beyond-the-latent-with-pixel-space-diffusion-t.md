---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.309307+05:30
arxiv_id: 2610.09450
url: https://huggingface.co/papers/2610.09450
arxiv_url: https://arxiv.org/abs/2610.09450
date: 2026-10-08
---

# Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning

Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a 256to512to1024 curriculum, after first ablating the prediction target and representation alignment at 256^2 to decide what to scale. We also convert a pretrained latent model, FLUX.2 Klein base 4B, to pixel space. We fine-tune both families for monocular depth estimation and for image restoration/super-resolution. We find no significant improvement from using a pixel-space generative prior. Fine-tuned for depth with one matched direct-regression recipe, Iris-3B is level with the latent FLUX.2 Klein and the converted pixel FLUX.2 Klein falls behind it, and on 4times DIV2K restoration neither pixel model beats a latent FLUX.2 Klein fine-tune, the converted one trailing it slightly. We document the recipes, the failure modes and the remaining confounds behind this negative result. Nevertheless, Iris-3B shows that pixel-space pretraining with the pixel-transformer (PiT) head of PixelDiT scales to 3B parameters and to text-to-image quality competitive with latent models, matching Qwen-Image on OneIG under the official evaluators at 1024^2. We release its weights and training code in the hope that they help pave the way for further work on pixel-space generation.
