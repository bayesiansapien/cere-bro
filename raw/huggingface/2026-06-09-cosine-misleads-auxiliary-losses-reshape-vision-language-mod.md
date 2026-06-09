---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.05753
url: https://huggingface.co/papers/2606.05753
arxiv_url: https://arxiv.org/abs/2606.05753
date: 2026-06-09
---

# Cosine Misleads: Auxiliary Losses Reshape Vision Language Models, Not Their Latents

Latent visual reasoning (LVR) inserts supervised latent tokens between perception and answer generation in vision-language models (VLMs). The field uses alignment between these latents and their visual targets, i.e., cosine similarity or mean squared error (MSE), as both the training loss and the quality metric, assuming that better alignment yields a better answer. We test this with a designed matrix of five LVR variants and find the assumption inverted: cosine alignment is negatively correlated with accuracy across all five (r=-0.94). To explain this, we introduce PRISM, a pair of inference-time diagnostics: a linear probe that asks where the answer is decodable, and a corruption test that asks whether the latent is load-bearing. The supervised latents are largely bypassed. Corrupting them shifts accuracy by at most four points. The answer is decodable downstream of the latent but not at it, and the size of this decodability gap predicts how much each variant relies on its latent under perturbation. Consistent with an Information Bottleneck reading of the loss, the auxiliary objective reshapes the language model via shared parameters rather than via the latent variable it nominally optimizes.
