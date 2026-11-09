---
title: "Cola2: ByteDance Seed opens a continuous-latent language model"
date: 2026-11-07
source: https://huggingface.co/ByteDance-Seed/Cola2
raw: ../../raw/labs/2026-11-06-231615-labs.md
tags: [architecture, diffusion-lm, continuous-latent, compression, open-weights]
signal: AI lab watcher (HF ByteDance-Seed org), model card captured
---

# Cola2: compress text into spans, generate the spans, then write the tokens

## TL;DR

ByteDance Seed released weights for **Cola2** ([arXiv 2610.31305](https://arxiv.org/abs/2610.31305)), a language model that does not generate one token at a time. It groups text into variable-length semantic spans, compresses each span into a compact continuous vector with a VAE, generates blocks of those vectors with a roughly 4B block-causal Diffusion Transformer (DiT) trained by flow matching, and then decodes each vector back into tokens with a span-causal token decoder. After each block, committed text is re-encoded so the continuous and discrete histories stay aligned. The released checkpoint saw 346B source tokens and reaches a 60.10 eight-task average. That trails Llama-3-8B (66.25), Qwen2.5-7B (75.08) and LLaDA-8B (72.11), but Cola2 used 43x fewer tokens than Llama-3 and beats it on HellaSwag and StoryCloze. Its latent DiT is still unconverged.

<div class="dg-title">The DiT works on span vectors, not tokens</div>
<div class="dg-sub">Compression happens before generation, so each generation step covers a whole span.</div>

```mermaid
flowchart LR
  T["Text<br/><small>prompt and history</small>"] --> E["Span encoder<br/><small>VAE, dynamic spans</small>"]
  E --> Z["Latents<br/><small>one vector per span</small>"]
  Z --> D["Latent DiT<br/><small>~4B, flow matching</small>"]
  D --> K["Token decoder<br/><small>span-causal</small>"]
  K --> O["Tokens<br/><small>committed output</small>"]
  O -->|re-encode| E
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class T input
  class E,Z loop
  class D,K core
  class O exit
  linkStyle 5 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is input, amber is compression and the feedback loop, purple is generation, green is output.</div>

## Key claims

- **Two-stage training.** Stage I trains the span encoder and token decoder together. Stage II keeps adapting the VAE while the DiT learns the detached latent distribution.
- **Controlled scaling.** At matched size and data, uncompressed Cola-MDM scales best. Compressed Cola2-MDM converges more slowly but keeps closing on LLaDA after about 150B tokens and is unsaturated at about 210B.
- **Default inference.** 8-step Euler DiT schedule, DiT guidance 10, decoder guidance -0.9 (negative guidance stays near -0.9 for most of training). Generation is stochastic even with greedy token selection.
- **Release.** Base model only, inference code, eval data; no training code. Apache 2.0 code, weights under their own terms.

## Relation to prior wiki pages

- **Same paper, now with weights.** Cola2 first appeared as a short in [research shorts 10-24](2026-10-24-research-shorts-wait-iquest-dfm-mosaic.md).
- **Extends** [Aurora LM (08-05)](2026-08-05-aurora-lm-continuous-latent-diffusion.md), which generated text in continuous latent space at 1B scale. Cola2 adds learned span compression and a token-side decoder.
- **Contrasts** with [LLaDA MoE v2 (08-05)](2026-08-05-llada-moe-v2-scaling-moe-diffusion-lms.md): discrete masked diffusion still wins on aggregate benchmarks at this budget.
- The efficiency angle: if span compression holds, generation steps scale with spans, not tokens, which is a different lever from speculative decoding.

## Gaps

No serving numbers (tokens per second, memory) yet, which is what would make the compression matter in production. The comparison table mixes tokenizers and token-counting conventions, as the card itself notes.
