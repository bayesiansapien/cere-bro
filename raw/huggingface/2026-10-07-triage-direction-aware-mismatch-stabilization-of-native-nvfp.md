---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07043
url: https://huggingface.co/papers/2610.07043
arxiv_url: https://arxiv.org/abs/2610.07043
date: 2026-10-07
---

# TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning

Low-precision execution can substantially accelerate reinforcement learning (RL) for large language models, but discrepancies between learner and sampler execution can destabilize policy optimization. In this paper, we characterize the interaction between mismatch and the policy-gradient direction, distinguishing locally amplifying from contracting update contributions that mismatch magnitude alone cannot identify. In native NVFP4 runs, we observe an early imbalance between the two amplifying regions, favoring negative-advantage, negative-gap updates. Their tail tokens become concentrated in a small fraction of response segments before mismatch spreads globally. Motivated by these findings, we introduce TRIAGE, a direction-aware stabilization method that uses segment-level diagnosis to selectively rebalance policy-gradient updates and applies bounded repair to residual severe mismatch. TRIAGE modifies the optimization objective while retaining native NVFP4 weight-and activation 4-bit (W4A4) forward execution on both the sampler and learner. Experiments on Qwen3-4B and Qwen3-30B-A3B show stable optimization throughout the evaluated training horizon and achieve full precision level performance across five mathematical reasoning benchmarks, while native NVFP4 with TRIAGE provides up to 2.3x higher rollout throughput than BF16.
