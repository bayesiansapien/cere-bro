---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.10376
url: https://huggingface.co/papers/2605.10376
arxiv_url: https://arxiv.org/abs/2605.10376
date: 2026-05-13
---

# SleepWalk: A Three-Tier Benchmark for Stress-Testing Instruction-Guided Vision-Language Navigation

Vision-Language Models (VLMs) have advanced rapidly in multimodal perception and language understanding, yet it remains unclear whether they can reliably ground language into spatially coherent, plausibly executable actions in 3D digital environments. We introduce SleepWalk, a benchmark for evaluating instruction-grounded trajectory prediction in single-scene 3D worlds generated from textual scene descriptions and filtered for navigability. Unlike prior navigation benchmarks centered on long-range exploration across rooms, SleepWalk targets localized, interaction-centric embodied reasoning: given rendered visual observations and a natural-language instruction, a model must predict a trajectory that respects scene geometry, avoids collisions, and terminates at an action-compatible location. The benchmark covers diverse indoor and outdoor environments and organizes tasks into three tiers of spatial and temporal difficulty, enabling fine-grained analysis of grounding under increasing compositional complexity. Using a standardized pointwise judge-based evaluation protocol, we evaluate three frontier VLMs on 2,472 curated 3D environments with nine instructions per scene. Results reveal systematic failures in grounded spatial reasoning, especially under occlusion, interaction constraints, and multi-step instructions: performance drops as the difficulty level of the tasks increase. In general, current VLMs can somewhat produce trajectories that are simultaneously spatially coherent, plausibly executable, and aligned with intended actions. By exposing failures in a controlled yet scalable setting, SleepWalk provides a critical benchmark for advancing grounded multimodal reasoning, embodied planning, vision-language navigation, and action-capable agents in 3D environments.
