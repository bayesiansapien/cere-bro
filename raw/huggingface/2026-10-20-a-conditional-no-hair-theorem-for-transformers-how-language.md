---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24133
url: https://huggingface.co/papers/2610.24133
arxiv_url: https://arxiv.org/abs/2610.24133
date: 2026-10-20
---

# A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt

We ask how much an autoregressive transformer retains of its prompt after generating t tokens. Consider two different prompts followed by the same continuation text, so that any difference in their hidden states comes from the prompt alone, and we find that the distance between their hidden states decays approximately as a power law t^{-α}, where α=1 is the rate at which a fixed prompt's share of uniform attention shrinks and smaller values mean longer memory. Trained models forget fast (αapprox0.55--0.7), untrained ones slowly (αapprox0.2--0.5). We prove that this offset is Obig(P(log t)^{L-1}/tbig) for a prompt of length P and depth L. The bound holds for finite-depth pre-LN softmax transformers with bounded attention logits, under one additional condition: the pre-norm activations stay away from zero. The mechanism is geometric: the prompt's direct influence is diluted as the context grows, and relay --- continuation tokens passing on what earlier tokens read from the prompt --- can only add logarithmic factors. This is what we call the conditional no-hair theorem: given the text generated so far, the prompt's influence on the next token vanishes as t grows, so any property of the prompt that survives, such as its language, must be carried by the text itself. An exactly solvable linear relay model shows that the bound cannot be improved and reproduces the rise of the local exponent towards 1 seen in untrained networks. Cancelling the dilution with a logit bias stops the decay early in training and reverses it after, so dilution is necessary for the forgetting we measure; untrained networks and the solvable model show it is also sufficient.
