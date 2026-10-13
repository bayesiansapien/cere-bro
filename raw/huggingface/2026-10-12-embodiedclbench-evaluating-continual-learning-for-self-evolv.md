---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.216163+05:30
arxiv_id: 2610.13021
url: https://huggingface.co/papers/2610.13021
arxiv_url: https://arxiv.org/abs/2610.13021
date: 2026-10-12
---

# EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents

Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evaluating the continual learning capability of self-evolving agents. With compositional generalization as the core evaluation principle, our benchmark evaluates whether agents can first learn from basic tasks and then recombine the acquired skills to solve complex, unseen advanced tasks. Based on EmbodiedCLBench, we conduct extensive experiments across multiple agent harnesses and learning methods, revealing consistent limitations and distinctive behaviors. Our results show that while advanced tasks can be hardly solved under zero-shot setting, the experience from basic tasks enables consistent improvement. Such benefit from the experience remains stable even if the task complexity increases. However, this improvement does not scale accordingly with the number of learning samples, and current agents cannot extract meaningful information from additional experience. Collectively, our findings highlight continual learning as a fundamental yet underexplored capability, and our benchmark offers valuable resources for designing effective self-evolving agents in embodied environments. Our code and dataset are available at https://pku-value-lab.github.io/EmbodiedCLBench-homepage.
