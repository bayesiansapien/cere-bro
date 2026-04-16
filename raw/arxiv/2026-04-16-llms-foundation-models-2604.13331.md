---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13331
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13331
published: 2026-04-16
authors: Mohsen Nayebi Kerdabadi, Arya Hadizadeh Moghaddam, Chen Chen
---

# Text-Attributed Knowledge Graph Enrichment with Large Language Models for Medical Concept Representation

**arXiv:** https://arxiv.org/abs/2604.13331
**Authors:** Mohsen Nayebi Kerdabadi, Arya Hadizadeh Moghaddam, Chen Chen

## Abstract

arXiv:2604.13331v1 Announce Type: new  Abstract: In electronic health record (EHR) mining, learning high-quality representations of medical concepts (e.g., standardized diagnosis, medication, and procedure codes) is fundamental for downstream clinical prediction. However, robust concept representation learning is hindered by two key challenges: (i) clinically important cross-type dependencies (e.g., diagnosis-medication and medication-procedure relations) are often missing or incomplete in existing ontology resources, limiting the ability to model complex EHR patterns; and (ii) rich clinical semantics are often missing from structured resources, and even when available as text, are difficult to integrate with KG structure for representation learning. To address these challenges, we present CoMed, an LLM-empowered graph learning framework for medical concept representation. CoMed first builds a global knowledge graph (KG) over medical codes by combining statistically reliable associations mined from EHRs with type-constrained LLM prompting to infer semantic relations. It then utilizes LLMs to enrich the KG into a text-attributed graph by generating node descriptions and edge rationales, providing semantic signals for both concepts and their relationships. Finally, CoMed jointly trains a LoRA-tuned LLaMA text encoder with a heterogeneous GNN, fusing text semantics and graph structure into unified concept embeddings. Extensive experiments on MIMIC-III and MIMIC-IV show that CoMed consistently improves prediction performance and serves as an effective plug-in concept encoder for standard EHR pipelines.
