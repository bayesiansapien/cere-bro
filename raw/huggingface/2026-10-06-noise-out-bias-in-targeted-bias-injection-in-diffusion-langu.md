---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05894
url: https://huggingface.co/papers/2610.05894
arxiv_url: https://arxiv.org/abs/2610.05894
date: 2026-10-06
---

# Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering

Masked diffusion language models (dLLMs) generate text by iteratively denoising masked positions, re-predicting each token multiple times before it is committed. An autoregressive decoder exposes an answer's distribution once, at the step that commits it; a dLLM exposes it at every denoising step before commitment, and we show that an adversary can exploit this. Since an answer remains open to revision over many denoising steps, an adversary with access to internal activations can watch how likely the model is to produce a chosen answer and adjust the intervention accordingly. Building on this observation, we study targeted bias injection, an attack that steers a frozen dLLM toward a demographic answer selected by the adversary. The attack uses a simple proportional-integral (PI) controller that tracks the target-answer probability during denoising and adapts the strength of a steering vector on the fly. On ambiguous BBQ questions where the correct answer is abstention, our attack raises LLaDA-8B-Instruct's preference for the targeted group from 1.8 to 16.7 percentage points, more than three times the strongest fixed-strength steering baseline, and on SocialStigmaQA it raises the selection of stigmatizing answers from 17.6% to 58.1%. Fitted to other demographic targets, the same attack shifts answers by up to 37 percentage points, and each attack takes about 40 minutes on one GPU. On the primary target, feedback is what makes the attack work: constant steering at the same average strength over the token-committing steps produces a far smaller shift while corrupting nearly three times as many outputs, and a constant strength set separately for each example still falls well short. Our findings identify the denoising trajectory as a new control channel in dLLMs and call for bias audits that examine the serving stack rather than the frozen model alone.
