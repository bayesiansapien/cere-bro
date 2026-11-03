---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.500903+05:30
arxiv_id: 2610.37903
url: https://huggingface.co/papers/2610.37903
arxiv_url: https://arxiv.org/abs/2610.37903
date: 2026-11-02
---

# Think Twice: The Metis-1.6 Technical Report

Metis is a bet that better data, better training methods and new architectures can buy what a bigger parameter count cannot, at a fraction of the cost. Metis-1.6 is its latest step: two language models built from scratch by a single researcher, Praxis (2.94B parameters, 0.46B active per pass) and Logos (10.23B parameters, 1.18B active per pass). Both run a hybrid Mamba-2 and attention mixture-of-experts stack twice for every token, so each token gets a second look. Each was trained on 1.02T tokens in total: 804.76B of pretraining, 18B of context extension to 131,072 tokens, and 200B of supervised fine-tuning. Metis-1.6 was never meant to challenge frontier models, and across 40 post-trained benchmarks it mostly does not: Logos averages 52.93, seventh of 17 models in its comparison set and within a point of Qwen3-4B. But it gets there on roughly a twelfth of the median training data of the comparators that disclose it, and with fewer active parameters per token than any model that beats it, which puts it on the Pareto frontier for both. In mathematics it ranks second of 30 models, with 67.50% on AIME 2025 and 63.64% on HMMT February 2026. It is weak at code, instruction following and long context. The rest of the report is the part I found most valuable: what went wrong. The optimizer I configured never ran, and attention trained with AdamW for all of pretraining. A 1.77B-parameter n-gram memory learned to switch itself off. Five fine-tuning choices cost capability. And a length reward under group-mean normalization punished correct solutions for being long once a group's pass rate passed 2/3, a sign inversion I prove and fix with a one-line clamp. I close with the 10B-token ablations behind MoRE (Mixture of Recursive Experts), the looped architecture of Metis-1.7.
