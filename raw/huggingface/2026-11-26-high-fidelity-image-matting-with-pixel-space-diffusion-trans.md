---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.904473+00:00
arxiv_id: 2611.34929
url: https://huggingface.co/papers/2611.34929
arxiv_url: https://arxiv.org/abs/2611.34929
date: 2026-11-26
---

# High-Fidelity Image Matting with Pixel-Space Diffusion Transformers

Diffusion models have shown strong potential for image matting by transferring generative priors learned from large-scale pretraining. However, existing approaches largely rely on latent diffusion models, whose compressed representations and VAE-based reconstruction introduce a mismatch with the high-frequency precision required for matting. We present PixelMatte, a framework that adapts pretrained pixel-space diffusion transformers for high-fidelity image matting. We show that strong image-conditioned matting capabilities can be acquired even from a pure text-to-image model without paired image-to-image pretraining. Our approach reuses the backbone's native patch embedding to jointly process the input image, trimap, and noisy alpha matte as spatially aligned tokens, enabling direct pixel-space prediction without additional condition encoders or adapters. With pixel-accurate synthetic supervision and real-image fine-tuning, PixelMatte predicts alpha mattes in a single forward pass. Two lightweight calibration modules, LayerShift and High-Pass Refiner, further improve regional opacity accuracy and boundary fidelity. Experiments across four benchmarks and two distinct pixel diffusion backbones demonstrate substantial improvements over existing methods, reducing SAD and gradient errors by 24-44% relative to RenderMatte on P3M-500-NP and AM-2K, while achieving competitive performance on AIM-500 and RenderMatte-2K. These results demonstrate the effectiveness of pixel-space generative priors for precision-sensitive image matting. Project page: https://white-yc.github.io/pixelmatte/.
