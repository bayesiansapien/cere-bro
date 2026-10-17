---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.19397
url: https://huggingface.co/papers/2610.19397
arxiv_url: https://arxiv.org/abs/2610.19397
date: 2026-10-16
---

# SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic Reinforcement Learning

Long-horizon agentic RL is constrained by the futures visited by the current policy. When rollouts fail to reach useful behaviors, improved credit assignment cannot provide supervision for states and actions that were never encountered. On-policy distillation (OPD) introduces teacher guidance on policy-induced states, and recent multi-turn variants improve how this guidance is scheduled, replayed, refined, or validated. However, they do not directly use the oracle-controlled future itself as the training trajectory. We introduce State-Rooted Executable Rollout Optimization (SERO), which augments on-policy agentic RL with executable oracle continuations. SERO restores a state actually reached by the current policy and lets a training-only oracle continue interacting with the real environment, making the downstream observations and oracle actions themselves available for learning. It then applies policy-reachability weighting, which weights each oracle step by the frozen behavior policy's compatibility with the preceding oracle actions. This allows deeper supervision to become effective as the policy becomes more compatible with the oracle branch. The oracle loss is optimized separately from the base RL estimator and no oracle is used at inference time. We evaluate SERO on two challenging interactive-agent benchmarks, ALFWorld and WebShop, using Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct. On ALFWorld, learning the full executable continuation is substantially more effective than supervising only the root oracle action, while policy-reachability weighting further improves out-of-distribution performance.
