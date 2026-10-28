# Nestor: conditional computation in attention, nested inside MoE (2610.31818)

**TL;DR.** MoE (mixture-of-experts) makes the MLP sparse: each token uses a few experts. Nestor (Ma Lab, Berkeley) adds an analogous sparsity mechanism that generalizes the attention operator, and it composes hierarchically with MoE sparsity ("nested sparsity"). At equal compute and equal sparsity, Nestor beats a conventional MoE transformer in LM pretraining. It also adapts to longer contexts better and to new domains with less forgetting, and the gains hold as model size, data and context grow. Code and checkpoints on GitHub.

<div class="dg-title">Sparsity in two places, one inside the other</div>
<div class="dg-sub">MoE already routes the MLP; Nestor routes inside attention too.</div>

```mermaid
flowchart LR
  X["Token<br/><small>hidden state</small>"] --> A["Sparse attention op<br/><small>conditional subset</small>"]
  A --> M["MoE MLP<br/><small>top-k experts</small>"]
  M --> Y["Output<br/><small>same compute budget</small>"]
  A -.->|nests with| M
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class X input
  class A,M loop
  class Y exit
```

<div class="dg-legend">Blue is input, amber are the two routed operators, green is the output at matched compute.</div>

## Relation to prior wiki pages
- Adds a third sparsity site to [model pruning and sparsity](../inference-efficiency/model-pruning-sparsity.md) alongside expert sparsity and attention-token sparsity (Stratified Sparse Attention, 10-23). Different from token selection: this is weight-level conditional compute in attention.
- The continual-learning angle connects to Google Research's sleep framework (today) and Continual Learning Exam (today's HF): three items on retaining knowledge without forgetting.

## Gaps
- Abstract gives no absolute scale; serving cost of the attention routing (load balance, kernel support) not addressed.

Raw: [HF](../../raw/huggingface/2026-10-27-nested-sparsity-for-scalable-pretraining-and-continual-learn.md) · [arXiv](https://arxiv.org/abs/2610.31818) · [GitHub](https://github.com/Ma-Lab-Berkeley/Nestor)
