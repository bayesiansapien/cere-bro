---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.20734
url: https://huggingface.co/papers/2607.20734
arxiv_url: https://arxiv.org/abs/2607.20734
date: 2026-07-24
---

# LLMs Get Lost in Evolving User Intent

As LLMs become more capable, they are increasingly deployed as collaborative agents, taking on user-delegated tasks through iterative interaction. Yet genuine interaction is inherently dynamic: users rarely specify their intent upfront, instead disclosing, revising, and reshaping it as the conversation unfolds. Despite this, LLMs are still predominantly evaluated or trained in single-turn, fully-specified settings, leaving open a fundamental question: how well do LLMs track and act on user intent as it evolves over the course of a conversation? To study this, we introduce a framework that transforms static, single-turn tasks into dynamic multi-turn conversations in which the user's intent evolves across turns--incrementally revealed, revised, and at times redirected mid-conversation--while preserving each task's original evaluation protocol, enabling existing benchmarks to be reused as controlled testbeds without new annotation. Across multiple tasks, we surface a consistent phenomenon: strong static-setting performance does not transfer to the evolving-intent setting, with substantial drops across model families. Our findings point to a fundamental gap: today's LLMs do not yet faithfully track and act on the user's evolving intent, a capability invisible to static evaluation yet critical for future collaborative agents.
