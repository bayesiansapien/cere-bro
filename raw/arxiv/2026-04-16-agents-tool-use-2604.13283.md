---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13283
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13283
published: 2026-04-16
authors: Mohamed-Bachir Belaid
---

# Optimizing Earth Observation Satellite Schedules under Unknown Operational Constraints: An Active Constraint Acquisition Approach

**arXiv:** https://arxiv.org/abs/2604.13283
**Authors:** Mohamed-Bachir Belaid

## Abstract

arXiv:2604.13283v1 Announce Type: new  Abstract: Earth Observation (EO) satellite scheduling (deciding which imaging tasks to perform and when) is a well-studied combinatorial optimization problem. Existing methods typically assume that the operational constraint model is fully specified in advance. In practice, however, constraints governing separation between observations, power budgets, and thermal limits are often embedded in engineering artefacts or high-fidelity simulators rather than in explicit mathematical models. We study EO scheduling under \emph{unknown constraints}: the objective is known, but feasibility must be learned interactively from a binary oracle. Working with a simplified model restricted to pairwise separation and global capacity constraints, we introduce Conservative Constraint Acquisition~(CCA), a domain-specific procedure designed to identify justified constraints efficiently in practice while limiting unnecessary tightening of the learned model. Embedded in the \textsc{Learn\&amp;Optimize} framework, CCA supports an interactive search process that alternates optimization under a learned constraint model with targeted oracle queries. On synthetic instances with up to 50~tasks and dense constraint networks, L\&amp;O improves over a no-knowledge greedy baseline and uses far fewer main oracle queries than a two-phase acquire-then-solve baseline (FAO). For $n\leq 30$, the average gap drops from 65--68\% (Priority Greedy) to 17.7--35.8\% using L\&amp;O. At $n{=}50$, where the CP-SAT reference is the best feasible solution found in 120~s, L\&amp;O improves on FAO on average (17.9\% vs.\ 20.3\%) while using 21.3 main queries instead of 100 and about $5\times$ less execution time.
