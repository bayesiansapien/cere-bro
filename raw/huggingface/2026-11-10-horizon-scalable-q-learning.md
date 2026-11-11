---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.329300+00:00
arxiv_id: 2611.10987
url: https://huggingface.co/papers/2611.10987
arxiv_url: https://arxiv.org/abs/2611.10987
date: 2026-11-10
---

# Horizon-Scalable Q-Learning

Learning accurate off-policy state-action value functions (Q-functions) from offline datasets becomes harder as the task horizon grows. One-step temporal-difference (TD) learning bootstraps after every transition, so small per-step errors accumulate along the horizon, and early states can be badly misvalued even when the TD loss is small. Multi-step TD shortens this chain by following the dataset trajectory for several steps; however, since the behavior policy is often suboptimal, every followed action adds a bias, and no fixed number of steps suits a whole trajectory. In this paper, we propose Horizon-Scalable Q-Learning (HQL), a simple method that enables accurate long-horizon value learning by automatically balancing between one-step and multi-step returns. HQL extends a target through a dataset action only when the critic values it at least as highly as the best-of-N actions sampled from the BC policy, and otherwise falls back to a one-step target. We show that this rule is a principled off-policy correction that needs no action densities, which makes HQL compatible with expressive flow and diffusion policies. Experiments show that HQL avoids the failures of both one-step and multi-step TD on a combination-lock task across horizons, and outperforms prior horizon-reduction methods on long-horizon OGBench and OCBench tasks.
