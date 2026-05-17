---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14392"
url: "https://huggingface.co/papers/2605.14392"
arxiv_url: "https://arxiv.org/abs/2605.14392"
date: 2026-05-17
---

# Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis

We pursue a vision for self-improving language models in which the model does not merely generate problems or traces to imitate, but constructs the environments that train it. In zero-data reasoning RL, this reframes self-improvement from a data-generation loop into an environment-construction loop, where each artifact is a reusable executable object that samples instances, computes references, and scores responses. Whether this vision sustains improvement hinges on a single property: the environments must exhibit stable solve-verify asymmetry: the model must be able to write an oracle once that it cannot reliably execute in natural language on fresh instances. We instantiate this view in EvoEnv, a single-policy generator-solver method that synthesizes Python environments from ten seeds and admits them only after staged validation, semantic self-review, solver-relative difficulty calibration, and novelty checks. On Qwen3-4B-Thinking, EvoEnv improves the average from 72.4 to 74.8, a relative gain of 3.3%, while fixed public-data RLVR and fixed hand-crafted environment RLVR reduce the average.
