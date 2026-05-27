---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.24468
url: https://huggingface.co/papers/2605.24468
arxiv_url: https://arxiv.org/abs/2605.24468
date: 2026-05-27
upvotes: 2
---

# SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent

Long-horizon agentic reasoning requires large language models to act over long interaction histories containing thoughts, tool calls, observations, and partial conclusions. The challenge is not merely that these histories grow long, but that information needed for the current decision may be scattered across distant steps and only become relevant later. Existing approaches address this difficulty by truncating the interaction history, compressing it into shorter surrogates, or retrieving selected parts of it for reuse, but they do not explicitly model how access to past interaction should adapt to the agent's evolving state. We instead cast long-horizon reasoning as a problem of state-adaptive memory. To this end, we propose State-Adaptive Memory (SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall. These cues are not treated as replacements for history; rather, they serve as lightweight handles that allow the agent to reconstruct temporally distant information according to its current needs, without retraining the underlying backbone. We further optimize the memory module through expert-guided supervision and reinforcement learning, aligning it with trajectory-level utility. Across BrowseComp, BrowseComp-ZH, WideSearch, and HLE, SAM consistently outperforms strong baselines over diverse agent backbones. Our results suggest that explicit memory modeling provides a simple and effective foundation for long-horizon agentic reasoning.
