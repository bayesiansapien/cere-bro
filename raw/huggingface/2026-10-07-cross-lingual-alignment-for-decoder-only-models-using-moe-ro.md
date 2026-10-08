---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.01921
url: https://huggingface.co/papers/2610.01921
arxiv_url: https://arxiv.org/abs/2610.01921
date: 2026-10-07
---

# Cross-Lingual Alignment for Decoder-Only Models using MoE Routers

Cross-lingual contrastive learning has been a core component of multilingual encoder training, but the ability to explicitly align representations is not possible in decoder-only LLMs because of varying multilingual tokenization. However, a growing amount of research suggests that even in LLMs, higher cross-lingual representational alignment leads to improved cross-lingual transfer. In this paper, we propose a novel approach to reimagine cross-lingual contrastive learning given the architectural constraints of modern LLMs. Rather than applying an auxiliary alignment loss on hidden states, we propose using the outputs of the mixture-of-experts (MoE) routers as the target for alignment. Router outputs lend themselves better to pooling over many tokens, enabling more reliable cross-lingual comparisons at the sequence-level. Controlled continual pre-training experiments on four open-source MoEs show that incorporating this routing loss also aligns the underlying hidden representations across languages. Most importantly, this loss improves multilingual performance on our diverse evaluation suite, demonstrating the potential of cross-lingual MoE router alignment.
