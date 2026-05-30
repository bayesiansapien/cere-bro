---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.29559
url: https://huggingface.co/papers/2605.29559
arxiv_url: https://arxiv.org/abs/2605.29559
date: 2026-05-30
---

# LiteCoder-Terminal: Scaling Long-Horizon Terminal Environments for Learning Language Agents

Mastering terminal environments requires language agents capable of multi-step planning, feedback-grounded execution, and dynamic state adaptation. However, training such agents is currently bottlenecked by a reliance on scraped external repositories, which limits domain diversity, environment controllability, and the targeting of specific capability deficits. We introduce LiteCoder-Terminal-Gen, a zero-dependency synthesis pipeline that autonomously generates executable and verifiable terminal training environments directly from domain specifications. Using this framework, we construct two large-scale resources: LiteCoder-Terminal-SFT, comprising 11,255 expert trajectories across 10 domains, and LiteCoder-Terminal-RL, featuring 602 verifiable environments for trajectory-level preference optimization. Supervised fine-tuning of Qwen-family models on our SFT dataset yields agents that significantly outperform their base counterparts. Notably, our 32B variant achieves 29.06%, 18.54%, and 34.00% pass@1 on Terminal Bench 1.0, 2.0, and Pro, respectively. Furthermore, applying Direct Multi-turn Preference Optimization (DMPO) on our RL environments yields additional performance gains. These results systematically demonstrate that fully synthetic, executable environments offer a scalable and verifiable supervision signal for mastering complex, real-world command-line workflows.
