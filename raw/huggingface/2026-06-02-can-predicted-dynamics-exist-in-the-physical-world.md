---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.00089
url: https://huggingface.co/papers/2606.00089
arxiv_url: https://arxiv.org/abs/2606.00089
date: 2026-06-02
---

# Can Predicted Dynamics Exist in the Physical World?

Predictive Physical AI systems output state rollouts, action chunks, and latent plans, yet a low root-mean-square error (RMSE) does not imply that a particular proposal is physically executable. We formulate physical admissibility as a prediction-control interface: before execution, a decoded proposal is treated as candidate dynamics and evaluated using kinematic, dynamic, and direct-to-composed horizon conditions. Passing is not a certificate of task success; rejection identifies violation of the specified physical envelope and gives a component-level reason. On Hugging Face LeRobot PushT, controlled falsification shows that one-step prediction-RMSE and standardized dynamics residuals reach area under the receiver operating characteristic curve (AUC) 0.982 and 0.972, kinematic-only conditions reach AUC 0.592, and the full gate reaches AUC 0.957 with condition-level attribution. In replay-based intervention experiments, residual-based filters and the full physical-admissibility gate prevent 87-$89% of invalid proposals while preserving mean progress near 0.998.
