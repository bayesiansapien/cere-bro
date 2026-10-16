---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.224443+05:30
arxiv_id: 2610.14448
url: https://huggingface.co/papers/2610.14448
arxiv_url: https://arxiv.org/abs/2610.14448
date: 2026-10-15
---

# KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization

Asynchronous rollout improves the efficiency of reinforcement learning with verifiable rewards (RLVR) by reducing under-utilization during long-tail generation. Sustained concurrency also concentrates context processing into fewer decode steps, increasing the KV workload per step. We characterize this KV concentration and find that KV cache quantization delivers substantially greater acceleration than weight-only and weight-activation quantization in our matched-workload comparisons. However, INT4 KV rollout can degrade learning even with token-level truncated importance sampling (TIS). We propose KV4-RL, which combines calibration-free INT4 KV quantization with selective INT8 protection of attention sinks and recent context. Protecting a bounded number of positions reduces sampler mismatch while retaining most of the speedup from INT4. Across 400 iterations of Qwen3-8B-Base GRPO training, KV4-RL achieves 1.80times cumulative rollout speedup and 1.27times cumulative full-iteration speedup over BF16 rollout, reaching 1.97times rollout speedup over the final 50 iterations. Under a common BF16 evaluator, its final six-benchmark mean accuracy is within 0.5 percentage points of BF16-rollout training for both Qwen3-4B-Base and Qwen3-8B-Base.
