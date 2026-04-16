---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.04844
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2512.04844
published: 2026-04-16
authors: Atsuki Yamaguchi, Terufumi Morishita, Aline Villavicencio
---

# Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates

**arXiv:** https://arxiv.org/abs/2512.04844
**Authors:** Atsuki Yamaguchi, Terufumi Morishita, Aline Villavicencio

## Abstract

arXiv:2512.04844v2 Announce Type: replace-cross  Abstract: Expanding the linguistic diversity of instruct large language models (LLMs) is crucial for global accessibility but is often hindered by the reliance on costly specialized target language labeled data and catastrophic forgetting during adaptation. We tackle this challenge under a realistic, low-resource constraint: adapting instruct LLMs using only unlabeled target language data. We introduce Source-Shielded Updates (SSU), a selective parameter update strategy that proactively preserves source knowledge. Using a small set of source data and a parameter importance scoring method, SSU identifies parameters critical to maintaining source abilities. It then applies a column-wise freezing strategy to protect these parameters before adaptation. Experiments across five typologically diverse languages and 7B and 13B models demonstrate that SSU successfully mitigates catastrophic forgetting. It reduces performance degradation on monolingual source tasks to just 3.4% (7B) and 2.8% (13B) on average, a stark contrast to the 20.3% and 22.3% from full fine-tuning. SSU also achieves target-language performance highly competitive with full fine-tuning, outperforming it on all benchmarks for 7B models and the majority for 13B models.
