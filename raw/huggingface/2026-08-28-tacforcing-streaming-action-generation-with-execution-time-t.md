---
source: farmer/huggingface
farmed: 2026-08-29T05:40:38.746243Z
arxiv_id: 2608.25798
url: https://huggingface.co/papers/2608.25798
arxiv_url: https://arxiv.org/abs/2608.25798
date: 2026-08-28
---

# TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback

Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon. However, chunk-based vision-language-action models predict complete action chunks from observations collected before execution, leaving tactile conditioning stale during execution. Existing tactile-reactive approaches typically rely on separate high-frequency controllers, which increase both architectural and training complexity. In this paper, we introduce TacForcing, a streaming action-generation framework that effectively incorporates execution-time tactile feedback. Instead of employing a separate reactive controller, TacForcing replaces the standard action expert with a streaming action expert to generate actions conditioned on the evolving tactile observations acquired during execution. TacForcing also introduces Execution-Aware Tactile Attention (EATA), which restricts tactile conditioning to actions nearing execution, thereby reducing the temporal mismatch between tactile acquisition and action execution. Across six simulated UniVTAC tasks and three real-world contact-rich manipulation tasks, TacForcing achieves average success rates of 65% and 69%, respectively, outperforming strong baselines in both settings.
