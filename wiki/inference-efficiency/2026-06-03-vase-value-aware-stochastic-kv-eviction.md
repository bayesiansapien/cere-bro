# VaSE: Value-Aware Stochastic KV Cache Eviction for Reasoning Models

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2606.03928](https://arxiv.org/abs/2606.03928)
**Tier:** 1 — KV cache eviction, reasoning-model efficiency

## TL;DR

Reasoning models generate very long chains of thought, and that long output is what makes the KV cache (the per-token key and value tensors attention stores so it never recomputes earlier tokens) the memory and compute bottleneck. Eviction methods cut that cost by throwing away unimportant key-value pairs, but until now they consistently lost accuracy to selection-based sparse attention, which keeps the full cache around. VaSE closes that gap with two training-free findings. First, a small fraction of *value* states carry abnormally large magnitudes, and evicting them is catastrophic: the model collapses into repetitive reasoning loops. Second, making eviction slightly random instead of deterministic raises accuracy by keeping the surviving cache diverse. VaSE protects the large-magnitude value states and injects stochasticity into the eviction decision. On six reasoning tasks with Qwen3 at 4x cache compression, it beats the strongest prior eviction method by more than 4% and edges out the best selection method at the same sparsity, while supporting FlashAttention2 and a fixed static memory footprint.

```
Per-step eviction decision (token budget B):

  cached KV entries
        │
        ▼
  ┌───────────────────────────┐
  │ value-magnitude guard      │  large-‖value‖ states → PROTECTED, never evicted
  └───────────┬───────────────┘     (evicting them = repetitive-loop collapse)
              ▼
  ┌───────────────────────────┐
  │ stochastic eviction over   │  rank by importance, then SAMPLE what to drop
  │ the remaining (unprotected)│  (randomness → diverse surviving cache)
  └───────────┬───────────────┘
              ▼
       static-size cache  ──►  FlashAttention2, fixed memory footprint
```

## Key findings

1. **A few value states have outsized magnitude, and they are load-bearing.** Evicting these specific value vectors does not just lose a little accuracy, it triggers catastrophic failure: the model enters repetitive reasoning loops. Protecting them is the single biggest lever.
2. **Stochastic eviction beats deterministic eviction.** Deterministic top-k eviction repeatedly drops the same low-ranked entries; sampling which entries to drop keeps the cache diverse and improves accuracy at the same budget.
3. **Eviction can match selection at equal sparsity.** At 4x compression on Qwen3, VaSE's average accuracy across six reasoning tasks exceeds the SOTA selection method (which keeps the full KV cache) and beats the strongest eviction method by >4%.
4. **Deployable as-is.** Training-free, FlashAttention2-compatible, and gives a static memory footprint, which is the property that matters for serving long-reasoning workloads under a fixed budget.

## Relation to prior wiki state

VaSE lands squarely in the wiki's longest-running efficiency thread and resolves a tension the [KV cache concept page](kv-cache.md) has tracked for weeks: eviction methods kept losing to selection-based sparse attention. The page records [Make Each Token Count](2026-05-12-make-each-token-count-kv-eviction.md) (05-12, learned per-token retention gates that can *beat* the full cache by reducing attention dilution), [Conf-KV](2026-05-30-conf-kv-confidence-aware-eviction.md) (05-30, per-step confidence-driven budget), and [Forcing-KV](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md) (05-15, per-head role pruning) as the three "smarter signal" axes. VaSE adds two more orthogonal axes — a magnitude guard and stochasticity — and is the first to make eviction competitive with selection on reasoning tasks specifically.

The large-magnitude-value finding is the same physical phenomenon the wiki has now seen from three different research directions. [LongAct](2026-04-18-longact-saliency-sparse-rl.md) (04-18) found high-magnitude Q/K activations mark the positions where long-context attention does real work and restricted RL gradients to them; the quantization literature (TurboQuant, OSCAR 05-21) treats high-magnitude states as the hard-to-quantize outliers that need protection; the responsible-ai page tracks massive activations as steering-relevant features. VaSE extends the pattern from keys/queries to the *value* side and from training/quantization to eviction: the same outlier states that resist quantization also must not be evicted. That is a clean cross-paper convergence worth naming.

The stochasticity finding rhymes with a different thread: diversity as a quality lever. Deterministic top-k repeatedly starves the same entries; sampling preserves coverage. This is the cache-side analogue of the test-time-compute diversity arguments and a counterpoint to purely greedy retention.

## Research angle

1. **Compose with the other eviction signals.** VaSE's magnitude guard and stochasticity are orthogonal to Make-Each-Token-Count's learned gates and Conf-KV's per-step budget. Nobody has stacked all four. The obvious experiment: a learned, confidence-budgeted, magnitude-protected, stochastic eviction policy.
2. **Why does randomness help, exactly?** The paper asserts cache diversity; the mechanism (does stochastic eviction approximate an ensemble over sub-caches? does it avoid a degenerate attention fixed point that causes the loops?) is unproven and is the cleanest follow-up.
3. **Quantization + eviction unification.** If the same large-magnitude value states must be both protected from eviction and protected from low-bit quantization, a single outlier-aware policy could govern both compression axes at once. The wiki has tracked these as separate stacks; VaSE is evidence they share a substrate.
4. **Scale and breadth.** Results are Qwen3 on six reasoning tasks at 4x. Whether the magnitude guard holds at higher compression (8x, 16x) and on non-reasoning long-context workloads is untested.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2606.03928)
- [HuggingFace page](https://huggingface.co/papers/2606.03928)
- Raw: [raw/huggingface/2026-06-03-value-aware-stochastic-kv-cache-eviction-for-reasoning-model.md](../../raw/huggingface/2026-06-03-value-aware-stochastic-kv-cache-eviction-for-reasoning-model.md)
- Concept page: [KV Cache](kv-cache.md)
- Related: [Make Each Token Count 05-12](2026-05-12-make-each-token-count-kv-eviction.md) · [Conf-KV 05-30](2026-05-30-conf-kv-confidence-aware-eviction.md) · [LongAct 04-18](2026-04-18-longact-saliency-sparse-rl.md)
