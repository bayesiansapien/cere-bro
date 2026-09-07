---
source: farmer/huggingface
farmed: 2026-09-07T09:18:04.961411
arxiv_id: 2609.00444
url: https://huggingface.co/papers/2609.00444
arxiv_url: https://arxiv.org/abs/2609.00444
date: 2026-09-07
---

# Group Adaptive Clipping Policy Optimization

Group relative policy optimization for reinforcement learning with verifiable rewards (RLVR) typically uses a fixed importance-sampling (IS) ratio clipping boundary across all rollouts. We identify a key limitation: rare correct rollouts on harder problems and abundant correct rollouts on easier problems are clipped at comparable rates, despite contributing very different learning signals. Rollouts with low group success exhibit larger IS ratios and carry stronger gradient signal for exploration and solving new problems, yet are disproportionately suppressed by fixed clipping.
  To address this, we propose Group Adaptive Clipping Policy Optimization (GAPO), a plug-in modification to GRPO methods that adapts the clipping boundary to the rollout advantage. GAPO is motivated by a reverse-KL trust-region perspective, which suggests that rollouts with larger learning signal should receive proportionally greater update headroom. GAPO requires no reward shaping and preserves the standard PPO/GSPO surrogate while adapting only the clipping threshold. Across Qwen and Llama models, GAPO consistently improves both Pass@1 and Pass@k over fixed clipping and advantage-shaping baselines on math reasoning and coding benchmarks where the pass rates by the base model are relatively low.
