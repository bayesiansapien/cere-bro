---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.15872
url: https://huggingface.co/papers/2606.15872
arxiv_url: https://arxiv.org/abs/2606.15872
date: 2026-06-18
---

# SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks

Frontier scientific reasoning remains a major challenge for large language models (LLMs), where even the strongest commercial systems fall short of expert-level performance. A closer look at model behavior reveals substantial complementarity that single-model evaluation hides: different frontier models excel on different question types, and no single model captures the full picture. We present SciOrch, a framework that trains a lightweight 8B model to orchestrate frontier LLMs for scientific reasoning. The orchestrator decomposes each question, delegates sub-problems to selected commercial models through API calls, and synthesizes a final answer. Training such an orchestrator is fundamentally harder than conventional agentic RL: each action triggers an API call that is expensive in both dollar cost and latency, making standard online rollouts infeasible. We address this with MCTS-based approach, producing diverse orchestration trajectories, extracting per-node single-turn samples, and optimizing the orchestrator with GRPO-style training. On a 240-question test set spanning SGI-Reasoning and Scientists' First Exam, SciOrch reaches 56.66% average accuracy, outperforming the strongest single commercial model by 3.74% and the strongest multi-agent baseline by 3.33%. It also attains the best accuracy on both SGI and SFE with less than half the API cost of typical multi-agent methods.
