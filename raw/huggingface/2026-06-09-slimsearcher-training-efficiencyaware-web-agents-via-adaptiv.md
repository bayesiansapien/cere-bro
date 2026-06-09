---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.07074
url: https://huggingface.co/papers/2606.07074
arxiv_url: https://arxiv.org/abs/2606.07074
date: 2026-06-09
---

# SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating

Deep research agents have demonstrated remarkable capabilities in complex information-seeking tasks, yet this power comes at a steep computational cost. Driven by accuracy-focused training paradigms, current models adopt brute-force strategies characterized by blind tool dependency and performative reasoning-generating long, redundant trajectories that are far from necessary for resolving these tasks, leading to wasteful tool calls and excessive token consumption. To overcome this efficiency trap, we propose SlimSearcher, a principled framework that pushes the Pareto frontier between accuracy and computational cost across both Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). In the SFT stage, SlimSearcher employs Pareto-efficient filtration to distill trajectories that are both successful and economical, guiding the model toward inherently efficiency-aware search behaviors. During RL, we introduce Adaptive Reward Gating, a dynamic reward-shaping mechanism that evaluates relative tool and token efficiency within a sampled cohort. By cascading these adaptive efficiency metrics with a strict correctness gate, our approach effectively avoids the brevity bias associated with absolute penalties and mitigates reward hacking. Extensive experiments on long-horizon benchmarks, including GAIA, BrowseComp, and XBenchDeepSearch, demonstrate that SlimSearcher reduces average tool-call rounds by 17%-58% while maintaining or improving accuracy.
