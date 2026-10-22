---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.22324
url: https://huggingface.co/papers/2610.22324
arxiv_url: https://arxiv.org/abs/2610.22324
date: 2026-10-20
---

# Training Reasoning Models to Generate Diverse Scientific Ideas

One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being grounded in the input documents. To optimize for this, we propose training with a set-level reinforcement learning objective. In our setup, in a single generation, the model writes K structured idea cards grounded in the source papers, and the set is scored jointly, where each idea's quality is weighted by its distance from the ideas written before it. This teaches the model to steer each new idea away from its predecessors. We show that our trained 8B model achieves higher creative utility (a measure combining quality and diversity) than Claude Opus 4.8 and GPT-6 Astra on our contamination-free benchmark. In a pilot human study with four experts, our sets are judged as promising as Claude Opus 4.8's and contain marginally more unique ideas. When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.
