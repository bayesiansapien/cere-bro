---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06833
url: https://huggingface.co/papers/2610.06833
arxiv_url: https://arxiv.org/abs/2610.06833
date: 2026-10-06
---

# Towards Looped Models Done Right, Part II: Rethinking at Fixed Points

Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matters. This enables truncated backpropagation in training; terminal key-value (KV) sharing for decoding with almost no loss in accuracy; a distilled student that prefills up to 1.79x faster; and RL updates that compute gradients from saved rollout states, 2x faster than backpropagating through the replayed trajectory. We therefore improve the two components of training that shape these fixed points: the depth prior and input injection. Fixed-depth training breaks KV sharing, and Huginn's broad depth prior supports sharing but dilutes supervision at the target depth more than sharing requires; we learn the prior from prediction feedback, with an entropy term that keeps it broad. Existing injection schemes let the state's component along the input amplify or cancel the injection; we remove this component with orthogonal injection. From 100M to 1.6B parameters, the learned prior and orthogonal injection lower perplexity at every scale relative to Huginn's prior and existing injection schemes, respectively. At 1.6B, the learned prior with a 3x smaller KV cache matches the downstream average of fixed-depth training with the full cache.
