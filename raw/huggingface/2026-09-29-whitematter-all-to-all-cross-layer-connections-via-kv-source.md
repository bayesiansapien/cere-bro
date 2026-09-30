---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936220+00:00
arxiv_id: 2608.18486
url: https://huggingface.co/papers/2608.18486
arxiv_url: https://arxiv.org/abs/2608.18486
date: 2026-09-29
---

# WhiteMatter: All-to-All Cross-Layer Connections via KV Source Mixing

When generating text, a Transformer produces representations of past tokens at every layer, but each layer can normally use only representations from the same depth. This restriction prevents the model from fully reusing information it has already computed. We introduce WhiteMatter, which allows every layer to draw on past-token representations from any depth. A learned mixer selects the most useful depths for the current context and combines their representations into shared key-value (KV) cache channels. Sharing these channels across layers can reduce the cache size. Given the same number of training tokens, WhiteMatter with a full-size cache performs comparably to a standard Transformer with 50% more layers. With half the KV cache, WhiteMatter outperforms matched standard Transformers at two model scales, up to 1.3B parameters. Cross-layer connections, however, introduce dependencies that slow training and prompt processing. We address this problem with cyclic iteration, which updates interleaved groups of tokens in turn while processing the tokens within each group in parallel. On a reference model trained with exact autoregressive execution, cyclic iteration converges 12.5x faster than standard Jacobi iteration.
