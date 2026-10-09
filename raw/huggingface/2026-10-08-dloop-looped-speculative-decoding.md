---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.308186+05:30
arxiv_id: 2610.07659
url: https://huggingface.co/papers/2610.07659
arxiv_url: https://arxiv.org/abs/2610.07659
date: 2026-10-08
---

# DLoop: Looped Speculative Decoding

Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary target-model forward passes even when drafting could have continued. Adaptive draft length methods decide during decoding how many draft tokens precede a verification, but they raise the speedup only for autoregressive draft models. For a parallel draft model, drafting further requires target-model hidden states for draft tokens that have not been verified. We propose DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. DLoop continues drafting while the draft model remains confident and verifies all accumulated draft tokens together. Loop-aware training keeps the draft model reliable in the additional drafting stages by exposing it to its own hidden states for unverified draft tokens. By spending additional draft-model forward passes, DLoop reduces the number of target-model forward passes required for verification. Across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules, DLoop improves the wall-clock speedup by 5 to 41 percent while preserving lossless decoding. Code will be available at https://github.com/naver-ai/DLoop.
