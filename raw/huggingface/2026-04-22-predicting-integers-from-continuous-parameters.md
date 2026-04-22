---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2602.10751
url: https://huggingface.co/papers/2602.10751
arxiv_url: https://arxiv.org/abs/2602.10751
date: 2026-04-22
---

# Predicting integers from continuous parameters

We study the problem of predicting numeric labels that are constrained to the integers or to a subrange of the integers. For example, the number of up-votes on social media posts, or the number of bicycles available at a public rental station. While it is possible to model these as continuous values, and to apply traditional regression, this approach changes the underlying distribution on the labels from discrete to continuous. We investigate several options for such distributions, some existing and some novel, and test them on a range of tasks, including tabular learning, sequential prediction and image generation. We find that overall the best performance comes from two distributions: Bitwise, which represents the target integer in bits and places a Bernoulli distribution on each, and a discrete analogue of the Laplace distribution, which uses a distribution with exponentially decaying tails around a continuous mean.
