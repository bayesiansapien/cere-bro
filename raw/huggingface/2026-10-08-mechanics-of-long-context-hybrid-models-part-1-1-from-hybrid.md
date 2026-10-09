---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.304213+05:30
arxiv_id: 2610.10114
url: https://huggingface.co/papers/2610.10114
arxiv_url: https://arxiv.org/abs/2610.10114
date: 2026-10-08
---

# Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position

The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we begin with hybrids of full attention and either sliding-window attention (SWA) or gated variants of linear attention (LA), represented by GLA and GDN. We first observe a Seesaw Effect in Context Extension: LA hybrids benefit more from long-context continual pretraining, whereas SWA hybrids perform better under length extrapolation. We attribute this behavior to differences in the positional inductive biases induced by these attention mechanisms. We find that SWA hybrids suffer from a Short-Context Learning Trap, Short-Window Weariness, and Long-Window Laziness, and require extended windows to enhance performance in continual long-context pretraining. For LA hybrids, we summarize the Matthew Effect of Hybrid Position Extrapolation and propose Sliding-Window Linear Attention, achieving 16times training-free length extrapolation while maintaining 100\% accuracy on NIAH-SK1 in 64k context length.
