---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.14368
url: https://huggingface.co/papers/2605.14368
arxiv_url: https://arxiv.org/abs/2605.14368
date: 2026-05-19
---

# Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement

Continuous diffusion language models lag behind autoregressive transformers, partly because diffusion is applied in spaces poorly suited to language denoising and token recovery. We propose DiHAL, a geometry-guided diffusion-transformer hybrid that asks where diffusion should enter a pretrained transformer. DiHAL scores layers with geometry-based proxies, selects a diffusion-friendly hidden-state interface, and replaces the lower transformer prefix with a diffusion bridge while retaining the upper layers and original LM head. By reconstructing the selected-layer hidden state rather than tokens, DiHAL avoids direct continuous-to-discrete recovery. Experiments on 8B-scale backbones show that the geometry score predicts effective shallow insertion layers under a fixed bridge-training protocol and that hidden-state recovery improves over continuous diffusion baselines in a diagnostic comparison matching the diffusion/recovery training budget. These results suggest that hidden-state geometry helps identify where diffusion-based replacement is feasible inside pretrained language models.
