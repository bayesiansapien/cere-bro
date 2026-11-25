---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.931423+00:00
arxiv_id: 2611.29361
url: https://huggingface.co/papers/2611.29361
arxiv_url: https://arxiv.org/abs/2611.29361
date: 2026-11-24
---

# Beyond Attention Maps: Understanding and Improving Medical MLLMs via Visual Values

Current MLLM methods largely focus on whether models attend to the right visual regions, implicitly treating spatial attention map as the primary key of effective visual perception. To examine this assumption, we introduce a medical VQA dataset with paired non-contrast (NC) and contrast-enhanced (CE) images that share corresponding anatomy while providing different cues. We show that this view is incomplete: across paired NC and CE medical images, MLLMs often exhibit similar attention patterns despite producing contrasting answers, while controlled bidirectional interventions induce substantially larger prediction changes on visual values than attention weights. These results identify the visual content retrieved through values as a critical factor in improving perception beyond spatial attention alone. Guided by this finding, we propose VIVID (VIsual Value Intervention Distillation), which uses enhanced visual values to identify and refine teacher corrections aligned with useful visual evidence to improve on-policy distillation from CE to NC images. Across six internal and external test sets, VIVID consistently outperforms existing on-policy distillation methods across different model scales and architectures, requires only NC images at inference, and maintains strong zero-shot performance on general-domain VQA benchmarks. The project page is available at https://qiuzyc.github.io/VIVID.
