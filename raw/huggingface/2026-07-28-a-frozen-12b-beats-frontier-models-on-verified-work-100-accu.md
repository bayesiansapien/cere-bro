---
source: farmer/huggingface
farmed: 2026-07-28T09:26:01.339781
arxiv_id: 2607.23806
url: https://huggingface.co/papers/2607.23806
arxiv_url: https://arxiv.org/abs/2607.23806
date: 2026-07-28
---

# A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever

Improving a language model today means retraining it: enormous compute, a new opaque model each cycle, non-deterministic output. We take the opposite path: the model stays frozen, and a persistent memory of verified solutions grows beside it. Once a problem family is solved and has passed an independent verification step that never consults the answer key, every new instance of that family is answered at zero generation tokens, bit-exact, deterministically. Across 180 fresh instances spanning nine problem families, four architectures from four vendors - dense and mixture-of-experts - each score 180/180 at zero generation tokens per answer: execution-bound capability decoupled from parameter scaling. A negative control attributes the capability fully to the memory: emptied, it solves nothing. The same verify-before-store contract holds for open-ended reasoning: 88/88 consistency-gated acceptances across all four models, machine-checked formal proof, and reasoning-method transfer at 77/80. Memory selection takes 1.4 microseconds; a full reuse completes in 6-23 ms at 36 mWh. Approximate similarity retrieval selects the wrong item 94.3% of the time on a 4,500-item verified store where exact addressing makes zero errors. The store also serves as working context at a scale no shipped engine matches: a 6,000,000-token movable window on a single 46 GB GPU at flat memory, where vLLM stops at 30,399 tokens and SGLang silently truncates past 32,000. On published benchmarks, frontier models remain far ahead of any 12B at raw from-scratch reasoning; on everything this system has solved and verified, the comparison inverts: a frontier API call pays a fresh generation pass on every query, forever, while verified reuse costs zero tokens and returns the identical bits every time. A public testbench with free, rate-limited access accompanies this report: https://corbenic-galahad-bench.hf.space
