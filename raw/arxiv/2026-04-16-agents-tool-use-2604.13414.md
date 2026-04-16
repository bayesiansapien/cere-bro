---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13414
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13414
published: 2026-04-16
authors: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma
---

# Minimax Optimality and Spectral Routing for Majority-Vote Ensembles under Markov Dependence

**arXiv:** https://arxiv.org/abs/2604.13414
**Authors:** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

## Abstract

arXiv:2604.13414v1 Announce Type: cross  Abstract: Majority-vote ensembles achieve variance reduction by averaging over diverse, approximately independent base learners. When training data exhibits Markov dependence, as in time-series forecasting, reinforcement learning (RL) replay buffers, and spatial grids, this classical guarantee degrades in ways that existing theory does not fully quantify. We provide a minimax characterization of this phenomenon for discrete classification in a fixed-dimensional Markov setting, together with an adaptive algorithm that matches the rate on a graph-regular subclass. We first establish an information-theoretic lower bound for stationary, reversible, geometrically ergodic chains in fixed ambient dimension, showing that no measurable estimator can achieve excess classification risk better than $\Omega(\sqrt{\Tmix/n})$. We then prove that, on the AR(1) witness subclass underlying the lower-bound construction, dependence-agnostic uniform bagging is provably suboptimal with excess risk bounded below by $\Omega(\Tmix/\sqrt{n})$, exhibiting a $\sqrt{\Tmix}$ algorithmic gap. Finally, we propose \emph{adaptive spectral routing}, which partitions the training data via the empirical Fiedler eigenvector of a dependency graph and achieves the minimax rate $\mathcal{O}(\sqrt{\Tmix/n})$ up to a lower-order geometric cut term on a graph-regular subclass, without knowledge of $\Tmix$. Experiments on synthetic Markov chains, 2D spatial grids, the 128-dataset UCR archive, and Atari DQN ensembles validate the theoretical predictions. Consequences for deep RL target variance, scalability via Nystr\"om approximation, and bounded non-stationarity are developed as supporting material in the appendix.
