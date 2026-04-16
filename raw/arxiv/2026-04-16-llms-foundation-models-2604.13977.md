---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13977
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13977
published: 2026-04-16
authors: Joel Niklaus, Atsuki Yamaguchi, Michal \v{S}tef\'anik
---

# How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data

**arXiv:** https://arxiv.org/abs/2604.13977
**Authors:** Joel Niklaus, Atsuki Yamaguchi, Michal \v{S}tef\'anik

## Abstract

arXiv:2604.13977v1 Announce Type: cross  Abstract: Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform both curated web baselines and prior synthetic methods. Notably, increasing the size of the generator model beyond 1B parameters provides no additional benefit. Our analysis also demonstrates that the selection of the original data used for mixing substantially influences performance. By applying our findings, we develop \textbf{\textsc{FinePhrase}}, a 486-billion-token open dataset of rephrased web text. We show that \textsc{FinePhrase} outperforms all existing synthetic data baselines while reducing generation costs by up to 30 times. We provide the dataset, all prompts, and the generation framework to the research community.
