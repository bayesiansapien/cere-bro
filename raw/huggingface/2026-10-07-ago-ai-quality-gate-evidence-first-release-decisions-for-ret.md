---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.01218
url: https://huggingface.co/papers/2610.01218
arxiv_url: https://arxiv.org/abs/2610.01218
date: 2026-10-07
---

# AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation

Enterprises adopting retrieval-augmented generation (RAG) face a recurring operational decision: promote, revise, or block a system version. The evidence is incomplete and the metrics come from fallible LLM judges. We report on AGO AI Quality Gate (AGO), an evidence-first quality-gate framework deployed in industrial RAG assessment engagements. AGO integrates four key components: a four-state decision model that treats missing data and judge errors as explicit outcomes; layered scoring combining deterministic checks, local guardrails, and structured LLM evaluation; a stratified beta-binomial gate that quantifies regression risk probabilistically; and a mandatory meta-evaluation protocol to validate the LLM judge before it influences decisions. Since engagement data is proprietary, we evaluate the judge layer on RAGBench, a public benchmark of 100k annotated RAG traces across 12 datasets. On identical stratified test samples (N=1200 per judge), a low-cost judge (gpt-4.1-nano) detects non-adherent answers barely above chance (AUROC 0.603 [0.570, 0.634]), despite producing flawless protocol output, while gpt-4o reaches 0.783 [0.756, 0.807] -- yet its per-domain performance still ranges from 0.62 to 0.88. A fixed-seed gate study spanning regression, no change, and improvement quantifies unsafe promotion, false-alarm cost, and improvement throughput. Under regression, the decision-grade profile reduces unsafe promotion to 22.2%-35.1%, against 29.3%-41.8% for a naive gate. These results support the design choices that judge quality must be measured per engagement and that point estimates alone are not a release decision.
