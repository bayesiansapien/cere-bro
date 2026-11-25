---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.921003+00:00
arxiv_id: 2611.25419
url: https://huggingface.co/papers/2611.25419
arxiv_url: https://arxiv.org/abs/2611.25419
date: 2026-11-24
---

# DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings

Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that combines task guidance with on-policy retrieval feedback. Specifically, a few learnable queries are used to encode task-relevant information in a compact latent space. Reasoning instructions and auxiliary answer-generation supervision shape these representations to support both task understanding and retrieval discrimination. To address task-specific discriminative needs, we design shared-private expert adaptation that integrates cross-task knowledge sharing with task-specific representation learning. Building on this, the on-policy hard-negative distillation is introduced: the student retrieves confusable candidates, and a reverse KL divergence objective aligns its embedding-based similarity distribution with the teacher's fine-grained relevance distribution over these candidates. Candidates are periodically refreshed using updated student snapshots, tying teacher supervision to the student's evolving retrieval behavior and confusions. Across four model configurations that span two backbone generations, DiLE achieves state-of-the-art performance on MMEB-v2, UVRB, and MRMR, demonstrating its effectiveness across modalities and tasks.
