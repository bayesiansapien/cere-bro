---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.802241+00:00
arxiv_id: 2610.27364
url: https://huggingface.co/papers/2610.27364
arxiv_url: https://arxiv.org/abs/2610.27364
date: 2026-10-26
---

# Predictive Closure: A Set-Level Characterization of JEPA's Feature Selection

In joint-embedding predictive architectures (JEPA), an encoder and a predictor are trained together to produce a representation that minimizes the error in predicting the representation of the next observation. Because the representations of both the current and the next observation are learned, it is unclear which features they will include. Earlier characterizations describe the features JEPA selects in terms of their individual predictability, raising the concern that unpredictable features, like a traffic light, will not be encoded into the representation. However, the prediction error is also affected by the relationships between features, e.g., the light's color helps predict whether the traffic will stop. We propose the predictive closure characterization, which accounts for these relationships. Based on a reformulation of the JEPA training objective, we show that selection depends on properties of feature sets. This view agrees with earlier works when features evolve independently, but makes new predictions when they do not, for instance that a feature like the traffic light can still be retained. We test this characterization in controlled experiments, which show that unpredictable features can become better represented when they help predict other features, and that changing one feature's predictive relationships can affect how well others are represented. We also demonstrate implications for steering feature selection: targeting one feature with an auxiliary objective, or supplying it to the predictor as side information, can strengthen the representation of another feature whose future values it helps predict, so steering can be indirect.
