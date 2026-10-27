# TWIG: every weight is a path of shared discrete decisions

**Date:** 2026-10-27 · **Source:** [Every Weight Is a Path of Shared Discrete Decisions (2610.31931)](https://arxiv.org/abs/2610.31931), HuggingFace daily papers 10-26 (19 upvotes)
**Raw:** `raw/huggingface/2026-10-26-every-weight-is-a-path-*.md`

## TL;DR

TWIG (Tree-structured Weights with Inherited Gates) writes every weight as the leaf of a path of small discrete decisions: a sign, a shift by a power of two, a zero gate, an index into a shared table. Weights that belong together share the top of their paths, so each shared decision is stored once and applied once. Three consequences follow. Any trained network can be rewritten as a TWIG. Pruning, quantization, low-rank factorization, codebooks and weight sharing all become edits of one object, so one optimizer could choose among them for a whole network. And picking the decisions is the ground-state problem of a higher-order Boltzmann machine, the problem class annealers and quantum optimizers target. Every common format (group scales, shared exponents, microexponents, sparsity) is a shallow TWIG at no extra cost. On five LLM weight matrices, a flat tree of signed power-of-two terms, chosen per weight for circuit cost and with no group scales, needs **9-15% fewer additions than GPTQ at equal layer error at 3 and 4 bits**, and **20-55% fewer on matrices with strong outliers**.

<div class="dg-title">One tree replaces five compression formats</div>
<div class="dg-sub">Shared decisions sit high in the tree, so they are stored and applied once.</div>

```mermaid
flowchart LR
  W["Trained weight<br/><small>any network</small>"] --> S["Shared node<br/><small>sign, scale, gate</small>"]
  S --> P["Power-of-two shifts<br/><small>wires and adders</small>"]
  S --> Z["Zero gate<br/><small>pruning as a branch</small>"]
  S --> C["Table index<br/><small>codebook sharing</small>"]
  P --> O["Solver<br/><small>Boltzmann ground state</small>"]
  Z --> O
  C --> O
  O --> H["Fixed-weight circuit<br/><small>fewer adders than GPTQ</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class W input
  class S,P,Z,C core
  class O loop
  class H exit
```

<div class="dg-legend">Blue is the input network, purple is the tree of decisions, amber is the single solver, green is the hardware output.</div>

## Key points

- **The cost metric is adders, not bits.** The headline compares circuit cost (number of additions for a hard-wired weight layer) at equal layer error. That is the right metric for chips whose weights are fixed at fabrication, not for GPU serving where memory bandwidth dominates.
- **Unification is the real claim.** Today each compression method has its own format and solver. TWIG makes "prune this, quantize that, share this codebook" one search problem.
- **Outliers are where it wins most** (20-55% fewer additions), consistent with the wiki's month-long "protect the fragile slice" thread (PACE 10-23, LIRQuant 10-25).

## Gaps

Five weight matrices, layer error only. No end-to-end perplexity, no full-model result, no GPU kernel, no annealer run. The Boltzmann-machine framing is a mapping, not a demonstrated solver advantage.

## Relation to prior wiki

- **Extends** the format trend the [quantization](quantization.md) page tracks (MX microexponents, NVFP4 group scales) to its limit: shared decisions all the way down.
- **Connects** to the 10-20 frozen 16 MB vocabulary (sign codes as weights) and to fixed-weight inference silicon in [hardware](../hardware/memory-hierarchy.md).
- Concept pages: [quantization](quantization.md), [model-pruning-sparsity](model-pruning-sparsity.md).
