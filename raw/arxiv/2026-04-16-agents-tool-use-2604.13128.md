---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13128
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13128
published: 2026-04-16
authors: Isaac Remy, Caleb Chang, Karen Leung
---

# Learning Probabilistic Responsibility Allocations for Multi-Agent Interactions

**arXiv:** https://arxiv.org/abs/2604.13128
**Authors:** Isaac Remy, Caleb Chang, Karen Leung

## Abstract

arXiv:2604.13128v1 Announce Type: cross  Abstract: Human behavior in interactive settings is shaped not only by individual objectives but also by shared constraints with others, such as safety. Understanding how people allocate responsibility, i.e., how much one deviates from their desired policy to accommodate others, can inform the design of socially compliant and trustworthy autonomous systems. In this work, we introduce a method for learning a probabilistic responsibility allocation model that captures the multimodal uncertainty inherent in multi-agent interactions. Specifically, our approach leverages the latent space of a conditional variational autoencoder, combined with techniques from multi-agent trajectory forecasting, to learn a distribution over responsibility allocations conditioned on scene and agent context. Although ground-truth responsibility labels are unavailable, the model remains tractable by incorporating a differentiable optimization layer that maps responsibility allocations to induced controls, which are available. We evaluate our method on the INTERACTION driving dataset and demonstrate that it not only achieves strong predictive performance but also provides interpretable insights, through the lens of responsibility, into patterns of multi-agent interaction.
