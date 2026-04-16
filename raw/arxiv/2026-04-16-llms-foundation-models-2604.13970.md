---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13970
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13970
published: 2026-04-16
authors: Felicia Bader, Philipp Seeb\"ock, Anastasia Bartashova
---

# MApLe: Multi-instance Alignment of Diagnostic Reports and Large Medical Images

**arXiv:** https://arxiv.org/abs/2604.13970
**Authors:** Felicia Bader, Philipp Seeb\"ock, Anastasia Bartashova

## Abstract

arXiv:2604.13970v1 Announce Type: new  Abstract: In diagnostic reports, experts encode complex imaging data into clinically actionable information. They describe subtle pathological findings that are meaningful in their anatomical context. Reports follow relatively consistent structures, expressing diagnostic information with few words that are often associated with tiny but consequential image observations. Standard vision language models struggle to identify the associations between these informative text components and small locations in the images. Here, we propose "MApLe", a multi-task, multi-instance vision language alignment approach that overcomes these limitations. It disentangles the concepts of anatomical region and diagnostic finding, and links local image information to sentences in a patch-wise approach. Our method consists of a text embedding trained to capture anatomical and diagnostic concepts in sentences, a patch-wise image encoder conditioned on anatomical structures, and a multi-instance alignment of these representations. We demonstrate that MApLe can successfully align different image regions and multiple diagnostic findings in free-text reports. We show that our model improves the alignment performance compared to state-of-the-art baseline models when evaluated on several downstream tasks. The code is available at https://github.com/cirmuw/MApLe.
