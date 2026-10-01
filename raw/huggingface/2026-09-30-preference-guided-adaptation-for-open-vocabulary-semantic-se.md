---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34528
url: https://huggingface.co/papers/2609.34528
arxiv_url: https://arxiv.org/abs/2609.34528
date: 2026-09-30
---

# Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement

Open-vocabulary semantic segmentation (OVSS) enables pixel-level prediction over arbitrary text-specified vocabularies and has shown strong generalization on common benchmarks. However, OVSS performance often degrades in specialized domains such as medical imaging, remote sensing, and industrial inspection, where dense pixel-level masks for adaptation are costly to obtain and require domain-specific expertise. We propose a preference-guided adaptation framework that replaces dense mask supervision with binary preferences. We observe that different prompt templates produce systematically different segmentations for the same image, a phenomenon we call prompt disagreement, and we repurpose it as a built-in source of preference supervision. Building on this, we mine localized preference queries from regions of high cross-template uncertainty, and adapt the OVSS model with Region-Localized Preference Optimization (RLPO) together with consistency regularization that stabilizes updates outside the queried region. Across extensive experiments on the MESS benchmark, the proposed method achieves consistent gains across diverse OVSS backbones without any pixel-level annotation, and remains effective under noisy preferences. Our code is available at https://github.com/blue-531/pref-ovss.
