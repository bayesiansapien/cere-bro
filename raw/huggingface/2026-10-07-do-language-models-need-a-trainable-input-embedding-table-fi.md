---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.04002
url: https://huggingface.co/papers/2610.04002
arxiv_url: https://arxiv.org/abs/2610.04002
date: 2026-10-07
---

# Do Language Models Need a Trainable Input Embedding Table? Fixed Minimal Token Codes at 1.7B-Class Scale

A trainable input embedding table assigns each vocabulary item an independently adjustable vector. We investigate whether this token-specific parameterization is required for substantial language-modeling capability, or whether a shared Transformer can learn from fixed token identities. We compare three decoder-only language models trained from scratch with the same tokenizer, contextual backbone, untied output-head architecture, and training recipe, with a target budget of 100 billion prediction tokens per model. Their input interfaces are a learned table, canonical 16-bit token-ID codes, and one fixed invertible recoding over GF(2). The fixed codes are repeated to model width without an additional trainable input projection. Both fixed-code models acquire substantial capabilities: canonical codes achieve 52.40\% HellaSwag normalized accuracy, 70.51\% PIQA accuracy, and 42.75\% LAMBADA accuracy. The learned-input control performs better on several evaluations, including HellaSwag and LAMBADA, so these results establish viability rather than performance parity. The fixed interfaces remove 100.7 million trainable parameters, yielding 1.711B-parameter models, but parameter reduction is not the central result. These single-run experiments distinguish architectural necessity from empirical utility: independently trainable token-specific input vectors are not required for the observed capabilities. A fixed identity interface also provides a controlled setting for studying representation learning downstream of an immutable input, without establishing where particular capabilities are localized.
