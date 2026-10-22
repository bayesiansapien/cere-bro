---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24766
url: https://huggingface.co/papers/2610.24766
arxiv_url: https://arxiv.org/abs/2610.24766
date: 2026-10-20
---

# ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction

Existing Multi-token prediction (MTP) methods are auxiliary by design: the multi-horizon loss mostly trains modules attached to the backbone, and each added horizon costs another module and another pass. We propose Efficient Causal Self-Recursion (ECHO), which removes both costs. The backbone's own final layer predicts every horizon, so the supervision lands on the parameters that generate the next token, and Dynamic Depth Sampling (DDS) keeps deeper horizons affordable by drawing the training depth with probabilities that decay along depth. Future prediction thus becomes part of the autoregressive objective rather than a task attached to it, and the gains follow on both sides of it. In pretraining, added depth converts into downstream accuracy where auxiliary modules saturate, concentrating on reasoning and code at half the MTP training overhead of training every depth. At inference, the pretrained model is its own drafter: it drafts beyond the depth it was trained for, and keeps its draft-target alignment on the open-ended, high-entropy generation where post-hoc drafters lose theirs. The advantage survives a doubled token budget, a repeated pretraining run, and supervised finetuning.
