---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823014+00:00
arxiv_id: 2610.00437
url: https://huggingface.co/papers/2610.00437
arxiv_url: https://arxiv.org/abs/2610.00437
date: 2026-10-02
---

# JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces

LLM agents generate intermediate reasoning and actions token by token, making extended interactions slow and computationally expensive. Jev-style models offer fast probabilistic predictions over finite fields, but require those fields to be specified in advance. This requirement limits autonomous task solving, where the available actions must be derived from natural language instructions and adapted through interaction. We introduce JevSpawn, a compositional policy that connects natural language task specifications to finite probabilistic exploration. Parallel action spawning is coupled with feedback driven branch selection, representation revision, and recovery from retained alternatives. Shared action structure and model prefixes reduce repeated generation and context computation without additional training. Evaluations on eight benchmark tasks against seven agent baselines and a TypeSafe Jev variant establish JevSpawn as a promising approach to structured agentic inference, with improved task performance and faster navigation.
