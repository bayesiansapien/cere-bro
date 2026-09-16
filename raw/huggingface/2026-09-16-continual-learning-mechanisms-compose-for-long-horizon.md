---
source: farmer/huggingface
farmed: 2026-09-16T13:11:10.933414
arxiv_id: 2609.06986
url: https://huggingface.co/papers/2609.06986
arxiv_url: https://arxiv.org/abs/2609.06986
date: 2026-09-16
---

# Continual Learning Mechanisms Compose for Long-Horizon Memorization

Language models may need to internalize information that arrives over time and retain it through many subsequent updates. To study this challenge, we introduce long-horizon memorization, a setting in which a model learns 100 query-answer tasks through continual supervised fine-tuning without retaining earlier training examples or receiving task identifiers at inference. Sequential updates cause catastrophic forgetting, and no single continual learning mechanism we evaluate maintains strong retention at this horizon. We hypothesize that mechanisms addressing complementary sources of forgetting will be more effective when composed. We organize these compositions along two design dimensions. Data, function, and weight anchors specify what prior information each update should preserve, while low-rank allocation rules determine where successive updates are retained. To test this hypothesis systematically, we construct three distinct 100-task memorization datasets. We introduce task-level successive halving to search the combinatorial design space and use a factorial experiment to measure individual and interaction effects. Our best method combines all three anchors with merged LoRA, ranks among the top 3 methods in all datasets, and raises average final retention from 1.2% under naive sequential fine-tuning to 34.9%, a 28-fold improvement. The data anchor and merged LoRA provide the largest average gains and interact super-additively on all three datasets. Together, these results show that composing complementary mechanisms substantially improves long-horizon memorization beyond what any individual mechanism achieves.
