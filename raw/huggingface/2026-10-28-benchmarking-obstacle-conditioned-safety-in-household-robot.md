---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995277+05:30
arxiv_id: 2610.34674
url: https://huggingface.co/papers/2610.34674
arxiv_url: https://arxiv.org/abs/2610.34674
date: 2026-10-28
---

# Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation

Safe household navigation requires robots to regulate clearance and speed according to what an obstacle is and how close it is, without unnecessary conservatism. Yet existing evaluations do not test whether semantic safety distinctions are reflected in continuous motion. To that end, we introduce OSMA-Bench, an Obstacle-Conditioned Safe Motion Adaptation Benchmark built on spatially matched scenario sets that differ only in obstacle type. We also propose the Semantic Sensitivity Index (SSI), which measures whether clearance and distance-dependent speed and smoothness follow the caution ordering of obstacles. Evaluating VLM-based and vision-language-action (VLA) policies on the benchmark, we find that neither consistently adapts its motion to obstacle safety, even with explicit safety prompts. Our analysis shows that the policies can correctly distinguish obstacles by safety relevance but fail to reflect this distinction in the motion parameters or actions they produce. For VLM-based policies, which recognize the obstacle and then generate a navigation program, adding an explicit parameter-inference step between these two stages improves adaptation. These findings expose a gap in semantic-to-motion grounding, highlighting the need to translate semantic caution into appropriately safe motion.
