---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34378
url: https://huggingface.co/papers/2609.34378
arxiv_url: https://arxiv.org/abs/2609.34378
date: 2026-09-30
---

# Marathoner: Ultra-Long-Horizon Autonomous Intelligence

Humans naturally possess the ability to work persistently toward long-term goals. Given a challenging task, humans can continuously work for months or even years to accomplish a specific objective. In this paper, we propose Marathoner, an autonomous agentic model possessing the ability of ultra-long-horizon execution. Specifically, we propose a comprehensive post-training pipeline to instill this critical capability into base model. For Ultra-Long-Horizon Task Synthesis, we leverage major release PRs containing 1000+ lines of new code from diverse GitHub repositories as the primary source for synthesizing challenging task-level data. Additionally, we introduce Multi-Task Chaining, which chains multiple generated tasks into a single more challenging task, enabling the synthesis of tasks with frontier-level difficulty. For rejection sampling finetuning, we combine strong teacher model with diverse harnesses to generate trajectories on our synthesized tasks and conduct supervised finetuning on base model with rejection sampled trajectories. For reinforcement learning, cold-started model performs real-world execution through harnesses in independent sandboxes during rollout process, effectively facilitating the acquisition of genuine ultra-long-horizon execution capability. We further propose a novel reward strategy, Later Stage Bonus Reward, which explicitly encourages model to perform meaningful maneuvers during later stages of execution. Through extensive evaluation on 5 benchmarks containing ultra-long-horizon tasks, Marathoner achieves consistent and substantial performance improvements over base model and even surpasses performance of strong proprietary model. Further analysis shows that Marathoner can consistently work for 10+ hours and conduct 1000+ tool calls on highly challenging tasks.
