---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13356
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13356
published: 2026-04-16
authors: Shi Feng, Hanlin Zhang, Fan Nie
---

# Peer-Predictive Self-Training for Language Model Reasoning

**arXiv:** https://arxiv.org/abs/2604.13356
**Authors:** Shi Feng, Hanlin Zhang, Fan Nie

## Abstract

arXiv:2604.13356v1 Announce Type: cross  Abstract: Mechanisms for continued self-improvement of language models without external supervision remain an open challenge. We propose Peer-Predictive Self-Training (PST), a label-free fine-tuning framework in which multiple language models improve collaboratively by leveraging a cross-model aggregated response as an internal training signal. Given a prompt question, the models generate responses sequentially; the final aggregated answer, often more reliable than individual responses in practice, serves as an internal target for learning. We measure how informative each intermediate response is about the aggregate using pointwise mutual information (PMI), and use this signal to scale self-training updates. Responses already aligned with the aggregate are updated less, while less informative or misaligned responses are updated more. On mathematical reasoning benchmarks (SimulEq, Math500, and MultiArith), PST improves exact-match accuracy by 2.2 to 4.3 percentage points across Gemma-2-2B, LLaMA-3.2-1B, and Qwen-2.5-1.5B, and reduces the average generator-verifier gap (GV-Gap) by 26 to 40 percent, while requiring no external supervision or teacher-student hierarchy and relying solely on cross-model interactions. These results suggest that cross-model generations and peer-predictive feedback can serve as an effective approach for self-supervised training.
