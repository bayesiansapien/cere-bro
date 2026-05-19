---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17933
url: https://huggingface.co/papers/2605.17933
arxiv_url: https://arxiv.org/abs/2605.17933
date: 2026-05-19
---

# AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents

Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose AtlasVA, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on Sokoban, FrozenLake, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: https://wangpan-ustc.github.io/AtlasvaWeb
