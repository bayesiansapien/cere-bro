---
source: farmer/huggingface
farmed: 2026-05-02T00:00:00Z
arxiv_id: "2604.24953"
url: https://huggingface.co/papers/2604.24953
arxiv_url: https://arxiv.org/abs/2604.24953
date: 2026-05-02
---

# ViPO: Visual Preference Optimization at Scale

The paper addresses scaling preference optimization for visual generative models. A key challenge is that existing preference datasets contain conflicting patterns where some outputs excel in certain dimensions but fall short in others. The authors propose Poly-DPO, which enhances the standard DPO objective by adding a polynomial term that dynamically calibrates model confidence based on data characteristics.

To overcome data quality limitations, the team created ViPO, a large-scale preference dataset comprising 1M image pairs at 1024px resolution across five categories and 300K video pairs at 720p+ across three categories. The dataset prioritizes reliable preference signals with balanced distributions.

Notably, when Poly-DPO was applied to the high-quality ViPO dataset, the approach converged to standard DPO, suggesting that sophisticated optimization becomes less critical when data quality is sufficiently high. Testing demonstrated substantial improvements: Poly-DPO achieved 6.87 and 2.32 gains over Diffusion-DPO on GenEval for SD1.5 and SDXL respectively on noisier datasets. Models trained on ViPO substantially outperformed those trained on existing open-source preference datasets.
