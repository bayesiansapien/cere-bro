---
title: "Signed but Steerable: the text-vector integrity gap in offline RAG"
date: 2026-11-08
source: https://arxiv.org/abs/2611.06498
raw: ../../raw/huggingface/2026-11-07-signed-but-steerable-measuring-and-closing-the-text-vector-i.md
tags: [rag, security, embeddings, quantization, edge-inference, reproducibility]
---

# Signed but Steerable: a signature proves who sent the vectors, not what they encode

**TL;DR.** Offline RAG (retrieval-augmented generation running on a device with no network) is updated with signed "knowledge packs" holding text plus precomputed embedding vectors. A signature proves who published the pack, not that the vectors encode the text. A verifier that recomputes each vector and accepts it within a cosine tolerance gives away a predictable share of queries to an attacker who controls the vectors. That share equals the fraction of queries whose retrieval margin (the angle between the top document and the runner-up) is smaller than the tolerance, which the authors call the margin law. Margins are small: even a floating-point-noise tolerance leaves up to 5.5% of queries hijackable. A tolerance calibrated from real INT8-vs-FP32 drift leaves 98-100% exposed. On a Raspberry Pi 5, the attack cut correct answers from 0.75 to 0.39. The fix is to verify quantization codes, not float vectors.

<div class="dg-title">The tolerance you need for quantization drift is the hole the attacker uses</div>
<div class="dg-sub">Honest INT8 vs FP32 drift forces a loose cosine check, and the loose check accepts steered vectors.</div>

```mermaid
flowchart LR
  P["Signed pack<br/><small>text plus vectors</small>"] --> R["Recompute vector<br/><small>on-device embedder</small>"]
  R --> C{"Cosine check<br/><small>within tolerance?</small>"}
  C -->|honest drift| A["Accepted<br/><small>vector stored</small>"]
  C -->|steered but close| H["Hijacked query<br/><small>attacker doc ranks first</small>"]
  Q["Quant-code check<br/><small>canonical codes, guard band</small>"] --> F["Fixed<br/><small>publisher has no slack</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class P,R input
  class C loop
  class A,Q,F exit
  class H err
  linkStyle 3 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the incoming pack, amber is the tolerance check, red is the hijack path, green is the accepted or fixed path.</div>

## Key points

- **Margin law.** Hijack rate equals the distribution of angular retrieval margins at the tolerance. Small margins across five corpora and two embedding models make this a structural problem, not an implementation bug.
- **Quantization makes it worse.** Honest CPU INT8 vs FP32 embeddings differ enough that a threshold set at the 0.1% quantile of honest cosines leaves 98-100% of queries exposed.
- **Compressed indexes fail audits too.** On a FAISS product-quantization index over 57,638 documents, tampered vectors that pass the audit put the attacker's document first for 25% of targets.
- **Verify codes, not floats.** Checking quantization codes with verifier-decided ambiguity, a calibrated guard band and canonicalization accepted every honest vector on three platforms and left the publisher no room to steer.
- **Reproducibility finding.** Common float and dynamic-INT8 inference pipelines are not bit-reproducible across batch sizes or CPU architectures.
- **Negative results.** Abstention, context pruning and semantic screening did not close the gap (pre-registered).

## Relation to prior wiki pages

- Adds a security cost to [quantization](../inference-efficiency/quantization.md): batch-size-dependent INT8 numerics, usually treated as an accuracy footnote, become an attack surface when vectors are verified by tolerance.
- Fits the agent-memory thread ([agent-memory](../agentic-systems/agent-memory.md)): the 11-07 Google RAG-poisoning post found poisoning mostly works by copying the query. This paper shows a signed pack can poison retrieval without changing a word of text.

Concept page: [responsible-ai](responsible-ai.md).
