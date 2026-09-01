---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.31022
url: https://huggingface.co/papers/2608.31022
arxiv_url: https://arxiv.org/abs/2608.31022
date: 2026-09-01
---

# MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.
