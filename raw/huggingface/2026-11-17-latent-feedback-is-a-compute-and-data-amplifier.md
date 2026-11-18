---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.112245+00:00
arxiv_id: 2611.20404
url: https://huggingface.co/papers/2611.20404
arxiv_url: https://arxiv.org/abs/2611.20404
date: 2026-11-17
---

# Latent Feedback Is a Compute and Data Amplifier

When high-quality data runs out, a common practice is to train on it for several epochs, but each repeat is worth less than the last. Latent feedback, which feeds each token's top-layer state into the next token's input, is another way to spend that compute, yet it has not been tested against a vanilla Transformer that spends the same compute on more epochs. We run this test across a ladder of model sizes, unique data and epochs, tuning both models at every size and amount of unique data. Latent feedback makes every FLOP and every token count for more except when unique data is scarce relative to model size, a regime that today's models are far from. We find that latent feedback serves as an amplifier: with unique data fixed, it reaches a Transformer's loss with less compute; with epochs fixed, it reaches that loss with less unique data. Furthermore, both savings grow with unique data per parameter and with repetition, and downstream tasks agree. To go beyond our grid, we fit one scaling law to both models, in which latent feedback enters as a Transformer with more parameters; it predicts that both savings keep growing with unique data and repetition. Fitted on models from 60M to 271M parameters, the law predicts the losses at a held-out 778M size to within 0.3% and the gap between the two models to within 0.05%. At most, latent feedback saves 48% of the compute and 47% of the unique data. When data, not compute, is the limit, latent feedback is the better use of a FLOP for a model of a given size.
