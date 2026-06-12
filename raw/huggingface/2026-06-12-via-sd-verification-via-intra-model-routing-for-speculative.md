---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.12243
url: https://huggingface.co/papers/2606.12243
arxiv_url: https://arxiv.org/abs/2606.12243
date: 2026-06-12
---

# VIA-SD: Verification via Intra-Model Routing for Speculative Decoding

Speculative decoding (SD) addresses the high inference costs of LLMs by having lightweight drafters generate candidates for large verifiers to validate in parallel. Existing draft-verify methods use binary decisions: accept or fully recompute. Yet we find that many rejected tokens can be verified correctly by a slim submodel derived from the full verifier via intra-model routing, instead of the full verifier. This motivates our slim-verifier to handle tokens requiring moderate verification resources, reducing expensive large-model calls. We propose Verification via Intra-Model Routing for Speculative Decoding (VIA-SD), a multi-tier framework using a routed slim-verifier. Draft tokens are processed hierarchically: direct acceptance for high-confidence cases, slim-verifier regeneration for medium-confidence cases, and full-model verification for uncertain cases. Across four representative tasks and multiple model families, VIA-SD reduces rejection rates by 0.10-0.22 and delivers 10-20% speedups over strong SD baselines, while achieving 2.5-3x acceleration over non-drafting decoding. Moreover, VIA-SD is compatible with existing SD frameworks without modifying their training procedures. Our results suggest multi-tier SD as a general paradigm for scalable and efficient LLM inference. Project page: https://zju-xyc.github.io/VIA-SD-Project-Page/
