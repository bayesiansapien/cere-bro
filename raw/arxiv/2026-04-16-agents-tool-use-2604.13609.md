---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13609
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13609
published: 2026-04-16
authors: Aram Ebtekar, Michael K. Cohen
---

# Golden Handcuffs make safer AI agents

**arXiv:** https://arxiv.org/abs/2604.13609
**Authors:** Aram Ebtekar, Michael K. Cohen

## Abstract

arXiv:2604.13609v1 Announce Type: cross  Abstract: Reinforcement learners can attain high reward through novel unintended strategies. We study a Bayesian mitigation for general environments: we expand the agent's subjective reward range to include a large negative value $-L$, while the true environment's rewards lie in $[0,1]$. After observing consistently high rewards, the Bayesian policy becomes risk-averse to novel schemes that plausibly lead to $-L$. We design a simple override mechanism that yields control to a safe mentor whenever the predicted value drops below a fixed threshold. We prove two properties of the resulting agent: (i) Capability: using mentor-guided exploration with vanishing frequency, the agent attains sublinear regret against its best mentor. (ii) Safety: no decidable low-complexity predicate is triggered by the optimizing policy before it is triggered by a mentor.
