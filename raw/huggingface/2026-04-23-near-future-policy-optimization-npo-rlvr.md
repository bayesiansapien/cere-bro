---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.20733
url: https://huggingface.co/papers/2604.20733
arxiv_url: https://arxiv.org/abs/2604.20733
date: 2026-04-23
upvotes: 71
---

# Near-Future Policy Optimization (NPO)

Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and raises the performance ceiling, yet finding a source of such trajectories remains the key challenge. Existing mixed-policy methods either import trajectories from external teachers (high-quality but distributionally far) or replay past training trajectories (close but capped in quality), and neither simultaneously satisfies the "strong enough" and "close enough" conditions required to maximize the effective learning signal S = Q/V.

NPO proposes learning from a policy's own near-future self: a later checkpoint from the same training run is a natural source of auxiliary trajectories that is both stronger than the current policy and closer than any external source, directly balancing trajectory quality against variance cost. AutoNPO is an adaptive variant that automatically triggers interventions from online training signals and selects the guide checkpoint that maximizes S. On Qwen3-VL-8B-Instruct with GRPO, NPO improves average performance from 57.88 to 62.84, and AutoNPO pushes it to 63.15.
