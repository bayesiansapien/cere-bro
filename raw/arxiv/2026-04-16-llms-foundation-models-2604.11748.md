---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.11748
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.11748
published: 2026-04-16
authors: Yuxin Chen, Chumeng Liang, Hangke Sui
---

# LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling

**arXiv:** https://arxiv.org/abs/2604.11748
**Authors:** Yuxin Chen, Chumeng Liang, Hangke Sui

## Abstract

arXiv:2604.11748v3 Announce Type: replace-cross  Abstract: Continuous diffusion has been the foundation of high-fidelity, controllable, and few-step generation of many data modalities such as images. However, in language modeling, prior continuous diffusion language models (DLMs) lag behind discrete counterparts due to the sparse data space and the underexplored design space. In this work, we close this gap with LangFlow, the first continuous DLM to rival discrete diffusion, by connecting embedding-space DLMs to Flow Matching via Bregman divergence, alongside three key innovations: (1) we derive a novel ODE-based NLL bound for principled evaluation of continuous flow-based language models; (2) we propose an information-uniform principle for setting the noise schedule, which motivates a learnable noise scheduler based on a Gumbel distribution; and (3) we revise prior training protocols by incorporating self-conditioning, as we find it improves both likelihood and sample quality of embedding-space DLMs with effects substantially different from discrete diffusion. Putting everything together, LangFlow rivals top discrete DLMs on both the perplexity (PPL) and the generative perplexity (Gen. PPL), reaching a PPL of 30.0 on LM1B and 24.6 on OpenWebText. It even exceeds autoregressive baselines in zero-shot transfer on 4 out of 7 benchmarks. LangFlow provides the first clear evidence that continuous diffusion is a promising paradigm for language modeling. Homepage: https://github.com/nealchen2003/LangFlow
