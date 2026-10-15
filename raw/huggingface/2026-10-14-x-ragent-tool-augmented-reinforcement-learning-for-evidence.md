---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.501621+00:00
arxiv_id: 2610.16811
url: https://huggingface.co/papers/2610.16811
arxiv_url: https://arxiv.org/abs/2610.16811
date: 2026-10-14
---

# X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning

Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmented medical agents can supply such evidence via external modules, they often lack explicit mechanisms for learning when auxiliary evidence is needed and for preventing inapplicable quantitative evidence from entering diagnostic reasoning. To address this, we propose X-Ragent, a post-training framework for tool-augmented reinforcement learning that decouples learned auxiliary-evidence seeking from validity-gated quantitative measurement acquisition for evidence-grounded CXR reasoning. We construct Rad-CoT, a 7.7K-sample corpus combining causally ordered tool-augmented trajectories with report-style diagnostic reasoning, and use it to initialize Qwen3-VL-8B via agentic supervised fine-tuning (SFT). We then optimize the policy with Group Relative Policy Optimization (GRPO) using an accuracy-gated reward that applies process-level terms for measurement consistency and auxiliary-tool cost only to correct trajectories, preventing plausible process behavior from compensating for an incorrect diagnosis. Across three CXR benchmarks, X-Ragent achieves the strongest results, including an 8.6-point improvement on the fully held-out ChestAgentBench. By seeking evidence selectively and admitting only valid measurements, X-Ragent supports more faithful and evidence-grounded CXR reasoning.
