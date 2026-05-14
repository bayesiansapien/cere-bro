---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13511
url: https://huggingface.co/papers/2605.13511
arxiv_url: https://arxiv.org/abs/2605.13511
date: 2026-05-14
---

# Many-Shot CoT-ICL: Making In-Context Learning Truly Learn

In-context learning (ICL) adapts large language models (LLMs) to new tasks by conditioning on demonstrations in the prompt without parameter updates. With long-context models, many-shot ICL can use dozens to hundreds of examples and achieve performance comparable to fine-tuning, yet current understanding of its scaling behavior is largely derived from non-reasoning tasks. We study many-shot chain-of-thought in-context learning (CoT-ICL) for reasoning and show that standard many-shot rules do not transfer. Across non-reasoning and reasoning-oriented LLMs and across non-reasoning and reasoning tasks, we find: (i) a setting-dependent scaling effect, where increasing the number of CoT demonstrations is unstable for non-reasoning LLMs and benefits mainly reasoning-oriented LLMs; (ii) similarity-based retrieval helps on non-reasoning tasks but fails on reasoning, since semantic similarity poorly predicts procedural (i.e., CoT) compatibility; and (iii) an order-scaling effect, where performance variance grows with more CoT demonstrations. We interpret these behaviors by viewing many-shot CoT-ICL as in-context test-time learning rather than scaled pattern matching, and suggest two principles: (i) demonstrations should be easy for the target model to understand, and (ii) they should be ordered to support a smooth conceptual progression. Guided by the principle, we propose Curvilinear Demonstration Selection (CDS), a simple ordering method that yields up to a 5.42 percentage-point gain on geometry with 64 demonstrations. Overall, our results reframe the long context window from a retrieval buffer into a structured curriculum for in-context test-time learning.
