---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935473+00:00
arxiv_id: 2609.31009
url: https://huggingface.co/papers/2609.31009
arxiv_url: https://arxiv.org/abs/2609.31009
date: 2026-09-29
---

# G^2PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation

Post-training quantization (PTQ) is a practical approach to reducing the memory and computational footprint of large language models (LLMs) without retraining. GPTQ-based methods have become the de facto standard, yet they suffer from two complementary limitations. Methods with local, layer-wise objectives lack global supervision; while methods with global objectives fix their Hessian estimates at the start and ignore first-order gradients, so their guidance grows stale as quantization proceeds. This paper presents G^2PTQ, a unified PTQ framework with Generalized Gradient Compensation that integrates both first- and second-order information under a globally supervised, block-wise optimization objective. By refreshing gradient and Hessian estimates before quantizing each Transformer block, G^2PTQ avoids the staleness of prior global methods. Furthermore, to stabilize the exact first-order compensation, we introduce a trust-region scaling mechanism that dynamically bounds the gradient step to prevent exploding weight updates. Finally, we derive efficient implementations for block-wise Hessian approximation and exact gradient compensation. Experimental results on various model families and bit-widths demonstrate that G^2PTQ enables better alignment with the full-precision model, outperforming state-of-the-art baselines. Code is available at: https://github.com/G2PTQ/G2PTQ.
