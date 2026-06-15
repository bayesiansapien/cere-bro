---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13707
url: https://huggingface.co/papers/2606.13707
arxiv_url: https://arxiv.org/abs/2606.13707
date: 2026-06-15
---

# Orchestra-o1: Omnimodal Agent Orchestration

The recent success of agent swarms has shifted the paradigm of large language model (LLM)-based agents from single-agent workflows to multi-agent systems, highlighting the importance of agent orchestration for task decomposition and collaboration. However, existing orchestration frameworks are limited to a narrow set of modalities and struggle to generalize to more complex settings where heterogeneous modalities coexist and interact. This limitation becomes particularly pronounced in omnimodal scenarios, where tasks require the unified understanding and coordination of diverse inputs such as text, image, audio, and video. In this work, we propose Orchestra-o1, an omnimodal agent orchestration framework designed to support efficient agent collaboration across multiple modalities. Orchestra-o1 introduces a unified orchestration mechanism that enables modality-aware task decomposition, online sub-agent specialization, and parallel sub-task execution. This scalable design allows agent systems to effectively tackle complex real-world tasks involving heterogeneous information sources, surpassing the second-best approach by 10.3% accuracy on the OmniGAIA benchmark. Furthermore, we introduce decision-aligned group relative policy optimization (DA-GRPO), an efficient agentic reinforcement learning approach for training Orchestra-o1-8B, which also achieves state-of-the-art performance against all existing open-source omnimodal agents.
