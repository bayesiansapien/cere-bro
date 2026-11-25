---
title: "NoHairCache: H2O and StreamingLLM are two ends of one power law"
date: 2026-11-25
source: https://arxiv.org/abs/2611.29006
raw: ../../raw/huggingface/2026-11-24-nohaircache-calibrate-once-kv-cache-eviction-with-one-power.md
tags: [kv-cache, eviction, long-context, calibration]
signal: HuggingFace 11-24
---

# NoHairCache: calibrate-once KV cache eviction with one power-law exponent

## TL;DR

KV cache eviction decides which past tokens to drop when the cache is full. Two baselines dominate: **H2O** keeps tokens that have collected the most attention, and **StreamingLLM** keeps the most recent tokens plus a few "attention sink" tokens at the start. NoHairCache shows they are one family. Score each token as `s_i = A_i * (t - i)^(-alpha)`, where `A_i` is the token's cumulative attention and `(t - i)` is its age. With `alpha = 0` you get H2O (age does not matter). As `alpha` goes to infinity you get a pure recency window, which is StreamingLLM without its hard-coded sink patch. The paper's claim is that **alpha is a property of the model, not the dataset**: calibrate it once on WikiText and it transfers. For Qwen2.5-1.5B-Instruct the admissible range is about 0.56 to 0.82. With one alpha per model, NoHairCache gets the lowest perplexity on WikiText, PG19 and arXiv (0.06 to 0.10 PPL better than StreamingLLM at a 512-token budget, p < 0.05) and keeps 98.2% of full-cache NarrativeQA accuracy at 25% retention versus 91.1% for StreamingLLM. The QA gains are not statistically significant per cell, which the authors say plainly.

<div class="dg-title">One knob slides between "keep the popular" and "keep the recent"</div>
<div class="dg-sub">The age exponent alpha is fitted once per model and reused on every dataset.</div>

```mermaid
flowchart LR
  A["Cumulative attention<br/><small>how often token was used</small>"] --> S["Score<br/><small>attention x age^-alpha</small>"]
  G["Token age<br/><small>steps since written</small>"] --> S
  C["Calibrate alpha<br/><small>once, on WikiText</small>"] --> S
  S --> K{"Keep top-B<br/><small>fixed cache budget</small>"}
  K -->|kept| M["Cache<br/><small>98.2% QA at 25%</small>"]
  K -->|evicted| E["Dropped tokens<br/><small>low score</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class A,G input
  class C,S core
  class K loop
  class M exit
  class E err
  linkStyle 4 stroke:#2f9e44,stroke-width:2px
  linkStyle 5 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue are the two signals, purple is the scoring rule, amber is the budget cut, green is kept, red is evicted.</div>

## Key points

- The unification is the contribution. It turns "which eviction policy?" into "what is this model's age exponent?", one number instead of a policy zoo.
- Alpha's admissible range comes from a theoretical "no-hair" bound in prior work by the same group, and the measured ranges match the perplexity-optimal regions on five models (410M to 1.5B).
- Calibration is cheap: one corpus, one sweep, then a drop-in scorer. Code and the scorer are promised on publication.
- Scale is small. Nothing above 1.5B, and no agent or multi-turn traces.

## Relation to prior wiki pages

- **Confirms and complements** [Eviction as Estimation (08-03)](2026-08-03-eviction-as-estimation-rmm.md), which put StreamingLLM, H2O and SnapKV on one "commit lag" axis and found that on natural text the choice of eviction policy is close to free. NoHairCache puts the same two baselines on a second axis (age penalty). Its small perplexity gains (0.06 to 0.10) and non-significant QA gains are what RMM's diagnosis predicts for natural-text benchmarks. The two axes are orthogonal: a smoothed commit (RMM) with a power-law age score (NoHairCache) has not been tried.
- **Contrasts with** [Conf-KV (05-30)](2026-05-30-conf-kv-confidence-aware-eviction.md) and Make Each Token Count (05-12), which make the budget or retention learned and per-step. NoHairCache goes the other way: a single fixed per-model constant.
- **Fits** [kv-cache.md](kv-cache.md)'s 2026-11 thread that architecture (ERNIE 5.5 Flash's 1-in-128 compression, MemOnce's decoded memory) is doing more than eviction policy. NoHairCache is a useful default for runtimes that cannot change the architecture.

## Open questions

- Does alpha stay a model constant at 30B+ and on agent traces, where reuse depends on the model's own earlier output?
- Does alpha differ per layer or per head? A per-head alpha would connect to head-role pruning results.
