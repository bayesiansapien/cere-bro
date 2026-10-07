---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.32510
url: https://huggingface.co/papers/2609.32510
arxiv_url: https://arxiv.org/abs/2609.32510
date: 2026-10-06
---

# GeoCR: Learning a Generalist Cloud Removal Prior from Heterogeneous Observations

Cloud removal methods are typically specialized to individual datasets and input configurations, limiting reuse across sensors, spectral bands, and observation settings. We introduce GeoCR, a generalist model that unifies RGB-only-based CR and multispectral-based CR from single- or multi-temporal cloudy observations, with optional SAR guidance, within a single network. To accommodate different spectral and sensing domains, compact input and output stems extend a pretrained RGB autoencoder while keeping its encoder and decoder trunks frozen. This shared latent interface enables a single flow transformer to jointly model clean RGB and non-RGB latents, conditioned on separate cloudy-observation streams and optional SAR tokens. Through joint pretraining on the training splits of ten datasets comprising 883,331 cloud-free target images, GeoCR learns a shared cloud removal prior across these heterogeneous configurations. The same pretrained checkpoint supports direct inference without dataset-specific fine-tuning and efficient adaptation through low-rank adaptation (LoRA). We evaluate GeoCR against general image restoration and cloud removal methods on test splits of the contributing datasets under full-band and RGB-only settings. GeoCR achieves the best FID and DISTS on full-band SEN12MS-CR and Sen2_MTC_New and RGB-only CUHK-CR2, outperforming existing models and demonstrating the effectiveness of a reusable generative model across diverse settings.
