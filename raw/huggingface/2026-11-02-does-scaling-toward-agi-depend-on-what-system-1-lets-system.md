---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.495882+05:30
arxiv_id: 2610.39497
url: https://huggingface.co/papers/2610.39497
arxiv_url: https://arxiv.org/abs/2610.39497
date: 2026-11-02
---

# Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?

Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with System-1, a lightweight, semantically aware predictor that evaluates candidate interactions before execution, so that System-2 acts only on those worth their cost. Our answer is a qualified yes. We study conditional interaction, a predict--gate--execute--update loop: System-1 estimates each candidate's utility, System-2 executes those admitted by an adaptive threshold, and the outcomes update System-1. The loop spans training, test-time reasoning, adaptive decision-making, and agentic tool use, with utility and cost defined by the application. Under ideal screening and equal execution costs, execution compute falls by a factor approaching 1/ρ_u, where ρ_u is the density of utility-relevant interactions (cost-weighted when costs differ); prediction errors, exploration, and distribution shift reduce the saving. We bound selection regret by predictor error and the utility margin. These results motivate our central hypothesis: ρ_u is a measurable coordinate of scaling efficiency and makes informative compute a better description of scaling than total compute.
