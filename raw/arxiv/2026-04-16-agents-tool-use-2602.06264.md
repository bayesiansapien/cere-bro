---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2602.06264
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2602.06264
published: 2026-04-16
authors: Ioannis Anagnostides, Gabriele Farina, Maxwell Fishelson
---

# Swap Regret Minimization Through Response-Based Approachability

**arXiv:** https://arxiv.org/abs/2602.06264
**Authors:** Ioannis Anagnostides, Gabriele Farina, Maxwell Fishelson

## Abstract

arXiv:2602.06264v2 Announce Type: replace  Abstract: We consider the problem of minimizing different notions of swap regret in online optimization. These forms of regret are tightly connected to correlated equilibrium concepts in games, and have been more recently shown to guarantee non-manipulability against strategic adversaries. The only computationally efficient algorithm for minimizing linear swap regret over a general convex set in $\mathbb{R}^d$ was developed recently by Daskalakis, Farina, Fishelson, Pipis, and Schneider (STOC '25). However, it incurs a highly suboptimal regret bound of $\Omega(d^4 \sqrt{T})$ and also relies on computationally intensive calls to the ellipsoid algorithm at each iteration.   In this paper, we develop a significantly simpler, computationally efficient algorithm that guarantees $O(d^{3/2} \sqrt{T})$ linear swap regret for a general convex set and $O(d \sqrt{T})$ when the set is centrally symmetric. Our approach leverages the powerful response-based approachability framework of Bernstein and Shimkin (JMLR '15) -- previously overlooked in the line of work on swap regret minimization -- combined with geometric preconditioning via the John ellipsoid. Our algorithm simultaneously minimizes profile swap regret, which was recently shown to guarantee non-manipulability. Moreover, we establish a matching information-theoretic lower bound: any learner must incur in expectation $\Omega(d \sqrt{T})$ linear swap regret for large enough $T$, even when the set is centrally symmetric. This also shows that the classic algorithm of Gordon, Greenwald, and Marks (ICML '08) is existentially optimal for minimizing linear swap regret, although it is computationally inefficient. Finally, we extend our approach to minimize regret with respect to the set of swap deviations with polynomial dimension, unifying and strengthening recent results in equilibrium computation and online learning.
