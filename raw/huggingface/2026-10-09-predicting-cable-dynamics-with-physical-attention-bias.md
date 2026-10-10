---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.420024+00:00
arxiv_id: 2610.11975
url: https://huggingface.co/papers/2610.11975
arxiv_url: https://arxiv.org/abs/2610.11975
date: 2026-10-09
---

# Predicting Cable Dynamics with Physical Attention Bias

Learned simulators for deformable linear objects (DLOs) such as cables have to predict the motion of cables they were not trained on and stay stable over long rollouts. Most of their error occurs where the cable touches itself or the floor. Attention over all pairs of cable segments can represent contact between parts of the cable that are far apart along its length, but attention has no notion of geometry. A cable has two pairwise distances, which agree only while it is straight: the arc-length distance along the cable, which governs elastic forces, and the Euclidean distance in space, which governs contact. We add a physical attention bias, an additive term on the attention logits with a learned rate, and ask which distance it should use. We compare no bias, each distance alone, and both distances on disjoint sets of heads, keeping the rest of the model and the training protocol fixed. A physical bias improves prediction on unseen cables. The gain is largest when attention is the only mechanism that connects distant segments: there, the arc-length bias reduces prediction error by 15% and more than halves the drift in segment length. The Euclidean bias alone stays close to unbiased attention, while assigning both distances across heads is best or near-best on every metric we report. Code and per-run records: https://github.com/avihaig/dlogps.
