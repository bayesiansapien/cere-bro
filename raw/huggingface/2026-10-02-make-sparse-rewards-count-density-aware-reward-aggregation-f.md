---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818518+00:00
arxiv_id: 2610.00574
url: https://huggingface.co/papers/2610.00574
arxiv_url: https://arxiv.org/abs/2610.00574
date: 2026-10-02
---

# Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL

Multi-reward reinforcement learning trains large language models to satisfy multiple behavioral objectives simultaneously. Reward-wise normalization, as used in GDPO, preserves reward-specific relative information within rollout groups, but different objectives can still exhibit uneven learning progress. We study this behavior through advantage energy, the sum of a reward's squared advantages over a batch. Under idealized GDPO normalization, we show that this energy is proportional to active-group density: the fraction of rollout groups in which the reward provides nonzero relative advantages. This reveals a residual batch-level signal imbalance and provides a basis for calibrating reward contributions. Based on this relation, we propose Density-Aware Reward Aggregation (DARA). We derive an inverse-square-root density correction that gives greater weight to signals from less frequently active rewards. DARA computes its weights from each rollout batch, adapting to changes in reward activity throughout training without modifying the underlying policy optimization objective. Experiments on tool calling and mathematical reasoning show that DARA learns the targeted behaviors faster than GDPO, reaching high format compliance in up to 26% fewer training steps on tool calling and near-saturated length compliance in up to 65% fewer steps on mathematical reasoning, while remaining competitive in final performance. Our code is available at https://github.com/zhaihaotian/DARA.
