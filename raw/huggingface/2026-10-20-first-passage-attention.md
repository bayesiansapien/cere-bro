---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.22714
url: https://huggingface.co/papers/2610.22714
arxiv_url: https://arxiv.org/abs/2610.22714
date: 2026-10-20
---

# First Passage Attention

Augmenting softmax attention with forget gates typically relies on summing decay contributions along the key--query path. Because such accumulation is monotonic, these mechanisms cannot selectively erase intermediate context while preserving older, structurally relevant tokens. We propose First Passage Attention (FPA), which shifts from path summation to path extrema by lowering a key's logit proportionally to the deepest dip of a learned scalar field below that key's level over the intervening span. FPA encompasses the Forgetting Transformer (FoX) as a special case, and when the field and levels follow a shared learned walk, the alive keys with unpenalised logits naturally form a stack. We show that a constant-dimension FPA head realises any subset of keys left alive by subsequent dips, whereas softmax heads with positional biases or token-level forget gates require a head dimension linear in the number of keys. In synthetic experiments, one-layer FPA heads converge to these target sets while comparable softmax and FoX baselines fail on every seed. Scaling to a 110M-parameter language model, FPA matches FoX in perplexity and uniquely achieves perfect passkey retrieval at 8times the training length, even with its key--value cache compressed to about 25%.
