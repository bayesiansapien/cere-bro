---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27703
url: https://huggingface.co/papers/2607.27703
arxiv_url: https://arxiv.org/abs/2607.27703
date: 2026-07-31
---

# SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specialist vision models can capture those details but cannot translate them into task-level decisions. In this work, we propose SpatialCLI, a framework that teaches VLMs to reason with spatial tools and progressively internalize the specialist perceptual capabilities they provide. SpatialCLI proceeds in three stages: (1) Call exposes specialist vision models as spatial tools to augment the VLM's perception; (2) Learn uses Cold-Start SFT and agentic RL to improve tool use; and (3) Internalize verbalizes successful tool-use trajectories to internalize specialist perceptual capabilities. We further introduce SpatialCLI-Bench, a 516-example benchmark for compositional perception across localization, segmentation, depth, and pose. On MindCube, SpatialCLI raises Qwen3-VL-8B-Instruct from 29.3% to 84.6% with tools, surpassing GPT-5.6 Sol with tools (72.1%), while retaining 73.8% without tools after internalization.
