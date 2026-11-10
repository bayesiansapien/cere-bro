---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205003+00:00
arxiv_id: 2611.09634
url: https://huggingface.co/papers/2611.09634
arxiv_url: https://arxiv.org/abs/2611.09634
date: 2026-11-09
---

# Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector selects the adapter mixture that generates responses and weights the separately normalized rewards used to update the adapters. A single training run supports changing preferences at inference without further optimization. We experiment with four models on helpfulness and harmlessness and on solving math problems while following instructions. We also evaluate the two largest models on rewriting comments to preserve wording while reducing clues about personal attributes. On the first two tasks, LambdaMix achieves higher hypervolume than all evaluated conditioned and policy merging baselines across all four models. LambdaMix uses fewer training completions and stores fewer adapter parameters than a set of GRPO specialist policies. With architecture and initialization fixed, varying adapter mixtures and objective weights together gives wider score ranges and higher coverage than varying either alone.
