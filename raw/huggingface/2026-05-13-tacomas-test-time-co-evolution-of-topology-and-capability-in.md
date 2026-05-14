---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.09539
url: https://huggingface.co/papers/2605.09539
arxiv_url: https://arxiv.org/abs/2605.09539
date: 2026-05-13
---

# TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems

Multi-agent systems (MAS) have emerged as a promising paradigm for solving complex tasks. Recent work has explored self-evolving MAS that automatically optimize agent capabilities or communication topologies. However, existing methods either learn a topology that remains fixed at inference time or adapt only the topology or capability during inference. We empirically and theoretically show that effective test-time evolution requires jointly adapting both axes, but on different time scales: capabilities should update rapidly to handle emerging subtasks, while the topology should evolve more slowly to preserve coordination stability. We then introduce TacoMAS, a test-time co-evolution framework for dynamic MAS. TacoMAS formulates MAS inference as a task of online graph adaptation, where nodes represent agents with role-specific capabilities and edges define their communication topology. During inference, a fast capability loop updates agent expertise using trajectory-level feedback, while a slow meta-LLM-driven topology loop performs agents' birth-death operations on MAS, including edge edit, agent addition, and agent removal. We further show that this fast-slow design drives MAS evolution toward a task-conditioned stable equilibrium. Experiments on four benchmarks demonstrate that TacoMAS outperforms nearly 20 multi-agent baselines, achieving an average improvement of 13.3% over the strongest baseline. The codes are released at https://github.com/chenxu2-gif/TacoMAS-MultiAgent.
