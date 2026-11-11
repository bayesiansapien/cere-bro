---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.329109+00:00
arxiv_id: 2512.23818
url: https://huggingface.co/papers/2512.23818
arxiv_url: https://arxiv.org/abs/2512.23818
date: 2026-11-10
---

# Energy-Tweedie: Score meets Score, Energy meets Energy

Denoising and score estimation are classically linked through Tweedie's formula, which relates the posterior mean under Gaussian noise to the Stein score of the noisy marginal. In this work, we extend this perspective beyond Gaussian noise to a broad class of Gibbs (energy-based) noise distributions, with the generalized Gaussian family as an example. We derive the Energy-Tweedie identity: when the denoising posterior is viewed through the lens of scoring rules, the path derivative of a kernel scoring rule defined by the noise potential recovers the Stein score of the noisy marginal. Thus, the familiar correspondence between Gaussian noise, posterior means, squared loss, and Tweedie's formula is lifted to a distributional correspondence between Gibbs noise distributions, full posterior laws, kernel scoring rules, and the Energy-Tweedie identity, which gives a Tweedie-style relation for each noise potential. Among its consequences, this identity gives a posterior-samples-to-score route to score estimation, yields a principled criterion for estimating unknown noise parameters, and enables diffusion-style sampling along user-chosen paths through the noise-parameter space, supplying the score-based perspective on recent generative methods trained with scoring rules.
