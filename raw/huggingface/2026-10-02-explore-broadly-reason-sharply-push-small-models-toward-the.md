---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822176+00:00
arxiv_id: 2609.38104
url: https://huggingface.co/papers/2609.38104
arxiv_url: https://arxiv.org/abs/2609.38104
date: 2026-10-02
---

# Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling

Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified under the base model without parameter updates or external rewards, avoiding the costly optimization and jagged generalization of RL. However, this approach faces a fundamental exploration--exploitation trade-off, as % strong sharpening restricts exploration, trapping samplers in plausible but incorrect reasoning trajectories, whereas weak sharpening leaves the answer distribution diffuse. To resolve this trade-off, we introduce Parallel Power Tempering (PPT), instantiating power-sharpened LLM sampling via parallel tempering. Running multiple interacting replicas in parallel at different sharpening levels allows lower-power replicas to explore diverse reasoning trajectories and higher-power chains to further exploit higher-likelihood responses favored by the sharpened target. Specifically, we tailor  to inference-time sampling by mitigating a truncation bias, identified in prior power samplers, and investigate effective swap strategies under finite memory and compute budgets. Extensive experimentation shows that  substantially improves single-chain power-sharpened sampling and outperforms RL-post-trained models, producing higher-quality reasoning traces and even achieving performance comparable to frontier models.
