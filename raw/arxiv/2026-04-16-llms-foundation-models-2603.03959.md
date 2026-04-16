---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.03959
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.03959
published: 2026-04-16
authors: Md Akib Haider, Ahsan Bulbul, Nafis Fuad Shahid
---

# LoRA-MME: Multi-Model Ensemble of LoRA-Tuned Encoders for Code Comment Classification

**arXiv:** https://arxiv.org/abs/2603.03959
**Authors:** Md Akib Haider, Ahsan Bulbul, Nafis Fuad Shahid

## Abstract

arXiv:2603.03959v4 Announce Type: replace-cross  Abstract: Code comment classification is a critical task for automated software documentation and analysis. In the context of the NLBSE'26 Tool Competition, we present LoRA-MME, a Multi-Model Ensemble architecture utilizing Parameter-Efficient Fine-Tuning (PEFT). Our approach addresses the multi-label classification challenge across Java, Python, and Pharo by combining the strengths of four distinct transformer encoders: UniXcoder, CodeBERT, GraphCodeBERT, and CodeBERTa. By independently fine-tuning these models using Low-Rank Adaptation(LoRA) and aggregating their predictions via a learned weighted ensemble strategy, we maximize classification performance without the memory overhead of full model fine-tuning. Our tool achieved an F1 Weighted score of 0.7906 and a Macro F1 of 0.6867 on the test set. However, the computational cost of the ensemble resulted in a final submission score of 41.20%, highlighting the trade-off between semantic accuracy and inference efficiency.
