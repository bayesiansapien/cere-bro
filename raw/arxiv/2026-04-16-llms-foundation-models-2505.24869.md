---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2505.24869
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2505.24869
published: 2026-04-16
authors: Ce Zhang, Yan-Bo Lin, Ziyang Wang
---

# SiLVR: A Simple Language-based Video Reasoning Framework

**arXiv:** https://arxiv.org/abs/2505.24869
**Authors:** Ce Zhang, Yan-Bo Lin, Ziyang Wang

## Abstract

arXiv:2505.24869v3 Announce Type: replace  Abstract: Recent advances in test-time optimization have led to remarkable reasoning capabilities in Large Language Models (LLMs), enabling them to solve highly complex problems in math and coding. However, the reasoning capabilities of multimodal LLMs (MLLMs) still significantly lag, especially for complex video-language tasks. To address this issue, we present SILVR, a Simple Language-based Video Reasoning framework that decomposes complex video understanding into two stages. In the first stage, SILVR transforms raw video into language-based representations using multisensory inputs, such as short clip captions and audio/speech subtitles. In the second stage, language descriptions are fed into a powerful reasoning LLM to solve complex video-language understanding tasks. To handle long-context multisensory inputs, we use an Adaptive Context Reduction scheme, which dynamically determines the temporal granularity with which to sample the tokens. Our simple, modular, and training-free video reasoning framework achieves the best-reported results on Video-MME (long), Video-MMMU (comprehension), Video-MMLU, CGBench, and EgoLife. Furthermore, our empirical study focused on video reasoning capabilities shows that, despite not being explicitly trained on video, strong reasoning LLMs can effectively aggregate multisensory input information from video, speech, and audio for complex temporal, causal, long-context, and knowledge acquisition reasoning tasks in video. More details can be found at https://sites.google.com/cs.unc.edu/silvr.
