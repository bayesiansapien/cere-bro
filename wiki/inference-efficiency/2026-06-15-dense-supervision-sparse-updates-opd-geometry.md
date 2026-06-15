# Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation

**TL;DR.** On-policy distillation (OPD) post-trains a model on its own generated trajectories while supervising every token against a teacher's full distribution. It combines RLVR's on-policy data with SFT's dense signal, and it has become a popular post-training recipe, but how it actually changes a model's weights was unknown. This paper measures it across several language and vision-language model pairs and finds OPD updates are **small and coordinate-sparse** (concentrated, FFN-heavy, spread across layers), and **geometrically distinctive**: numerically full-rank but spectrally concentrated, lying mostly *away* from the source weights' principal singular directions and falling disproportionately on coordinates where the source weight is near zero. Training only the discovered subnetwork recovers almost all of full OPD. So dense teacher supervision does *not* turn OPD into ordinary dense rewriting, it keeps the geometric fingerprint of on-policy post-training.

**Source:** HuggingFace · [Paper](https://arxiv.org/abs/2606.13657) · arxiv 2606.13657 (Nanjing University + Amap/Alibaba)

```mermaid
flowchart LR
  S[Student policy] -->|on-policy<br/>rollouts| TR[Trajectories]
  T[Teacher] -->|dense per-token<br/>distribution| SUP[OPD loss]
  TR --> SUP
  SUP --> UPD{Parameter update}
  UPD -->|small, coordinate-sparse<br/>FFN-heavy| SUB[Discovered subnetwork]
  UPD -->|full-rank but<br/>spectrally concentrated| GEO[Off principal subspace<br/>near-zero coords]
  SUB -->|train only this| REC[Recovers ~full OPD]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class S,T input
  class UPD decision
  class TR,SUP aux
  class SUB,GEO,REC output
```

## What it is

A measurement study of *where in weight space* OPD writes. OPD sits between SFT/offline distillation (dense token supervision on a fixed dataset, but off-policy so it suffers distribution shift) and RLVR (on-policy but sparse outcome reward, so it has a credit-assignment problem). OPD keeps on-policy student data and replaces the sparse reward with dense teacher supervision. The question: does that hybrid produce dense SFT-like updates, sparse RLVR-like updates, or something distinct?

## What problem it solves

The field adopted OPD empirically without knowing its mechanical signature. Prior work showed dense off-policy SFT produces denser updates while sparse RLVR modifies a small subnetwork and moves away from principal weight directions. OPD's hybrid nature left it ambiguous. This paper resolves the ambiguity with direct measurement.

## Core novelty

Two concrete, reproducible findings. **Sparsity:** OPD updates are small and coordinate-sparse, distributed across layers, FFN-heavy, and the discovered subnetwork alone recovers nearly full performance, so OPD has an exploitable lottery-ticket-style structure. **Geometry:** updates are full-rank but spectrally concentrated, sit off the principal singular subspace of the source weights, and land disproportionately on near-zero coordinates. Also an optimizer result: sparsity-inducing SGD *under*performs AdamW here, because dense teacher supervision preserves heterogeneous per-coordinate gradient scales that AdamW's adaptive scaling still exploits, the opposite of the sparse-RLVR regime where SGD is competitive.

## Key takeaways

- OPD updates are small, coordinate-sparse, FFN-heavy, spread across layers.
- Training only the discovered subnetwork ~recovers full OPD, an efficiency lever.
- Updates are full-rank but spectrally concentrated, off the principal subspace, on near-zero coordinates.
- AdamW beats SGD for OPD (unlike sparse RLVR), because dense supervision keeps coordinate-wise gradient heterogeneity.

## Gaps

The "train only the subnetwork" recovery is shown post-hoc (the subnetwork is discovered *from* a full OPD run); whether it can be predicted *before* training, which is what would make it a real compute saving, is not shown. Held to specific model pairs and tasks; no scaling study of whether the sparsity fraction changes with model size.

## How it relates to prior wiki knowledge

- Direct continuation of the wiki's OPD thread. The [Extrapolation Cliff](2026-05-14-extrapolation-cliff-on-policy-distillation.md) (05-14) gave OPD a closed-form collapse threshold; [Many Faces of OPD](2026-05-13-many-faces-on-policy-distillation.md) (05-13) gave a failure taxonomy; [TrOPD](2026-06-03-tropd-trust-region-on-policy-distillation.md) (06-03) gave a trust-region stabilizer. This paper adds the **weight-space anatomy** none of them measured.
- It extends the wiki's longest-running "the learning signal is sparse and locatable" line (TIP 04-16: <10% of distillation tokens carry signal; [LongAct](../llms-foundation-models/2026-04-18-longact-saliency-sparse-rl.md) 04-18; [Temporal Scheduling for RLVR](../llms-foundation-models/2026-06-02-temporal-scheduling-rlvr.md) 06-02) from *which tokens* and *when* to *which weight coordinates*. The sparseness is now visible in three places: data, time, and parameters.
- The "off the principal subspace, on near-zero coordinates" geometry echoes the RLVR finding (Zhu et al. 2025) that RL updates move away from principal directions, suggesting on-policy data, not the density of the reward, is what imprints that geometry.

## Research angle

If OPD's effective subnetwork could be *predicted* from the source weights (e.g. the near-zero coordinates plus FFN bias) before training, OPD becomes a sparse-update method with RLVR-like memory cost but dense-supervision sample efficiency, the best of both. The SGD-vs-AdamW reversal is also a clean probe: optimizer choice is now a diagnostic for reward density (sparse → SGD competitive, dense → AdamW wins), useful for inferring what regime an unlabeled post-training run is actually in.

→ Raw: `raw/huggingface/2026-06-15-dense-supervision-sparse-updates-on-the-sparsity-and-geometr.md`
