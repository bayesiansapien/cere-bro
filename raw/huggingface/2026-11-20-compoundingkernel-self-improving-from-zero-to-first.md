---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.386293+00:00
arxiv_id: 2611.19230
url: https://huggingface.co/papers/2611.19230
arxiv_url: https://arxiv.org/abs/2611.19230
date: 2026-11-20
---

# CompoundingKernel: Self-Improving from Zero to First

We present CompoundingKernel, a self-improving agent system that writes GPU kernels by search. As of 2026-11-11, its generated kernels rank #1 on the public L1, L2 and Quantization boards of SOL-ExecBench (NVIDIA B200). They have held #1 on L1 since 2026-10-27, albeit a short loss on 2026-11-07. All 235 problems have a site-verified correct kernel; on the 209 public-board problems they are 4.40x faster than the benchmark's reference baseline. The search starts from zero: agents get each problem's PyTorch definition but no reference kernels or official scores. A per-problem archive outside the model holds every correct kernel and its lineage. An LLM controller reads it, picks a parent or a new design, and gives each parallel child agent one direction. Checks outside the model decide correctness. At equal wall time, it beat a coded UCB style tree on 35 of 38 problems by making 2.4x as many correct attempts. Over a thousand agents ran at once, and one warm restart fix raised their evaluation rate 3.6x. We find that the rate of reliable measurements, not the number of agents, limits how far such a search scales. Our code and kernels are available on URL.
