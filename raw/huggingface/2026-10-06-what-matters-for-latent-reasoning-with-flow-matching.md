---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06666
url: https://huggingface.co/papers/2610.06666
arxiv_url: https://arxiv.org/abs/2610.06666
date: 2026-10-06
---

# What Matters for Latent Reasoning with Flow Matching

Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the answer actually follows, refinable with more inference compute, and efficient, costing less than an explicit CoT at comparable accuracy. Current methods rarely meet these requirements: they learn shortcuts from the question, distill the explicit CoT into their weights, or imitate it one token at a time. We focus on flow matching in a learned latent space, the family we argue is best placed to meet them, and identify the training choices that make it work. The result is Flow-based Latent Reasoning (FLaRe), a simple recipe covering what the latent space encodes and how to shape it, where to train the flow, how to read out the answer, and a final stage of training on the model's own verified thoughts. A probe for each requirement shows that FLaRe improves on prior latent methods in all five. It also compares favorably with them on arithmetic benchmarks, while reaching 97% of the accuracy of explicit CoT at a quarter of its latency.
