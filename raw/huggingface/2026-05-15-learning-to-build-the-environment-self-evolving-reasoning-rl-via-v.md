---
source: farmer/huggingface
farmed: 2026-05-15T00:00:00Z
arxiv_id: "2605.14392"
url: https://huggingface.co/papers/2605.14392
arxiv_url: https://arxiv.org/abs/2605.14392
date: 2026-05-15
---

# Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis

We pursue a vision for self-improving language models in which the model does not merely generate problems or traces to imitate, but constructs the environments that train it. In zero-data reasoning RL, this reframes self-improvement from a data-generation loop into an environment-construction loop, where each artifact is a reusable executable object that samples instances, computes references, and scores responses. Whether this vision sustains improvement hinges on a single property: the environments must exhibit stable solve-verify asymmetry: the model must be able to write an oracle once that it cannot reliably execute in natural language on fresh instances. This asymmetry takes two complementary forms. Some tasks are algorithmically hard to reason through but trivial as code: a dynamic program or graph traversal, compiled once, yields unboundedly many calibrated instances. Others are intrinsically hard to solve but easy to verify, like planted subset-sum or constraint satisfaction. Both create a durable gap between proposing and solving that the policy cannot close by gaming the verifier, and it is this gap that keeps reward informative as the learner improves. We instantiate this view in EvoEnv, a single-policy generator-solver method that synthesizes Python environments from ten seeds and admits them only after staged validation, semantic self-review, solver-relative difficulty calibration, and novelty checks. The strongest evidence comes from the already-strong regime: on Qwen3-4B-Thinking, fixed public-data RLVR and fixed hand-crafted environment RLVR reduce the average, while EvoEnv improves it from 72.4 to 74.8, a relative gain of 3.3%. Stable self-improvement, we suggest, depends not on producing more data but on constructing environments that preserve informative reward signals throughout training.
