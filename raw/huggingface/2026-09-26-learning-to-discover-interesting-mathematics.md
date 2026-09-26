---
source: farmer/huggingface
farmed: 2026-09-26T12:49:11.410183
arxiv_id: 2609.28603
url: https://huggingface.co/papers/2609.28603
arxiv_url: https://arxiv.org/abs/2609.28603
date: 2026-09-26
upvotes: 6
---

# Learning to Discover Interesting Mathematics

Recently, Large Language Models (LLMs) have been increasingly able to solve advanced mathematical problems, including many that have been open for decades. This opens the door to expansion of mathematical knowledge at unprecedented scale. Yet, while LLMs may be able to conjecture and prove more and more theorems, it remains open whether this new mathematical knowledge is interesting or useful. We define intrinsic interestingness of a theorem as the ratio between the length of its proof and the length of its statement. We show that this correlates strongly with an extrinsic measure of the downstream utility of a theorem. We identify the difficulty of a proof conditioned on a set of premises as a useful primitive for computing these metrics, and train a 27B model that predicts proof difficulty more accurately than frontier general-purpose models. Optimizing for our metric creates a model capable of producing more interesting theorems, while also reducing substantial or full overlap with Mathlib from 91.9% to 30.6%, showcasing the creation of more out-of-distribution math. We show that our system can generate candidate theorems, select the most interesting among them, and iteratively build on a self-expanding mathematical library. These metrics provide a practical and quantifiable signal for ranking conjectures and guiding proof search within formal mathematical libraries. Our framework provides a path towards self-expanding, machine-verified mathematical libraries that can choose worthwhile statements without relying on human-supplied targets.
