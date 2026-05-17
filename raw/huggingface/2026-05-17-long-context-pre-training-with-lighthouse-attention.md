---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.06554"
url: "https://huggingface.co/papers/2605.06554"
arxiv_url: "https://arxiv.org/abs/2605.06554"
date: 2026-05-17
---

# Long Context Pre-Training with Lighthouse Attention

Training causal transformers at extreme sequence lengths is bottlenecked by the quadratic time and memory of scaled dot-product attention (SDPA). In this work, we propose Lighthouse Attention, a training-only symmetrical selection-based hierarchical attention algorithm that wraps around ordinary SDPA and can be easily removed towards the end of the training. Our hierarchical selection is also gradient-free, which exempts us from dealing with a complicated and potentially inefficient backward pass kernel. Our contribution is three-fold: (i) A subquadratic hierarchical pre- and post-processing step that does adaptive compression and decompression of the sequence. (ii) A symmetrical compression strategy that pools queries, keys and values at the same time, while preserving left-to-right causality, which greatly improves parallelism. (iii) A two stage training approach which we pre-train for the majority of the time with Lighthouse Attention and recover a full attention model at the end with a short training. We run preliminary small scale LLM pre-training experiments that show the effectiveness of our method compared to full attention training with all other settings matched, where we achieve a faster total training time and lower final loss after the recovery phase.
