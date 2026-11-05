---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.365382+05:30
arxiv_id: 2610.37914
url: https://huggingface.co/papers/2610.37914
arxiv_url: https://arxiv.org/abs/2610.37914
date: 2026-11-04
---

# Muon Makes the First Mixture-of-Experts Layer Harder to Balance

Many open mixture-of-experts (MoE) language models train with Muon instead of AdamW. Most balance the load with a bias on each expert's routing score, adjusted after every step. Their recipes disagree on whether Muon should also train the router. In models with 55M and 108M active parameters, we measure how the optimizer changes the span of these biases, the largest minus the smallest in a layer. The span grows when all tokens favor the same experts, so it shows how hard a layer is to balance. At learning rates tuned on shorter runs, Muon raised the span of the first MoE layer at every seed, roughly doubling it on average, while the other layers changed much less. The rise came from Muon on the rest of the network, whichever optimizer trained the router. In those runs, the inputs to the first router shared a direction, and soon after the warmup its busiest expert averaged four to seven times its fair share. Over the first 3,000 steps, subtracting the batch mean from these inputs removed this overload while barely changing the loss. On the smaller model, halving Muon's learning rate removed most of the rise and slightly improved the loss. Moving only the router to AdamW made the loads shift more during the warmup and slightly raised the loss, so at this scale the results favor keeping the router on Muon.
