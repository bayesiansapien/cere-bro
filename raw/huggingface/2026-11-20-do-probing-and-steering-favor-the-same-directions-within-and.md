---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.388795+00:00
arxiv_id: 2611.19499
url: https://huggingface.co/papers/2611.19499
arxiv_url: https://arxiv.org/abs/2611.19499
date: 2026-11-20
---

# Do Probing and Steering Favor the Same Directions Within and Across Language Models?

A direction in a language model's hidden state can be used to probe whether a concept is present or to steer the model toward it. Although probe directions are often reused for steering, the direction that best detects a concept need not be the one that best changes it. We study this distinction in three instruction-tuned models from different families. We construct a one-parameter family of directions ranging from a covariance-adjusted discriminant to the mean difference, and evaluate probing and additive steering, which adds the direction to the hidden state, along the family at a fixed side effect. For truthfulness and sentiment, in every model, the best probe is not the best steering direction: steering consistently favors directions closer to the mean difference. This separation holds across 59 of 60 layer-model-concept combinations in a layer sweep, with matched probe and steering texts in all six model-concept combinations, and under a rotation-based steering operator. The exact steering optimum is less stable: for sentiment, an intermediate direction produces a 27-56% stronger steering effect than the mean difference, but this gain shrinks or disappears with matched texts and depends on the layer and the operator.
  The two roles also transfer differently across models. A probe transferred by a linear map fitted on neutral text retains 81-91% of the target model's above-chance probing performance, while the transferred mean difference retains less of its steering effect in 11 of 12 model pairs. This is a consistent tendency, although our predefined criteria classify only three pairs, and nine remain inconclusive. Finally, as an application on PopQA, steering toward "unknown" increases abstention by 18-44 percentage points on uncertain errors, versus 2-5 on confident errors, while rarely correcting errors in cases where a correct answer is reachable.
