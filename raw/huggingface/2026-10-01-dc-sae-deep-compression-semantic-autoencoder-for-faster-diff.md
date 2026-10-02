---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.346508+05:30
arxiv_id: 2609.39222
url: https://huggingface.co/papers/2609.39222
arxiv_url: https://arxiv.org/abs/2609.39222
date: 2026-10-01
---

# DC-SAE: Deep Compression Semantic Autoencoder for Faster Diffusion Convergence

High-compression tokenizers are essential for scaling latent image generative models. However, aggressive compression creates a fundamental tradeoff between reconstruction fidelity and generation efficiency: high compression image encoder always increases the learning difficulty of diffusion training, resulting in slow model convergence. Recent representation autoencoders speed up the diffusion training by improving the latent feature's expressive capability by replacing VAE encoders with pretrained semantic encoders, yet they are typically limited to moderate compression and lose pixel-level details necessary for faithful reconstruction. To achieve both high compression and fast diffusion training, we propose DC-SAE, a Decoupled Compact Semantic Autoencoder designed for high-compression image generation with accelerated diffusion model convergence. DC-SAE consists of two key components: (1) a macro-level architecture design that leverages semantic encoders to enable higher compression ratios, and (2) a pixel-level encoder that preserves low-level details, ensuring high-fidelity image reconstruction. We empirically demonstrate that DC-SAE performs strongly on image generation tasks, achieving both compact latent representations and efficient training dynamics. Specifically, on the ImageNet dataset with 512 times 512 resolution, DC-SAE achieves 32times spatial compression, with 29.79 PSNR and 3.37 gFID, substantially outperforming the previous state-of-the-art high-compression tokenizer baselines DC-AE by 13.5% and 54.9% on PSNR and gFID, respectively, maintaining comparable throughput and faster diffusion model training convergence. Beyond class-conditional generation, a 1.6B-parameter DiT using DC-SAE achieves 0.84 on GenEval and 86.007 on DPG-Bench for text-to-image generation at 1024times1024 resolution.
