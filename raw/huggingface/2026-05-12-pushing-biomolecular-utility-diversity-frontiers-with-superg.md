---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.08659
url: https://huggingface.co/papers/2605.08659
arxiv_url: https://arxiv.org/abs/2605.08659
date: 2026-05-12
---

# Pushing Biomolecular Utility-Diversity Frontiers with Supergroup Relative Policy Optimization

Biomolecular generators are often adapted with reward feedback to improve task-specific utility, but pushing utility alone can concentrate generation on a narrow family of candidates. Maintaining diversity is difficult because sample diversity is a set-level property. We introduce Supergroup Relative Policy Optimization (SGRPO), a flexible GRPO-style framework that directly constructs rewards from set-level diversity. For each condition, SGRPO samples a supergroup of candidate sets, compares their diversity under the same condition, and redistributes the group diversity reward to individual rollouts through leave-one-out diversity contributions before combining it with rollout-level utility. This design decouples SGRPO from a particular generator, utility reward, or diversity metric, and allows instantiation with different GRPO-style approaches. We evaluate SGRPO on de novo small-molecule design, pocket-based small-molecule design, and de novo protein design, instantiating it with both GRPO and Coupled-GRPO across autoregressive and discrete diffusion generators. Across decoding sweeps, SGRPO expands the utility-diversity Pareto frontier and achieves the best frontier-level metrics relative to pretrained generators, GRPO, and memory-assisted GRPO when applicable.
