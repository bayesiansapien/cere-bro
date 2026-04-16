---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13392
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13392
published: 2026-04-16
authors: Chenlang Yi, Gang Li, Zizhan Xiong
---

# ReSS: Learning Reasoning Models for Tabular Data Prediction via Symbolic Scaffold

**arXiv:** https://arxiv.org/abs/2604.13392
**Authors:** Chenlang Yi, Gang Li, Zizhan Xiong

## Abstract

arXiv:2604.13392v1 Announce Type: new  Abstract: Tabular data remains prevalent in high-stakes domains such as healthcare and finance, where predictive models are expected to provide both high accuracy and faithful, human-understandable reasoning. While symbolic models offer verifiable logic, they lack semantic expressiveness. Meanwhile, general-purpose LLMs often require specialized fine-tuning to master domain-specific tabular reasoning. To address the dual challenges of scalable data curation and reasoning consistency, we propose ReSS, a systematic framework that bridges symbolic and neural reasoning models. ReSS leverages a decision-tree model to extract instance-level decision paths as symbolic scaffolds. These scaffolds, alongside input features and labels, guide an LLM to generate grounded natural-language reasoning that strictly adheres to the underlying decision logic. The resulting high-quality dataset is used to fine-tune a pretrained LLM into a specialized tabular reasoning model, further enhanced by a scaffold-invariant data augmentation strategy to improve generalization and explainability. To rigorously assess faithfulness, we introduce quantitative metrics including hallucination rate, explanation necessity, and explanation sufficiency. Experimental results on medical and financial benchmarks demonstrate that ReSS-trained models improve traditional decision trees and standard fine-tuning approaches up to $10\%$ while producing faithful and consistent reasoning
