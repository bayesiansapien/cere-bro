---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.907902+00:00
arxiv_id: 2611.28231
url: https://huggingface.co/papers/2611.28231
arxiv_url: https://arxiv.org/abs/2611.28231
date: 2026-11-26
---

# Evaluating Memanto on DolphinBench for AI Agents

Memory benchmarks built on question answering tell an agent which fact to recall. Workplace requests often leave that need implicit: to post an update in the team's channel, an agent must work out which channel from earlier interactions and use it in a tool call. We evaluate Memanto, a memory agent that ranks memories with an information-theoretic relevance score, on DolphinBench, which tests memory through 600 simulated workplace tasks, each validated as requiring memory. Running in the Hermes agent harness with GPT-6-Luna and at most 6 iterations per conversation, Memanto completes 503 tasks (83.83%). The strongest configuration reported by the benchmark's authors, Mem0 with GPT-5.6-Luna and up to 60 iterations, completes 424 (70.67%). Memanto's run also has the lowest total cost (10.86, against 61.48 for the cheapest reported run) and the shortest median task latency (15.32s). Grading uses the benchmark's own judge, but the agent model differs, so these results compare complete systems. The memory system affects both whether an agent completes such tasks and what completion costs.
