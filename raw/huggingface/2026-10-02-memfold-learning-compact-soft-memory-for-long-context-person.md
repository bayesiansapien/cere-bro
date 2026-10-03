---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822786+00:00
arxiv_id: 2609.36435
url: https://huggingface.co/papers/2609.36435
arxiv_url: https://arxiv.org/abs/2609.36435
date: 2026-10-02
---

# MemFold: Learning Compact Soft Memory for Long-Context Personalization via On-Policy Optimization

An assistant that serves the same user over a long horizon has to answer from what that user has revealed: which preferences still hold, which were revised, and which constraints apply now. Retaining that information is not the same as acting on it, and the two are usually optimized as if they were. Keeping the information as text makes the reader's input grow with the retained history, while compressing it into a fixed number of latent vectors bounds the interface but is typically trained to reconstruct text or imitate reference answers, both of which are scored on sequences the reader never produced. We present MemFold, which optimizes a fixed-budget soft memory by the behavior it supports. A query-conditioned textual memory is compressed into K continuous vectors that form the reader's memory interface, and the reader is then trained on its own rollouts under two complementary signals: group-relative rewards for task outcomes, and confidence-gated on-policy distillation in which a frozen textual-memory teacher re-scores the student's sampled tokens under the textual memory. The teacher is never sampled from, so supervision stays on the student's current distribution and adds no autoregressive decoding; at inference it is removed entirely. Across three Qwen backbones, MemFold attains the highest accuracy we measure on PersonaMem-32K and PersonaMem-128K, with margins that widen at the longer history length, and transfers to PrefEval and LongMemEval without target-domain training. Ablations attribute most of the task gain to the reward term and a smaller additional gain to the teacher signal, and memory interventions show that the reader depends on the instance-specific content of its soft memory.
