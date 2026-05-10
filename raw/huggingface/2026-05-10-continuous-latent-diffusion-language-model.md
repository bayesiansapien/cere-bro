---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06548
url: https://huggingface.co/papers/2605.06548
arxiv_url: https://arxiv.org/abs/2605.06548
date: 2026-05-10
---

# Continuous Latent Diffusion Language Model

Large language models have achieved remarkable success under the autoregressive paradigm, yet high-quality text generation need not be tied to a fixed left-to-right order. We propose Cola DLM, a hierarchical latent diffusion language model that frames text generation through hierarchical information decomposition. Cola DLM first learns a stable text-to-latent mapping with a Text VAE, then models a global semantic prior in continuous latent space with a block-causal DiT, and finally generates text through conditional decoding. Through experiments spanning 4 research questions, 8 benchmarks, strictly matched ~2B-parameter autoregressive and LLaDA baselines, and scaling curves up to about 2000 EFLOPs, we identify an effective overall configuration of Cola DLM and verify its strong scaling behavior for text generation.
