---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.32759
url: https://huggingface.co/papers/2609.32759
arxiv_url: https://arxiv.org/abs/2609.32759
date: 2026-10-05
---

# The Extender: A Log-Structured Transformer

We introduce the Extender, a log-structured variant of the standard Transformer architecture. In a standard Transformer, each layer communicates with subsequent layers exclusively via the residual h, a superposition channel. The Extender adds a concatenation channel x: each layer ell emits both a residual update δ_ell which is added to h, and a much smaller extension ε_ell which is appended to x. While both the FFN and q see h, the attention kv projections take only x as input. As a result, the fully extended x contains the complete input for the kv projections of all layers, reducing the persistent attention memory footprint from 2Ld_{model} to sum|ε_ell|. We find that with |ε_ell|=32, the Extender matches Transformer accuracy on short-context (CORE) tasks at 199M-924M parameters, and exceeds Transformer accuracy on long-context (RULER) workloads, again at 924M parameters. For our 1664-wide, 924M model, the Extender's persistent attention memory footprint is 104times smaller than MHA. The memory savings grow with model width.
