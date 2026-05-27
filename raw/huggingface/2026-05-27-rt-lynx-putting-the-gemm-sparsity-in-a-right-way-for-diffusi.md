---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.26632
url: https://huggingface.co/papers/2605.26632
arxiv_url: https://arxiv.org/abs/2605.26632
date: 2026-05-27
upvotes: 1
---

# RT-Lynx: Putting the GEMM Sparsity In a Right Way for Diffusion Models

Diffusion Transformers (DiT) achieve strong performance in image generation but incur substantial inference costs. While prior work has reduced this cost via quantization and distillation, semi-structured sparsity, which can nearly halve FLOPs, remains underexplored. A key reason is that most existing approaches focus on weight sparsification, and pruning 50% of the weights can remove critical model capacity and degrade generation quality. Our study, however, shows that DiT activations are intrinsically sparse and significantly more robust to N:M semi-structured sparsification than weights. Motivated by this observation, we advocate a paradigm shift from weight sparsification to activation sparsification. We propose RT-Lynx, which applies N:M sparsification to activations and incorporates error-compensation techniques to mitigate accuracy loss. We further implement highly optimized CUDA kernels tailored to this setting, achieving up to a 1.55x speedup on average in linear layers. Extensive experiments across multiple diffusion models demonstrate that our method preserves the generation quality of the original models while substantially accelerating inference.
