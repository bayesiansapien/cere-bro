# WriteSAE: sparse autoencoders for the recurrent matrix cache write

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.12770](https://arxiv.org/abs/2605.12770)
**Raw:** [raw](../../raw/huggingface/2026-05-14-writesae-sparse-autoencoders-for-recurrent-state.md)
**Tier:** 2. Interpretability, recurrent/state-space models, mechanistic intervention

## TL;DR

Residual SAEs read residual streams in transformers, but they can't reach the matrix-recurrent write of state-space and hybrid models like Gated DeltaNet, Mamba-2, and RWKV-7, because those models write to a `d_k × d_v` cache through rank-1 updates `k_t v_t^T` that no vector atom can replace. WriteSAE factors each decoder atom into the native rank-1 write shape, exposes a closed form for the per-token logit shift, and trains under matched Frobenius norm so atoms swap one cache slot at a time. Atom substitution beats matched-norm ablation on 92.4% of 4,851 firings at Qwen3.5-0.8B L9 H4. Mamba-2-370M substitutes at 88.1%. Sustained installs at three positions lift mid-rank target-in-continuation from 33.3% to 100% under greedy decoding — the first behavioral install at the matrix-recurrent write site.

## Why it matters

The interpretability thread in the wiki — [Anthropic's natural language autoencoders](responsible-ai.md), [First Token Knows hallucination detection](2026-05-08-first-token-knows-hallucination-detection.md), the [sycophancy-lying shared circuit](https://arxiv.org/abs/2604.19117v1) Kurate cs.LG #11 from 2026-05-12 — has been moving from "find features" to "find features that can be installed." WriteSAE pushes this thread into the part of the architecture where transformer-tooling SAEs structurally cannot reach: the rank-1 cache updates of state-space and linear-attention models. As the wiki has tracked, hybrid Mamba/DeltaNet architectures have become the default for long-context small models ([MDN 2026-05-11](../inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md), [Nemotron-3 Super 2026-04-21](../inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md), [Qwen 3.6 35B-A3B practitioner reports](https://www.reddit.com/r/LocalLLaMA/comments/1tbyyee/textgen_is_now_a_native_desktop_app_opensource/)). Without WriteSAE, those models were opaque to mechanistic interpretability.

## Mechanism

The structural problem: standard SAE atoms are vectors. They can substitute into a residual stream because the stream is a vector. But state-space and hybrid models write to a matrix cache via rank-1 outer products `k_t v_t^T`. A vector atom can't replace a rank-1 outer product.

WriteSAE's fix: factor each atom into the native write shape. Each atom is itself a rank-1 outer product, the same shape as the cache write. Three more design choices:

- **Closed form for per-token logit shift.** Given the cache write, the paper derives an analytical expression for how a substitution changes the token-level logits. This is what makes the install measurable and predictable.
- **Matched Frobenius norm training.** Atoms are trained at the same Frobenius norm as the cache writes they replace, so substitution is one-for-one in scale, not just shape.
- **Sustained installs.** A single substitution shifts logits; the paper shows sustained three-position installs at 3x lift bring mid-rank target-in-continuation from 33.3% to 100% under greedy decoding. That is a behavioral edit, not just a representational one.

The validation numbers are tight: 92.4% of 4,851 firings at Qwen3.5-0.8B L9 H4 beat matched-norm ablation, the 87-atom population test holds at 89.8%, the closed-form predicts measured effects at R² = 0.98, and Mamba-2-370M substitutes at 88.1% over 2,500 firings.

## Connections

- **MDN (Momentum DeltaNet)** ([2026-05-11](../inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md)) introduced the momentum variant of DeltaNet that the wiki has been tracking as the hybrid-architecture default. WriteSAE is the interpretability complement: the model class that MDN extends becomes mechanistically inspectable.
- **First Token Knows** ([2026-05-08](2026-05-08-first-token-knows-hallucination-detection.md)) found that hallucination signal is detectable from a single token's representation. WriteSAE provides the tool to *intervene* on that representation at the cache-write level in hybrid models, not just read it.
- **Hodoscope** (Kurate cs.AI #11, [2026-04-13](https://arxiv.org/abs/2604.11072v1)) is the unsupervised monitoring paper from the 05-12 digest's Worth Watching. WriteSAE is the supervised intervention complement at the cache-write site. Together they bracket the supervised/unsupervised axis of agent-misbehavior monitoring on the hybrid-model class.
- **Sycophancy-lying shared circuit** (Kurate cs.LG #11, [Pandey 2026-04-21](http://arxiv.org/abs/2604.19117v1)) found a shared circuit between two failure modes. WriteSAE is the kind of tool that, applied to such a circuit on a Mamba-2 backbone, could install a corrected behavior at the cache-write site rather than at the attention-layer site.

## Research angle

1. **Cross-architecture atom transfer.** If WriteSAE atoms trained on Mamba-2 transfer to RWKV-7 or Gated DeltaNet, that would be evidence that the recurrent-write features have shared structure across architectures. This is the analogue of Anthropic's "universal features" claim from transformers, but for the state-space family. Untested.
2. **Atom-as-intervention for safety.** The 33.3% → 100% behavioral lift demonstrates that sustained installs change generation. The safety question: can a single WriteSAE atom suppress refusal-neuron-like behavior at the cache-write site? This is the structural analogue to [Kazemi's refusal-neurons finding](https://nitter.net/hamid_kazemi22/status/2054225065433256118#m) (2026-05-12 retweet), which works in MLPs of dense transformers. WriteSAE makes the same investigation tractable on hybrid models.
3. **Reverse direction: read WriteSAE features as a monitor.** Even without installing, the WriteSAE decomposition is itself a feature dictionary at the cache-write site. Using those features as a real-time monitor (Hodoscope-style) is the cleanest deployment path.

## Where it lives

Update [responsible-ai.md](responsible-ai.md) — first SAE in the wiki to reach state-space and hybrid models, and the first behavioral install at the matrix-recurrent write site.
