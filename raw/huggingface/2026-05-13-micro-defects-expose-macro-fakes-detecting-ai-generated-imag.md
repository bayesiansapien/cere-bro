---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.09296
url: https://huggingface.co/papers/2605.09296
arxiv_url: https://arxiv.org/abs/2605.09296
date: 2026-05-13
---

# Micro-Defects Expose Macro-Fakes: Detecting AI-Generated Images via Local Distributional Shifts

Recent generative models can produce images that appear highly realistic, raising challenges in distinguishing real and AI-generated images. Yet existing detectors based on pre-trained feature extractors tend to over-rely on global semantics, limiting sensitivity to the critical micro-defects. In this work, we propose Micro-Defects expose Macro-Fakes (MDMF), a local distribution-aware detection framework that amplifies micro-scale statistical irregularities into macro-level distributional discrepancies. To avoid localized forensic cues being diluted by plain aggregation, we introduce a learnable Patch Forensic Signature that projects semantic patch embeddings into a compact forensic latent space. We then use Maximum Mean Discrepancy (MMD) to quantify distributional discrepancies between generated and real images. Our theory-grounded analysis shows that patch-wise modeling yields provably larger discrepancies when localized forensic signals are present in generated images, enabling more reliable separation from real images. Extensive experiments demonstrate that MDMF consistently outperforms baseline detectors across multiple benchmarks, validating its general effectiveness. Project page: https://zbox1005.github.io/MDMF-project/
