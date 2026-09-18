---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.20744
url: https://huggingface.co/papers/2609.20744
arxiv_url: https://arxiv.org/abs/2609.20744
date: 2026-09-18
---

# Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation

Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for long-range video context. Its linear branch introduces Video Delta Attention (VDA), which updates memory once per frame by jointly incorporating its spatial tokens. Separate output projections and learnable gates calibrate the two branches, while a staged teacher-alignment recipe progressively introduces the new pathway into pretrained models. We instantiate VDN on MiniMax H3, applying the hybrid to video-to-video interactions while retaining Softmax for interactions involving text or audio. With eight-step distillation and an optimized SGLang serving stack, VDN-H3 completes DiT denoising for a 14.3-second, 768p video in 6.70 seconds on eight NVIDIA B200 GPUs, corresponding to a 14.5x speedup over the 50-step dense H3 baseline on the same GPU count.
