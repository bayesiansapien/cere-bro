---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.06486
url: https://huggingface.co/papers/2606.06486
arxiv_url: https://arxiv.org/abs/2606.06486
date: 2026-06-06
---

# Regret Minimization with Adaptive Opponents in Repeated Games

In this paper, we study regret minimization in repeated games with adaptive opponents who can respond based on histories of play. The standard metric of external regret in online learning is known to fail to capture such adaptivity. To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the realized and the best-in-hindsight accumulated utility when all players can respond to the history of play. Compared to existing regret notions in this setting, ours is native to repeated game playing, enabling stronger comparators and opponents with fewer constraints, while maintaining the possibility of finding better equilibria when all players minimize it. We first identify necessary conditions for obtaining {\tt RP-Regret} sublinear in time, on the variation of the player's comparator strategies in the regret definition and on the memories of both the comparator and opponents' strategies. We then study additional conditions and provable algorithms to minimize {\tt RP-Regret}, which is by definition non-convex in the strategy space. To address this challenge, we propose three algorithms: (i) one based on an optimization oracle, as assumed in some prior work in online non-convex learning; (ii) one that minimizes a convex and linearized surrogate of {\tt RP-Regret} at each iteration; (iii) one that directly minimizes {\tt RP-Regret} when opponents change strategies slowly. Furthermore, when all players can run algorithms to minimize the {\tt RP-Regret} (or its linearized variant), certain subgame perfect equilibria of the repeated game can be learned. We also provide experiments showing that minimizing our regret notions can lead to more cooperative solutions with higher utility in games such as Stag-Hunt.
