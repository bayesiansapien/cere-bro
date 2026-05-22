---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.20258
url: https://huggingface.co/papers/2605.20258
arxiv_url: https://arxiv.org/abs/2605.20258
date: 2026-05-21
---

# It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs

Contextual Integrity (CI) defines privacy not merely as keeping information hidden, but as governing information flows according to the norms of a given context. As large language models are increasingly deployed as personal agents handling sensitive workflows, adhering to CI becomes critical. However, even frontier models remain unreliable in making disclosure decisions, and existing mitigation strategies often degrade underlying task performance. To overcome this privacy-utility trade-off, we propose SELFCI, a complementary self-distillation framework that decouples information suppression from task resolution. SELFCI jointly optimizes two independent reverse KL divergences over distinct teacher distributions derived from feedback: one encourages preserving task-relevant information for utility, while the other enforces minimal and appropriate disclosure. This complementary formulation induces a Product-of-Experts (PoE) target, aligning the policy with the intersection of capability and privacy requirements. Empirical evaluations demonstrate that SELFCI, without relying on costly external supervision, consistently outperforms competitive baselines such as online reinforcement learning algorithms (e.g., GRPO). These trends further extend to out-of-domain settings involving agentic workflows and accumulated private context, suggesting that SELFCI provides a practical path toward CI alignment.
