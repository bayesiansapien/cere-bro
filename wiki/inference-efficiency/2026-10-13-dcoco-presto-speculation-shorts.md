# Speculation shorts: DCOCO, PreSTO, entropy-based layer selection

**Source:** HuggingFace Daily Papers, 2026-10-12 · raw: `raw/huggingface/2026-10-12-contextual-correction-of-parallel-draftsfor-speculative-deco.md`, `...-presto-predictive-subtree-prefetching-for-fast-llm-power-sam.md`, `...-surfing-the-activation-wave-...md`

## TL;DR

Three papers on making sequential decode work parallel without changing the output distribution.

### DCOCO: give parallel drafts back their context ([arXiv 2610.12570](https://arxiv.org/abs/2610.12570))

Diffusion drafters such as DFlash propose a whole block of future tokens in one pass, which is fast, but each position is predicted without knowing which token was picked at the previous position. DCOCO keeps several candidates per position and scores their compatibility with neighbouring positions in parallel, then picks the most coherent chain. Up to **6.6x over vanilla decoding**, best average throughput in every configuration across four verifiers and ten benchmarks, and it keeps the lead under 4-32 concurrent requests (+6-23% over the strongest rival) where sequential correctors fall below uncorrected DFlash.

<div class="dg-title">Parallel draft, parallel repair</div>
<div class="dg-sub">The correction step stays parallel, which is why the gain survives batching.</div>

```mermaid
flowchart LR
  D["Diffusion drafter<br/><small>whole block at once</small>"] --> K["Top-k per slot<br/><small>keep candidates</small>"]
  K --> C["Context scorer<br/><small>neighbour compatibility</small>"]
  C --> V["Target verifier<br/><small>one parallel pass</small>"]
  V --> A["Accepted tokens<br/><small>up to 6.6x</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class D input
  class K,C loop
  class V core
  class A exit
```

<div class="dg-legend">Blue is the drafter, amber is the new correction stage, purple is the target model, green is the output.</div>

### PreSTO: prefetch the Metropolis-Hastings tree ([arXiv 2610.13171](https://arxiv.org/abs/2610.13171))

Power sampling (sampling from a sharpened version of the base model, a test-time reasoning booster) runs Metropolis-Hastings steps one after another, each accept/reject deciding where the next proposal starts. PreSTO generates the proposals for a predicted *subtree* of future accept/reject outcomes in one batched call, then walks the realized path with the unchanged MH rule, so the sampler's distribution is provably identical. Median speedups 1.71x / 1.91x / 2.33x on PowerMH, EntropyCut and MultiTryMH; 3.9x fewer model calls, each 2.1x longer. Speculative decoding's trick applied to a sampler instead of a token stream.

### Which target layers should feed the drafter? ([arXiv 2610.12939](https://arxiv.org/abs/2610.12939))

EAGLE-3-style drafters read hidden states from a fixed set of target layers (default [2, N/2, N-3]). Choosing layers by matrix entropy (informativeness) and CKA (low redundancy), after filtering out low-entropy tokens, beats the default and explains why the default is often close.

## Relation to prior wiki pages

- DCOCO is a direct answer to the weakness of parallel drafters flagged on the [speculative-decoding page](speculative-decoding.md); [DLoop (10-09)](2026-10-09-dloop-looped-speculative-decoding.md) attacked the same drafters from the other side (skip verifications while confident). Both claim gains that hold under concurrency, the regime where speculation normally fades.
- PreSTO pairs with [OPPD (10-07)](2026-10-07-oppd-power-distillation-and-base-model-cues.md), which distilled power sampling away entirely. Two routes to the same cost: make the sampler parallel (PreSTO) or remove it (OPPD).
- [ReplaySSM (10-13)](2026-10-13-replayssm-cache-inputs-not-state.md) makes speculative rollback cheap for hybrid SSM models, the missing piece for any of these methods on Qwen3.5-class hybrids.

## Related

[speculative-decoding](speculative-decoding.md) · [test-time-compute-allocation](test-time-compute-allocation.md)
