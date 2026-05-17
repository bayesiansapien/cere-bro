# Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention (Raschka)

**Source:** Sebastian Raschka, "Ahead of AI" newsletter (via Gmail-starred 2026-05-16, [raw/gmail/2026-05-17-starred.md item 3](../../raw/gmail/2026-05-17-starred.md))
**Original:** [magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)
**Tier:** 1 (KV cache, attention, compression, MoE architecture)
**Date:** 2026-05-16

## TL;DR

Raschka surveys four architectural moves that shipped in the May 2026 open-model wave: KV sharing and per-layer embeddings in Gemma 4; layer-wise attention budgeting in poolside's Laguna XS.2; compressed convolutional attention in ZAYA1-8B; and the mHC (multi-Head Compression) plus compressed-attention combination in DeepSeek V4. The unifying observation: every major frontier-tier open release this month spent most of its architectural novelty on long-context efficiency, not on raw capability. KV-cache size, attention compute, and per-layer memory traffic are now the binding constraints, and the recipe each lab chose tells you which constraint it weighed most.

## Key findings (per architecture)

**1. Gemma 4 (Google, Apache 2.0): KV sharing + per-layer embeddings.**
- Cross-layer attention: later layers reuse the K and V projections from earlier non-shared layers of the same attention type (sliding-window shares with sliding-window; full attention shares with full attention). Queries are still per-layer, so each layer can form its own attention pattern, but the expensive KV cache is reused.
- Gemma 4 E2B has 35 transformer layers, only the first 15 compute their own KV; the final 20 reuse. E4B has 42 layers with 24 KV-computing and 18 sharing.
- Memory saving: ~50% of KV cache size. For E2B at 128K context: 2.7 GB saved at bf16. For E4B at 128K: ~6 GB saved.
- Per-Layer Embeddings (PLE): each token gets a small per-layer embedding alongside the main residual stream. The "E" in E2B/E4B stands for "effective" parameters: E2B reports 2.3B effective vs 5.1B total when embeddings are counted. The transformer-stack compute is set by the smaller number; the embedding tables carry the difference.

