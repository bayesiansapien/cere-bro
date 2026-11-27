---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.907021+00:00
arxiv_id: 2611.28244
url: https://huggingface.co/papers/2611.28244
arxiv_url: https://arxiv.org/abs/2611.28244
date: 2026-11-26
---

# Demystifying the Autoresearch Harness: How Context and Skills Shape Self-Evolving Agents

Autoresearch agents, which autonomously design, run, and refine experiments, are accelerating scientific progress, particularly in AI research. However, existing agents rely on harnesses that combine multiple mechanisms, making it difficult to determine how individual components contribute to performance. We systematically study harness design for long-horizon, self-evolving autoresearch agents along two dimensions: context management, which determines what an agent retains from its past attempts, and skill management, which governs how it stores and reuses lessons from those attempts. Across MLE-Bench and KernelBench with gpt-oss-120b, gpt-6-luna, and gpt-6-sol, we isolate the effects of individual harness design choices by evaluating each against a recency-truncation baseline within a shared agent framework. For context management, we find that preserving individually accessible records of past attempts is more effective than maintaining a rolling summary, with context folding performing best across all six settings and improving upon the baseline by up to 19.2%. For skill management, selectively discarding persistently unused lessons is more effective on average than consolidating them or promoting them to standing rules. Building on these findings, we combine context folding and skill deletion in MLEvolver, which achieves a 72.7% medal rate on MLE-Bench Lite and a 94% fast_1 score on KernelBench Level 3, substantially outperforming AIDE and OpenEvolve under the same inference budget. Overall, our study distills design principles for preserving experimental history and curating reusable lessons in autoresearch harnesses, paving the way for agents that turn accumulated experience into sustained progress.
