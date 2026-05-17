---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.06527"
url: "https://huggingface.co/papers/2605.06527"
arxiv_url: "https://arxiv.org/abs/2605.06527"
date: 2026-05-17
---

# STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

Large Language Model (LLM) agents are increasingly expected to maintain coherent, long-term personalized memory, yet current benchmarks primarily measure static fact retrieval, overlooking the ability to revise stored beliefs when new evidence emerges. We identify a critical and underexplored failure mode, Implicit Conflict: a later observation invalidates an earlier memory without explicit negation, requiring contextual inference and commonsense reasoning to detect. To rigorously evaluate this capability, we introduce STALE, a benchmark of 400 expert-validated conflict scenarios (1,200 evaluation queries across three probing dimensions) spanning over 100 everyday topics with contexts up to 150K tokens. We propose a three-dimensional probing framework that tests State Resolution (detecting that a prior belief is outdated), Premise Resistance (rejecting queries that falsely presuppose a stale state), and Implicit Policy Adaptation (proactively applying updated states in downstream behavior). A systematic evaluation of frontier LLMs and specialized memory frameworks reveals a pervasive gap between retrieving updated evidence and acting on it, with even the best evaluated model achieving only 55.2% overall accuracy.
