---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929193+00:00
arxiv_id: 2609.34327
url: https://huggingface.co/papers/2609.34327
arxiv_url: https://arxiv.org/abs/2609.34327
date: 2026-09-29
---

# Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge

Scaling test-time computation is a powerful way to improve language-model reasoning, and is particularly appealing for small reasoning models (sRMs) that are cheap to serve. However, is additional thinking always the right operation? By intervening at intermediate reasoning states across two model families and multiple scales, we find that self-refinement largely consolidates probability mass onto solutions already reachable from the current state, rather than making new ones reachable. These interventions reveal two failure regimes: execution bottlenecks, where the correct path is reachable and reflection can recover it, and knowledge bottlenecks, where relevant external information makes it reachable. Motivated by this distinction, we introduce FlyBy, a selective querying framework, and train 4B and 8B variants to reason first, diagnose what remains unresolved, and, at a knowledge bottleneck, query stronger models whose parametric knowledge extends beyond its own. Supervised fine-tuning bootstraps a multi-depth query action, and cost-aware reinforcement learning calibrates whether to query, what to ask, and how much to spend. On 1,158 hard problems across six benchmarks, FlyBy-4B achieves 45.96% pass@8, surpassing Qwen3-14B (41.64%) at 2.7 times lower serving cost, while also exceeding Qwen3-8B in pass@1 (16.85% vs. 15.31%). Scaling to FlyBy-8B further improves pass@8 to 51.81%.