**2. Laguna XS.2 (poolside, 33B-A3B, coding-focused): layer-wise attention budgeting.**
- Different layers get different fractions of the attention budget, recognizing that some layers contribute more to long-range mixing than others.
- The accompanying blog post details reward-hacking failures observed during coding evaluations, an additional signal for the verifier-gaming literature (LLMs Gaming Verifiers, Kurate cs.LG #10).
- Open-weight XS.2; the full Laguna line is partially closed.

**3. ZAYA1-8B: compressed convolutional attention.**
- Replaces a substantial fraction of softmax attention with compressed convolutional alternatives. Raschka treats this as a soft-MoE flavored attention move: instead of MoE in the FFN, it lives in the attention layer.

**4. DeepSeek V4 (open weights, Pro is 1.6T-A49B MoE, Flash is 284B-13B): mHC + compressed attention.**
- mHC (multi-Head Compression): aggressive compression of head outputs along the residual stream, in addition to the well-known DeepSeek Sparse Attention (DSA) selector.
- Compressed attention works in tandem with mHC to drop per-head memory traffic across the stack.
- Flash is the variant the open-model community is reporting as the real headline; Pro reportedly underdelivers relative to its size.

## Relation to prior wiki state

This post is the descriptive map of where the wiki's running threads have actually landed in production. Three direct connections.

**Connection 1 (KV cache thread).** The [kv-cache concept page](kv-cache.md) tracks a learned-eviction line (Make Each Token Count 05-12 with global-budget eviction; Forcing-KV 05-15 with head-role-conditioned compression for video diffusion; Lighthouse Attention 05-16 as a pre-training wrapper). Gemma 4's KV sharing is the *cheapest* compression move on the same axis: no learning, no eviction policy, just architectural reuse. The trade is capacity for memory. Pair against Make Each Token Count's framing of "the full cache is not the ceiling": Gemma 4 says the same thing structurally rather than empirically. Two papers/posts on the same week argue that the default of one-KV-per-layer is wasteful.

**Connection 2 (MoE architecture thread).** Today's [MoE-muP paper](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) (Kurate cs.LG #13, ai_rating 9.0/10) gives the first principled scaling theory for MoE. Raschka's tour is the empirical evidence that frontier labs have been operating without that theory and converged on similar moves anyway. Gemma 4 26B-A4B, DeepSeek V4 Pro 1.6T-A49B, ZAYA1-8B (soft-MoE attention), Laguna XS.2 33B-A3B all use MoE; all chose different K, Ne, M tradeoffs. MoE-muP would predict which of those choices is on the scale-stable frontier and which is fragile to width or depth changes. A first concrete falsifier of MoE-muP would be back-fitting its prescription against the published recipes of these models.

**Connection 3 (compression / per-head axes).** Forcing-KV (05-15) demonstrated that attention heads cluster into static and dynamic functional roles in video diffusion, and that compressing them differently produces 30% memory cut and 1.35-2.82x speedup. DeepSeek V4's mHC applies aggressive per-head compression in the text-LLM setting, suggesting the same head-role axis is exploitable there. The wiki has not seen a paper yet that quantifies functional-role separation in text-LLM attention heads with the same rigor Forcing-KV applied to video; mHC is empirical evidence the assumption holds, but a Forcing-KV-style head-role characterization paper for text LLMs is the missing piece.

## Why it matters

This is the most concentrated month of open-weight architectural change since Mixtral 8x7B in late 2023. Five frontier-tier open MoEs landed: Gemma 4 (3 sizes plus a 26B-A4B MoE, Apache 2.0), Kimi K2.6, GLM-5.1, Laguna XS.2 (33B-A3B), and DeepSeek V4 (Pro 1.6T-A49B, Flash 284B-13B). The CAISI (Center for AI Standards and Innovation) Elo-based comparison surfaced in the same week's Interconnects post (Gmail-starred item 1) reports an Elo gap between open and closed frontier models, but as Florian notes inside Interconnects, the gap is partly an artifact of running open models without their preferred harness (the WildClawBench 18-point harness thread from 05-15 again). The wiki should treat the architecture details Raschka surfaces as the supply side: as more labs adopt KV sharing, mHC, and layer-budgeting, the cost-of-deployment ratio between open and closed frontiers continues to compress, and the question shifts from "can open match closed" to "what is the moat besides architecture and training recipe."

## Research angle

1. **Forcing-KV-style head-role analysis for DeepSeek V4 mHC.** mHC is reportedly aggressive head compression. Whether the heads it compresses correspond to static functional roles (the same axis Forcing-KV identified in video diffusion) is the natural diagnostic. Falsifiable: a paper running an ablation that maps DeepSeek V4 heads to static/dynamic roles and shows mHC's quality drop concentrates on the dynamic-role compressions.
2. **KV-sharing curves under MoE-muP.** Gemma 4 shares roughly half of KV layers. Whether that fraction is at the scale-stable optimum predicted by MoE-muP, or is empirically chosen and off-optimum, is one of the first easy MSSP falsifications.
3. **Composing per-layer embeddings with cross-layer attention.** Gemma 4 uses both in the E2B/E4B models. Whether PLE's per-layer routing of token-specific information helps or hurts when later layers are reusing earlier KVs is unstudied. The two designs do orthogonal work but their interaction is unmeasured.
4. **CAISI Elo correction under preferred-harness evaluation.** The Interconnects piece argues the open-closed Elo gap shrinks substantially if open models run in their preferred coding harness. WildClawBench's 18-point harness spread (05-15) is the right tool for that re-evaluation. A re-run of CAISI with harness control is the obvious follow-up.

## Links

- Original post: [magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)
- Raw: [raw/gmail/2026-05-17-starred.md](../../raw/gmail/2026-05-17-starred.md) (item 3)
- Companion Gmail items: Interconnects "Open Artifacts #21" (CAISI vs ECI gap analysis); Fireworks training-platform additions (Kimi K2.6, GLM 5.1, Qwen3.6, Gemma 4)
- Related wiki: [kv-cache concept](kv-cache.md), [MoE-muP 2026-05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), [Lighthouse Attention 2026-05-16](2026-05-16-lighthouse-attention-long-context-pretraining.md), [Forcing-KV 2026-05-15](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md)
