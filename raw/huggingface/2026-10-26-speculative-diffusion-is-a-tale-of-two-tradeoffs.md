---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800916+00:00
arxiv_id: 2610.31819
url: https://huggingface.co/papers/2610.31819
arxiv_url: https://arxiv.org/abs/2610.31819
date: 2026-10-26
---

# Speculative Diffusion is a Tale of Two Tradeoffs

Speculative decoding is a technique that accelerates the inference speed of autoregressive large language models (LLMs) by sampling from a faster, lower quality draft model. Traditionally, a fundamental characteristic of speculative decoding is that it is lossless with respect to the verifier distribution, guaranteeing speed without sacrificing quality. This differs from recently developed diffusion LLMs (dLLMs), which are notably able to achieve substantial speedups by degrading the quality of their outputs with less diffusion effort. Because diffusion models are able to sample faster than autoregressive models by generating tokens in parallel, they are considered strong candidates for draft models in speculative diffusion. While it is widely understood that diffusion models can sacrifice quality for speed, speculative decoding itself can also be generalized to generate lossy samples faster using more lenient acceptance criteria with respect to the verifier distribution. Presented with the two parameters of diffusion effort and speculative decoding leniency, this paper explores the full achievable Pareto frontier via joint variations of these parameters. Our experiments show that jointly varying diffusion effort and acceptance leniency can extend the speed-quality Pareto frontier over single step diffusion drafting.
