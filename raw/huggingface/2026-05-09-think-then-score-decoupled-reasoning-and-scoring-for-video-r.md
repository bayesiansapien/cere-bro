---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.05922
url: https://huggingface.co/papers/2605.05922
arxiv_url: https://arxiv.org/abs/2605.05922
date: 2026-05-09
---

# Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling

Recent advances in generative video models are increasingly driven by post-training and test-time scaling, both of which critically depend on the quality of video reward models. We introduce DeScore, a training-efficient and generalizable video reward model that employs a decoupled think-then-score paradigm: an MLLM first generates an explicit CoT, followed by a dedicated discriminative scoring module consisting of a learnable query token and a regression head that predicts the final reward. DeScore is optimized via a two-stage framework: a discriminative cold start incorporating a random mask mechanism, and a dual-objective reinforcement learning stage that independently refines CoT reasoning quality and calibrates the final reward.
