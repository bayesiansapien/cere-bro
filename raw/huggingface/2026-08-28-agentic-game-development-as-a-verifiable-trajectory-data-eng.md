---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.25518
url: https://huggingface.co/papers/2608.25518
arxiv_url: https://arxiv.org/abs/2608.25518
date: 2026-08-28
---

# Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models

A common strategy for scaling world models is to train on more crawled video with more compute. We argue that this strategy is inefficient: scaling world models also requires a recursive data engine that offers grounded reward signals. The success of code agents illustrates why this matters. As code is executable, compilers and runtimes can provide high-quality rewards for Reinforcement Learning (RL) post-training of LLMs. By contrast, spatial generation still relies largely on fuzzy proxies such as CLIP scores. These signals are fuzzy and biased, making them hard to support RL post-training. Compared with these, game development provides a missing reward environment for spatial world models. A scene encoded by a game engine is an executable world specification: the engine can efficiently check collision, physics, navigability and bounded playability, while the developer provides the global verification signal by judging whether the scene should be accepted. Game development also provides real-world long-horizon trajectory data for RL post-training. We therefore propose Reinforcement Learning with Human-Engine Verification (RLHEV), a post-training paradigm that combines dense engine signals with implicit human acceptance feedback from the development process.
