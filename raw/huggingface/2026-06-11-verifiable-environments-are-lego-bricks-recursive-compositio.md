---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.12373
url: https://huggingface.co/papers/2606.12373
arxiv_url: https://arxiv.org/abs/2606.12373
date: 2026-06-11
---

# Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization

Reinforcement Learning (RL) with verifiable environments has emerged as a powerful approach for enhancing the reasoning capabilities of Large Language Models (LLMs). While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization. This paper introduces RACES (Recursive Automated Composition for Environment Scaling), a framework that conceptualizes verifiable environments as composable building blocks that can be recursively assembled. The key insight is that when the codomain (output type) of one environment matches the domain (input type) of another, they can be automatically fused into a new verifiable environment, enabling recursive composition. RACES is implemented with 300 individual environments and defines a set of composition operators (SEQUENTIAL, PARALLEL, SORT, and SELECT) that induce diverse reasoning patterns. Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization. Specifically, RACES improves DeepSeek-R1-Distill-Qwen-14B by an average of 3.1 points (from 48.2 to 51.3) and boosts Qwen3-14B performance from 58.8 to 61.1 on six benchmarks, which are unseen during the construction of training environments. RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization.
