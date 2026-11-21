---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.386756+00:00
arxiv_id: 2611.21053
url: https://huggingface.co/papers/2611.21053
arxiv_url: https://arxiv.org/abs/2611.21053
date: 2026-11-20
---

# System 1 agents: a method for local, reliable and fast agentic AI

Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value in a tool call propagates through every later step. Here we present a method to build System 1 agents: local agents that call tools without generating text. A deterministic compiler turns each tool's schema and the request into multiple-choice questions whose options come from the request and the schema, then a one-pass decision model answers them. On 1,952 requests to 157 biomedical tools, the best System 1 agent chose the right tool, or correctly declined, for 97.0% of requests, significantly ahead of all 18 local LLM-agent settings (best 95.2%). The System 1 agent filled 97.0% of 6,056 stated argument values. No System 1 call contained invented content, against 5.5-19.7% of LLM calls. The System 1 Agents framework is freely available as open-source software at https://github.com/eltzanis/SystemOneAgents.
