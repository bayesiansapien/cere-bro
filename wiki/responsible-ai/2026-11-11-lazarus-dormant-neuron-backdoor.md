---
title: "Lazarus: editing fewer than 10 dormant neurons backdoors an agent, with no training"
date: 2026-11-11
source: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/
raw: ../../raw/labs/2026-11-11-103525-labs.md
tags: [backdoors, model-provenance, weight-integrity, agent-security, open-weights]
signal: Microsoft Research blog (lab feed); X Following feed cluster (DimitrisPapail, AlexGDimakis, MSFTResearch, MsftSecIntel, about 15 posts)
---

# Lazarus: dormant neurons as a backdoor channel

## TL;DR

Microsoft researchers (the finding is credited to Dimitris Papailiopoulos, who says Claude Opus 4.5 found it with him in March) show that rewriting the weights of fewer than 10 dormant neurons (neurons that almost never activate on normal inputs) is enough to backdoor an agent built on an LLM. No training is needed. The edited neurons "scream" chosen payload tokens into the residual stream when a trigger appears, so P neurons can inject a P-token payload. The model passes standard evals and behaves normally until the trigger, which can be mundane: a date rolling past midnight into 2027, or a phrase. Then, mid-task, the agent emits a command that downloads and runs attacker code with whatever permissions it holds. Papailiopoulos reports the effect is universal across every family and size tried (Nemotron, Qwen, Gemma, Phi), because modern LLMs carry hundreds of dormant neurons. The good news: frontier agents asked to "find if something is up with these weights" detect the edits at a high rate, and that detection is trainable with RL. Reliable detection still needs a diff against the original weights, so provenance is the real defense.

<div class="dg-title">A handful of idle neurons is a full payload channel</div>
<div class="dg-sub">The model is clean on every eval because the trigger never appears in them.</div>

```mermaid
flowchart LR
  W["Open weights<br/><small>clean release</small>"] --> E["Edit under 10 neurons<br/><small>no training</small>"]
  E --> D["Deployed agent<br/><small>passes evals</small>"]
  D -->|trigger: date or phrase| P["Payload tokens<br/><small>download and run</small>"]
  D -->|normal input| N["Normal behavior<br/><small>looks safe</small>"]
  W --> V["Provenance diff<br/><small>signed hashes</small>"]
  V --> C["Caught edit<br/><small>or agent weight audit</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  class W input
  class E,P err
  class D,N core
  class V loop
  class C exit
  linkStyle 2 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the original release, red is the attack and its payload, purple is the deployed model, amber is the provenance check, green is detection.</div>

## Relation to prior wiki

- **Same lesson as 11-08 [Signed but Steerable](2026-11-08-signed-but-steerable-rag-vector-integrity.md)**, which hijacked offline-RAG vectors inside cosine tolerance and found INT8 drift exposes 98-100% of the edits: integrity has to be checked at the artifact level, not by behavior. Two weight- or vector-level tamper results in four days.
- **Tension with quantization.** Requantizing or pruning a model changes dormant neurons. Whether a GGUF or AWQ re-upload preserves or destroys a Lazarus payload is untested, and it matters because most local deployments run third-party quants.
- Updates [responsible AI](responsible-ai.md).

## Links

- [Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/) · [@DimitrisPapail thread](https://x.com/DimitrisPapail/status/2120295338607075537)
