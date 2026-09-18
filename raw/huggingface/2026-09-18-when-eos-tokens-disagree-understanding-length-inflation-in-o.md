---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.20511
url: https://huggingface.co/papers/2609.20511
arxiv_url: https://arxiv.org/abs/2609.20511
date: 2026-09-18
---

# When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation

We study length inflation in on-policy distillation (OPD), where student responses can become excessively long and even exhaust the generation budget. We identify termination-token mismatch between base students and post-trained teachers as an important source of this behavior. Across Qwen3, Llama, and Gemma, the two models can place their stopping probability on different EOS tokens, even when their declared stopping sets are identical. This mismatch can suppress the student's preferred termination action without reliably transferring the teacher-preferred alternative. We show that aligning the decoding stopping set alone is insufficient, while treating functionally equivalent EOS tokens as a shared semantic stopping action substantially mitigates mismatch-induced length inflation across all three model families. To further understand how termination behavior evolves over training, we study OPD across different K2-Horizon training stages. This stage-wise analysis shows that termination preferences can shift substantially during training, while also revealing a distinct length inflation late in the OPD run that persists beyond termination alignment. Together, these results identify termination mismatch as an important, but not exhaustive, source of OPD length dynamics. We release an implementation incorporating the proposed termination-handling corrections.
