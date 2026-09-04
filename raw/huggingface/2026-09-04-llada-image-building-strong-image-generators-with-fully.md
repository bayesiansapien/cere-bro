---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.03796
url: https://huggingface.co/papers/2609.03796
arxiv_url: https://arxiv.org/abs/2609.03796
date: 2026-09-04
---

# LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes

We introduce LLaDA-Image, a unified framework that pairs a 6B Diffusion Transformer (DiT) trained from scratch with a frozen vision-language understanding module built on the LLaDA2.0-Mini diffusion language model backbone. Instead of relying heavily on paired image-text data from the beginning, we first build a strong visual generative prior through image-only pre-training and mid-training. The generation pipeline comprises 220M samples, 98 of which are real images. For efficient and scalable optimization, we use parameter-free RMSNorm throughout the DiT together with the Muon optimizer. The resulting unified model produces highly photorealistic images while accurately following fine-grained editing instructions. We further distill LLaDA-Image into LLaDA-Image-Turbo, enabling fast inference in 2-4 sampling steps. On Qwen-Image-Bench, LLaDA-Image achieves overall scores of 53.53 and 53.38 on the English and Chinese tracks, respectively, setting a new state-of-the-art among open-source models on both tracks. To support further research on capable and efficient generative models, we release our model weights, training code, and detailed recipes.
