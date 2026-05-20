---
source: farmer/huggingface
farmed: 2026-05-20T09:55:05.319379+00:00
arxiv_id: 2605.20104
url: https://huggingface.co/papers/2605.20104
arxiv_url: https://arxiv.org/abs/2605.20104
date: 2026-05-20
---

# Draft Less, Retrieve More: Hybrid Tree Construction for Speculative Decoding

Speculative decoding (SD) accelerates large language model inference by leveraging a draft-then-verify paradigm. To maximize the acceptance rate, recent methods construct expansive draft trees, which unfortunately incur severe VRAM bandwidth and computational overheads that bottleneck end-to-end speedups. While dynamic-depth pruning can reduce this latency by removing marginal branches, it also discards potentially valid candidates, preventing the acceptance rate from reaching the upper bound of dense trees. In this paper, we identify a critical opportunity in resource allocation: the transition from dense to pruned drafting frees up significant computational budget. To break this Pareto tradeoff, we introduce Graft, a compensation framework that couples pruning and retrieval as mutually reinforcing operations. Pruning supplies sufficient budget for retrieval, while retrieval compensates for pruning-induced coverage loss and recovers accepted length. By employing a sequential `prune-then-graft&#39; mechanism, Graft attaches highly predictive retrieved tokens into positions opened by pruning, filling the topological gaps with near-zero overhead. Graft is entirely training-free and lossless. Comprehensive evaluations show that Graft establishes a new Pareto frontier across practical deployment settings, including short-context generation, long-context generation, and large-scale models. On short-context benchmarks, it achieves up to 5.41$\times$ speedup and improves average speedup over EAGLE-3 by up to 21.8% on the large-scale Qwen3-235B. We also provide a preliminary exploration of applying Graft to the DFlash-style block drafting paradigm, offering initial evidence and insights for extending grafting beyond autoregressive draft trees.
