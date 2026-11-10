---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.208203+00:00
arxiv_id: 2611.06844
url: https://huggingface.co/papers/2611.06844
arxiv_url: https://arxiv.org/abs/2611.06844
date: 2026-11-09
---

# Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers

A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual granularities. Recent multi-layer fusion methods either compress hierarchical features on the encoder side or rely on predefined sparse or hierarchical layer-to-layer connections, and therefore stop short of modeling adaptive cross-layer interactions between the ViT and LLM hierarchies. We address this gap with DGP (Dynamic Gated Pathways), a routing mechanism that establishes all-to-all connections between every ViT layer and every LLM layer, with each LLM layer dynamically gating its preference over visual layers conditioned on its own semantic state. Built on top of LLaVA-1.5-7B and 13B, DGP delivers consistent gains over the LLaVA-1.5-7B baseline (e.g., +4.2 on SQA^{I}, +3.3 on MM-Vet, +3.1 on VizWiz and LLaVA^{W}) and surpasses prior multi-layer visual fusion methods on most benchmarks. Layer-wise routing analyses further show that different LLM layers do select different visual granularities on demand, supporting both the effectiveness and interpretability of the proposed dynamic gated pathways. The code is available: https://github.com/YingyingYan1/DGP.
