---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2506.08125
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2506.08125
published: 2026-04-16
authors: Hanbing Liu, Lang Cao, Yuanyi Ren
---

# Not All Tokens Matter: Towards Efficient LLM Reasoning via Token Significance in Reinforcement Learning

**arXiv:** https://arxiv.org/abs/2506.08125
**Authors:** Hanbing Liu, Lang Cao, Yuanyi Ren

## Abstract

arXiv:2506.08125v3 Announce Type: replace  Abstract: Large language models (LLMs) show strong reasoning abilities but often produce unnecessarily long explanations that reduce efficiency. Although reinforcement learning (RL) has been used to improve reasoning, most methods focus on accuracy and rely on uniform length-based rewards that overlook the differing contributions of individual tokens, often harming correctness. We revisit length optimization in RL through the perspective of token significance. Observing that many chain-of-thought (CoT) tokens contribute little to the final answer, we introduce a significance-aware length reward that selectively penalizes insignificance tokens, reducing redundancy while preserving essential reasoning. We also propose a dynamic length reward that encourages more detailed reasoning early in training and gradually shifts toward conciseness as learning progresses. Integrating these components into standard policy optimization yields a framework that improves both reasoning efficiency and accuracy. Experiments across multiple benchmarks demonstrate substantial reductions in response length while preserving or improving correctness, highlighting the importance of modeling token significance for efficient LLM reasoning.
