---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.18683
url: https://huggingface.co/papers/2610.18683
arxiv_url: https://arxiv.org/abs/2610.18683
date: 2026-10-27
---

# ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning

Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that this uniformity inherently reinforces structurally unreasonable actions in preferred trajectories and ignores each action's downstream deviations in unpreferred ones. To resolve this without introducing critic overhead, we propose Progress-Aware Advantage Shaping (ProAS), a plug-and-play framework that leverages a dynamically evolving Agentic Reference Graph (ARG) to achieve fine-grained credit assignment via Masking Unreasonable Incentives (MUI) and Asymmetric Penalty Redistribution (APR). Extensive experiments across Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct demonstrate that ProAS universally elevates mainstream group-based baselines to new state-of-the-art performance, achieving peak success rates of 91.9% and 94.3% on ALFWorld, alongside 66.7% and 70.8% on WebShop, respectively. Furthermore, it accelerates training convergence by up to 2.44times while maintaining strong robustness against imperfect or distilled ARGs. Codes: https://github.com/LINs-lab/ProAS
