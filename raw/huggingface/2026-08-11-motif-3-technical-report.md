---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.09119
url: https://huggingface.co/papers/2608.09119
arxiv_url: https://arxiv.org/abs/2608.09119
date: 2026-08-11
---

# Motif 3: Technical Report

We introduce Motif 3, a decoder-only Mixture-of-Experts language model with 314 billion total parameters and 13.2 billion activated per token. Each sparse MoE layer contains 384 routed experts, with eight selected per token. This fine-grained sparsity provides substantial expert capacity while limiting computation. Motif 3 is built around Grouped Differential Latent Attention (GDLA), which integrates grouped differential attention with the compressed key-value representation of Multi-head Latent Attention. The architecture further incorporates modified manifold-constrained hyper-connections, Expert Specific PolyNorm activations, and multi-token prediction to improve optimization stability, expert specialization, and inference efficiency. We pretrain Motif 3 on approximately 12.5 trillion tokens spanning web documents, STEM, code, mathematics, multilingual content, and domain-specialized corpora. Expert-balancing and numerical-stabilization techniques support stable training at scale, while selective MXFP8 computation and communication, memory-efficient fused kernels, and window-aware context parallelism enable training with context lengths up to 256K tokens. Our post-training pipeline combines general supervised fine-tuning, six specialist teachers trained with reinforcement learning, a software-engineering teacher trained with supervised fine-tuning, and Multi-teacher On-Policy Distillation. The resulting unified model consolidates complementary capabilities in reasoning, coding, tool use, professional work, long-context understanding, calibrated abstention, and instruction following. Across a broad evaluation suite, Motif 3 demonstrates competitive performance against leading open weight models, including strong results on long-horizon agentic tasks, mathematical reasoning, scientific knowledge, and hallucination-sensitive evaluation.
