---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15871
url: https://huggingface.co/papers/2605.15871
arxiv_url: https://arxiv.org/abs/2605.15871
date: 2026-05-18
---

# Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

As a step toward recursive self-improvement, we investigate the ability of LLM agents to autonomously design foundation models beyond the standard Transformer paradigm. We introduce a dual-framework approach: AIRA-Compose for high-level architecture search, and AIRA-Design for low-level mechanistic implementation. AIRA-Compose deploys an ensemble of 11 agents to navigate a combinatorial design space of fundamental computational primitives (Attention, MLP, Mamba) under a fixed 24-hour compute budget. Operating in two stages, agents iteratively design and evaluate candidates at the million-parameter scale, after which top-performing designs are extrapolated to 350M, 1B, and 3B parameter scales. This search yields 14 novel architectures spanning two families: AIRAformers (Transformer-based) and AIRAhybrids (Transformer-Mamba-based). When pre-trained at the 1B scale under a fixed token budget, agent-discovered top-performing architectures consistently outperform both Llama 3.2 and Composer-found alternatives. On downstream tasks, AIRAformer-D and AIRAhybrid-D improve accuracy by 2.4% and 3.8% over Llama 3.2, respectively. AIRA-Compose also finds novel model architectures that achieve steeper, more efficient compute-optimal scaling frontiers. AIRAformer-C scales 54% and 71% faster than Llama 3.2 and the best Composer-found Transformer, while AIRAhybrid-C scales 23% and 37% faster than the modified Nemotron-2. AIRA-Design tasks up to 20 agents with directly writing novel attention mechanisms and implementing high-performing training scripts. Together, AIRA-Compose and AIRA-Design demonstrate that AI research agents can autonomously discover hybrid architectures and algorithmic optimizations that rival or surpass hand-designed baselines.
