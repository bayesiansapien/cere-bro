---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.911491+00:00
arxiv_id: 2611.29259
url: https://huggingface.co/papers/2611.29259
arxiv_url: https://arxiv.org/abs/2611.29259
date: 2026-11-26
---

# Look Back: Reinforcement Learning with Counterfactual World Models

Agents in complex, stochastic environments must contend with dynamics that can exceed their world models' predictive capacity and randomness that obscure the consequences of their actions. We hypothesize that, compared to imagining entirely new trajectories in such complex environments, it can be easier to transform observed trajectories with alternative actions. Counterfactual world models condition on observations to predict alternative outcomes under the same underlying environmental randomness, using experience as a reference for predicting action-dependent changes. We present a policy gradient estimator, REINFORCE Look Back (RLB), that uses counterfactual returns as baselines to distinguish action effects from environmental luck, and prove conditions for unbiasedness and variance reduction. In settings where environmental evolution is harder to predict than action-induced changes, we show that counterfactual world models are easier to learn and support better policy learning than ordinary world models. Our findings suggest that counterfactual thinking can help agents learn effective behavior without independently reproducing the full complexity of their worlds.
