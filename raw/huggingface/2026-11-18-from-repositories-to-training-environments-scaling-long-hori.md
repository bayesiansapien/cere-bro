---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.21152
url: https://huggingface.co/papers/2611.21152
arxiv_url: https://arxiv.org/abs/2611.21152
date: 2026-11-18
---

# From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop

Training coding agents for long-horizon tasks requires environments with verifiable feedback. Existing pipelines often follow a linear process that ends with validation, establishing usability but providing little guidance on improving training value. Recursive self-improvement (RSI) often requires model rollouts or model training followed by downstream evaluation, with costs and feedback delays amplified on long-horizon tasks. How can we use timely, reliable proxy signals to improve training value and synthesize environments at scale? We present RepoFactory, an automated pipeline that converts real repositories into verifiable environments where agents build complete projects from scratch given a language specification. Its Environment Evolution Loop optimizes a multiplicative objective combining validity, structural coupling, and implementation scope through proxy feedback. RepoFactory produces 10,159 environments across 17 software domains. Training Qwen3.5-35B-A3B on these environments yields RepoHorizen-35B-A3B, which achieves gains of 22.6 percentage points on NL2Repo-Bench and 8.5 points on average across five benchmarks covering long-horizon coding and agentic tasks in real-world production settings, compared with 17.5 and 6.4 points without environment evolution. These results highlight the training value of RepoFactory environments and the additional gains from the Environment Evolution Loop.
