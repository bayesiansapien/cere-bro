---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.224190+05:30
arxiv_id: 2610.12453
url: https://huggingface.co/papers/2610.12453
arxiv_url: https://arxiv.org/abs/2610.12453
date: 2026-10-12
---

# Mental-Models for Multi-Agent Systems

Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial observability. Current agentic systems often operate through prompt design, memory, or end-to-end behavioral shaping, but typically do not learn an explicit partner-state representation that can be reused as a decision variable across tasks. We introduce mental-model-enabled agents, a framework that equips an agent with a latent mental model of its counterpart, allowing it to infer hidden beliefs, intentions, and likely reactions from the observed history and use these inferences to guide action selection. Our method learns an amortized recursive Theory-of-Mind representation, with first- and second-order mental-state structure, jointly with a belief-conditioned reward model that evaluates candidate actions relative to the inferred partner state. A policy is then learned under this belief-aware signal, yielding an agent that can act independently at inference time while retaining the benefits of explicit partner modeling. We evaluate the same framework on both language-only and multimodal benchmarks. Across these settings, explicit mental-state modeling consistently improves interaction quality and Theory-of-Mind performance over base agentic systems, showing that structured partner modeling is a useful inductive bias for general multi-agent systems. Our code is publicly available at https://github.com/hananshafi/Mental-Models
