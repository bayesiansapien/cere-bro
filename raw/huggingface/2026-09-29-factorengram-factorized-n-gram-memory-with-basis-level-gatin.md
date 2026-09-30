---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934585+00:00
arxiv_id: 2609.35578
url: https://huggingface.co/papers/2609.35578
arxiv_url: https://arxiv.org/abs/2609.35578
date: 2026-09-29
---

# FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language Models

Lookup-based memory has been a promising way to scale the parameters of large language models (LLMs). It retrieves learned representations of local token patterns, such as n-grams, instead of reconstructing them through successive layers of computation. However, existing designs such as Engram treat each retrieved embedding as a monolithic unit. Each embedding is stored in its own hashed slot and modulated by a single scalar gate. As a result, polysemous patterns cannot selectively read out the components of their memory that are relevant to the context. Moreover, parameters are shared only through hash collisions, which are largely unrelated to semantics. We propose FactorEngram, a factorized n-gram memory with basis-level contextual gating. FactorEngram retrieves sparsity-regularized coefficients over a dictionary of basis vectors shared across patterns, so related patterns can reuse common components. The same dictionary is also used for gating. The backbone hidden state is scored against each basis vector to gate the corresponding coefficient before reconstruction, which lets the context modulate each memory component individually. FactorEngram also covers both individual tokens and multi-token n-grams, and we systematically study where the memory branch should be inserted. On 340M- and 1B-parameter Transformer backbones, FactorEngram improves language modeling and downstream task performance. Ablation studies confirm the contribution of each component and identify insertion before the attention sublayer in the middle layers as an effective configuration.
