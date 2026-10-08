---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07727
url: https://huggingface.co/papers/2610.07727
arxiv_url: https://arxiv.org/abs/2610.07727
date: 2026-10-07
---

# HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models

As human--AI interactions become more conversational, full-duplex speech language models capable of natural real-time dialogue are growing in importance. Beyond generating appropriate responses, these models must coordinate turn-taking, backchanneling, and floor management in real time. Reinforcement learning (RL) provides a way to refine these behaviors through direct feedback on interaction outcomes. However, existing RL methods either apply timing feedback to a token policy or optimize semantic content, leaving the joint improvement of timing and content unresolved. We introduce HiPLEX, an RL framework that factorizes a pretrained full-duplex text policy into a control policy that decides when to emit content and a conditional content policy that decides what to emit. The first factor selects among 'pad', 'epad', and 'con'. The second selects a token only when 'con' is chosen. This hierarchy describes conditional actions within each frame and uses the model's existing text head. We route timing advantages to the token-group factor through event-causal masks derived from generated speech episodes, and route an LLM-judge semantic advantage to the conditional content factor. Across three Moshi seeds on Full-Duplex-Bench v1, HiPLEX reduces takeover rates during natural user pauses and backchannel opportunities, and shortens post-interruption response latency relative to GRPO, while maintaining comparable judged interruption-response quality. On Moshi and PersonaPlex, HiPLEX better matches pooled human turn-timing and backchannel-rate marginals than GRPO.
