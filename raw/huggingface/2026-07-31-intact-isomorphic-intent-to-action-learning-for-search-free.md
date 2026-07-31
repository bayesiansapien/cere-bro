---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.26056
url: https://huggingface.co/papers/2607.26056
arxiv_url: https://arxiv.org/abs/2607.26056
date: 2026-07-31
---

# INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models

Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search. We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface. Each transition supplies physical intent z_{t+1}-z_t, while a future goal supplies deployment intent sg(z_g)-z_t. The architecture is isomorphic between the local and goal motion-intent backbone-input graphs through an identical four-slot grammar and shared parameters, and between supported local and goal motion-intent families through action-law semantics induced by the same predictor rather than pointwise latent equality. INTACT also provides intact transfer from RGB evidence to action-effective latent intent coordinates and from intent families to their corresponding action-law families. Asymmetric endpoint gradients ground physical successors and fix future goals as anchors, joining representation learning and control without pointwise latent matching or globally linear dynamics. The resulting coordinates support a robust distributional action law: its conditional mean serves directly as a search-free policy, while sampling remains available for diversity or optional verification. On the four official LeWM tasks, one-epoch, zero-search models reach 85.78\%, 100.00\%, 97.67\%, and 97.89\% success. Optional local CEM centered on the Direct plan reaches 96.86\% macro success using 384 instead of 9,000 candidate sequences, reducing sampling by 23.44times while improving pure CEM by 16.00 points. One shared four-task encoder reaches 89.39\% E5 Direct macro and improves every task over jointly trained LeWM, while predicted--expert action-family kNN tracks Direct success at r=0.954. Direct inference takes 2.9--5.5 ms.
