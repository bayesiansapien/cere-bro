---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.162338+00:00
arxiv_id: 2610.39293
url: https://huggingface.co/papers/2610.39293
arxiv_url: https://arxiv.org/abs/2610.39293
date: 2026-10-30
---

# Unlocking Any-Order Generation in Pretrained Autoregressive Image Models

Autoregressive (AR) image generators are powerful in principle but inflexible in practice: training with a fixed raster-scan order hardcodes a single factorization of the image distribution into the model, leaving it unable to inpaint, outpaint, or edit at inference time. Existing solutions, including the modern discrete-diffusion family, train from scratch on a mixture of token orderings, paying roughly 3x the compute of standard raster-scan training; discrete diffusion further sacrifices compatibility with the AR inference ecosystem (KV caching, vLLM) by construction. We argue that this cost is unnecessary. A pretrained raster-scan AR model has already learned the joint distribution over image tokens; what it lacks is not knowledge but the ability to express that knowledge through non-sequential conditional pathways. We propose a recipe for adapting pretrained raster-scan models into any-order generators using two components: future-aware positional embeddings that resolve a target-position identifiability problem at negligible overhead, and an ordering curriculum that traces a stable optimization path from the pretrained solution to a good any-order basin. Applied to four base models across two architectures and two scales (LlamaGen-L/XL, RAR-L/XL), the recipe substantially outperforms MaskGIT on ImageNet inpainting (FID 6.21 vs. 10.44) and outpainting, is competitive with MAR-L, trades a 1.2-1.9 increase in class-conditional FID for this flexibility, and costs 13-33% additional compute beyond pretraining, while leaving the standard AR inference stack untouched. Inpainting, outpainting, and editing, our results suggest, need not be added to autoregressive image models. They can be unlocked from the ones that exist. Code is available at https://github.com/Ordered-AR/unlockedadaptation.
