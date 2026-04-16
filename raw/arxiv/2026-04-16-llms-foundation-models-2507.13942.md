---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2507.13942
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2507.13942
published: 2026-04-16
authors: Jacob C Walker, Pedro V\'elez, Luisa Polania Cabrera
---

# Frozen Forecasting: A Unified Evaluation

**arXiv:** https://arxiv.org/abs/2507.13942
**Authors:** Jacob C Walker, Pedro V\'elez, Luisa Polania Cabrera

## Abstract

arXiv:2507.13942v2 Announce Type: replace-cross  Abstract: Forecasting future events is a fundamental capability for general-purpose systems that plan or act across different levels of abstraction. Yet, evaluating whether a forecast is "correct" remains challenging due to the inherent uncertainty of the future. We propose a unified evaluation framework for assessing the forecasting capabilities of frozen vision backbones across diverse tasks and abstraction levels. Rather than focusing on single time steps, our framework evaluates entire trajectories and incorporates distributional metrics that better capture the multimodal nature of future outcomes. Given a frozen vision model, we train latent diffusion models to forecast future features directly in its representation space, which are then decoded via lightweight, task-specific readouts. This enables consistent evaluation across a suite of diverse tasks while isolating the forecasting capacity of the backbone itself. We apply our framework to nine diverse vision models, spanning image and video pretraining, contrastive and generative objectives, and with or without language supervision, and evaluate them on four forecasting tasks, from low-level pixel predictions to high-level object motion. We find that forecasting performance strongly correlates with perceptual quality and that the forecasting abilities of video synthesis models are comparable or exceed those pretrained in masking regimes across all levels of abstraction. However, language supervision does not consistently improve forecasting. Notably, video-pretrained models consistently outperform image-based ones.
