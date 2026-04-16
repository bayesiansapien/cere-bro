---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13432
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13432
published: 2026-04-16
authors: Simin Huo, Ning Li
---

# MaMe & MaRe: Matrix-Based Token Merging and Restoration for Efficient Visual Perception and Synthesis

**arXiv:** https://arxiv.org/abs/2604.13432
**Authors:** Simin Huo, Ning Li

## Abstract

arXiv:2604.13432v1 Announce Type: cross  Abstract: Token compression is crucial for mitigating the quadratic complexity of self-attention mechanisms in Vision Transformers (ViTs), which often involve numerous input tokens. Existing methods, such as ToMe, rely on GPU-inefficient operations (e.g., sorting, scattered writes), introducing overheads that limit their effectiveness. We introduce MaMe, a training-free, differentiable token merging method based entirely on matrix operations, which is GPU-friendly to accelerate ViTs. Additionally, we present MaRe, its inverse operation, for token restoration, forming a MaMe+MaRe pipeline for image synthesis. When applied to pre-trained models, MaMe doubles ViT-B throughput with a 2% accuracy drop. Notably, fine-tuning the last layer with MaMe boosts ViT-B accuracy by 1.0% at 1.1x speed. In SigLIP2-B@512 zero-shot classification, MaMe provides 1.3x acceleration with negligible performance degradation. In video tasks, MaMe accelerates VideoMAE-L by 48.5% on Kinetics-400 with only a 0.84% accuracy loss. Furthermore, MaMe achieves simultaneous improvements in both performance and speed on some tasks. In image synthesis, the MaMe+MaRe pipeline enhances quality while reducing Stable Diffusion v2.1 generation latency by 31%. Collectively, these results demonstrate MaMe's and MaRe's effectiveness in accelerating vision models. The code is available at https://github.com/cominder/mame}{https://github.com/cominder/mame.
