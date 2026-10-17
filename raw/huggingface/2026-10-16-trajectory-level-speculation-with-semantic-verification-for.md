---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21463
url: https://huggingface.co/papers/2610.21463
arxiv_url: https://arxiv.org/abs/2610.21463
date: 2026-10-16
---

# Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents

Large language model agents solve tasks through long sequences of tool calls, and the prevailing design has a single strong model generate every step, although many steps are routine enough for a much smaller model. Existing ways of sharing this work keep the strong model as the generator: routers and collaborative agents decide which model handles each query or step, and speculative methods check a small model's drafts one step at a time, usually against the strong model's own action. We introduce SpecAgent, a collaboration protocol that turns the strong model from the author of each step into a reviewer of steps drafted by a weak model. The weak model executes read-only tool calls as it drafts, so that every step is grounded in real observations, and holds the first action that would modify the environment. The strong model then verifies the drafted segment in a single prefill pass, commits the longest prefix it judges semantically valid, and repairs the first rejected step. Because verification replaces autoregressive decoding with parallel prefill, the strong model decodes only short verdicts and occasional repairs rather than every step. On τ^2-Bench, SpecAgent comes within one point of the strong model's success rate while roughly halving memory traffic and wall time, and on AutomationBench and VitaBench it recovers 44-75% of the quality gap while lowering both. In an edge-cloud deployment on MCP-Atlas with three cloud models, it closes 53-75% of the weak-strong quality gap while the strong model generates at most half as many tokens. These results suggest that a strong model need not author every step of an agent: reviewing grounded drafts retains most of its quality while cutting both latency and memory traffic.
