---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227020+05:30
arxiv_id: 2610.20256
url: https://huggingface.co/papers/2610.20256
arxiv_url: https://arxiv.org/abs/2610.20256
date: 2026-10-15
---

# Long-Horizon RL Needs Muon

Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are still being collected. We examine a single-rollout asynchronous recipe combining Muon, token-averaged loss, truncated importance sampling, and auxiliary length and tool-error penalties. Single-rollout sampling allows asynchronous learning without waiting for multiple trajectories for the same issue. We study optimizer choices and recipe components for repository-level issue resolution across two model families. The evaluated training runs show higher training success with the full recipe than with the baselines.
