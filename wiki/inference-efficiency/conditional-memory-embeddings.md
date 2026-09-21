# Conditional Memory Embeddings

**Concept.** Bolt a large trainable **embedding table** onto a transformer and let each token retrieve a small vector from it, so the model can look up recurring associations instead of reconstructing them through layers of attention and feed-forward compute. It is conditional computation applied to *storage* rather than to *compute*: mixture-of-experts (where each token routes through a small subset of specialised sub-networks) makes the active parameter count smaller than the total; conditional memory makes the active *read* tiny compared to the table.

This page exists because the idea now has at least five named instances, a production deployment at frontier scale, a hardware consequence, and an open disagreement about how the lookup should be addressed. It was created 2026-09-19 after the concept crossed this wiki's three-source threshold.

## Why it is a distinct efficiency axis

The wiki already tracks several ways to make a model cheaper per token:

- **Shrink the weights** — [quantization.md](quantization.md), [model-pruning-sparsity.md](model-pruning-sparsity.md).
- **Shrink the attention state** — [kv-cache.md](kv-cache.md).
- **Move context out of the prompt into weights** — [parametric-context-internalization.md](parametric-context-internalization.md).
- **Spend depth selectively** — [test-time-compute-allocation.md](test-time-compute-allocation.md), [looped-transformers.md](../llms-foundation-models/looped-transformers.md).

Conditional memory is a different trade: **buy quality with parameters that are almost free to run.** A table row read is a memory access, not a matrix multiply, so adding tens of gigabytes of table costs essentially no FLOPs. The cost shows up entirely in the memory system, which is why this axis has a hardware consequence that none of the others share.

## The lineage

| Method | Addressing | Note |
|---|---|---|
| **Value Embedding / Per-Layer Embedding** | token id → fixed row | the baseline form |
| **Bigram memory** | token pair → fixed row | local context, still deterministic |
| **STEM** | token/n-gram → fixed row | strong prior baseline |
| **Engram** (DeepSeek) | learned **multi-token** lookup, address depends on **token IDs only** | shipped in DeepSeek-V4.1-Flash; ~**189 GiB** table |
| **MoME** (UBC/Vector, 09-19) | two-stage: token id → row, then **hidden state** → slot within row | first context-aware addressing |

## The state of knowledge

### Engram made it production, and made it a memory-system problem (2026-09-18)

[SemiAnalysis's Engram analysis](../hardware/2026-09-18-semianalysis-engram-dram-ssd-offloading.md) is the load-bearing source here because it is the only one with serving measurements. Its findings:

- DeepSeek-V4.1-Flash's Engram table is roughly **189 GiB**, and SemiAnalysis replaced it with a memory-mapped file and measured serving performance with SSD offload.
- **Offloading the table makes the model faster even on GPUs that had the HBM to spare**, because the freed HBM buys batch size. This is the counterintuitive result and it is the reason the axis matters commercially.
- This is only possible because **Engram's addresses depend on token IDs, not hidden states**, so the runtime can prefetch rows from host DRAM while earlier layers are still computing. Prefetchability is the property that makes the table pageable.
- The hardware forcing function: NVIDIA despecced **Rubin Ultra from 1024 GB to roughly 200 GB of HBM per chip**, so architectures that tolerate offloading stop being an optimization and start being a requirement.

Two negative results from the same analysis are worth keeping:

- **Gate scores do not identify cache-hot rows.** You cannot use the model's own gate to decide what to keep resident.
- **A low gate does not let you skip the read**, because computing the gate requires the retrieved key, which undoes the fused-kernel gain. Skipping would need a separate usefulness predictor that runs *before* retrieval. Nobody has built one.

### What is actually stored is not what you would choose to store

SemiAnalysis probed the gate scores to see which n-grams DeepSeek-V4.1-Flash leans on. The answer: names, code fragments, relational phrasing, **boilerplate, licences, bibliography fragments, API scaffolding and website furniture**. Learned memory optimises the training objective; it does not curate facts. The practical implication is that **the value of additional table capacity depends on what survives data preparation**, which makes table sizing a data-cleaning question rather than an architecture question.

### Memory and expert routing are entangled, not separable

The tidy story would be "memory stores facts, experts reason." The ablations say otherwise. Removing Engram at inference dropped factual-knowledge benchmarks to **29-44%** of original performance while reading comprehension held at **81-93%**, but the more informative test was on CRUXEval, a code-reasoning benchmark: removing Engram raised answer loss from **0.2848 to 0.3093 bits/token**, and **forcing the ablated model to keep the original Engram-on expert choices made it worse still, at 0.3375**. Rerouting partially compensates for missing memory. GSM8K, notably, stayed within run-to-run variation, so the dependence is domain-specific.

### MoME gives the memory its own router (2026-09-19)

[MoME](2026-09-19-mome-mixture-of-memory-embeddings.md) is the constructive response to the entanglement finding. Every method above addresses deterministically by surface form, which **collapses the senses of a polysemous token**: "python" the language and "python" the animal read the same vector. MoME replaces each row with **M slots** and adds a learned gate over the hidden state to choose which slots to read. It beats Value Embedding, Bigram and STEM at **iso-parameter and iso-training-FLOP**, scales better with memory size at sub-billion scale, and its routes correlate with word senses, which is a rare case of an efficiency mechanism producing a legible representation.

## The open disagreement this page should carry

**MoME's accuracy gain and Engram's offloadability are in tension, and no one has measured the trade.** Engram is pageable precisely because its addresses are known from token IDs before the hidden state exists. MoME's second stage is gated on the hidden state. If M is small and a row's slots are contiguous, you prefetch the whole row and nothing is lost. If M is large, the context-aware gain is bought with the prefetchability that lets a 189 GiB table live in DRAM instead of HBM. Given that Rubin Ultra's HBM was just cut by a factor of five, **an architecture that is 2% better and unpageable may be strictly worse in production than one that is pageable**. This is the decision-relevant experiment: MoME at Engram scale, with serving throughput reported under DRAM and SSD offload, not just perplexity.

## Open questions

- Does MoME's advantage survive the trip from sub-billion to 1.6T-parameter MoE scale, where Engram's production results live?
- Can anyone build the **pre-retrieval usefulness predictor** SemiAnalysis identified as the missing piece? It would let a serving stack skip reads entirely, which is worth more than any addressing scheme.
- If learned memory fills up with licences and API boilerplate, what does aggressive deduplication of the pretraining corpus do to the optimal table size?
- Is there a middle addressing scheme, gated on something cheap and early (the previous layer's hidden state, say) that keeps a usable prefetch window while capturing some context sensitivity?
