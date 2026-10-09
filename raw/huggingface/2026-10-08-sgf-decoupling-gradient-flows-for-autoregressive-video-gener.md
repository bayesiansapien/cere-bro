---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.302862+05:30
arxiv_id: 2610.10429
url: https://huggingface.co/papers/2610.10429
arxiv_url: https://arxiv.org/abs/2610.10429
date: 2026-10-08
---

# SGF+: Decoupling Gradient Flows for Autoregressive Video Generation

Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while preserving their interaction through causal attention. Both roles are jointly optimized using the original generation objective without auxiliary losses, with context writing supervised through its contribution to future predictions. This simple change improves visual quality and long-horizon consistency over the evaluated baselines in both framewise and chunkwise generation, without additional video training data or a longer training horizon. Trained on only 5s rollouts, SGF+ supports continuous generation for up to 24 hours without long-video fine-tuning. These results highlight role-specific parameterization as an effective design principle for high-quality autoregressive video generation and native long-horizon extrapolation.
