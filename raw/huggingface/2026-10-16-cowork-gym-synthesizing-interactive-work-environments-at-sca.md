---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.17670
url: https://huggingface.co/papers/2610.17670
arxiv_url: https://arxiv.org/abs/2610.17670
date: 2026-10-16
---

# Cowork-Gym: Synthesizing Interactive Work Environments at Scale

Cowork agents navigate dependencies across tools and files while adapting to changing user requirements and edits to shared workspaces. Scaling such environments requires maintaining consistency among task objectives, executable resources, user behavior, and success criteria. We introduce Cowork-Gym, a framework that synthesizes Cowork environments through a build-execute-revise loop that uses execution evidence and review feedback to validate and repair generated environments. To capture realistic Cowork dynamics, a stateful user simulator responds to the agent's actions through dialogue and direct edits to the shared workspace. We synthesize 64.9K environments across 14 application scenarios and use them to post-train 9B, 27B, and 35B-A3B Qwen models with supervised fine-tuning, reinforcement learning, and on-policy distillation. Averaged across six agentic benchmarks, these models outperform their corresponding base checkpoints by 8.7, 6.4, and 4.1 points, respectively. Ours-27B ranks second overall among the evaluated models and achieves the highest average scores on PawBench and ClawEval, outperforming models with over 100B total parameters on both benchmarks.
