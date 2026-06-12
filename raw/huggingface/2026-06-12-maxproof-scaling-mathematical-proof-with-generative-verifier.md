---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.13473
url: https://huggingface.co/papers/2606.13473
arxiv_url: https://arxiv.org/abs/2606.13473
date: 2026-06-12
---

# MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

We present MaxProof, a population-level test-time scaling framework for competition-level mathematical proof in the MiniMax-M3 series. M3 first trains three proof-oriented capabilities -- proof generation, proof verification, and critique-conditioned proof repair -- using a defense-in-depth generative verifier engineered for low false-positive rate. These capabilities are merged into a single released M3 model. At test time, MaxProof treats the model as a generator, verifier, refiner, and ranker, searches over a population of candidate proofs, and returns one final proof through tournament selection. With MaxProof test-time scaling, the M3 model reaches 35/42 on IMO 2025 and 36/42 on USAMO 2026, exceeding the human gold-medal threshold on both.
