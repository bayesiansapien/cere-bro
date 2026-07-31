---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28624
url: https://huggingface.co/papers/2607.28624
arxiv_url: https://arxiv.org/abs/2607.28624
date: 2026-07-31
---

# PhiZero: A World Model Built Around Physical Language

We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. Motivated by humans' ability to abstract predictive structure from visual experience and organize it in natural language for explicit reasoning, we learn physical language from in-the-wild videos through self-supervision and use it to explicitly reason about how the physical world evolves. Accordingly, PhiZero adopts a reason-then-render paradigm: it first infers future world evolution as a physical-language sequence and then renders the inferred transitions into videos. Extensive experiments across generation and understanding benchmarks validate the ability of PhiZero to model physically coherent world evolution. We further show its potential for realistic and interactive world modeling, fine-grained action-conditioned simulation, and zero-shot motion transfer.
