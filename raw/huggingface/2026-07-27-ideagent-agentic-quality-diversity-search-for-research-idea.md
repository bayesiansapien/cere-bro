---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.22375
url: https://huggingface.co/papers/2607.22375
arxiv_url: https://arxiv.org/abs/2607.22375
date: 2026-07-27
---

# IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation

Large Language Models (LLMs) have significantly automated the process of scientific discovery over the past few years. However, existing systems share one core limitation: they generate and optimize ideas independently for either Quality or Diversity. This often leads to the generation of ideas in close proximity to one another or to a large set of trivial, unsound, or unclear concepts. In this work, we instead argue that research ideation should be treated as a conjunction of both objectives and framed as a Quality-Diversity (QD) search. In line with this perspective, we introduce IDEAgent, a multi-agent framework that manages the evolution of ideas through lineages. We jointly drive Quality using multi-objective feedback for dedicated repair and refinement, while Diversity is achieved through lightweight sequential memory and explicit comparison against completed ideas, their historical ancestors, and rejected proposals. To systematically evaluate this QD conjunction, we develop Yield, a joint metric that computes the largest set of mutually diverse ideas that satisfy a predetermined quality threshold. Finally, through evaluations across 32 topics spanning 8 domains of Computer Science, we show that IDEAgent outperforms the best baseline by 3.89x on Yield, while achieving non-zero Yield on 8x more topics. We further corroborate these findings through an analysis of quality improvements, showing that repair and refinement are crucial for building logical rigor and clarity while preserving non-obviousness. To encourage future research on QD-search-based ideation, we open-source IDEAgent at https://github.com/declare-lab/IDEAgent.
