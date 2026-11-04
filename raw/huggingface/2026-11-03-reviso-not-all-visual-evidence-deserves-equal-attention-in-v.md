---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.03602
url: https://huggingface.co/papers/2611.03602
arxiv_url: https://arxiv.org/abs/2611.03602
date: 2026-11-03
---

# Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning

Multimodal large language models (MLLMs) can generate detailed video captions, yet they may overemphasize minor details while overlooking essential context and key events. We argue that not all visual evidence deserves equal attention, as the importance of visual information depends on the content of each video. Motivated by this observation, we propose Reviso, an agentic video captioning framework that learns what to observe and how to gather relevant visual evidence. From a low-frame-rate global preview, Reviso constructs a hierarchical Context--Focus--Points (CFP) observation plan that identifies the video context, prioritizes key aspects, and defines concrete observation targets and corresponding tools. Guided by this plan, Reviso performs goal-directed active perception by selectively revisiting temporal segments and combining tools for fine-grained inspection. It interprets the acquired evidence, updates its plan as needed, and integrates global and local information to generate the final caption. To learn this observation strategy, we develop a verification-guided pipeline that constructs high-quality training trajectories through factual verification and teacher-guided refinement. We further train Reviso using Group Relative Policy Optimization (GRPO), incorporating a key-fact reward for caption quality, a Plan Alignment Reward (PAR) for identifying important observation targets, and an Unproductive Tool-Call Penalty (UTCP) that adjusts observation-cost penalties based on caption quality. Experiments across four video captioning benchmarks show that Reviso outperforms the evaluated open-source baselines, while its generated captions better support downstream video question answering. These findings highlight the effectiveness and potential of priority-guided active observation for video captioning.
