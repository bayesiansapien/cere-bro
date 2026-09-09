---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.07108
url: https://huggingface.co/papers/2609.07108
arxiv_url: https://arxiv.org/abs/2609.07108
date: 2026-09-09
---

# Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training

Speculative decoding accelerates rollout generation, which dominates the cost of reinforcement learning (RL) post-training. Online co-training can further increase the draft's accuracy, yielding greater speedups. However, scaling this approach to co-training on large models with long contexts poses two obstacles: (1) branch attention is unsupported by standard causal context-parallel (CP) implementations, and (2) target features span across pipeline-parallel (PP) stages. We address both with an end-to-end system for large-scale online draft co-training. For CP, we extend packed, load-balanced zigzag ring attention by merging rank-local branch attention with causal main-sequence attention. For PP, TapChannel transports intermediate target features across stages via a separate path, leaving the pipeline schedule unaffected. Experiments demonstrate that co-trained drafts closely track the policy baseline while delivering substantial rollout and end-to-end speedups across model scales up to 122B. Our CP design achieves strong scaling at 256K tokens with significant memory savings over prior work, and our PP transport incurs modest overhead. Code can be found at https://github.com/NVIDIA-NeMo/RL/issues/3698.
