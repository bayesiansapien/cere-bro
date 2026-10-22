---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26216
url: https://huggingface.co/papers/2610.26216
arxiv_url: https://arxiv.org/abs/2610.26216
date: 2026-10-20
---

# RoAR-VAE: Improving Latent Diffusability through Robust Prediction

An effective visual tokenizer must preserve image fidelity while producing latents that downstream diffusion models can learn efficiently. Prior work improves latent diffusability through semantic alignment or joint tokenizer--diffusion training. Revisiting REPA-E, a representative approach, we find that removing its diffusion objective and dedicated generative blocks while retaining semantic prediction from corrupted latents yields comparable downstream generation performance under a matched setting. This observation motivates a general principle of robust prediction: generation-relevant information should remain recoverable from corrupted latents. We instantiate this principle with two complementary objectives. RobustAlign predicts pretrained semantic features from corrupted latents to preserve high-level structure, while RobustRecon reconstructs the clean image to retain fine-grained spatial and appearance information. Together, they form Robust Alignment and Reconstruction VAE (RoAR-VAE). Our analysis suggests that robust prediction improves diffusability by making useful information more accessible in high-variance latent directions, which diffusion models tend to learn earlier. Empirically, RoAR-VAE improves average generation benchmark performance by 2.19 points over the strongest baseline tokenizer under the same training budget, while improving small-text reconstruction accuracy by 16.93 percentage points over FLUX.1-VAE. These results demonstrate that RoAR-VAE achieves a favorable balance between reconstruction fidelity and downstream generative learnability.
