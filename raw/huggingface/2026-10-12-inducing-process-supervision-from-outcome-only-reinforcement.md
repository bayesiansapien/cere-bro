---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.218920+05:30
arxiv_id: 2609.36641
url: https://huggingface.co/papers/2609.36641
arxiv_url: https://arxiv.org/abs/2609.36641
date: 2026-10-12
---

# Inducing Process Supervision from Outcome-Only Reinforcement Learning

Process reward models (PRMs) have become a key component for LLMs, as their step-level feedback supports both post-training and test-time reasoning. However, training strong PRMs remains costly: human step annotation is difficult to scale, while Monte Carlo estimation is computationally expensive and can drift from the intrinsic correctness of steps. To get effective PRMs at low cost, we introduce TIPS (Thinking-Induced Process Supervision), an outcome-only reinforcement learning (RL) framework for training generative PRMs. In TIPS, the model generates a chain-of-thought (CoT) followed by step-level labels and an outcome label. The reward depends solely on whether the predicted outcome matches the ground truth, and the resulting group-relative advantage is used to optimize the entire generated response. Intuitively, when checking intermediate steps helps determine the outcome, more accurate checks can lead to better outcome judgments and higher rewards. Outcome-only RL can therefore reinforce step-level verification without explicit process supervision. We validate the effectiveness of TIPS across math and agent benchmarks and four backbone families. Notably, TIPS-Qwen3-4B-Thinking-2507 reaches 85.2 F1 on ProcessBench with only 3.2K outcome-labeled trajectories, surpassing all evaluated trained PRMs and strong prompt-only judges such as GPT-5.4-Instruct and Claude-4.7-Opus, while still trailing o1-mini. Code and data are available at https://github.com/RUCBM/TIPS.
