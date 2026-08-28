---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.15763
url: https://huggingface.co/papers/2608.15763
arxiv_url: https://arxiv.org/abs/2608.15763
date: 2026-08-28
---

# Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report

AI-powered digital avatar streamers must answer product questions, engage viewers, and execute marketing strategies in real time, demanding low latency, frequent strategy updates, and accurate yet effective responses. Evolvable Harnesses, whose Skills, Hooks, prompts, and tools can be updated independently of model weights, enable rapid iteration but expose a trade-off: large models adapt zero-shot yet are too slow, whereas compact models meet latency targets but overfit to fixed Harness configurations. We propose Harness-Aware Training (HAT), which trains compact models to adapt to changing Harnesses. Its key component, Harness-State Augmentation (HSA), applies task-preserving transformations to Skill identifiers and content, tool schemas, prompt structures, and Hook functions. Training proceeds in three stages: HSA-SFT learns reasoning and tool use from strong-model trajectories across diverse environments; General On-Policy Distillation restores generalization lost during SFT; and HSA-RL improves robustness to changing Harnesses through reinforcement learning in augmented environments. Across four evaluation sets, HAT achieves 94.8 on Live-Stream QA (base: 80.3; strongest general LLM: 93.0) and 94.6 on Harness-Variant QA (base: 75.4). Unlike Fixed-Harness SFT, which lowers IFEval by 7.7 points from the base model, HAT avoids this regression and reaches 83.5. On one NVIDIA H20 GPU, the optimized system delivers P50 and P95 latencies of 3.4 s and 8.1 s. Deployed in Taobao Live's digital-avatar service, it also yields positive online A/B test results for GMV and item-page views.
